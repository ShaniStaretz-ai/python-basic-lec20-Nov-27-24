def is_valid_brackets(s1: str) -> bool:
    my_bracket_dictionary: dict[str, str] = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    for i in range(0, len(s1), 2):
        if s1[i + 1] != my_bracket_dictionary.get(s1[i]):
            return False
    return True


def non_duplicate_sorted_list(l1: list[int]) -> list[int]:
    result: list[int] = [l1[0]]

    for i in range(1, len(l1)):
        if l1[i] != l1[i - 1]:
            result.append(l1[i])
    return result


def merge_sorted_lists(l1: list[int], l2: list[int]) -> list[int]:
    result: list[int] = []
    i = 0
    n1 = len(l1)
    j = 0
    n2 = len(l2)
    while i < n1 and j < n2:
        if l1[i] == l2[j]:
            result.append(l1[i])
            result.append(l2[j])
            i += 1
            j += 1
            continue
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
            continue
        else:
            result.append(l2[j])
            j += 1

    while i < n1:
        result.append(l1[i])
        i += 1
    while j < n2:
        result.append(l2[j])
        j += 1

    return result


tested_string = "{}()[]"
print(f"Is the string '{tested_string}' is a valid brackets string:{is_valid_brackets(tested_string)}")

tested_dup_list = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]
print(f"for origin sorted list {tested_dup_list} the list without duplicate"
      f" {non_duplicate_sorted_list(tested_dup_list)}")

test_l1 = [1, 2, 4, 4, 4, 5, 5, 6, 7]
test_l2 = [1, 2, 3, 3, 4]
print(f"the merged list of {test_l1} and {test_l2} is {merge_sorted_lists(test_l1, test_l2)}")
