'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: schema
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from .types import *


class Schema:
    @staticmethod
    def get_domains() -> typing.List['Domain']:
        '''
        Returns supported domains.
        :returns: List of supported domains.
        '''

        cmd_dict = {
            'method': 'Schema.getDomains',
        }
        response = yield cmd_dict
        return [Domain.from_response(i) for i in response['domains']]
