def star_triangle_hollow(n):
    """
    Write a program that produce the following output giving an integer input n.

    Expected Output:

    n=1    n=2      n=3    	  n=4       n=5
    *       *        *         *         *
           * *      * * 	  * *       * *
                   *   *	 *   *     *   *
                            *     *   *     *
                                     *       *
    """
    # create a counter
    count = 0

    # Loop created for the number of rows.
    for row in range(1, n + 1):

        # Inner loop to handle the spaces.
        for space in range(row, n):
            print(" ", end="")

        # Loop to print the pattern.
        while count != (2 * row - 1):
            if count == 0 or count == 2 * row - 2:
                print("*", end="")
            else:
                print(" ", end="")
            count = count + 1
        count = 0
        print("\r")


# Ask for user input for number of rows they would like.
n = int(input("Enter a number: "))
# pass n to the function.
star_triangle_hollow(n)
