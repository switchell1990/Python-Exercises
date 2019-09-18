def star_x_shape(n):
    """

    Write a program that produce the following output giving an integer input n.

    Expected Output:

    n=1	    n=2	    n=3	    n=4     n=5
     *	    **	    * *	    *  *	*   *
	        **	     * 	     **      * *
		            * *	     **       *
			                *  *	 * *
					                *   *
    """
    # Loop created for the number of rows.
    for row in range(0, n):
        # loop created for the number of columns
        for col in range(0, n):
            # printing stars.
            if (row == col) or ((n - col - 1) == row):
                print("*", end="")
            else:
                print(" ", end="")
        print("\r")


# Ask for user input for number of rows they would like.
n = int(input("Enter a number: "))
# passing n to the function
star_x_shape(n)
