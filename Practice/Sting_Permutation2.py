userInput = input(""); # cat
myStr = "";
count = 0;
myOtherStr = "";
for x in userInput:
    myStr = x;
    nCount = 0;
    myOtherStr = "";
    for y in userInput:
        if nCount != count:
            myOtherStr += y;
        nCount+= 1;
    print(myStr + myOtherStr);
    print(myStr + myOtherStr[1] + myOtherStr[0]);
