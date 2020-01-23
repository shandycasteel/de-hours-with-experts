#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])
    

def next_biggest_number(num):
    #TODO: Implement me!

    numbers = [int(x) for x in str(num)]
    num_size = len(numbers)

    for i in range(num_size-1, -1, -1):
        if i == 0:
            return -1
        if numbers[i] <= numbers[i-1]:
            continue
        else:
            map = {}
            for j in range(i, num_size):
                if numbers[i-1] < numbers [j]:
                    map[numbers[j]] = j

            temp_digit_one = numbers[i-1]
            temp_digit_two = map[sorted(map.keys())[0]]
            numbers[i-1] = numbers[temp_digit_two]
            numbers[temp_digit_two] = temp_digit_one
            numbers = numbers[0:i] + sorted(numbers[i:num_size])

            next_number = 0

            for k in range(num_size):
                next_number = next_number * 10 + numbers[k]

            return next_number
            

if __name__ == "__main__":
    main()