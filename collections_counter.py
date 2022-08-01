# Task:
#     Raghu is a shoe shop owner. His shop has `x` number of shoes.
#     He has a list containing the size of each shoe he has in his shop.
#     There are `n` number of customers who are willing to pay `y` amount
#     of money only if they get the shoe of their desired size.
#
#     Your task is to compute how much money Raghu earned.
#
# Input Format:
#     The first line contains `x`, the number of shoes.
#     The second line contains the space separated list of all the shoe sizes in the shop.
#     The third line contains `n`, the number of customers.
#     The next `n` lines contain the space separated values of the shoe size desired by the customer
#     and `y` , the price of the shoe.

import collections

shoes = int(input())
sizes = collections.Counter(map(int, input().split()))
customers = int(input())

income = 0

print(sizes)
for x in range(customers):
    size, price = map(int, input().split())
    if sizes[size]:
        income += price
        sizes[size] -= 1

print(income)
