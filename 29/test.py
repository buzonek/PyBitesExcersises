def get_index_different_char(chars):
    alpha = list(map(str.isalnum, map(str, chars)))
    if alpha.count(True) > 1:
        return alpha.index(False)
    else:
        return alpha.index(True)


inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1,9)) + ['}'] + list('abcde'),  # noqa E230
        [2, '.', ',', '!']
    )

for line in inputs:
    res = get_index_different_char(line)
    print(res)