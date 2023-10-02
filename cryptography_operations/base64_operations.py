def calculate_base64(data):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    result = []
    bits = 0
    buffer = 0

    for byte in data:
        buffer = (buffer << 8) | byte
        bits+= 8
        while bits >= 6:
            index = (buffer >> (bits - 6)) & 0x3F
            result.append(base64_chars[index])
            bits -= 6

    if bits > 0:
        index = (buffer << (6 - bits)) & 0x3F
        result.append(base64_chars[index])
    
    while len(result) % 4 != 0:
        result.append('=')

    return ''.join(result)

def decode_base64(encoded_data):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    base64_mapping = {char: index for index, char in enumerate(base64_chars)}

    decoded_bytes = bytearray()
    buffer = 0
    bits = 0

    for char in encoded_data:
        if char in base64_mapping:
            buffer = (buffer << 6) | base64_mapping[char]
            bits += 6
            if bits >= 8:
                decoded_bytes.append((buffer >> (bits - 8)) & 0xFF)
                bits -= 8

    return bytes(decoded_bytes)
