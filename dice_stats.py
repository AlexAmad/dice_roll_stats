from itertools import product
from math import prod
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

rolls_d6 = 2
d6 = Die(6, rolls_d6)
#caso 2d6
all_rolls = []
def compute_min(*dice):
    return sum([die.min for die in dice])

def compute_max(*dice):
    return sum([die.faces*die.rolls for die in dice]), prod([die.faces**die.rolls for die in dice])

d4 = Die(4, 1)
min_ = d6.rolls
min_ = compute_min(d6)


max_, number_different_outputs = compute_max(d6)

# max_ = d6.rolls*d6.max
print(min_)
print(max_)
print(number_different_outputs)


possible_rolls = []
for _ in range(d6.rolls):
    possible_rolls.append(d6.values)

print(f"{possible_rolls=}")



res = compute_all_combinations(*possible_rolls)

print(f"{res=}")


def count_values(lst):
    count_dict = {}
    for value in lst:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict

all_possible_outcomes = count_values(res)

# if __name__ == "__main__":
#     # print("Number of d2: ")
#     # n_d2 = int(input())
#     # print("Number of d4: ")
#     # n_d4 = int(input())
#     print("Number of d6: ")
#     n_d6 = int(input())
#     # print("Number of d8: ")
#     # n_d8 = int(input())
#     # print("Number of d10: ")
#     # n_d10 = int(input())
#     # print("Number of d12: ")
#     # n_d12 = int(input())
#     # print("Number of d20: ")
#     # n_d20 = int(input())