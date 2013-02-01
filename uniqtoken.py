'''
Simple generator of unique tokens.

* Starts with a sequence random enough to be indexed efficiently when token is used as a hash key.
* This random sequence is long enough to be hard to guess.
* Ends with explicit timestamp with precision about 0.01 seconds (system dependent) to be more unique.
* Is more than 3x faster than standard uuid.uuid4() - see tests in uniqtoken.py:test().
* Is ready to be used as a fixed length string token containing exactly 64 safe hex digits.

Usage:

    pip install uniqtoken
    from uniqtoken import uniqtoken

    token1 = uniqtoken()
    token2 = uniqtoken()
    assert token1 != token2

uniqtoken.py version 0.1.1
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
'''

#### import

from hashlib import sha256
from random import random
from time import time

#### valid_token_length

valid_token_length = 64

#### uniqtoken

def uniqtoken():
    return (sha256(str(random())).hexdigest().upper() + '{:X}'.format(int(time() * 100)))[-valid_token_length:]

#### test

def test():

    from uuid import uuid4
    times = dict()
    tokens = dict()

    for func in uniqtoken, uuid4:
        start = time()
        previous_tokens = set()

        for _ in xrange(10**4):
            token = str(func())
            assert token not in previous_tokens
            previous_tokens.add(token)

        times[func] = time() - start
        tokens[func] = token

    print(times)
    assert times[uniqtoken] * 3 < times[uuid4], times
    assert 32 == len(tokens[uuid4].replace('-', '')) < len(tokens[uniqtoken]) == valid_token_length, tokens

    print('OK')

if __name__ == '__main__':
    test()
