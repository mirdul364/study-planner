# test_project.py
# Validation tests using assert. Run with:  python test_project.py
# If every check passes, "All tests passed." is printed.

import planner
import report
import basic_algorithms
import number_algorithms


def test_basic_algorithms():
    assert basic_algorithms.factorial(0) == 1
    assert basic_algorithms.factorial(5) == 120
    assert basic_algorithms.fibonacci(1) == [0]
    assert basic_algorithms.fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert basic_algorithms.reverse_text('abc') == 'cba'
    assert basic_algorithms.reverse_text('') == ''
    assert basic_algorithms.decimal_to_base(10, 2) == '1010'
    assert basic_algorithms.decimal_to_base(0, 2) == '0'
    assert basic_algorithms.decimal_to_base(255, 16) == 'FF'


def test_number_algorithms():
    assert number_algorithms.square_root(0) == 0
    assert number_algorithms.square_root(25) == 5.0
    assert number_algorithms.square_root(2) == 1.4142
    assert number_algorithms.smallest_divisor(15) == 3
    assert number_algorithms.smallest_divisor(13) == 13
    assert number_algorithms.smallest_divisor(2) == 2
    assert number_algorithms.gcd(12, 18) == 6
    assert number_algorithms.gcd(7, 13) == 1
    assert number_algorithms.generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert number_algorithms.generate_primes(2) == [2]
    assert number_algorithms.prime_factors(1) == []
    assert number_algorithms.prime_factors(60) == [2, 2, 3, 5]
    assert number_algorithms.prime_factors(97) == [97]


def test_planner():
    subjects = []
    assert planner.add_subject(subjects, 'Maths', 3) is True
    assert planner.add_subject(subjects, 'maths', 2) is False   # duplicate
    assert planner.add_subject(subjects, 'Physics', 5) is True
    assert planner.find_subject(subjects, 'PHYSICS') == 1
    assert planner.find_subject(subjects, 'Chemistry') == -1
    assert planner.mark_completed(subjects, 1) is True
    assert planner.mark_completed(subjects, 9) is False
    planner.sort_by_hours(subjects)
    assert subjects[0]['name'] == 'Physics'
    assert planner.remove_subject(subjects, 1) is True
    assert planner.remove_subject(subjects, 5) is False
    assert len(subjects) == 1
    assert planner.get_plan_lines([]) == ['No study items yet.']


def test_report():
    subjects = []
    planner.add_subject(subjects, 'Maths', 3)
    planner.add_subject(subjects, 'Physics', 5)
    planner.mark_completed(subjects, 1)
    lines = report.make_report(subjects)
    assert 'Total items: 2' in lines
    assert 'Completed: 1' in lines
    assert 'Total study hours: 8' in lines
    assert 'Hours remaining: 5' in lines
    assert 'Completion: 50.0%' in lines
    assert 'Completion: 0%' in report.make_report([])


test_basic_algorithms()
test_number_algorithms()
test_planner()
test_report()
print('All tests passed.')
