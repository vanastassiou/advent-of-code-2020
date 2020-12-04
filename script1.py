expense_list = []
with open("input.txt") as expense_file:
  for line in expense_file:
    expense_list.append(int(line))

## Part 1

for current_expense in expense_list: 
  unknown_expense = 2020 - current_expense
  if unknown_expense in expense_list:
    print(unknown_expense * current_expense)