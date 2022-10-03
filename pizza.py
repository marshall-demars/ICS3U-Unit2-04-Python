#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Sept 2022
# This program calculates cost of a pizza
#    with user input


import constants


def main():
    # this function calculates cost of a pizza

    # input
    diameter = int(
        input("Enter the diameter of the pizza you would " + "like (inch): ")
    )

    # process
    sub_total = constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("\nThe cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))

    print("\nDone.")


if __name__ == "__main__":
    main()
