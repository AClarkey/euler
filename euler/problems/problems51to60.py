"""Project Euler: Problems 41 to 50"""
import time
import string
import math
import itertools

import statistics
from statistics import mode
from tkinter.filedialog import test


from euler import helper, prime


def problem_51(length: int, choose: int, target: int):
    """
    By replacing the 1st digit of the 2-digit number *3, it turns out that
    six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family:
    56003, 56113, 56333, 56443, 56663, 56773, and 56993.
    Consequently 56003, being the first member of this family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number
    (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
    """
    upper = 10 ** (length)
    lower = upper // 10

    primes = prime.eratosthenes_sieve_prime(upper)

    choose = itertools.combinations(range(length), choose)
    max = 0

    for i in choose:
        for y in range(lower, upper):
            if primes[y]:
                common = []

                for b in range(0, 10):
                    temp = list(str(y))
                    for a in i:
                        temp[a] = str(b)
                    if primes[int("".join(temp))]:
                        common.append("".join(temp))

                if len(common) == target:
                    if common[0][1] != "0":
                        output = common[0]
                    break
    return output


def problem_52(factors: int) -> int:
    """
    It can be seen that the number, 125874, and its double, 251748,
    contain exactly the same digits, but in a different order.
    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    """

    def list_of_digits(num: int) -> list:
        """returns a list of digits"""
        digits = list(str(num))
        digits.sort()
        return digits

    n = 1
    while True:
        flag = True
        for i in range(2, factors + 1):
            if list_of_digits(n) != list_of_digits(n * i):
                flag = False
                break
        if flag:
            break
        n += 1

    return n


def problem_53():
    """
    How many, not necessarily distinct, values of (n / r) for 1<=n<=100, are greater than one-million?
    """

    def num_combinations(items: int, choose: int) -> int:
        """calcs number of combinations"""
        return math.factorial(items) // (
            math.factorial(choose) * (math.factorial(items - choose))
        )

    count = 0
    for i in range(1, 101):
        for y in range(1, i):
            if num_combinations(i, y) > 1000000:
                count += 1
    return count


def problem_54(filename: str) -> int:
    """
    The file, poker.txt, contains one-thousand random hands dealt to two players.
    Each line of the file contains ten cards (separated by a single space):
    the first five are Player 1's cards and the last five are Player 2's cards.
    You can assume that all hands are valid (no invalid characters or repeated cards),
    each player's hand is in no specific order, and in each hand there is a clear winner.
    How many hands does Player 1 win?
    """

    list_of_hands = []

    with open(f"./data/{filename}", "r", encoding="utf-8") as file:
        for line in file:
            list_of_hands.append(line.strip().split(" "))

    deck_suits = ("S", "C", "D", "H")
    deck_cards = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")

    def hand_value(hand: list) -> int:
        """determine value of a hand"""

        final_hand = {
            0: None,  # "High Card"         DONE, suit buggy
            1: None,  # "One Pair"          DONE, suit buggy
            2: None,  # "Two Pairs"         DONE, suit buggy
            3: None,  # "Three of a Kind"   DONE
            4: None,  # "Straight"          DONE
            5: None,  # "Flush"             DONE
            6: None,  # "Full House"        DONE
            7: None,  # "Four of a Kind"    DONE
            8: None,  # "Straight Flush"    DONE
            9: None,  # "Royal Flush"       DONE
        }

        cards = ["".join(hand)[i] for i in range(0, 10, 2)]
        suits = ["".join(hand)[i] for i in range(1, 10, 2)]

        # ONE, TWO PAIR, THREE, FOUR of a kind
        pair_counter = 0
        for i in hand:
            count = cards.count(i[0])
            if count == 2:
                if pair_counter > 1:
                    final_hand[2] = (deck_cards.index(i[0]), deck_suits.index(i[1]))
                else:
                    final_hand[1] = (deck_cards.index(i[0]), deck_suits.index(i[1]))
                pair_counter += 1

            if count == 3:
                final_hand[3] = (deck_cards.index(i[0]), deck_suits.index(i[1]))

            if count == 4:
                final_hand[7] = (deck_cards.index(i[0]), deck_suits.index(i[1]))

        # STRAIGHT
        card_ranks = [deck_cards.index(i) for i in cards]
        card_ranks.sort()
        start = card_ranks[0]
        straight = True
        for i in card_ranks[1:5]:
            if i - start != 1 or i - start != 12:
                straight = False
        if straight:
            final_hand[4] = (card_ranks[-1], None)

        # FLUSH
        if len(set(suits)) == 1:
            final_hand[5] = (True, deck_suits.index(hand[0][1]))

        # FULLHOUSE
        if final_hand[1] is not None and final_hand[3] is not None:
            final_hand[6] = final_hand[3]

        # STRAIGHT FLUSH
        if final_hand[4] is not None and final_hand[5] is not None:
            final_hand[8] = (final_hand[4][0], final_hand[5][1])

        # STRAIGHT FLUSH
        if final_hand[8] is not None:
            if final_hand[8][0] == 12:
                final_hand[9] = final_hand[8]

        # HIGH CARD
        for key, value in reversed(final_hand.items()):
            if value != None:
                break
            if key == 0:
                print(card_ranks[-1], deck_cards[card_ranks[-1]])
                final_hand[0] = (card_ranks[-1], None)

        # FINAL
        for key, value in reversed(final_hand.items()):
            if value != None:
                return (key, value)

    def who_wins(one_value: tuple, two_value: tuple) -> str:
        # print(one_value, two_value)
        if one_value[0] > two_value[0]:
            return "P1"
        if one_value[0] == two_value[0]:
            if one_value[1][0] > two_value[1][0]:
                return "P1"
            elif one_value[1][0] < two_value[1][0]:
                return "P2"
            else:
                return "Tied hands"
        return "P2"

    for i in list_of_hands[0:1]:
        p1_hand = i[0:5]
        p2_hand = i[5:10]
        outcome = who_wins(hand_value(p1_hand), hand_value(p2_hand))
        print(p1_hand, hand_value(p1_hand), p2_hand, hand_value(p2_hand), outcome)


if __name__ == "__main__":
    # start = time.time()

    answer = problem_54("p054_poker.txt")

    # end = time.time()
    # runtime = end - start
    # print(f"Answer: {answer}, Runtime: {'%.3f' % runtime} seconds")
