#from attr import set_run_validators


secret_no = 1980
print(secret_no)
secret_digit = [int(secret_no / 1000), int((secret_no / 100) % 10), int((secret_no / 10) % 10), secret_no % 10]
print(secret_digit)

guess_no = 0
while (guess_no != secret_no):
    guess_no = 0
    guess_no = int(input("Enter a 4-digit guess: "))

    if secret_no == guess_no:
        print("Congrats!!! You guessed the right number ", str(secret_no))

    print(guess_no)
    guess_digit = [int(guess_no / 1000), int((guess_no / 100) % 10), int((guess_no / 10) % 10), guess_no % 10]
    #print(guess_digit)
    
    sub = 0
    ship = 0
    
    i = 0
    sub_pos_list = []
    
    while i < 4:
        if guess_digit[i] == secret_digit[i]:
            sub += 1
            sub_pos_list.extend([i])
        i += 1
    print("No of Subs: ", str(sub))
    print(sub_pos_list)

'''
    sub_len = len(sub_pos_list)
    print(sub_len)


    if sub_len == 0:
        loop_len = 4
    elif sub_len == 1:
        loop_len = 3
    elif sub_len == 2:
        loop_len = 2
    elif sub_len == 3:
        loop_len = 1

    n = 0
    m = 0
    ship = 0
    
    while n < loop_len:
        if guess_digit[n] == sub_pos_list.index(n):
            break
        else:
            while m < 4:
                if guess_digit[n] == secret_digit[m]:
                    m += 1
                    ship += 1
                else:   
                    m += 1
            n += 1
    
    print("No of Ships: ", str(ship))

    n = 0
    m = 0
    ship = 0  

    for n in range(0,4):
        for m in range(0,4):
            if guess_digit[n] == sub_pos_list.index(m):
                break
            elif guess_digit[n] == secret_digit[m]:
                ship += 1
            else:   
                pass
    print("No of Ships: ", str(ship))
'''    


if sub == 4:
        print("You guessed the right number")
