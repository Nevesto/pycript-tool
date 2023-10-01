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









original_data = "secreto"
base64_calculated = calculate_base64(original_data.encode('utf-8'))

print("Calculated Base64:", base64_calculated)