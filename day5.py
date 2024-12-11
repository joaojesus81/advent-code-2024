example = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]

input_groups: dict[int, list] = {}
input_page_order: list = []
updates: list = []
result = 0


def clean_input() -> None:
    with open("./day5/input", "r") as file:
        for line in file:
            if "|" in line:
                leader_page, following_page = line.split("|")
                if int(leader_page) in input_groups:
                    input_groups[int(leader_page)].append(int(following_page))
                else:
                    input_groups[int(leader_page)] = [int(following_page)]
            if "," in line:
                page_order = line.split(",")
                input_page_order.append([int(x) for x in page_order])


def recur_forward(input_list, result):
    if len(input_list) == 1 or result is False:
        return result
    else:
        first_page, *rest = input_list
        check_list = []
        for page in rest:
            if first_page in input_groups:
                check_list.append(page in input_groups[first_page])
        return recur_forward(rest, any(check_list))


def recur_reverse(reverse_list, result):
    if len(reverse_list) == 1 or result is True:
        return result
    else:
        last_page, *rest = reverse_list
        check_list = []
        for page in rest:
            if last_page in input_groups:
                check_list.append(page in input_groups[last_page])
        return recur_reverse(rest, any(check_list))


def check_page_order():
    for page_order in input_page_order:
        x = recur_forward(page_order, True)
        y = recur_reverse(list(reversed(page_order)), False)
        if x is True and y is False:
            updates.append(page_order)


def check_middle_finger():
    result = 0
    for page_set in updates:
        middle_index = len(page_set) // 2
        result += page_set[middle_index]
    return result


clean_input()
check_page_order()
print(check_middle_finger())
