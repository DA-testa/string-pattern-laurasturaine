def read_input():
    # lasa paraugu un tekstu no inputa
    inputs = input()
    
    if 'I' in inputs:
        para=input().rstrip() #ievada paraugu
        string=input().rstrip() #ievada tekstu
    elif 'F'in inputs:
        with open("tests/06","r") as file:  #atver failu lasīšanai
            para=file.readline().rstrip() #nolasa paraugu un tekstu no faila
            string=file.readline().rstrip()
    else:
        print('wrong input')
    return (para, string)

def print_occurrences(output):
    print(' '.join(map(str, output))) #printē sarakstu, atdalot katru vērtību ar atstarpi

def get_occurrences(para, teksts):
    paral=len(para) #nosaka parauga garumu
    tekstal=len(teksts) #nosaka teksta garumu
    parah=hash(para) #nosaka parauga koda vērt
    lhash=hash(teksts[:paral]) #nosaka pirmo apakšvirknē garuma paraugu teksta koda vērtību 
    rez=[] #jauns sarkasts rezultātiem
    for x in range(tekstal-paral+1):
        if parah==lhash:
            if para==teksts[x:x+paral]:
                rez.append(x)
        if x<tekstal-paral:
            lhash=hash(teksts[x+1:x+1+paral])
    return rez

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
