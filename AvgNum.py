#This program has been changed

def AverageNumber():
    num_sum = 0
    how_many_nums = int(input("How many numbers do you want to input?:\n"))
    for number in range(how_many_nums):
        current_num = int(input('what is the number?:\n'))
        num_sum = num_sum + current_num
        number += 1

    print(f'your average is {num_sum/how_many_nums}')


AverageNumber()
