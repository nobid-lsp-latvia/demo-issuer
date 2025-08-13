# coding: latin-1
###############################################################################
# Copyright (c) 2023 European Commission
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###############################################################################
"""
The PID Issuer Web service is a component of the PID Provider backend. 
Its main goal is to issue the PID in cbor/mdoc (ISO 18013-5 mdoc) and SD-JWT format.

This config_countries.py contains configuration data related to the countries supported by the PID Issuer. 

NOTE: You should only change it if you understand what you're doing.
"""

from .config_service import ConfService as cfgserv
from .environments import Environments as env

class ConfCountries:
    urlReturnEE = "https://pprpid.provider.eudiw.projj.eu/tara/redirect"

    formCountry = "FC"
    # supported countries
    supported_countries = {
        "EU": {
            "name": "nodeEU",
            "pid_url_oidc": env.service_url + "eidasnode/lightrequest?country=EU",
            "pid_mdoc_privkey": env.pid_mdoc_privkey,
            # "pid_mdoc_privkey": 'app\certs\PID-DS-0001_EU.pem',
            "pid_mdoc_privkey_passwd": env.pid_mdoc_privkey_passwd,  # None or bytes,
            "pid_mdoc_cert": env.pid_mdoc_cert,
            "loa": "http://eidas.europa.eu/LoA/high",
            "supported_credentials": [
                "eu.europa.ec.eudi.pid_mdoc",
                "eu.europa.ec.eudi.pid_jwt_vc_json",
                "eu.europa.ec.eudi.rtu_diploma_mdoc",
                "eu.europa.ec.eudi.iban_sd_jwt_vc",
            ],
            "custom_modifiers": {
                "family_name": "CurrentFamilyName",
                "given_name": "CurrentGivenName",
                "birth_date": "DateOfBirth",
            },
            "connection_type": "eidasnode",
            "dynamic_R2": env.service_url + "eidasnode/dynamic_R2",
        },
        formCountry: {
            "name": "FormEU",
            "pid_url": env.service_url + "pid/form",
            "pid_mdoc_privkey": env.pid_mdoc_privkey,
            # "pid_mdoc_privkey": "./app/cert/PID-DS-0002.pid-ds-0002.key.pem",
            # "pid_mdoc_privkey": "/etc/eudiw/pid-issuer/privkey/hackathon-DS-0001_UT.pem",
            # "pid_mdoc_privkey": 'app\certs\PID-DS-0001_UT.pem',
            "pid_mdoc_privkey_passwd": env.pid_mdoc_privkey_passwd,  # None or bytes,
            # "pid_mdoc_privkey_passwd": b"pid-ds-0002",  # None or bytes
            "pid_mdoc_cert": env.pid_mdoc_cert,
            # "pid_mdoc_cert": "./app/cert/PID-DS-0002.cert.der",
            # "pid_mdoc_cert": "/etc/eudiw/pid-issuer/cert/hackathon-DS-0001_UT_cert.der",
            "un_distinguishing_sign": "FC",
            "supported_credentials": [
                "eu.europa.ec.eudi.pid_mdoc",
                "eu.europa.ec.eudi.pid_jwt_vc_json",
                "eu.europa.ec.eudi.mdl_jwt_vc_json",
                "eu.europa.ec.eudi.mdl_mdoc",
                "eu.europa.ec.eudi.rtu_diploma_mdoc",
                "eu.europa.ec.eudi.iban_sd_jwt_vc",
            ],
            "dynamic_R2": env.service_url + "dynamic/form_R2",
        },
        "LV": {
            "name": "Latvia",
            "pid_mdoc_privkey": env.pid_mdoc_privkey,
            "pid_mdoc_privkey_passwd": env.pid_mdoc_privkey_passwd,  # None or bytes,
            "pid_mdoc_cert": env.pid_mdoc_cert,
            # "pid_mdoc_privkey": "./app/cert/PID-DS-0002.pid-ds-0002.key.pem",
            # "pid_mdoc_privkey_passwd": b"pid-ds-0002",  # None or bytes,
            # "pid_mdoc_cert": "./app/cert/PID-DS-0002.cert.der",
            "un_distinguishing_sign": "LV",
            "supported_credentials": [
                "eu.europa.ec.eudi.pid_mdoc",
                "eu.europa.ec.eudi.pid_jwt_vc_json",
                "eu.europa.ec.eudi.mdl_jwt_vc_json",
                "eu.europa.ec.eudi.mdl_mdoc",
                "eu.europa.ec.eudi.rtu_diploma_mdoc",
                "eu.europa.ec.eudi.iban_sd_jwt_vc",
            ],
            "connection_type": "openid",
            "oidc_auth": {
                # "base_url": "https://example.lv/oauth",
                "base_url": "https://example.lv/oauth",
                "redirect_uri": env.service_url + "dynamic/redirect",
                "scope": "openid profile",
                "state": "hkMVY7vjuN7xyLl5",
                "response_type": "code",
                "client_id": "edim-local",
                "client_secret": "Up6R6kDwiqVR4KNAWVY6e23pseY4Y3c6y2XtPKGif2t43TV",
            },
            "attribute_request": {
                "header": {"Host": "example.lv"},
            },
            "oidc_redirect": {
                # "headers": {
                #     "Host": "example.lv/oauth",
                #     "Content-Type": "application/x-www-form-urlencoded",
                #     "Authorization": "Basic ZXVfZXVyb3BhX2VjX2V1ZGl3X3BpZF9wcm92aWRlcl8xX3BwcjpINUVpVjdPaGZMTUs1TFBvcXB0NG5WT1FJeEdicEZ3MQ==",
                # },
                "grant_type": "authorization_code",
                "redirect_uri": env.service_url + "dynamic/redirect",
            },
        },
    }
