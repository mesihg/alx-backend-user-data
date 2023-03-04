#!/usr/bin/env python3
"""
Filtered logger file
"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    regex_p = re.compile(r'({})=[^{}]*'.format('|'.join(fields), separator))
    return regex_p.sub(r'\1={}'.format(redaction), message)
