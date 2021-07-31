def main():
    #write your code below this line
    numbers = []

    while True:
        number = int(input())

        if number == 0:
            break

        numbers.append(number)

    print(numbers[0])

if __name__ == '__main__':
    main()
