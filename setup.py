from distutils.core import setup

setup(
    name='uniqtoken',
    version='0.1.2',
    description='Simple generator of unique tokens.',
    long_description='''
Usage::

    pip install uniqtoken
    from uniqtoken import uniqtoken

    token1 = uniqtoken()
    token2 = uniqtoken()
    assert token1 != token2

* Starts with a sequence random enough to be indexed efficiently when token is used as a hash key.
* This random sequence is long enough to be hard to guess.
* Ends with explicit timestamp with precision about 0.01 seconds (system dependent) to be more unique.
* Is more than 3x faster than standard ``uuid.uuid4()`` - see tests in `uniqtoken.py:test() <https://github.com/denis-ryzhkov/uniqtoken/blob/master/uniqtoken.py#L41>`_.
* Is ready to be used as a fixed length string token containing exactly 64 safe hex digits.

''',
    url='https://github.com/denis-ryzhkov/uniqtoken',
    author='Denis Ryzhkov',
    author_email='denisr@denisr.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['uniqtoken'],
)
