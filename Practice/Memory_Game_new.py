# Guessing a four digit number

import random

secret_no = 0
number_list = [2456,2457,2458,2459,2467,2468,2469,2478,2479,2489, 2567,2568,2569,2578,2579,2589,2678,2679,2689,2789, 3456,3457,3458,3459,3467,3468,3469,3478,3479,3489] 
secret_no = random.choice(number_list)
#print(secret_no)
secret_digit = [int(secret_no / 1000), int((secret_no / 100) % 10), int((secret_no / 10) % 10), secret_no % 10]

guess_no = 0
while (guess_no != secret_no):
    guess_no = 0
    guess_no = int(input("Enter a four digit number without repeated numbers: "))

    if secret_no == guess_no:
        print("Congrats!!! You guessed the right number ", str(secret_no))

    guess_digit = []
    guess_digit = [int(guess_no / 1000), int((guess_no / 100) % 10), int((guess_no / 10) % 10), guess_no % 10]
    
    no_digits_in_right_pos = 0
    no_right_digits = 0
    
    i = 0
    while i < 4:
        if str(secret_digit[i]) in str(guess_digit):
            no_right_digits += 1
        i += 1
    print("No of right digits: ", str(no_right_digits))

    j = 0
    while j < 4:
        if guess_digit[j] == secret_digit[j]:
            no_digits_in_right_pos += 1
        j += 1
    print("No of digits in right position: ", str(no_digits_in_right_pos))

    if no_digits_in_right_pos == 4:
        print("Congrats!!! You guessed the right number ", str(secret_no))
        print("Hop you enjoyed the game, PLAY AGAIN!!!!")
