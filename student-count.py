"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Count how many times each student appears in the list.

    Args:
        student_string (str): A semicolon-separated string of student entries
                              (e.g. "Alice, Math, 09:00; Bob, Science, 10:00")

    Returns:
        list[tuple[str, int]]: A list of (student, count) tuples,
                               sorted by count (descending), then name (ascending).
"""
def organize_students(student_string: str):
    entries = student_string.split('; ')
    student_counts: dict[str, int] = {}

    for entry in entries:
        student = entry.split(', ')[0]  # get student name
        student_counts[student] = student_counts.get(student, 0) + 1

    # Sort by count (desc), then by student name (asc)
    output = sorted(student_counts.items(), key=lambda x: (-x[1], x[0]))
    return output


# Example usage
    students = (
        "Alice, Math, 09:00; "
        "Bob, Science, 10:00; "
        "Alice, History, 11:00; "
        "Charlie, Math, 12:00; "
        "Bob, English, 13:00"
    )

print(organize_students(students))
