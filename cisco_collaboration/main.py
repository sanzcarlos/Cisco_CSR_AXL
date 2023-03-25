"""
main.py.

Cisco AXL Python

Copyright (C) 2023 Carlos Sanz <carlos.sanzpenas@gmail.com>

  This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
"""
import logging
import os
import signal
import sys
import time
import urllib3
import uuid

from dotenv import load_dotenv


# Define Working DIrectory for logging
if ("cisco_collaboration" in os.getcwd()):
    path = "../log/"
else:
    path = "log/"

# Define the logging global settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)-18s | %(filename)-18s:%(lineno)-4s | %(levelname)-9s'
    ' | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=path +
    time.strftime("%Y%m%d-%H%M%S-") +
    str(
        uuid.uuid4()) +
    '.log',
    filemode='w',
)
logger = logging.getLogger('cisco.cucm.axl.zeep')


def def_handler(sig, frame):
    """Code to handle CRTL+C."""
    logger.debug('[!] Ending...')
    sys.exit(1)


# CRTL+C
signal.signal(signal.SIGINT, def_handler)

# Main Function


def main():
    """Start the script."""
    urllib3.disable_warnings()
    time.sleep(10)


if __name__ == '__main__':
    logger.info("[!] Starting...")
    main()
