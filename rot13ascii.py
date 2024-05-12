#!/bin/python3

"""
add 13 to each ascii character -> b64 -> subtract 13 from each ascii character pretty simple (:
"""

import base64
import fileinput
import sys

ROT_AMOUNT = 13

def main():
    """main"""
    should_decode = False
    if "-d" in sys.argv:
        sys.argv.remove('-d')
        should_decode = True
    text = ""
    for line in fileinput.input():
        text += line
    print(decode(text) if should_decode else encode(text))
    # print(rot(13, "I followed the rules"))
    return 0

def encode(string):
    """yeah good luck reading this one (:"""
    return rot(-ROT_AMOUNT, bytes_to_str(base64.b64encode(bytes(rot(ROT_AMOUNT, string), "UTF-8"))))

def decode(string):
    """the reverse"""
    return rot(ROT_AMOUNT, bytes_to_str(base64.b64decode(bytes(rot(-ROT_AMOUNT, string), "UTF-8"))))

def rot(amount, string):
    """rotate string by amount"""
    chars = list(string)
    for i, char in enumerate(chars):
        if char.isalpha():
            if char.islower():
                chars[i] = chr(ord('a') + (ord(char) - ord('a') + amount) % 26)
            else:
                chars[i] = chr(ord('A') + (ord(char) - ord('A') + amount) % 26)
    return "".join(chars)

def bytes_to_str(byte_array):
    """convert bytearray to string"""
    return byte_array.decode("UTF-8")

if __name__ == "__main__":
    main()
