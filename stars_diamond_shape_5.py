def star_diamand_shape(n):
    """

    Write a program that produce the following output giving an integer input n.

    Expected Output:

    n=1     n=2     n=3     n=4    n=5        n=9
     *       *       *       *      *          *
             *      ***     ***    ***        ***
                     *      ***   *****      *****
                             *     ***      *******
                                    *      *********
                                            *******
                                             *****
                                              ***
                                               *
    """

    space = n // 2
    stars = 1

    # outer loop for the number of rows.
    for row in range(1, n + 1):
        # inner loop for the number of spaces.
        for j in range(1, space + 1):

            for k in range(1, stars + 1):
                print (count, end = "")
            else:



# Ask for user input for number of rows they would like.
n = int(input("Enter a number: "))
# passing n to the function
star_diamand_shape(n)
