# ==============================================================================
# tests.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from datetime import datetime
import unittest

from MessageProcessor import MessageProcessor
from TextMessage import TextMessage


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

class TestMessageProcessorMethods(unittest.TestCase):
    """
    Test message processing methods.
    """

    def setUp(self):
        """
        Create test messages for each test case.
        """
        sender = 'Test Sender'
        timestamp = datetime.now()

        body1 = '?'
        body2 = 'Pretty TYPICAL content ;)'
        body3 = 'First. Second! Third!! Fourth?! Fifth...!'

        self.message_question_mark = TextMessage(sender, timestamp, body1)
        self.message_sentences = TextMessage(sender, timestamp, body3)
        self.message_simple = TextMessage(sender, timestamp, body2)

        self.processor = MessageProcessor() 


    # --------------------------------------------------------------------------
    # Tests for average_message_length()
    # --------------------------------------------------------------------------

    def test_average_message_length_empty_list(self):
        result = self.processor.average_message_length([])
        self.assertEqual(result, 0)


    def test_average_message_length_single_message(self):
        result = self.processor.average_message_length([self.message_simple])
        self.assertEqual(result, len(self.message_simple.body))


    def test_average_message_length_multiple_messages(self):
        messages = [self.message_simple, self.message_sentences]
        result = self.processor.average_message_length(messages)

        expected = (len(self.message_simple.body) + \
            len(self.message_sentences.body)) / 2

        self.assertEqual(result, expected)


    # --------------------------------------------------------------------------
    # Tests for average_sentence_length()
    # --------------------------------------------------------------------------

    def test_average_sentence_length_empty_list(self):
        result = self.processor.average_sentence_length([])
        self.assertEqual(result, 0)


    def test_average_sentence_length_single_message(self):
        result = self.processor.average_sentence_length([self.message_simple])
        self.assertEqual(result, len(self.message_simple.body))


    def test_average_sentence_length_multiple_messages(self):
        messages = [self.message_simple, self.message_sentences]
        result = self.processor.average_sentence_length(messages)

        expected = 52.0 / 6
        self.assertEqual(result, expected)


# ------------------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
