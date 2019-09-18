def star_triangle_one(n):
    """
    Write a program that produce the following output giving an integer input n.

    Expected Output:

    n=3   n=4    n=6
    *     *      *
    **    **     **
    ***   ***    ***
          ****   ****
                 *****
                 ******
    """

    # loop created for number of rows.
    for row in range(0, n):
        # loop created for number of columns.
        for col in range(0, row+1):
            # printing stars.
            print("*", end = "")
        # ending line after each row.
        print("\r")


# Ask for user input for number of rows they would like.
n = int(input("Enter a number: "))
# passing n to the function
star_triangle_one(n)