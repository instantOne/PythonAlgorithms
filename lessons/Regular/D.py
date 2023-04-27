import re
import sys

REGEX_MASK = r'\$v_([a-zZ-Z0-9])\$|\$v_{([0-9A-Za-z\w]+)}\$'
REGEX_SUB = r'v[\1\2]'

for line in sys.stdin:
    res = re.sub(REGEX_MASK, REGEX_SUB, line)
    print(res, end='')
