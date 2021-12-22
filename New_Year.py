import os
year = input('What year would you like to work on: ')

try:
    os.makedirs(year)
except FileExistsError as e:
    print(e)

cwd = os.getcwd() + '\\' + year + '\\'

for i in range(1, 26):
    try:
        os.makedirs(os.path.join(cwd, f"day{i:02d}"))
        with open(os.path.join(cwd, f"day{i:02d}" , f'day{i:02d}.py'), 'w') as file:
            file.write(
                f"import random, math\n\ndef load():\n\twith open('day{i:02d}/day{i:02d}Input.txt') as file:\n\t\tdata = file.readlines()\n\t\td = [line.strip() for line in data]\n\treturn d\n\ninpt = load()\ndef part1(inpt):\n\treturn inpt\n\ndef part2(inpt):\n\treturn 0\n\nprint(f'Part1: " + "{part1(inpt)}\\nPart2: {part2(inpt)}')"
            )
            file.close()
        immediately_close = open(os.path.join(cwd, f"day{i:02d}", f"day{i:02d}Input.txt"), 'w')
        immediately_close.close()
    except FileExistsError as e:
        print(e)
