row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
treasure_row = int(position[0]) - 1
treasure_column = int(position[1]) - 1
treasure_map[treasure_column][treasure_row] = "X"
print(f"{row1}\n{row2}\n{row3}")
