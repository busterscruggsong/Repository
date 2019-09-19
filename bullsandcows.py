import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # 返回一个由 NUM_DIGITS 个不重复随机数组成的字符串
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # 返回一个由 Almost, Right 和 Wrong 组成的，用来提示用户的字符串
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Right')
        elif guess[i] in secretNum:
            clues.append('Almost')
    if len(clues) == 0:
        return 'Wrong'
    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    # 如果字符串只包含数字，返回真。否则返回假
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True


print('I am thinking of a %s-digit number. Try to guess what it is.' % NUM_DIGITS)
print('The clues I give are...')
print('When I say:    That means:')
print('  Wrong       None of the digits is correct.')
print('  Almost         One digit is correct but in the wrong position.')
print('  Right       One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a %s-digit number. You have %s guesses to get it.' % (NUM_DIGITS,MAX_GUESS))
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()
        print(getClues(guess, secretNum))
        guessesTaken += 1
        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
