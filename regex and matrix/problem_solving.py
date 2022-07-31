import numpy as np
import re

# Uncomment and implement two of the following.  Refer to the Problem solving brief for specifications.

def censor(s):
    a = re.subn(("\\ba\\b"), "#", s, flags=re.IGNORECASE)
    an = re.subn(("\\ban\\b"), "##", a[0], flags=re.IGNORECASE)
    the = re.subn(("\\bthe\\b"), "###", an[0], flags=re.IGNORECASE)
    if the[0] != s:
        return the[0] + (" <n10775676>")
    return the[0]

def fertiliser(an, ap, bn, bp, n, p):
    fertMatrix = np.array([[an, bn], [ap, bp]])
    cropMatrix = np.array([[n], [p]])

    # Check if invertible
    if (np.linalg.det(fertMatrix) == 0):
        return None
    resultMatrix = np.matmul(np.linalg.inv(fertMatrix), cropMatrix)

    # Check if negative
    if (float(resultMatrix[0]) < 0 or float(resultMatrix[1]) < 0):
        return None
    return float(resultMatrix[0]), float(resultMatrix[1])

# def makeBet(headsOdds, tailsOdds, previousOutcome, state):
#  # bet =
#  # state =
#  return (bet, state)


# The following will be run if you execute the file like python3 problem_solving.py
# Your solutions should not depend on this code.
# The automated marker will ignore any changes to this code; feel free to modify it
# but keep the if and the indenting as is
if __name__ == '__main__':
    try:
        print(censor('aN-otter-ate-An-apple'))  # should give "### cat ate # mouse. <n1234567>"
        print(censor('I went to the store.'))
        print(censor('A cookie is a very nice thing'))
        print(censor('THe thing over there.is.tHe.best!'))
        print(censor("Don't change anything!"))
    except NameError:
        print("Not attempting censoring problem")

    try:

        print(fertiliser(1, 0, 0, 1, 2, 2))  # should give (2.0, 2.0)
        print(fertiliser(0.3, 0.2, 0.1, 0.4, 10, 20))
        print(fertiliser(0.111, 0.444, 0.322, 0.211, 5.7545, 10.111))
        print(fertiliser(0.5, 0.5, 0.5, 0.3, 10, 2))
        print(fertiliser(0.3, 0.3, 0.3, 0.3, 10, 20))
    except NameError:
        print("Not attempting fertiliser problem")

    import random

    try:
        random.seed(0)
        totalprofit = 0
        for round in range(10000):
            if random.randint(0, 1) == 0:
                headsprob = 0.7
            else:
                headsprob = 0.4

            previousOutcome = None
            state = None
            profit = 0
            odds = dict()
            for _ in range(100):
                odds['heads'] = random.uniform(1, 3)
                odds['tails'] = random.uniform(1, 3)

                bet, state = makeBet(odds['heads'], odds['tails'], previousOutcome, state)

                previousOutcome = 'heads' if random.random() < headsprob else 'tails'
                if bet == previousOutcome:
                    profit += odds[bet] - 1
                elif bet != 'no bet':
                    profit -= 1  # stake lost

            print("Probability of heads was", headsprob, "Profit was", profit)
            totalprofit += profit
        print("Average profit per run:", totalprofit / 10000)

    except NameError as e:
        print("Not attempting probability problem")