# for i in range(1, 501):
#     if i % 2 == 0:
#         print(i)

todo = ["Cook", "run", "study"]
todo.append("Cook")
todo.append("workout")
todo.append("study")
todo.append("laundry")
for task in todo:
    if task.__contains__("workout"):
        print("yes")
    # else:
    #     print("no")