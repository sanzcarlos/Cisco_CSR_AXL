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
import platform
import signal
import sys
import time
import urllib3
import uuid

from dotenv import dotenv_values
from lxml import etree
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client, Settings, Plugin
from zeep.transports import Transport
from zeep.cache import SqliteCache
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault


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

# Class My logging Pluging


class MyLoggingPlugin(Plugin):
    """Plugin class."""

    def egress(self, envelope, http_headers, operation, binding_options):
        """Plugin egress method."""
        # Format the request body as pretty printed XML
        xml = etree.tostring(envelope, pretty_print=True, encoding='unicode')
        print(f'\nRequest\n-------\nHeaders:\n{http_headers}\n\nBody:\n{xml}')

    def ingress(self, envelope, http_headers, operation):
        """Plugin ingress method."""
        # Format the response body as pretty printed XML
        xml = etree.tostring(envelope, pretty_print=True, encoding='unicode')
        print(f'\nResponse\n-------\nHeaders:\n{http_headers}\n\nBody:\n{xml}')

# Function to create a SOAP connection to Cisco Unified Communications Manager.


def client_soap(config_file):
    """Create a SOAP client."""
    """Function to create a SOAP Client

    Args:
        dotenv_values: Dict with config of Customer

    Returns:
        ServiceProxy: Return of the Class zeep.proxy.ServiceProxy
    """
    logger.debug("    [!] Creating SOAP client...")

    if platform.system() == 'Windows':
        logger.debug(
            '    [!] The Operating System is: %s' %
            (platform.system()))
        wsdl = 'file:////' + os.getcwd().replace("\\", "//") + \
            '//Schema//CUCM//' + config_file['CUCM_VERSION'] + '//AXLAPI.wsdl'
    else:
        logger.debug(
            '    [!] The Operating System is: %s' %
            (platform.system()))
        wsdl = 'file://' + os.getcwd() + '/Schema/CUCM/' + \
            config_file['CUCM_VERSION'] + '/AXLAPI.wsdl'

    location = 'https://' + config_file['CUCM_SERVER'] + '/axl/'

    # history shows http_headers
    global history
    history = HistoryPlugin()

    # Change to true to enable output of request/response headers and XML
    if logger.level > 10:
        DEBUG = False
    else:
        DEBUG = True

    # The first step is to create a SOAP client session
    session = Session()

    # We avoid certificate verification by default, but you can uncomment
    # and set your certificate here, and comment out the False setting

    # session.verify = CERT
    session.verify = False
    session.auth = HTTPBasicAuth(
        config_file['CUCM_USER'],
        config_file['CUCM_PASS'])

    transport = Transport(session=session, timeout=5, cache=SqliteCache())

    # strict=False is not always necessary, but it allows zeep to parse
    # imperfect XML
    settings = Settings(strict=False, xml_huge_tree=True)
    try:
        soap_client = Client(
            wsdl,
            settings=settings,
            transport=transport,
            plugins=[
                MyLoggingPlugin(),
                history] if DEBUG else [],
        )
        service = soap_client.create_service(
            "{http://www.cisco.com/AXLAPIService/}AXLAPIBinding", location)

    except KeyboardInterrupt:
        logger.error('    [!] KeyboardInterrupt: Error to create soap client.')
    except SystemExit:
        logger.error('    [!] SystemExit: Error to create soap client.')
    except BaseException:
        logger.error('    [!] Error to create soap client.')
        logger.debug(sys.exc_info())
        logger.error(sys.exc_info()[1])
        sys.exit()
    else:
        logger.info('    [!] SOAP client has been created.')
        # ogger.info('    [!] %s' % type(service))
        return service


# Main Function


def main():
    """Start the script."""
    """Creating the SOAP client"""
    client_soap(dotenv_values())

    urllib3.disable_warnings()
    time.sleep(10)


if __name__ == '__main__':
    logger.info("[!] Starting...")
    main()
