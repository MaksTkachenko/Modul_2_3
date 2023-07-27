import task_1
import task_2
import task_3


if __name__ == '__main__':
    value = int(input("Choose a task: "))
    match value:
        case 1:
            task_1.task_1()
        case 2:
            task_2.task_2()
        case 3:
            task_3.task_3()
        case _:
            print("Incorrect number")
