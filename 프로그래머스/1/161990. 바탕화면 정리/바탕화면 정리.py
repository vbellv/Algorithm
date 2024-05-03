def solution(wallpaper):
    files_index = []
    
    for idx1, files in enumerate(wallpaper):
        for idx2, file in enumerate(files):
            if file == '#':
                files_index.append((idx1, idx2))
    
    # lux 좌표
    lux = sorted(files_index)[0][0]
    
    # luy 좌표
    luy = sorted(files_index, key=lambda x: x[1])[0][1]
    
    # rdx 좌표
    rdx = sorted(files_index)[-1][0]
    
    # rdy 좌표
    rdy = sorted(files_index, key=lambda x: -x[1])[0][1]
    
    return [lux, luy, rdx+1, rdy+1]
