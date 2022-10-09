from itertools import zip_longest


def encrypt_by_add_mod(m, k):
    """
    >>> encrypt_by_add_mod('Hello',123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    """
    return "".join(chr((ord(c) + k) % 0x100) for c in m)


def encrypt_xor_with_changing_key_by_prev_cipher(m, k, task):
    """
    >>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
    '3V:V9'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    """
    if task == "encrypt":
        return "".join(chr(k := ((ord(c) ^ k) % 0x100)) for c in m)

    if task == "decrypt":
        return "".join(chr((k ^ (k := ord(c)) % 0x100)) for c in m)


def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(m, ks, task):
    """
    >>> key_list = [0x20, 0x44, 0x54,0x20]
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt')
    'A&7D$@P'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt')
    'A%5B#GW'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'),
    ...        key_list,'decrypt')
    'abcdefg'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'),
    ...        key_list,'decrypt')
    'Hellobello, it will work for a long message as well'
    """
    return "".join(c for l in zip_longest(*(encrypt_xor_with_changing_key_by_prev_cipher(m[i::len(ks)], k, task)
                                            for i, k in enumerate(ks)))
                   for c in l if c)
