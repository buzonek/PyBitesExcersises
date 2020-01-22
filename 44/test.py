import secrets
import string

alphabet = string.ascii_ + string.digits


def gen_key(parts=4, chars_per_part=8):
    return '-'.join(
        [''.join([secrets.choice(alphabet) for i in range(chars_per_part)]) for
         j in range(parts)])


print(gen_key(10, 10))
