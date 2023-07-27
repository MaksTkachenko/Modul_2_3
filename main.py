import task_1
import task_2
import task_3
import task_4
import task_5
import task_6
import task_7

if __name__ == '__main__':
    value = int(input("Choose a task: "))
    match value:
        case 1:
            task_1.task_1()
        case 2:
            task_2.task_2()
        case 3:
            task_3.task_3()
        case 4:
            task_4.task_4()
        case 5:
            task_5.task_5()
        case 6:
            task_6.task_6()
        case 7:
            task_7.task_7()
        case _:
            print("Incorrect number")
