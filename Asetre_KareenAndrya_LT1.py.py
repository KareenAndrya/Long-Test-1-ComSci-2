# Filled Boxes and Loose Notebooks Calculator
notebooks = int(input("Total number of notebooks:"))
box_capacity = int(input("How many can fit in a box:"))

full = notebooks // box_capacity # gets the number of boxes filled
print("the number of full boxes is", + full)
loose = notebooks % box_capacity # gets the number of left over notebooks
print("the number of loose notebooks is", + loose)

# This conditional statement tells that no boxes were filled.
if notebooks < box_capacity:
    print("no box was filled")

