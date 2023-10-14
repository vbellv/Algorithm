def solution(strings, n):
    string_list = [(string[n], string) for string in strings]
    string_list = sorted(string_list, key=lambda x: (x[0], x[1]))

    return [string[1] for string in string_list]