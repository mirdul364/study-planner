# validation.py
# Input helpers. They keep asking until the user gives valid input,
# so the program never crashes on bad input.


# Ask until the user enters a whole number between minimum and maximum.
# minimum : smallest allowed value
# maximum : largest allowed value (None means no upper limit)
def get_integer(prompt, minimum, maximum=None):
    while True:
        text = input(prompt).strip()
        if not text.isdecimal():
            print('Please enter a whole number (digits only).')
            continue
        value = int(text)
        if value < minimum:
            print('Please enter a number >= ' + str(minimum) + '.')
            continue
        if maximum is not None and value > maximum:
            print('Please enter a number <= ' + str(maximum) + '.')
            continue
        return value


# Ask until the user enters some non-empty text.
def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if len(text) > 0:
            return text
        print('Input cannot be empty.')
