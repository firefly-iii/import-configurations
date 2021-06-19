#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

KEYWORDS = ['Verwendungszweck', 'Zahlungsempfänger', 'Zahlungsreferenz', 'IBAN Zahlungsempfänger', 'BIC Zahlungsempfänger', 'Auftraggeber', 'IBAN Auftraggeber', 'BIC Auftraggeber']

is_in = lambda x, y : len([p for p in x if p in y])

def get_part(line, keyword, match_num=0):
    parts = line.split(': ')
    match = parts.index([x for x in parts if keyword in x][match_num])
    res = " ".join(parts[match+1].split(' ')[:-1])
    if res.endswith('IBAN') or res.endswith('BIC'):
        return '"'+" ".join(res.split(' ')[:-1])+'"'
    return '"'+res+'"'

with open('./orig.csv', 'r') as infile:
    for line in infile.readlines():
        line = line.replace('\n', '').strip()
        if is_in(KEYWORDS, line.split(';')[1]) > 0:
            desc = line.split(';')[1]
            src_name = get_part(desc, KEYWORDS[5]) if KEYWORDS[5] in desc else ''
            src_iban = get_part(desc, KEYWORDS[6]) if KEYWORDS[6] in desc else ''
            src_bic = get_part(desc, KEYWORDS[7]) if KEYWORDS[7] in desc else ''
            dst_name = get_part(desc, KEYWORDS[1]) if KEYWORDS[1] in desc else src_name
            dst_iban = get_part(desc, KEYWORDS[3]) if KEYWORDS[3] in desc else src_iban
            dst_bic = get_part(desc, KEYWORDS[4]) if KEYWORDS[4] in desc else src_bic
            usage = get_part(desc, KEYWORDS[0]) if KEYWORDS[0] in desc else ''
            ref = get_part(desc, KEYWORDS[2]) if KEYWORDS[2] in desc else usage
            note = desc
            print(line.replace(desc, ref)+dst_name+';'+dst_iban+';'+dst_bic+';'+usage+';'+note+';')
        else:
            print(line+';;;;;')
