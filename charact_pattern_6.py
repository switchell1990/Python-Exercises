def top_pattern(n):
    """
    Step 1
        +

    Step 2

    A+B
    +E+
    C+D

    Step 3

    AA+BB
    A+E+B
    +EEE+
    C+E+D
    CC+DD

    Step 4

    AAA+BBB
    AA+E+BB
    A+EEE+B
    +EEEEE+
    C+EEE+D
    CC+E+DD
    CCC+DDD

    Step 5
    AAAA+BBBB
    AAA+E+BBB
    AA+EEE+BB
    A+EEEEE+B
    +EEEEEEE+
    C+EEEEE+D
    CC+EEE+DD
    CCC+E+DDD
    CCCC+DDDD


                A       +       B       E       C       D
    row 1:      4       1       4       0       0       0
    row 2:      3       2       3       1       0       0
    row 3:      2       2       2       3       0       0
    row 4:      1       2       1       5       0       0
    row 5:      0       2       0       7       0       0


    DIFFERENCE  A       +       B       E
                -1      Max:2   -1      +2



    """

    rows = n + n - 1

    matrix = []
    line = ""
    count = 0
    eCount = 0
    limit = n - 1

    half = rows // 2 + 1

    for i in range(0, half):
        if half == 1:
            print("+")

        if count == 1:
            eCount = 1

        for j in range(0, limit - count):
            line += "A"

        if half != 1:
            line += "+"

        for k in range(0, eCount):
            line += "E"

        if count > 0:
            line += "+"

        for j in range(0, limit - count):
            line += "B"

        if eCount > 0:
            eCount = eCount + 2

        matrix.append(line)
        count = count + 1
        line = ""

    print('\n'.join(matrix))


def bottom_pattern(n):
    rows = n + n - 1

    matrix = []
    line = ""
    count = 0
    eCount = 0
    limit = n - 1

    half = rows // 2

    for i in range(0, half):
        # if half == 1:
        #     break

        if count == 1:
            eCount = 1

        for j in range(0, limit - count):
            line += "C"

        line += "+"

        for k in range(0, eCount):
            line += "E"

        if count > 0:
            line += "+"

        for j in range(0, limit - count):
            line += "D"

        if eCount > 0:
            eCount = eCount + 2

        matrix.append(line)
        count = count + 1
        line = ""

    matrix = reversed(matrix)
    print('\n'.join(matrix))


def print_pattern(n):
    top_pattern(n)
    if n != 1:
        bottom_pattern(n)


n = int(input("Please enter a number: "))
print_pattern(n)
