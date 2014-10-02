# ==============================================================================
# TextMessage.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Class
# ------------------------------------------------------------------------------

class TextMessage(object):
    """
    Stores information about a text message, such as the sender, the date and
    time it was sent, and the content of the text.
    """

    def __init__(self, sender, timestamp, body):
        """
        Creates a TextMessage object.

        Arguments:
            sender<string>      -- Sender name.
            timestamp<datetime> -- Timestamp message was sent.
            body<string>        -- Body of the text message.
        """
        if sender == None or sender == '':
            raise Exception('Sender cannot be empty or None.')
        if timestamp == None: 
            raise Exception('Timestamp cannot be None.')
        if body == None or body == '':
            raise Exception('Body cannot be empty or None.')

        self.sender = sender
        self.timestamp = timestamp
        self.body = body
