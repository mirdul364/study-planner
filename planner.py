# planner.py
# Study plan management.
# The plan is a list of dictionaries:
#   {'name': 'Maths', 'hours': 3, 'done': False}


# Return the position of a subject (0-based), or -1 if not found.
# Linear search; the comparison ignores upper/lower case.
def find_subject(subjects, name):
    target = name.lower()
    for i in range(len(subjects)):
        if subjects[i]['name'].lower() == target:
            return i
    return -1


# Add a new subject. Returns False if it already exists.
def add_subject(subjects, name, hours):
    if find_subject(subjects, name) != -1:
        return False
    subjects.append({'name': name, 'hours': hours, 'done': False})
    return True


# Build the lines that display the plan.
def get_plan_lines(subjects):
    lines = []
    if len(subjects) == 0:
        lines.append('No study items yet.')
    for i in range(len(subjects)):
        item = subjects[i]
        if item['done']:
            status = 'Done'
        else:
            status = 'Pending'
        lines.append(str(i + 1) + '. ' + item['name'] + ' - '
                     + str(item['hours']) + ' hour(s) [' + status + ']')
    return lines


# Mark item number (1-based) as completed. Returns False if number is invalid.
def mark_completed(subjects, number):
    if number < 1 or number > len(subjects):
        return False
    subjects[number - 1]['done'] = True
    return True


# Remove item number (1-based). Returns False if number is invalid.
def remove_subject(subjects, number):
    if number < 1 or number > len(subjects):
        return False
    subjects.pop(number - 1)
    return True


# Sort the plan so the subject with the most hours comes first.
# Bubble sort; neighbours are exchanged with tuple assignment.
def sort_by_hours(subjects):
    n = len(subjects)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if subjects[j]['hours'] < subjects[j + 1]['hours']:
                subjects[j], subjects[j + 1] = subjects[j + 1], subjects[j]
