#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssl
import socket
from datetime import datetime

class CertInfo(object):

    def __init__(self):
        self.context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.context.load_default_certs()
        self.context.verify_mode = ssl.CERT_REQUIRED
        self.default_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

    def raw_query_data(self, host, port):
        sock = socket.create_connection((host, port))
        raw_data = self.context.wrap_socket(sock, server_hostname=host)
        return raw_data

    def raw_stats_data(self):
        raw_data = self.default_context
        return raw_data

    def info(self, host, port):
        data = self.raw_query_data(host, port)
        return data.getpeercert()

    def expire(self, host, port, format=False):
        data = self.raw_query_data(host, port)
        if format == True:
            time_format = "%b %d %H:%M:%S %Y %Z"
            return datetime.strptime(data.getpeercert()['notAfter'], time_format)
        else:
            return data.getpeercert()['notAfter']

    def protocol(self, host, port):
        data = self.raw_query_data(host, port)
        return data.version()

    def cipher(self, host, port):
        data = self.raw_query_data(host, port)
        return data.cipher()

    def default_paths(self):
        return ssl.get_default_verify_paths()

    def stats(self):
        return self.raw_stats_data().cert_store_stats()

    def ca_certs(self):
        return self.raw_stats_data().get_ca_certs()
