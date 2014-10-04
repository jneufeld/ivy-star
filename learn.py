# ==============================================================================
# learn.py
#
# This very hacky, ugly file is what I use to mess around with the ANN.
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from sys import argv

from pybrain.datasets import SupervisedDataSet
from pybrain.structure import FeedForwardNetwork, FullConnection, LinearLayer, \
    SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer

from MessageProcessor import MessageProcessor
from RawWhatsAppDataProcessor import RawWhatsAppDataProcessor


# ------------------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------------------

def get_trained_network(messages):
    print 'Training network (this may take some time)...'

    network = make_network()
    training_set = make_training_set(messages)
    trainer = make_trainer(network, training_set)

    max_error, current_error = 0.5, 999

    while current_error > max_error:
        current_error = trainer.train()
        print '\t%s' % current_error

    print 'Network sufficiently trained'

    return network


def make_network():
    network = FeedForwardNetwork()

    in_layer = LinearLayer(6, name='in')
    hidden_layer = SigmoidLayer(3, name='hidden')
    out_layer = LinearLayer(1, name='out')

    network.addInputModule(in_layer)
    network.addModule(hidden_layer)
    network.addOutputModule(out_layer)

    in_to_hidden = FullConnection(in_layer, hidden_layer, name='in_to_hidden')
    hidden_to_out = FullConnection(hidden_layer, out_layer, name='hidden_to_out')

    network.addConnection(in_to_hidden)
    network.addConnection(hidden_to_out)

    network.sortModules()

    return network


def make_training_set(messages):
    input_dimension = 6
    output_dimension = 1

    training_set = SupervisedDataSet(input_dimension, output_dimension)
    processor = MessageProcessor()

    for message in messages:
        msg_len = processor.average_message_length([message])
        snt_len = processor.average_sentence_length([message])
        wrd_len = processor.average_word_length([message])
        snt_msg = processor.average_sentences_per_message([message])
        wrd_snt = processor.average_words_per_sentence([message])
        wrd_msg = processor.average_words_per_message([message])
        sender = 1 if message.sender == 'Jonathan Neufeld' else -1

        sample = [msg_len, snt_len, wrd_len, snt_msg, wrd_snt, wrd_msg]
        training_set.addSample(sample, sender)

    return training_set


def make_trainer(network, training_set):
    return BackpropTrainer(network, training_set, learningrate=0.1)


def get_messages(file_names):
    result = []

    whatsapp_processor = RawWhatsAppDataProcessor()

    for raw_file in file_names:
        messages = whatsapp_processor.get_messages(raw_file)
        print 'Extracted %d messages from %s' % (len(messages), raw_file)

        result.extend(messages)

    return result

def test_ann(network, messages):
    print 'Testing neural network accuracy...'

    correct, wrong = 0, 0
    processor = MessageProcessor()

    for message in messages:
        msg_len = processor.average_message_length([message])
        snt_len = processor.average_sentence_length([message])
        wrd_len = processor.average_word_length([message])
        snt_msg = processor.average_sentences_per_message([message])
        wrd_snt = processor.average_words_per_sentence([message])
        wrd_msg = processor.average_words_per_message([message])

        features = [msg_len, snt_len, wrd_len, snt_msg, wrd_snt, wrd_msg]
        result = network.activate(features)

        if message.sender == 'Jonathan Neufeld':
            if result < 0:
                correct += 1
            else:
                wrong += 1
        else:
            if result > 0:
                correct += 1
            else:
                wrong += 1

    print 'Network identified sender of %d messages, failed %d messages.' % \
        (correct, wrong)

# ------------------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    raw_data_files = argv[1:]
    messages = get_messages(raw_data_files)
    network = get_trained_network(messages)
    test_ann(network, messages)
