"""
Exam 3, problem 1.

Authors: Vibha Alangar, Aaron Wilkin, David Mutchler, Dave Fisher, 
         Matt Boutell, Amanda Stouder, their colleagues and 
         Ben Hawkins.  January 2019.

"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


def run_test_problem1():
    """ Tests the  problem1   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')

    format_string = '    problem1( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    x = 12
    expected = 8
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem1(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    x = 2
    expected = 1
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem1(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    x = 8
    expected = 5
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem1(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    x = 33
    expected = 21
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem1(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    x = 34
    expected = 21
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem1(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    x = 35
    expected = 34
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem1(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    x = 36
    expected = 34
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem1(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    x = 1200
    expected = 987
    print_expected_result_of_test([x], expected,
                                  test_results, format_string)
    actual = problem1(x)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)
    

def fibonacci(n):
    """ Returns the Nth fibonacci number. """
    if n == 1: return 0
    elif n == 2: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)


def problem1(n):
    """
    What comes in:
      -- An integer greater than 1:  n
    What goes out:  Returns the largest Fibonacci number that is less than n
    Side effects: None.
    Recall that the Fibonacci sequence is the series of numbers:
        0, 1, 1, 2, 3, 5, 8, ...
    where the next number is found by adding the two previous numbers.
    So the next number in this sequence would be 5 + 8 = 13.

    Examples:
     problem1(12) would return 8,
         since the next Fibonacci number (13) is greater than 12.
     problem1(2) would return 1 and
     problem1(8) would return 5.

    Type hints:
      :type n: int
      :rtype: int
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # **** IMPORTANT ****:
    # We supplied a   fibonacci   function above.
    #   For FULL credit: solve this WITHOUT calling that fibonacci function
    #      or otherwise using its code.
    #   For PARTIAL credit, call the fibonacci function as needed.
    #
    # The partial-credit version is an easier problem (in our view),
    # so you might solve the partial-credit version FIRST, save that solution,
    # and THEN try the full-credit version.
    # As always, CONTINUE to the next problem if you are STUCK on this one.
    # -------------------------------------------------------------------------
    total = 0
    num = 1
    prev_num = 0
    while n > total:
        total = num + prev_num
        prev_num = num
        num = total

    return prev_num


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results,
                                                 format_string)


def print_actual_result_of_test(expected, actual, test_results):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
