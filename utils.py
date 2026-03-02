def calculate_average(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def assign_letter_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


def validate_grade(score):
    try:
        value = float(score)
    except ValueError:
        raise ValueError("Grade must be a number.")

    if value < 0 or value > 100:
        raise ValueError("Grade must be between 0 and 100.")

    return value


# ⭐ Bonus Function
def find_class_extremes(students):
    if not students:
        return None, None

    averages = {
        name: calculate_average(grades)
        for name, grades in students.items()
    }

    highest_avg = max(averages.values())
    lowest_avg = min(averages.values())

    top_students = [name for name, avg in averages.items() if avg == highest_avg]
    low_students = [name for name, avg in averages.items() if avg == lowest_avg]

    return (top_students, highest_avg), (low_students, lowest_avg)