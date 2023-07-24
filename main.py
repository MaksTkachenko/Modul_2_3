import task_1


if __name__ == '__main__':
    value = int(input("Choose a task: "))
    match value:
        case 1:
            task_1.task_1()
        case _:
            print("Incorrect number")
