def encrypt_with_power(m, k):
    """
    >>> encrypt_with_power('Hello',250)
    '²A|lo'
    >>> encrypt_with_power(encrypt_with_power('Hello',123),123)
    'Hello'
    >>> encrypt_with_power(encrypt_with_power('Cryptography',10),10)
    'Cryptography'
    """
    l = []
    for c in m:
        l.append(ord(c) ^ k)
        k **= 2
        k %= 256
    return "".join(map(chr, l))

def encrypt_with_power2(m, k, task):
    """
    >>> encrypt_with_power2('Hello',253,'encrypt')
    'µl=Í.'
    >>> encrypt_with_power2('Hello2',131,'encrypt')
    'Ël=Í.³'
    >>> encrypt_with_power2(encrypt_with_power2('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_with_power2(encrypt_with_power2('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    """
    l = []
    prevc = None
    for c in map(ord, m):
        if k <= 1:
            if task == "encrypt":
                k = prevc
            else:
                k = l[-1]
        l.append(c ^ k)
        k **= 2
        k %= 256
        prevc = c
    return "".join(map(chr, l))


def swap_lower_and_upper_bits(byte):
    """
    >>> swap_lower_and_upper_bits(0)
    0
    >>> swap_lower_and_upper_bits(1)
    16
    >>> swap_lower_and_upper_bits(2)
    32
    >>> swap_lower_and_upper_bits(8)
    128
    >>> bin(swap_lower_and_upper_bits(0b1111))
    '0b11110000'
    >>> bin(swap_lower_and_upper_bits(0b10011010))
    '0b10101001'
    """
    return byte >> 4 | byte << 4 & 0xff


def encrypt_with_power_and_swap(m, k, task):
    """
    >>> encrypt_with_power_and_swap('Hello',11,'encrypt')
    '4ÁÕÐê'
    >>> encrypt_with_power_and_swap(encrypt_with_power_and_swap('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_with_power_and_swap(encrypt_with_power_and_swap('Cryptography',12,'encrypt'),12,'decrypt')
    'Cryptography'
    """
    l = []
    prevc = None
    for c in map(ord, m):
        if task == "encrypt":
            if k <= 1:
                k = prevc
            l.append(swap_lower_and_upper_bits(c) ^ k)
        else:
            if k <= 1:
                k = l[-1]
            l.append(swap_lower_and_upper_bits(c ^ k))
        k **= 2
        k %= 256
        prevc = c
    return "".join(map(chr, l))

print(repr(encrypt_with_power2('I\x16i\tE\x0e¦ó\x13´x\x11',10,'decrypt')))