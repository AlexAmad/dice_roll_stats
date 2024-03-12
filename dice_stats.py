from itertools import product
from math import prod
import matplotlib.pyplot as plt


class Die:
    def __init__(self, faces, rolls):
        self.faces = faces
        self.values = list(range(1, self.faces + 1))
        self.max = self.faces
        self.rolls = rolls
        self.min = self.rolls


def compute_all_combinations(*lists):
    combinations = product(*lists)
    result = [sum(comb) for comb in combinations]
    return result


def compute_min(*dice):
    return sum([die.min for die in dice])


def compute_max(*dice):
    return sum([die.faces * die.rolls for die in dice]), prod(
        [die.faces**die.rolls for die in dice]
    )


def value_with_max_prob(configurations):
    max_value = max(configurations.values())
    return [key for key, value in configurations.items() if value == max_value]


def count_values(lst, constant):
    count_dict = {}
    for value in lst:
        value += constant
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict


def collect_possible_rolls(*dice):
    return [die.values for die in dice for _ in range(die.rolls)]


if __name__ == "__main__":

    n_d2 = int(input("Number of d2: "))
    n_d4 = int(input("Number of d4: "))
    n_d6 = int(input("Number of d6: "))
    n_d8 = int(input("Number of d8: "))
    n_d10 = int(input("Number of d10: "))
    n_d12 = int(input("Number of d12: "))
    constant = int(input("Constant value: "))

    all_faces = [2, 4, 6, 8, 10, 12]
    all_rolls = [n_d2, n_d4, n_d6, n_d8, n_d10, n_d12]
    dice = [Die(face, roll) for face, roll in zip(all_faces, all_rolls)]

    min_ = compute_min(*dice)
    max_, number_different_outputs = compute_max(*dice)
    possible_rolls = collect_possible_rolls(*dice)

    res = compute_all_combinations(*possible_rolls)
    print(f"{possible_rolls=}")

    all_possible_outcomes = count_values(res, constant)
    max_output = value_with_max_prob(all_possible_outcomes)
    print(f"{max_output}")

    xvalue = list(all_possible_outcomes.keys())
    yvalue = [el / number_different_outputs for el in all_possible_outcomes.values()]

    plt.plot(xvalue, yvalue, "r+")

    for i in range(len(all_possible_outcomes)):
        plt.text(xvalue[i], yvalue[i], xvalue[i], ha="center", va="bottom")

    plt.xlabel("Output value")
    plt.ylabel("Probability")
    plt.show()
