<h1><img src="https://raw.githubusercontent.com/remindr/certifier/master/doc/certifier.png" height=85 alt="certifier" title="certifier"> certifier</h1>

[![PyPi Version](http://img.shields.io/pypi/v/certifier.svg)](https://pypi.python.org/pypi/certifier/)   [![Downloads](http://img.shields.io/pypi/dm/certifier.svg)](https://pypi.python.org/pypi/certifier/)
[![Code Health](https://landscape.io/github/mrsmn/certifier/master/landscape.svg)](https://landscape.io/github/mrsmn/certifier/master)

**certifier** is an APACHE licensed Python library allowing you to get all the information you'll ever want about your SSL certificates.

## Installation:

From source use

		$ python setup.py install

or install from PyPi

		$ pip install certifier
		
## Documentation:

```
>>> from certifier import CertInfo
>>> cert = CertInfo()
>>> cert.info('example.com', 443)
{'crlDistributionPoints': (u'http://crl3.digicert.com/sha2-ha-server-g3.crl', u'http://crl4.digicert.com/sha2-ha-server-g3.crl'), 'subjectAltName': (('DNS', 'www.example.org'), ('DNS', 'example.com'), ('DNS', 'example.edu'), ('DNS', 'example.net'), ('DNS', 'example.org'), ('DNS', 'www.example.com'), ('DNS', 'www.example.edu'), ('DNS', 'www.example.net')), 'notBefore': u'Nov  6 00:00:00 2014 GMT', 'caIssuers': (u'http://cacerts.digicert.com/DigiCertSHA2HighAssuranceServerCA.crt',), 'OCSP': (u'http://ocsp.digicert.com',), 'serialNumber': u'0411DE8F53B462F6A5A861B712EC6B59', 'notAfter': 'Nov 13 12:00:00 2015 GMT', 'version': 3L, 'subject': ((('countryName', u'US'),), (('stateOrProvinceName', u'California'),), (('localityName', u'Los Angeles'),), (('organizationName', u'Internet Corporation for Assigned Names and Numbers'),), (('organizationalUnitName', u'Technology'),), (('commonName', u'www.example.org'),)), 'issuer': ((('countryName', u'US'),), (('organizationName', u'DigiCert Inc'),), (('organizationalUnitName', u'www.digicert.com'),), (('commonName', u'DigiCert SHA2 High Assurance Server CA'),))}
```

```
>>> cert.expire('example.com', 443)
'Nov 13 12:00:00 2015 GMT'
```

```
>>> cert.protocol('example.com', 443)
u'TLSv1'
```

```
>>> cert.cipher('example.com', 443)
('RC4-SHA', 'TLSv1/SSLv3', 128)
```

```
>>> cert.default_paths()
DefaultVerifyPaths(cafile=None, capath='/System/Library/OpenSSL/certs', openssl_cafile_env='SSL_CERT_FILE', openssl_cafile='/System/Library/OpenSSL/cert.pem', openssl_capath_env='SSL_CERT_DIR', openssl_capath='/System/Library/OpenSSL/certs')
```

```
>>> cert.stats()
{'x509': 0, 'x509_ca': 0, 'crl': 0}
```

```
>>> cert.ca_certs()
[]
```


## License:

```
	Apache v2.0 License
	Copyright 2014-2015 Martin Simon

	 Licensed under the Apache License, Version 2.0 (the "License");
	 you may not use this file except in compliance with the License.
	 You may obtain a copy of the License at

		 http://www.apache.org/licenses/LICENSE-2.0

	 Unless required by applicable law or agreed to in writing, software
	 distributed under the License is distributed on an "AS IS" BASIS,
	 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	 See the License for the specific language governing permissions and
	 limitations under the License.

```