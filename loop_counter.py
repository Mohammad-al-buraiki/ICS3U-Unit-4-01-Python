# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a loop a while loop


def main():
    # this function uses a while loop
    loop_counter = 0
    sum = 0

    # input
    print("")
    positive_integer = input("Enter how many times to repeat: ")

    # process and output
    try:
        positive_integer = int(positive_integer)
        while loop_counter < positive_integer:
            print("{0} time through loop.". format(loop_counter))
            loop_counter = (loop_counter + 1)
            sum = (sum + loop_counter)
        print("the sum {0} .". format(sum))

    except Exception:
        print("sorry, this was not an integer")


if __name__ == "__main__":
    main()
