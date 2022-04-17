def solution(files):
    file_list = []
    for file in files:
        count1 = 0
        count2 = 0
        for i in range(len(file)):
            if not file[i].isdigit(): 
                count1 += 1
            else: 
                break
        for i in range(count1, len(file)):
            if file[i].isdigit():
                count2 += 1
            else:
                break
        head = file[:count1]
        number = file[count1:count1+count2]
        tail = file[count1+count2:]
    
        file_list.append([head, number,tail])
    file_list.sort(key=lambda x: [x[0].lower(), int(x[1])])
    
    answer = [''.join(file) for file in file_list]
    return answer