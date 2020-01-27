def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all(map(lambda x: 0 <= x <= 255, rgb)):
        raise ValueError
    result = '#'
    for value in rgb:
        result += hex(value).split('x')[1].ljust(2, '0').upper()
    return result
