def solution(arr, query):
    for index, number in enumerate(query):
        if index % 2 == 0:
            arr = arr[:number+1]
        else:
            arr = arr[number:]
    return arr
