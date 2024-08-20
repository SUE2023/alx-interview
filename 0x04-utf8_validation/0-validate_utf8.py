#!/usr/bin/python3
""" Validate UTF8 Representation"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0  # Tracks the number of continuation bytes expected

    for byte in data:
        # Mask to extract the 8 LSB(since data might be > 8 bits)
        byte = byte & 0xFF

        if number_bytes == 0:
            # Determine bytes in the UTF-8 character based on the first byte
            if (byte >> 5) == 0b110:  # 2-byte character
                number_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                number_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                number_bytes = 3
            elif (byte >> 7):  # Single-byte(ASCII) character to have 0 in MSB
                return False
        else:
            # Check if this byte is a valid continuation byte
            if (byte >> 6) != 0b10:  # Continuation bytes must start with '10'
                return False
            number_bytes -= 1

    # If all characters have been validated, number_bytes should be 0
    return number_bytes == 0
