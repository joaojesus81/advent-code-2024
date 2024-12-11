import re

matrix_list = []
total_result = 0
regex_expression = r"(?=(XMAS))|(?=(SAMX))"
part2_regex_expression = r"(?=(MAS))|(?=(SAM))"
test = [["XMAS"], ["SAMX"], ["JOAO"], ["LAPA"]]
example = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

working_list = []

with open("./day4/input", "r") as file:
    for line in file:
        matrix_list.append(list(map(str, line.rstrip())))


def clean_up(input_list):
    for line in input_list:
        working_list.append(list(map(str, line)))


def look_results(clean_list):
    result = 0
    for idx1 in range(1, len(clean_list) - 1, 1):
        for idx2 in range(1, len(clean_list[idx1]) - 1, 1):
            value = clean_list[idx1][idx2]
            if value == "A":
                if (
                    clean_list[idx1 - 1][idx2 - 1] == "M"
                    and clean_list[idx1 + 1][idx2 + 1] == "S"
                ):
                    if (
                        clean_list[idx1 - 1][idx2 + 1] == "M"
                        and clean_list[idx1 + 1][idx2 - 1] == "S"
                    ):
                        result += 1
                    if (
                        clean_list[idx1 - 1][idx2 + 1] == "S"
                        and clean_list[idx1 + 1][idx2 - 1] == "M"
                    ):
                        result += 1
                if (
                    clean_list[idx1 - 1][idx2 - 1] == "S"
                    and clean_list[idx1 + 1][idx2 + 1] == "M"
                ):
                    if (
                        clean_list[idx1 - 1][idx2 + 1] == "M"
                        and clean_list[idx1 + 1][idx2 - 1] == "S"
                    ):
                        result += 1
                    if (
                        clean_list[idx1 - 1][idx2 + 1] == "S"
                        and clean_list[idx1 + 1][idx2 - 1] == "M"
                    ):
                        result += 1

    return result


print(look_results(matrix_list))


def rotate_list_90d(input_list):
    result_list = []
    for line in input_list:
        split_string = [c for c in line[0]]
        result_list.append(split_string)

    return [["".join(row)] for row in zip(*reversed(result_list))]


def rotate_list_45d(
    direction: str, input_list: list, input_matrix: list = []
) -> dict[str, list]:
    result_list = [[] for _ in range(len(input_list) * 2 - 1)]
    matrix_output = [[] for _ in range(len(input_list) * 2 - 1)]
    for idx1, h_line in enumerate(input_list):
        line = h_line[0]
        f_line = line[::-1] if direction == "ccw" else line
        for idx2, c in enumerate(f_line):
            result_list[idx2 + idx1].append(c)
            if len(input_matrix):
                matrix_output[idx2 + idx1].append(input_matrix[idx1][idx2])

    if direction == "ccw":
        formatted_list = [["".join(row)] for row in result_list]
    else:
        formatted_list = [["".join(row)[::-1]] for row in result_list]

    return {"result": formatted_list, "matrix": matrix_output}


def create_grid_pattern(input_list: list) -> list:
    result = []
    for idx1, line in enumerate(input_list):
        line_string: str = line[0]
        block = []
        for idx2 in range(len(line_string)):
            block.append({"r": idx1, "c": idx2})
        result.append(block)
    return result


# [
#     ['XMAS'],
#     ['SAMX'],
#     ['JOAO'],
#     ['LAPA']
# ]
#
# [
#     ['S'],
#     ['AX'],
#     ['MMO'],
#     ['XAAA'],
#     ['SOP'],
#     ['JA'],
#     ['L']
# ]
# [
#     ['X'],
#     ['SM'],
#     ['JAA'],
#     ['LOMS'],
#     ['AAX'],
#     ['PO'],
#     ['A']
# ]


def find_elements_in_list(input_list: list) -> int:
    result = 0
    for h_line in input_list:
        found = re.findall(regex_expression, h_line[0])
        result += len(found)
    return result


def find_elements_iter(input_list: list):
    iter_result = []
    for idx, h_line in enumerate(input_list):
        iter_result.append([])
        for m in re.finditer(part2_regex_expression, h_line[0]):
            g1_index = m.span(1)[0]
            g2_index = m.span(2)[0]
            if g1_index != -1:
                iter_result[idx].append(g1_index + 1)
            elif g2_index != -1:
                iter_result[idx].append(g2_index + 1)
    return iter_result


# example_grid_pattern = create_grid_pattern(example)
# rotated_list_45_ccw = rotate_list_45d("ccw", example, example_grid_pattern)
# rotated_list_45_cw = rotate_list_45d("cw", example, example_grid_pattern)
# find_indexes_1 = find_elements_iter(rotated_list_45_ccw["result"])
# print(find_indexes_1)
# find_indexes_2 = find_elements_iter(rotated_list_45_cw["result"])
# print(find_indexes_2)

# return elements from list in original position
# total_result += find_elements_in_list(matrix_list)

# rotate the original list 90 degrees and find results
# total_result += find_elements_in_list(rotate_list_90d(matrix_list))

# rotate the original list 45 degrees and find results
# total_result += find_elements_in_list(rotate_list_45d("ccw", matrix_list))
# total_result += find_elements_in_list(rotate_list_45d("cw", matrix_list))

# print(total_result)
