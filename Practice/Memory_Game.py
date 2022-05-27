secret_no = 1980
print(secret_no)
secret_digit = [int(secret_no / 1000), int((secret_no / 100) % 10), int((secret_no / 10) % 10), secret_no % 10]
print(secret_digit)



'''
def check_sub(n):
    if guess_digit[n] == secret_digit[n]:
        sub += 1
        break
    else:   
        m += 1
    return(sub)
''' 
guess_no = 0
while (guess_no != secret_no):
    guess_no = 0
    guess_no = int(input("Enter a 4-digit guess: "))
    print(guess_no)
    guess_digit = [int(guess_no / 1000), int((guess_no / 100) % 10), int((guess_no / 10) % 10), guess_no % 10]
    #print(guess_digit)
    
    i = 0
    sub = 0
    sub_pos_list = []
    while i < 4:
        if guess_digit[i] == secret_digit[i]:
            sub += 1
            sub_pos_list.extend([i])
        i += 1
    print("No of Subs: ", str(sub))
    print(sub_pos_list)

    n = 0
    m = 0
    ship = 0  
    for n in range(0,4):
        for m in range(0,4):
            if m == sub_pos_list.index(m):
                break
            elif guess_digit[n] == secret_digit[m]:
                ship += 1
                continue
            else:   
                continue
    print("No of Ships: ", str(ship))
        



''' 
        m += 1
    elif guess_digit[n] == secret_digit[m+=1]:
        ship += 1
    elif guess_digit[n] == secret_digit[m+=1] or guess_digit[n] == secret_digit[m+=1]):
        ship += 1
        m += 1

print("Sub: ", sub)
print("Ship: ", ship)

if sub == 4:
    print("You guessed the right number")
'''