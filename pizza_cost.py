#!/usr/bin/env python3

# Created By: Amara Tie

# Date: March 4, 2025

# Calculates total cost of pizza
import constants


def main():
    #input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    #process
    subtotal = constants.LABOUR_COST + constants.LABOUR_COST+ constants.INGRED_COST * diameter 
    tax = constants.HST * subtotal
    total = subtotal + tax

    #output
    print("")
    print("The total cost is = ${:,.2f}".format(total))

if __name__ == "__main__":
    main()