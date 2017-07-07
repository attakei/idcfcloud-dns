#!/usr/bin/env python
# -*- coding:utf8 -*-
"""TOp module."""
import os

__version__ = '0.0.1'


class Setting():
    def __init__(self):
        self._api_key = os.environ.get('IDCF_DNS_API_KEY')
        self._secret_key = os.environ.get('IDCF_DNS_SECRET_KEY')

    @property
    def api_key(self):
        return self._api_key

    @property
    def secret_key(self):
        return self._secret_key


def find_settings():
    return Setting()
