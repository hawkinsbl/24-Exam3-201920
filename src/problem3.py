"""
Exam 3, problem 3.

Authors: Vibha Alangar, Aaron Wilkin, David Mutchler, Dave Fisher, 
         Matt Boutell, Amanda Stouder, their colleagues and 
         Ben Hawkins.  January 2019.

"""  # Doe: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def is_prime(n):
    """
    What comes in:  An integer n.
    What goes out:
      -- Returns True if the given integer is prime,
                 False if the given integer is NOT prime.
         Treats integers less than 2 as NOT prime.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
      -- is_prime(1)  returns  False
    Note: The algorithm used here is simple and clear but slow.
    """
    if n < 2:
        return False
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no TO DO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


def run_test_problem3():
    """ Tests the    problem3    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3  function:')
    print('--------------------------------------------------')

    format_string = '    problem3( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    number_passed = test_results[0]
    number_failed = test_results[1]

    # Test 1:
    sequence = [4, 5, 6, 7, 8, 9, 10]
    expected = 2
    copy_of_sequence = [4, 5, 6, 7, 8, 9, 10]
    expected_mutation = [4, 8, 6, 10, 8, 9, 10]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print()
    if sequence != expected_mutation:
        print('FAILED part of the above test!', color='red')
        print('BEFORE the function call, the argument is:')
        print('   ', copy_of_sequence, color='red')
        print('AFTER  the function call, the argument should be:')
        print('   ', expected_mutation, color='red')
        print('Running your code, the argument after the function call is:')
        print('   ', sequence, color='red')

        test_results[0] = number_passed
        test_results[1] = number_failed + 1
    else:
        print('PASSED the MUTATION part of the above test -- good!',
              color='blue')

    number_passed = test_results[0]
    number_failed = test_results[1]

    # Test 2:
    sequence = [10, 11, 20, 21, 30, 31, 40, 41]
    expected = 3
    copy_of_sequence = [10, 11, 20, 21, 30, 31, 40, 41]
    expected_mutation = [10, 14, 20, 21, 30, 34, 40, 44]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print()
    if sequence != expected_mutation:
        print('FAILED part of the above test!', color='red')
        print('BEFORE the function call, the argument is:')
        print('   ', copy_of_sequence, color='red')
        print('AFTER  the function call, the argument should be:')
        print('   ', expected_mutation, color='red')
        print('Running your code, the argument after the function call is:')
        print('   ', sequence, color='red')

        test_results[0] = number_passed
        test_results[1] = number_failed + 1
    else:
        print('PASSED the MUTATION part of the above test -- good!',
              color='blue')

    number_passed = test_results[0]
    number_failed = test_results[1]

    # Test 3:
    sequence = [14, 16, 18]
    expected = 0
    copy_of_sequence = [14, 16, 18]
    expected_mutation = [14, 16, 18]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem3(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    print()
    if sequence != expected_mutation:
        print('FAILED part of the above test!', color='red')
        print('BEFORE the function call, the argument is:')
        print('   ', copy_of_sequence, color='red')
        print('AFTER  the function call, the argument should be:')
        print('   ', expected_mutation, color='red')
        print('Running your code, the argument after the function call is:')
        print('   ', sequence, color='red')

        test_results[0] = number_passed
        test_results[1] = number_failed + 1
    else:
        print('PASSED the MUTATION part of the above test -- good!',
              color='blue')

    # number_passed = test_results[0]
    # number_failed = test_results[1]

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem3(sequence):
    """
    What comes in:
      -- A sequence of integers.
    What goes out:
      -- The number of integers that are prime.
    Side effects:
       Replaces each prime number with a number that is 3 greater than it.
    Examples:
      If  sequence = [4, 5, 6, 7, 8, 9, 10]
      problem5(sequence)
         RETURNS 2
            (because 5 and 7 are the only prime numbers in the sequence)
         MUTATES sequence so that its new value is [4, 8, 6, 10, 8, 9, 10]

      If sequence = [10, 11, 20, 21, 30, 31, 40, 41]
      problem5(sequence)
         RETURNS 3
            (because 11, 31, and 41 are the only prime numbers in the sequence)
         MUTATES sequence so that its new value is:
             [10, 14, 20, 21, 30, 34, 40, 44]
      If sequence = [14, 16, 18]
      problem5(sequence)
         RETURNS 0 (because no number in the sequence is prime)
         and leaves sequence unchanged: [14, 16, 18]

    Type hints:
      :type sequence: [int]
      :rtype: int
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    total_prime = 0
    for k in range(len(sequence)):
        if is_prime(sequence[k]) is True:
            sequence[k] = sequence[k] + 3
            total_prime = total_prime + 1
    return total_prime

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
