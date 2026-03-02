from utils import (
    calculate_average,
    assign_letter_grade,
    validate_grade,
    find_class_extremes,
)


def main():
    students = {}

    print("=== Grade Calculator ===")

    while True:
        name = input("\nEnter student name (or press Enter to finish): ").strip()

        if name == "":
            break

        grades = []

        for i in range(1, 4):
            while True:
                score_input = input(f"Enter grade {i} for {name}: ")
                try:
                    score = validate_grade(score_input)
                    grades.append(score)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

        students[name] = grades

    if not students:
        print("\nNo student data entered.")
        return

    print("\n=== Final Report ===")
    print(f"{'Name':<20}{'Average':<10}{'Grade':<10}")
    print("-" * 40)

    for name, grades in students.items():
        avg = calculate_average(grades)
        letter = assign_letter_grade(avg)
        print(f"{name:<20}{avg:<10.2f}{letter:<10}")

    # ⭐ Bonus: Class extremes
    top, low = find_class_extremes(students)

    if top and low:
        top_names, top_avg = top
        low_names, low_avg = low

        print("\nHighest Average:")
        print(f"{', '.join(top_names)} with {top_avg:.2f}")

        print("Lowest Average:")
        print(f"{', '.join(low_names)} with {low_avg:.2f}")


if __name__ == "__main__":
    main()