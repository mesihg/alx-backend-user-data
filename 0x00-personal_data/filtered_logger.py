#!/usr/bin/env python3
"""
Filtered logger file
"""
import re


def filter_datum(fields, redaction, message, separator):
    regex_p = re.compile(r'({})=[^{}]*'.format('|'.join(fields), separator))
    return regex_p.sub(r'\1={}'.format(redaction), message)
