# ==============================================================================
# MessageProcessor.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

import operator
import re


# ------------------------------------------------------------------------------
# Class
# ------------------------------------------------------------------------------

class MessageProcessor(object):
    """
    Methods for processing messages and gaining insight into patterns.
    """

    def __init__(self):
        """
        Creates a message processor.
        """
        self.common_words = [
            'i',
            'you',
            'a',
            'to',
            'the',
            'and',
            'it',
            'that',
            'of',
            'is',
            'its',
            'so',
            'in',
            'but',
            'not',
            'my',
            'was',
            'are',
            'do',
            'im',
            'your',
            'for',
            'me',
            'on',
            'at',
            'have',
            'be',
            'thats',
            'with',
            'what',
            'if',
            'how',
            'dont',
            'or',
            'this',
        ]

        self.swear_words = [
                'fuck',
                'shit',
                'asshole',
                'bitch',
                'ass',
                'damn',
                'damned',
                'motherfucker',
            ]

        self.sexual_words = [
                'dick',
                'penis',
                'cock',
                'prick',
                'wang',
                'balls',
                'nuts',
                'nutsack',
                'scrotum',
                'vagina',
                'pussy',
                'twat',
                'breast',
                'breasts',
                'tit',
                'tits',
                'titties',
                'boob',
                'boobs',
                'boobies',
                'slut',
                'whore',
                'blowjob',
                'sex',
                'sexual',
            ]


    def most_used_words(self, messages, top=10):
        """
        Find the most used words in the messages. Exclude common words. Return
        as many as asked for, but by default, return the top 10.

        Arguments:
            messages<[TextMessage]> -- List of messages.
            top<int>                -- Option, number of words to return.

        Returns:
            List of tuples with most used, non-common words and it's hit count,
            like so: [(word, hits), ...].
        """
        if len(messages) == 0:
            return []

        result = []

        all_words = {}
        for message in messages:
            words = self.extract_words(message.body)
            words = [word.lower() for word in words]

            for word in words:
                if word in self.common_words:
                    continue
                if word not in all_words:
                    all_words[word] = 1
                else:
                    all_words[word] += 1

        result = sorted(all_words.items(), key=operator.itemgetter(1))
        result.reverse()
        result = result[:top + 1]

        return result


    def swear_words_per_message(self, messages):
        """
        Find the average number of swear words per message.

        Arguments:
            messages<[TextMessage]> -- List of messages.

        Returns:
            Average number of swear words per message.
        """
        if len(messages) == 0:
            return 0.0

        result = 0.0

        swears = 0
        for message in messages:
            words = self.extract_words(message.body)
            words = [word.lower() for word in words]

            for word in words:
                if word in self.swear_words:
                    swears += 1

        result = float(swears) / len(messages)

        return result


    def sexual_words_per_message(self, messages):
        """
        Find the average number of sexual words per message.

        Arguments:
            messages<[TextMessage]> -- List of messages.

        Returns:
            Average number of sexual words per message.
        """
        if len(messages) == 0:
            return 0.0

        result = 0.0

        total_sexual_words = 0
        for message in messages:
            words = self.extract_words(message.body)
            words = [word.lower() for word in words]

            for word in words:
                if word in self.sexual_words:
                    total_sexual_words += 1

        result = float(total_sexual_words) / len(messages)

        return result


    def average_message_length(self, messages):
        """
        Find the average message length for the given messages.

        Arguments:
            messages<[TextMessage]> -- List of messages.

        Returns:
            Average number of characters per message.
        """
        if len(messages) == 0:
            return 0.0

        result = 0.0

        total_characters = 0
        for message in messages:
            total_characters += len(message.body)

        result = float(total_characters) / len(messages)

        return result


    def average_sentence_length(self, messages):
        """
        Find the average sentence length for the given messages.

        Arguments:
            messages<[TextMessage]> -- List of messages.

        Returns:
            Average number of characters per sentence.
        """
        if len(messages) == 0:
            return 0.0

        result = 0.0

        total_characters, total_sentences = 0, 0

        for message in messages:
            sentences = self.extract_sentences(message.body)

            for sentence in sentences:
                total_characters += len(sentence)
                total_sentences += 1

        if total_sentences > 0:
            result = float(total_characters) / total_sentences

        return result


    def average_word_length(self, messages):
        """
        Find the average word length for the given messages.

        Arguments:
            messages<[TextMessage]> -- List of messages.

        Returns:
            Average number characters per word.
        """
        if len(messages) == 0:
            return 0.0

        result = 0.0

        total, count = 0, 0

        for message in messages:
            words = self.extract_words(message.body)
            total += len(''.join(words))
            count += len(words)

        if count > 0:
            result = float(total) / count

        return result


    def average_sentences_per_message(self, messages):
        """
        Find the average number of sentences per message.

        Arguments:
            messages<[TextMessage]> -- List of messages.

        Returns:
            Average number of sentences per message.
        """
        if len(messages) == 0:
            return 0.0

        result = 0.0

        total_sentences = 0
        for message in messages:
            sentences = self.extract_sentences(message.body)
            total_sentences += len(sentences)

        result = float(total_sentences) / len(messages) 

        return result


    def average_words_per_sentence(self, messages):
        """
        Find the average number of words per sentence.

        Arguments:
            messages<[TextMessage]> -- List of messages.

        Returns:
            Average number of words per sentence.
        """
        if len(messages) == 0:
            return 0.0

        result = 0.0

        total_words, total_sentences = 0, 0

        for message in messages:
            sentences = self.extract_sentences(message.body)
            words = self.extract_words(None, sentences)

            total_sentences += len(sentences)
            total_words += len(words)

        if total_sentences > 0:
            result = float(total_words) / total_sentences

        return result


    def average_words_per_message(self, messages):
        """
        Find the average number of words per message.

        Arguments:
            messages<[TextMessage]> -- List of messages.

        Returns:
            Average number of words per message.
        """
        if len(messages) == 0:
            return 0.0

        result = 0.0

        total_words = 0
        for message in messages:
            words = self.extract_words(message.body)
            total_words += len(words)

        result = float(total_words) / len(messages)

        return result


    def extract_sentences(self, body):
        """
        Find the sentences in the message and return them.

        Arguments:
            body<string> -- The content of a single message.

        Returns:
            List of strings, each element being a sentence.
        """
        result = []

        sentence_re = '[\.\?\!]+'
        sentences = re.split(sentence_re, body)

        if len(sentences) > 0:
            if sentences[len(sentences) - 1] == '':
                del sentences[len(sentences) - 1]

            for sentence in sentences:
                result.append(sentence.lstrip())

        return result


    def extract_words(self, body, sentences=None):
        """
        Find the words in the message and return them. Providing the sentences
        if you already have them can make this faster.

        Arguments:
            body<string>        -- The content of a single message.
            sentences<[string]> -- Optional List of sentences from the body.

        Returns:
            List of strings, each element being a word.
        """
        result = []

        if sentences == None:
            sentences = self.extract_sentences(body)
        remove_re = '[\*\(\)\[\]\{\}\|\;\:\\\'\"\,\<\>]'

        for sentence in sentences:
            cleaned = re.sub(remove_re, '', sentence) 
            result.extend(cleaned.split())

        return result
