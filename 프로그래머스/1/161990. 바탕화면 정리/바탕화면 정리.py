def solution(wallpaper):
    x_list, y_list = [], []
    
    for idx1, files in enumerate(wallpaper):
        for idx2, file in enumerate(files):
            if file == '#':
                x_list.append(idx1)
                y_list.append(idx2)
    
    # lux 좌표
    lux = min(x_list)
    
    # luy 좌표
    luy = min(y_list)
    
    # rdx 좌표
    rdx = max(x_list) + 1
    
    # rdy 좌표
    rdy = max(y_list) + 1
    
    return [lux, luy, rdx, rdy]
