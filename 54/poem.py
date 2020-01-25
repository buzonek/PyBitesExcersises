INDENTS = 4


def print_hanging_indents(poem):
    lines = poem.split('\n')
    result = []
    for index, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        elif not lines[index - 1]:
            result.append(line + '\n')
        else:
            result.append('    ' + line + '\n')
    print(''.join(result).strip())
