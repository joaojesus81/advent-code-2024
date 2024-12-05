def pass_sorting(record: list) -> bool:
    return (
        True
        if sorted(record) == record or sorted(record, reverse=True) == record
        else False
    )


def pass_distance(record: list) -> bool:
    data_list = record
    result = True
    while len(data_list) >= 2:
        if (
            abs(data_list[0] - data_list[1]) >= 1
            and abs(data_list[0] - data_list[1]) <= 3
        ):
            result = True
        else:
            result = False
            break
        data_list = data_list[1:]
    return result


def main() -> int:
    formatted_list = []
    # read from input
    with open("./day2/input", "r") as file:
        for line in file:
            formatted_list.append(line.rstrip().split(" "))
    safe = 0
    for record in formatted_list:
        int_record = [int(x) for x in record]
        result = pass_sorting(int_record) and pass_distance(int_record)
        if result is True:
            safe += 1
    return safe


print(main())
