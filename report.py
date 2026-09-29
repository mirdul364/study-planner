# report.py
# Builds the study report using counting and summation.


# Return the report as a list of text lines.
def make_report(subjects):
    total = 0
    done = 0
    total_hours = 0
    remaining_hours = 0
    for item in subjects:
        total += 1                       # counting
        total_hours += item['hours']     # summation
        if item['done']:
            done += 1
        else:
            remaining_hours += item['hours']

    percent = 0
    if total > 0:
        percent = round(done * 100 / total, 1)

    lines = []
    lines.append('Total items: ' + str(total))
    lines.append('Completed: ' + str(done))
    lines.append('Pending: ' + str(total - done))
    lines.append('Total study hours: ' + str(total_hours))
    lines.append('Hours remaining: ' + str(remaining_hours))
    lines.append('Completion: ' + str(percent) + '%')
    return lines
