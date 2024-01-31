#!/usr/bin/python3
"""
Module that contains method to determine valid utf-8 encoding
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8
least significant bits of each integer.
"""


def count_bytes(val):
    """
    Function to count number of bytes used in encoding byte sequence.

    Description:
    UTF-8 encoding works as thus for different byte sequences:
    1-byte:  First byte begins with 0
    2-bytes: First byte of the 2 byte seq begins with 110
    3-bytes: First byte of the 3 byte seq begins with 1110
    4-bytes: First byte of the 4 byte seq begins with 11110

    Subsequent bytes for multi-byte encoding begins with 10

    Returns:
        Number of byte as determined from starting bits in first byte else None
        if encoding is invalid.
    """
    new_val = val & 0xFF
    s_byte_checker = [1 << 7, 0b11100000, 0b11110000, 0b11111000]
    # start_byte = [0b0, 0b11000000, 0b11100000, 0b11110000]

    for i in range(len(s_byte_checker)):
        start_byte = 0 if i == 0 else s_byte_checker[i] & ~(1 << (8 - i - 2))
        if new_val & s_byte_checker[i] == start_byte:
            return i + 1

    return None


def check_sequence(n, seq):
    """
    Helper Function to check if a sequence of bytes is valid.

    Args:
        n: Number of bytes
        seq: byte sequence

    Return True if valid else False
    """
    check_byte = 0b10 << 6
    bytes_after_first = seq[1:]
    if len(bytes_after_first) + 1 != n:
        return False
    for val in bytes_after_first:
        if val & check_byte != check_byte:
            return False

    return True


def validUTF8(data):
    """
    Method that determines if a given
    data set represents a valid UTF-8 encoding.
    """
    i = 0
    while i < len(data):
        no_bytes = count_bytes(data[i])
        if no_bytes:
            tmp_seq = data[i:i + no_bytes]
            if not check_sequence(no_bytes, tmp_seq):
                return False
            i += no_bytes
        else:
            return False
    return True
