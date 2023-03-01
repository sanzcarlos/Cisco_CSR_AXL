import logging
import signal
import sys
import time
import urllib3
import uuid

# Define the logging global settings
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)-18s | %(filename)-18s:%(lineno)-4s | %(levelname)-9s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='../log/' + time.strftime("%Y%m%d-%H%M%S-") + str(uuid.uuid4()) + '.log',
                    filemode='w',
                    )
logger = logging.getLogger('cisco.cucm.axl.zeep')

def def_handler (sig, frame):
    logger.debug('[!] Ending...')
    sys.exit(1)

# CRTL+C
signal.signal(signal.SIGINT, def_handler)

# Main Function
def main():
    urllib3.disable_warnings()
    time.sleep(10)

if __name__=='__main__':
    logger.info("[!] Starting...")
    main()