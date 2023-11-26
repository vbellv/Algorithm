def solution(data, ext, val_ext, sort_by):
    data_dict = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    new_data = []
    
    for datum in data:
        if datum[data_dict[ext]] < val_ext:
            new_data.append(datum)
            
    return sorted(new_data, key=lambda x: x[data_dict[sort_by]])