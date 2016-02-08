#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssl
import socket
from datetime import datetime

class CertInfo(object):

    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port
        self.context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.context.load_default_certs()
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.default_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

    def _raw_query_data(self, host, port):
        sock = socket.create_connection((self.host, self.port))
        raw_data = self.context.wrap_socket(sock, server_hostname=self.host)
        return raw_data

    def _raw_stats_data(self):
        raw_data = self.default_context
        return raw_data

    def openssl_version(self):
        """ https://docs.python.org/2/library/ssl.html#ssl.OPENSSL_VERSION """
        return ssl.OPENSSL_VERSION

    def session_stats(self):
        """ https://docs.python.org/2/library/ssl.html#ssl.SSLContext.session_stats """
        return self.context.session_stats()

    def info(self, binary_form=None):
        """ https://docs.python.org/2/library/ssl.html#ssl.SSLSocket.getpeercert """
        data = self._raw_query_data(self.host, self.port)
        return data.getpeercert(binary_form=binary_form)

    def expire(self, format=None):
        data = self._raw_query_data(self.host, self.port)
        if format == None:
            return data.getpeercert()['notAfter']
        else:
            """ Example: '%b %d %H:%M:%S %Y %Z' """
            return datetime.strptime(data.getpeercert()['notAfter'], format)

    def protocol(self):
        """ https://docs.python.org/2/library/ssl.html#ssl.SSLSocket.version """
        data = self._raw_query_data(self.host, self.port)
        return data.version()

    def cipher(self):
        """ https://docs.python.org/2/library/ssl.html#ssl.SSLSocket.cipher """
        data = self._raw_query_data(self.host, self.port)
        return data.cipher()

    def default_paths(self):
        """ https://docs.python.org/2/library/ssl.html#ssl.get_default_verify_paths """
        return ssl.get_default_verify_paths()

    def cert_stats(self):
        """ https://docs.python.org/2/library/ssl.html#ssl.SSLContext.cert_store_stats """
        return self._raw_stats_data().cert_store_stats()

    def ca_certs(self, binary_form=None):
        """ https://docs.python.org/2/library/ssl.html#ssl.SSLContext.get_ca_certs """
        return self._raw_stats_data().get_ca_certs(binary_form=binary_form)
