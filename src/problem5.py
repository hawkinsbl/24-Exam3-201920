"""
Exam 3, problem 5.

Authors: Vibha Alangar, Aaron Wilkin, David Mutchler, Dave Fisher, 
         Matt Boutell, Amanda Stouder, their colleagues and 
         Ben Hawkins.  January 2019.

"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem5()


###############################################################################
# Done: 2.  READ the doc-string for the   is_prime   function defined below.
# It is the same as you have seen before.
# After you UNDERSTAND the doc-string (JUST the doc-string, NOT the code),
# ASKING QUESTIONS AS NEEDED, change the above _TODO_ to DONE.
###############################################################################
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


def run_test_problem5():
    """ Tests the  problem5   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem5   function:')
    print('--------------------------------------------------')

    format_string = '    problem5( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    sequence = [[1,3,2], [10, 5], []]
    expected = [3, 10]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    sequence = [[10, 12], (23, 1)]
    expected = [12, 23]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    sequence = [(4, 25),
                (33, 54, 20, 55, 10),
                (6, 11, 70, 33),
                (7, 11),
                (),
                (5, 5, 3)
                ]
    expected = [25, 55, 70, 11, 5]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    sequence = ([1], [], [2, 5])
    expected = [1, 5]
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    sequence = ([], [], [])
    expected = []
    print_expected_result_of_test([sequence], expected,
                                  test_results, format_string)
    actual = problem5(sequence)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem5(seq_of_seq):
    """
    What comes in:
      -- A sequence of sub-sequences of integers.
    What goes out:
      -- Returns a NEW list containing largest integer of each sequence.
      If one of the original sub-sequences were empty, it has no largest number,
      so contributes no integer to the returned list.
    Side effects:  None.
    Examples:
      problem5([(4, 25),
                 (33, 54, 20, 55, 10),
                 (6, 11, 70, 33),
                 (7, 11),
                 (),
                 (5, 5, 3)
                ])
                returns [25, 55, 70, 11, 5]

      problem5( [[10, 12], (23, 1)]  ) returns [12, 23]
      problem5( ([1], [], [2, 5] )   ) returns [1, 2]
      problem5( [[], [], [] )          returns []
      problem5( [1,3,2], [10, 5], []]) returns [3,10]

    Type hints:
      :type seq_of_seq: list of list of int
      :rtype: (list of int) | int
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    a = []
    for k in range(len(seq_of_seq)):
        if len(seq_of_seq[k]) > 0:
            max_num = seq_of_seq[k][0]
            for l in range(len(seq_of_seq[k])):
                if seq_of_seq[k][l] > max_num:
                    max_num = seq_of_seq[k][l]
            a = a + [max_num]
    return a

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