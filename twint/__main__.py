import logging
from twint.cli import run_as_command

# Send loggging messages to standard out or a log file:
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, filename='twint.log')
logging.debug('Started Twint')
run_as_command()
logging.debug('Finished Twint')
