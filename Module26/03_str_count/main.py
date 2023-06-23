import os


def count_lines(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                linest = f.readlines()
                code_lines = 0
                for line in linest:
                    stripped_line = line.strip()
                    if stripped_line and not stripped_line.startswith('#'):
                        code_lines += 1
                yield code_lines


for lines in count_lines('C:/Users/nana/PycharmProjects/pythonProject9'):
    print(lines)

# зачтено
# P.S. офигеть, он yield использовал, оказывается для этого нужно в тз уточнять
