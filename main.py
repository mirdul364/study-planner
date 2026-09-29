# main.py
# Entry point: Student Study Planner with an Algorithm Lab.
# Run with:  python main.py

from validation import get_integer, get_text
import planner
import report
import number_algorithms

MAX_BIG = 10 ** 12          # upper limit for the large-number algorithms


def show_menu():
    print('\n--- Student Study Planner ---')
    print('1. Add subject')
    print('2. View plan')
    print('3. Mark item completed')
    print('4. Remove item')
    print('5. Search subject')
    print('6. Sort plan by hours')
    print('7. Report')
    print('8. Algorithm Lab')
    print('9. Exit')


def show_algorithm_menu():
    print('\n--- Algorithm Lab ---')
    print('1. Factorial')
    print('2. Fibonacci')
    print('3. Reverse text')
    print('4. Base conversion')
    print('5. GCD')
    print('6. Prime numbers up to N')
    print('7. Prime factors')
    print('8. Smallest divisor')
    print('9. Square root')
    print('10. Back')


def show_plan(subjects):
    for line in planner.get_plan_lines(subjects):
        print(line)


def run_algorithm_lab():
    while True:
        show_algorithm_menu()
        choice = input('Choose an option: ').strip()
        if choice == '1':
            n = get_integer('Enter an integer (0-100): ', 0, 100)
            print('Factorial:', basic_algorithms.factorial(n))
        elif choice == '2':
            n = get_integer('How many Fibonacci numbers (1-100)? ', 1, 100)
            print('Fibonacci:', basic_algorithms.fibonacci(n))
        elif choice == '3':
            print('Reverse:', basic_algorithms.reverse_text(input('Enter text: ')))
        elif choice == '4':
            n = get_integer('Enter a non-negative integer: ', 0, MAX_BIG)
            base = get_integer('Convert to base (2-16): ', 2, 16)
            print('Result:', basic_algorithms.decimal_to_base(n, base))
        elif choice == '5':
            a = get_integer('First positive integer: ', 1, MAX_BIG)
            b = get_integer('Second positive integer: ', 1, MAX_BIG)
            print('GCD:', number_algorithms.gcd(a, b))
        elif choice == '6':
            n = get_integer('Generate primes up to (2-100000): ', 2, 100000)
            print('Primes:', number_algorithms.generate_primes(n))
        elif choice == '7':
            n = get_integer('Enter an integer (1-%d): ' % MAX_BIG, 1, MAX_BIG)
            print('Prime factors:', number_algorithms.prime_factors(n))
        elif choice == '8':
            n = get_integer('Enter an integer (2-%d): ' % MAX_BIG, 2, MAX_BIG)
            print('Smallest divisor:', number_algorithms.smallest_divisor(n))
        elif choice == '9':
            n = get_integer('Enter an integer (0-%d): ' % MAX_BIG, 0, MAX_BIG)
            print('Square root:', number_algorithms.square_root(n))
        elif choice == '10':
            break
        else:
            print('Invalid choice.')


def complete_item(subjects):
    # Ask for an item number and mark it done (with an "already done" check).
    number = get_integer('Enter item number: ', 1, len(subjects))
    if subjects[number - 1]['done']:
        print('This item is already completed.')
    elif planner.mark_completed(subjects, number):
        print('Completed.')
    else:
        print('Invalid item number.')


def remove_item(subjects):
    number = get_integer('Enter item number: ', 1, len(subjects))
    if planner.remove_subject(subjects, number):
        print('Removed.')
    else:
        print('Invalid item number.')


def run():
    subjects = []
    while True:
        show_menu()
        choice = input('Choose an option: ').strip()
        if choice == '1':
            name = get_text('Enter subject name: ')
            hours = get_integer('Enter study hours (1-100): ', 1, 100)
            if planner.add_subject(subjects, name, hours):
                print('Study item added.')
            else:
                print('Subject already exists.')
        elif choice == '2':
            show_plan(subjects)
        elif choice == '3' or choice == '4':
            if len(subjects) == 0:
                print('No study items yet.')
                continue
            show_plan(subjects)
            if choice == '3':
                complete_item(subjects)
            else:
                remove_item(subjects)
        elif choice == '5':
            name = get_text('Enter subject name to search: ')
            position = planner.find_subject(subjects, name)
            if position != -1:
                print('Subject found at position:', position + 1)
            else:
                print('Subject not found.')
        elif choice == '6':
            planner.sort_by_hours(subjects)
            print('Plan sorted (most hours first).')
            show_plan(subjects)
        elif choice == '7':
            for line in report.make_report(subjects):
                print(line)
        elif choice == '8':
            run_algorithm_lab()
        elif choice == '9':
            print('Thank you for using Student Study Planner.')
            break
        else:
            print('Invalid choice.')


if __name__ == '__main__':
    try:
        run()
    except (KeyboardInterrupt, EOFError):
        print('\nProgram ended.')