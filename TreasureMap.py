line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

user_input=input("Enter Input:")
letter=user_input[0]
columns=['A','B','C']
row_number=int(user_input[1])
column_number=int(columns.index(letter) + 1)
map[row_number -1][column_number -1]='X'
  

print(f"{line1}\n{line2}\n{line3}")