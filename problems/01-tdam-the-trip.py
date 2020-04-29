# the trip
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=29&page=show_problem&problem=1078

from decimal import Decimal
import math

# compute, from a list of expenses, the minimum amount of money that must achange hands in order to equalize (within a cent) all the students' costs.

def equalize_expenses(expenses = []):
    to_equalize = 0

    # get average of all expenses
    average = float(Decimal(sum(expenses) / len(expenses) * 1.0).quantize(Decimal('.01'), rounding="ROUND_UP"))

    # iterate through all expenses
    for expense in expenses:
        
        # add average - expense to amount needed to equalize
        # if this expense is more than the average
        if expense > average:
            to_equalize += average - expense

    return abs(to_equalize)


if __name__ == "__main__":
    result = equalize_expenses([15.00, 15.01, 3.00, 3.01])
    print(f'the result is {result}')