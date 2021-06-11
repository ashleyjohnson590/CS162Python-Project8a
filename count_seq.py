#Author: Ashley Johnson
#Date: 5/13/2021
#Description: Program generates a sequence that enumerates how many there are of each digit in the previous
#term. Generator function keeps going indefinitely and yields the terms of the sequences as strings.
def count_seq():
    numbers = '2'
    count = 0

    if count == 0:
        yield numbers

    while True:
        i = 0
        count = 0
        new_numbers = ""
        number = numbers[i]
        count += 1
        if len(numbers) == 1:
            numbers = str(count) + number
            yield numbers
        else:
            while i < len(numbers):
                number = numbers[i]
                i += 1
                if i == len(numbers):
                    numbers = new_numbers + str(count) + number
                    count = 0
                    index = 0
                    i = len(numbers) + 1
                    yield numbers
                elif number == numbers[i]:
                    count += 1
                else:
                    new_numbers = new_numbers + str(count) + number
                    count = 1


def main():
    gen = count_seq()
    i = 0
    while i < 10:
        i += 1
        print(next(gen))

if __name__ == "__main__":


    main()
