def solution(data, ext, val_ext, sort_by):
    data_list = ['code', 'date', 'maximum', 'remain']
    new_data = []
    
    for idx in range(len(data_list)):
        temp_data = []
        if data_list[idx] == ext:
            for datum in data:
                if datum[idx] < val_ext:
                    temp_data.append(datum)
            new_data += temp_data
    
    for idx in range(len(data_list)):
        if data_list[idx] == sort_by:
            return sorted(new_data, key=lambda x: x[idx])
