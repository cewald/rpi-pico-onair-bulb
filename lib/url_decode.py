def url_decode(s):
    s = s.replace("+", " ")
    hex_chars = ""
    i = 0
    while i < len(s):
        if s[i] == "%":
            hex_chars += chr(int(s[i + 1 : i + 3], 16))
            i += 3
        else:
            hex_chars += s[i]
            i += 1
    return hex_chars
