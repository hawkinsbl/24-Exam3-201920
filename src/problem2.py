"""
Exam 3, problem 2.

Authors: Vibha Alangar, Aaron Wilkin, David Mutchler, Dave Fisher, 
         Matt Boutell, Amanda Stouder, their colleagues and 
         Ben Hawkins.  January 2019.

"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_shape()


def run_test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('There is no automatic testing for this one; just compare it'
          'to the expected output given in the comments:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: n=5')
    shape(5)

    print()
    print('Test 2 of shape: n=3')
    shape(3)

    print()
    print('Test 3 of shape: n=9')
    shape(9)


def shape(n):
    ####################################################################
    # IMPORTANT: In your final solution for this problem,
    #   you must NOT use string multiplication.
    ####################################################################
    """
    Prints a shape with numbers on the left side of the shape,
    other numbers on the right side of the shape,
    and stars in the middle, per the pattern in the examples below.

    You do NOT need to deal with any test cases where n > 9.

    It looks like this example for n=5:
11111*
2222*1
333*12
44*123
5*1234

    And this one for n=3:
111*
22*1
3*12


    And this one for n=9:
111111111*
22222222*1
3333333*12
444444*123
55555*1234
6666*12345
777*123456
88*1234567
9*12345678

    :type n: int
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Some tests are already written for you (above).
    ####################################################################
    # IMPORTANT: In your final solution for this problem,
    #   you must NOT use string multiplication.
    ####################################################################
    for k in range(n):
        for j in range(n-k):
            print(k+1, end='')
        print("*", end="")
        for l in range(k):
            print(l+1, end="")
        print()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
