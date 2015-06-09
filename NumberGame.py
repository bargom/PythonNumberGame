import random, re

def test_number(guess, real):
    if validate_number(guess):
        plus, same = 0, set(guess) & set(real)
        for i,x in enumerate(same):
            plus += (guess.index(str(x))==real.index(str(x)))
        return plus, len(same)-plus
    return (0,0)
    
def validate_hint(strHint):
    if not re.match('\+(\d)\-(\d)', strHint):
        print("Hint should be exact 4 characters and should start with + and continue with -")
        print("Example: +2-1 or +1-0 or +0-0 or +0-1")
        return False
    return True
    
def validate_number(strNumber):
    if not re.match('^\d\d\d\d$', strNumber):
        print("Number should be exact 4 characters without letters")
        print("Example: 4567")
        return False
    return True
    
currentNums = [str(x) for x in range(1000, 9999) if len(set(str(x))) == len(list(str(x)))]

print("""Game start, I am holding a number between 1000 to 9999, try to guess! For each guess, I will give a hint, + numbers means the location is correct. - numbers means it exists but location is not correct.""")
computer_number = random.choice(currentNums)

while True:
    user_number = input("Enter your guess> ")
    if user_number == "hint":
        print(computer_number)
    result = test_number(user_number, computer_number)
    if result == (4, 0):
        print("Well done, you found the number")
        break
    print("Hint is: +{} -{}".format(*result))
counter = 0
print("Now I will guess your number")
print("Enter my hints in the format +n-m without spaces")
print("if the guess not exists, enter zero like +2-0")

while True:
    my_guess = random.choice(currentNums)
    hint = input("My guess is {}, please enter hint>".format(my_guess))
    if not validate_hint(hint):
        continue
    counter += 1
    if hint == "+4-0":
        print("I found it in {} tries".format(counter))
        break
    hintTuple = int(hint[1]), int(hint[3])
    new_list = []
    for n in currentNums:
        if test_number(n, my_guess) == hintTuple:
            new_list.append(n)
    if len(new_list) == 0:
        print("Hints are not correct, the number should be one of this values:")
        print(currentNums)
        counter -= 1
    else:
        currentNums = new_list