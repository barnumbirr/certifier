<h1><img src="https://raw.githubusercontent.com/barnumbirr/certifier/master/doc/certifier.png" height=85 alt="certifier" title="certifier"> certifier</h1>

[![PyPi Version](http://img.shields.io/pypi/v/certifier.svg)](https://pypi.python.org/pypi/certifier/)   [![Downloads](http://img.shields.io/pypi/dm/certifier.svg)](https://pypi.python.org/pypi/certifier/)

**certifier** is an APACHE licensed Python library allowing you to get all the information you'll ever want about your SSL certificates. This library has been tested with Python 2.7.x and Python 3.6+.

## Installation:

From source use

```bash
	$ python setup.py install
```

or install from PyPi

```bash
	$ pip install certifier
```

## Documentation:

```python
>>> from certifier import CertInfo
>>> cert = CertInfo('example.com', 443)
>>> cert.info([ binary_form ])
{'subject': ((('countryName', 'US'),), (('stateOrProvinceName', 'California'),), (('localityName', 'Los Angeles'),), (('organizationName', 'Internet Corporation for Assigned Names and Numbers'),), (('organizationalUnitName', 'Technology'),), (('commonName', 'www.example.org'),)), 'issuer': ((('countryName', 'US'),), (('organizationName', 'DigiCert Inc'),), (('commonName', 'DigiCert SHA2 Secure Server CA'),)), 'version': 3, 'serialNumber': '0FD078DD48F1A2BD4D0F2BA96B6038FE', 'notBefore': 'Nov 28 00:00:00 2018 GMT', 'notAfter': 'Dec  2 12:00:00 2020 GMT', 'subjectAltName': (('DNS', 'www.example.org'), ('DNS', 'example.com'), ('DNS', 'example.edu'), ('DNS', 'example.net'), ('DNS', 'example.org'), ('DNS', 'www.example.com'), ('DNS', 'www.example.edu'), ('DNS', 'www.example.net')), 'OCSP': ('http://ocsp.digicert.com',), 'caIssuers': ('http://cacerts.digicert.com/DigiCertSHA2SecureServerCA.crt',), 'crlDistributionPoints': ('http://crl3.digicert.com/ssca-sha2-g6.crl', 'http://crl4.digicert.com/ssca-sha2-g6.crl')}
```

```python
>>> cert.expire([ format ])
'Nov 13 12:00:00 2020 GMT'
```

```python
>>> cert.protocol()
u'TLSv1.2'
```

```python
>>> cert.cipher()
('ECDHE-RSA-AES128-GCM-SHA256', 'TLSv1/SSLv3', 128)
```

```python
>>> cert.default_paths()
DefaultVerifyPaths(cafile='/usr/local/etc/openssl/cert.pem', capath='/usr/local/etc/openssl/certs', openssl_cafile_env='SSL_CERT_FILE', openssl_cafile='/usr/local/etc/openssl/cert.pem', openssl_capath_env='SSL_CERT_DIR', openssl_capath='/usr/local/etc/openssl/certs')
```

```python
>>> cert.cert_stats()
{'x509': 179, 'crl': 0, 'x509_ca': 179}
```

```python
>>> cert.ca_certs([ binary_form ])
[{'notBefore': u'Apr 16 07:09:14 2007 GMT', 'serialNumber': u'49330001', 'notAfter': 'Apr 16 07:09:14 2027 GMT', 'version': 3L, 'subject': ((('countryName', u'CN'),), (('organizationName', u'CNNIC'),), (('commonName', u'CNNIC ROOT'),)), 'issuer': ((('countryName', u'CN'),), (('organizationName', u'CNNIC'),), (('commonName', u'CNNIC ROOT'),))}, {[...]}]
```

```python
>>> cert.openssl_version()
OpenSSL 1.0.2s  28 May 2019
```

```python
>>> cert.session_stats()
{'connect_renegotiate': 0L, 'hits': 0L, 'accept_good': 0L, 'cache_full': 0L, 'accept_renegotiate': 0L, 'timeouts': 0L, 'number': 0L, 'accept': 0L, 'connect_good': 2L, 'connect': 2L, 'misses': 0L}
```

## License:

```
Copyright 2015-2019 Martin Simon

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

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
BTC : 1BNFXHPNRtg7LrLUmQWwPUwzoicUi3uP8Q
ETH : 0xd061B7dD794F6EB357bf132172ce06D1B0E5b97B
BCH : qpcmv8vstulfhgdf29fd8sf2g769sszscvaktty2rv
```
