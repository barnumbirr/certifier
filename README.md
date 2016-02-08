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

```python
>>> from certifier import CertInfo
>>> cert = CertInfo('example.com', 443)
>>> cert.info([ binary_form ])
{'crlDistributionPoints': (u'http://crl3.digicert.com/sha2-ha-server-g3.crl', u'http://crl4.digicert.com/sha2-ha-server-g3.crl'), 'subjectAltName': (('DNS', 'www.example.org'), ('DNS', 'example.com'), ('DNS', 'example.edu'), ('DNS', 'example.net'), ('DNS', 'example.org'), ('DNS', 'www.example.com'), ('DNS', 'www.example.edu'), ('DNS', 'www.example.net')), 'notBefore': u'Nov  6 00:00:00 2014 GMT', 'caIssuers': (u'http://cacerts.digicert.com/DigiCertSHA2HighAssuranceServerCA.crt',), 'OCSP': (u'http://ocsp.digicert.com',), 'serialNumber': u'0411DE8F53B462F6A5A861B712EC6B59', 'notAfter': 'Nov 13 12:00:00 2015 GMT', 'version': 3L, 'subject': ((('countryName', u'US'),), (('stateOrProvinceName', u'California'),), (('localityName', u'Los Angeles'),), (('organizationName', u'Internet Corporation for Assigned Names and Numbers'),), (('organizationalUnitName', u'Technology'),), (('commonName', u'www.example.org'),)), 'issuer': ((('countryName', u'US'),), (('organizationName', u'DigiCert Inc'),), (('organizationalUnitName', u'www.digicert.com'),), (('commonName', u'DigiCert SHA2 High Assurance Server CA'),))}
```

```python
>>> cert.expire([ format ])
'Nov 13 12:00:00 2015 GMT'
```

```python
>>> cert.protocol()
u'TLSv1'
```

```python
>>> cert.cipher()
('RC4-SHA', 'TLSv1/SSLv3', 128)
```

```python
>>> cert.default_paths()
DefaultVerifyPaths(cafile='/usr/lib/ssl/cert.pem', capath='/usr/lib/ssl/certs', openssl_cafile_env='SSL_CERT_FILE', openssl_cafile='/usr/lib/ssl/cert.pem', openssl_capath_env='SSL_CERT_DIR', openssl_capath='/usr/lib/ssl/certs')
```

```python
>>> cert.cert_stats()
{'x509': 155, 'x509_ca': 155, 'crl': 0}
```

```python
>>> cert.ca_certs([ binary_form ])
[{'notBefore': u'Apr 16 07:09:14 2007 GMT', 'serialNumber': u'49330001', 'notAfter': 'Apr 16 07:09:14 2027 GMT', 'version': 3L, 'subject': ((('countryName', u'CN'),), (('organizationName', u'CNNIC'),), (('commonName', u'CNNIC ROOT'),)), 'issuer': ((('countryName', u'CN'),), (('organizationName', u'CNNIC'),), (('commonName', u'CNNIC ROOT'),))}, {[...]}]
```

```python
>>> cert.openssl_version()
OpenSSL 0.9.8zg 14 July 2015
```

```python
>>> cert.session_stats()
{'connect_renegotiate': 0L, 'hits': 0L, 'accept_good': 0L, 'cache_full': 0L, 'accept_renegotiate': 0L, 'timeouts': 0L, 'number': 0L, 'accept': 0L, 'connect_good': 2L, 'connect': 2L, 'misses': 0L}
```

## License:

```
	Apache v2.0 License
	Copyright 2014-2016 Martin Simon

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