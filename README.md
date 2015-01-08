uniqtoken
=========

**"uniqtoken" is DEPRECATED!**  
Please see new version "uqid": https://github.com/denis-ryzhkov/uqidpy

Simple generator of unique tokens.

Usage:

    pip install uniqtoken
    from uniqtoken import uniqtoken

    token1 = uniqtoken()
    token2 = uniqtoken()
    assert token1 != token2

* Starts with a sequence random enough to be indexed efficiently when token is used as a hash key.
* This random sequence is long enough to be hard to guess.
* Ends with explicit timestamp with precision about 0.01 seconds (system dependent) to be more unique.
* Is more than 3x faster than standard `uuid.uuid4()` - see tests in [`uniqtoken.py:test()`](https://github.com/denis-ryzhkov/uniqtoken/blob/master/uniqtoken.py#L41).
* Is ready to be used as a fixed length string token containing exactly 64 safe hex digits.

uniqtoken version 0.1.3  
Copyright (C) 2013 by Denis Ryzhkov <denisr@denisr.com>  
MIT License, see http://opensource.org/licenses/MIT
