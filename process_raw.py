# ==============================================================================
# process_raw.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

from sys import argv

from MessageProcessor import MessageProcessor
from RawWhatsAppDataProcessor import RawWhatsAppDataProcessor


# ------------------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    data_files = argv[1:]
    all_messages = []
    whatsapp_processor = RawWhatsAppDataProcessor()
    
    for data_file in data_files:
        messages = whatsapp_processor.get_messages(data_file)
        print 'Extracted %d messages from %s' % (len(messages), data_file)

        all_messages.extend(messages)

    print 'Gathered %d messages for data set' % len(all_messages)

    message_processor = MessageProcessor()
