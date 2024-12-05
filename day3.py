import re

expression = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
filtering_expression = r"(^.*don't\(\))|(do\(\).*don't\(\))|(do\(\).*$)"


def clean_up(text: str):
    split_dont = text.split("don't()")
    first, *rest = split_dont
    dos = [first]
    for el in rest:
        dos.append("-".join(el.split("do()")[1:]))
    return "".join(dos)


with open("./day3/input", "r") as file:
    formatted_list: str = clean_up(file.read())
    list_sets = re.findall(expression, formatted_list)
    result = 0
    for el in list_sets:
        result += int(el[0]) * int(el[1])
    print(result)
