text = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

# text = """
#                           To be, or not to be, that is the question:
#                           Whether 'tis nobler in the mind to suffer
#
#                           The slings and arrows of outrageous fortune,
#                           Or to take Arms against a Sea of troubles,
#                           """

rosetti_formatted = """
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
"""

INDENTS = 4


def print_hanging_indents(poem):
    lines = poem.split('\n')
    result = []
    for index, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        elif not lines[index-1]:
            result.append(line + '\n')
        else:
            result.append('\t' + line + '\n')
    print(''.join(result).strip())


print_hanging_indents(text)

