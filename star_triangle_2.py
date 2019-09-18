def star_triangle_two(n):
    """
    Write a program that produce the following output giving an integer input n.

    Expected Output:

    n=3    n=4      n=6
    *      *        *
    **     **       **
    ***    ***      ***
           ****     ****
                    *****
                    ******
    """

    # number of spaces.
    space = 2 * n - 2

    # outer loop to handle the number of rows.
    for row in range(0, n):

        # inner loop to handle the spaces.
        for j in range(0, space):
            print(end=" ")
        # decrease the row for each row.
        space = space - 1
        # print stars
        for j in range(0, row + 1):
            print("*", end="")
        print("\r")


# Ask for user input for number of rows they would like.
n = int(input("Enter a number: "))
star_triangle_two(n)
