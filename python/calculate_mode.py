def calculate_mode(list):
    
    letters = {}
    answer = []

    for x in list:
        if x in letters:
            letters[x] += 1
        else:
            letters.update({x:1})   

    letters = sorted(letters.items(), key = lambda x:x[1], reverse = True)
    
    max = letters[0][1]
    
    for k in letters:
        if k[1] == max:
            answer.append(k[0])



    return answer

        
