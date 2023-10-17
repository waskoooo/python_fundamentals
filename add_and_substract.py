def sum_numbers(first , second):
    return first + second


def subtract (result, third):
    return result - third


def add_and_subtract(first, second , third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num,second_num,third_num))
