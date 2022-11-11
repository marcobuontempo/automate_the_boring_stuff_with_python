import random
import logging
logging.basicConfig(filename="myProgramLog.txt", level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.info("The logging module is working.")


def get_guess():
    guess = ""
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    return guess


guess = get_guess()
toss = "tails" if random.randint(
    0, 1) == 0 else "heads"     # 0 is tails, 1 is heads
logging.debug("guess=%s, toss=%s" % (guess, toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = get_guess()
    logging.debug("guess=%s, toss=%s" % (guess, toss))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
