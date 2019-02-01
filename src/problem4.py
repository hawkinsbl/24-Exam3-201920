"""
Exam 3, problem 4.

Authors: Vibha Alangar, Aaron Wilkin, David Mutchler, Dave Fisher, 
         Matt Boutell, Amanda Stouder, their colleagues and 
         Ben Hawkins.  January 2019.
         
"""  # Don: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4()


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


def run_test_problem4():
    """ Tests the  problem5   function. """
    ####################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ####################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem5   function:')
    print('--------------------------------------------------')

    format_string = '    problem5( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    seq_seq = [(3, 25),
               (33, 50, 20, 55, 10),
               (6, 13, 70, 33, 37),
               (7, 11, 109, 61),
               (),
               (5, 5, 3, 150)
               ]
    n = 5
    expected = 13
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    seq_seq = [(3, 25),
               (33, 50, 20, 55, 10),
               (6, 13, 70, 33, 37),
               (7, 11, 109, 61),
               (),
               (5, 5, 3, 150)
               ]
    n = 50
    expected = 109
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    seq_seq = [(3, 25),
               (33, 50, 20, 55, 10),
               (6, 13, 70, 33, 37),
               (7, 11, 109, 61),
               (),
               (5, 5, 3, 150)
               ]
    n = 120
    expected = -1
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    seq_seq = [(3, 25),
               (33, 50, 20, 55, 10),
               (6, 13, 70, 33, 37),
               (7, 11, 109, 61),
               (),
               (5, 5, 3, 150)
               ]
    n = 17
    expected = 37
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    seq_seq = [(3, 25),
               (33, 50, 20, 55, 10),
               (6, 13, 70, 33, 37),
               (7, 11, 109, 61),
               (),
               (5, 5, 3, 150)
               ]
    n = 2
    expected = 3
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    seq_seq = [(3, 25),
               (33, 50, 20, 55, 10),
               (6, 13, 70, 33, 37),
               (7, 11, 109, 61),
               (),
               (5, 5, 3, 150)
               ]
    n = 3
    expected = 13
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    seq_seq = [(2, 5, 30),
               (8, 40),
               (13,),
               (400, 23, 17),
               ]

    n = 1
    expected = 2
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    seq_seq = [(2, 5, 30),
               (8, 40),
               (13,),
               (400, 23, 17),
               ]

    n = 2
    expected = 5
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    seq_seq = [(2, 5, 30),
               (8, 40),
               (13,),
               (400, 23, 17),
               ]

    n = 7
    expected = 13
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    seq_seq = [(2, 5, 30),
               (8, 40),
               (13,),
               (400, 23, 17),
               ]

    n = 14
    expected = 23
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    seq_seq = [(2, 5, 30),
               (8, 40),
               (13,),
               (400, 23, 17),
               ]

    n = 100
    expected = -1
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    seq_seq = []
    n = 3
    expected = -1
    print_expected_result_of_test([seq_seq, n], expected, test_results,
                                  format_string)
    actual = problem4(seq_seq, n)  # Run the code to test
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of the test results:
    print_summary_of_test_results(test_results)


def problem4(seq_of_seq, n):
    """
    What comes in:
      -- A sequence of sequences: seq_of_seq
            where the sub-sequences contain only positive integers
      -- A non-negative integer:  n
    What goes out:  Returns the first number in the sub-sequences
        that is both prime and greater than n.
        Returns -1 if there are no prime numbers greater than n.
    Side effects: None.

    Examples:
     Let seq_of_seq = [(3, 25),
                 (33, 50, 20, 55, 10),
                 (6, 13, 70, 33, 37),
                 (7, 11, 109, 61),
                 (),
                 (5, 5, 3, 150)
                ]

    Then if n = 5, returns 13.
    If n = 50,  returns 109.
    If n = 120, returns -1.
    If n = 17,  returns 37.
    If n = 2,   returns 3.
    If n = 3,   returns 13.

    Type hints:
      :type seq_of_seq: [[int]]
      :type n:          int
      :rtype: int
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    for k in range(len(seq_of_seq)):
        for l in range(len(seq_of_seq[k])):
            if seq_of_seq[k][l] > n:
                if is_prime(seq_of_seq[k][l]) is True:
                    return seq_of_seq[k][l]
    return -1


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
