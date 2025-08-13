"""
The PID Issuer Web service is a component of the PID Provider backend. 
Its main goal is to issue the PID in cbor/mdoc (ISO 18013-5 mdoc) and SD-JWT format.

This environments.py contains variable mapping to environment. 

NOTE: You should only change it if you understand what you're doing.
"""

import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
import os

class Environments:
    pid_mdoc_privkey = os.getenv("PID_MDOC_PRIVKEY")
    pid_mdoc_privkey_passwd = os.getenv("PID_MDOC_PRIVKEY_PASSWD").encode('utf-8')
    pid_mdoc_cert = os.getenv("PID_MDOC_CERT")
    service_url = os.getenv("SERVICE_URL")