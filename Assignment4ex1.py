
start = input()

valid = False
while valid == False: 
    if start[0].isalpha():
        end = input()
        if (end[0].isalpha() and start[0] < end[0]):
            for a in range (ord(start[0]), ord(end[0]) + 1 , 1):
                print (chr(a), end = " ")
            valid = True
        else: 
            start = input('start')
    else:
        start = input('start')