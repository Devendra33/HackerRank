def print_formatted(number):
    n = number
    space = ' ' * len(bin(n)[2:])

    for i in range(1, number + 1):
        end = '\n'
        if i == n:
            end = ''
        first = str(i)
        second = oct(i)[2:]
        third = hex(i)[2:].upper()
        four = bin(i)[2:]
        ns = len(space)
        print(f'{(ns - len(first))*" "}{first}{(ns - len(second) + 1)*" "}{second}{(ns - len(third) + 1)*" "}{third}{(ns - len(four) + 1)*" "}{four}',
              end=end)


