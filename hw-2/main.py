def hex2bin(s):
    """
    >>> hex2bin('f')
    '1111'
    >>> hex2bin('5')
    '101'
    >>> hex2bin('1')
    '1'
    """
    return f"{int(s, base=16):b}"


def bin2hex(s):
    """
    >>> bin2hex('1111')
    'f'
    >>> bin2hex('100001')
    '21'
    >>> bin2hex('1')
    '1'
    """
    return f"{int(s, base=2):x}"


def fillupbyte(s):
    """
    >>> fillupbyte('011')
    '00000011'
    >>> fillupbyte('1')
    '00000001'
    >>> fillupbyte('10111')
    '00010111'
    >>> fillupbyte('11100111')
    '11100111'
    >>> fillupbyte('111001111')
    '0000000111001111'
    """
    return "0" * ((8-len(s)) % 8) + s


def char_range(start, end):
    return map(chr, range(ord(start), ord(end) + 1))


B64CHARS = [*char_range("A", "Z"), *char_range("a", "z"), *char_range("0", "9"), "+", "/"]


def int2base64(n):
    """
    >>> int2base64(0x61)
    'YQ=='
    >>> int2base64(0x78)
    'eA=='
    """
    binstr = fillupbyte(f"{n:b}")
    binstr += "0" * ((6 - len(binstr)) % 6)
    b64str = "".join(B64CHARS[int(binstr[i:i+6], base=2)] for i in range(0, len(binstr), 6))
    b64str += "=" * ((4 - len(b64str)) % 4)
    return b64str


def hex2base64(s):
    """
    >>> hex2base64('61')
    'YQ=='
    >>> hex2base64('123456789abcde')
    'EjRWeJq83g=='
    """
    return int2base64(int(s, base=16))
