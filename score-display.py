""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Analyze competition logs and return a sorted list of student statistics.

    Args:
        logs (str): A string of entries separated by ', '. Each entry format:
                    "student_id action time score", e.g., "1 solve 09:00 50"

    Returns:
        List[Tuple[int, int, int, int]]: List of tuples in the format
                    (student_id, total_score, success_count, fail_count),
                    sorted by total_score descending.
"""
def analyze_competition(logs):
    output = []  # List to store final tuples
    resultdictsuccess = {}  # Dictionary to track successes and scores per student
    resultdictfail = {}     # Dictionary to track failure counts per student

    # Split logs into individual entries
    entries = logs.split(', ')  # Example entry: "1 solve 09:00 50"

    for entry in entries:
        entryDisected = entry.split()  # Split into parts: [student_id, action, time, score]

        if entryDisected[1] == 'solve':
            # Initialize student in success dict if not present
            if entryDisected[0] not in resultdictsuccess:
                resultdictsuccess[entryDisected[0]] = {"successCount": 0, "score": 0}
            # Increment success count and add score
            resultdictsuccess[entryDisected[0]]["successCount"] += 1
            resultdictsuccess[entryDisected[0]]["score"] += int(entryDisected[3])
        else:
            # Increment fail count
            resultdictfail[entryDisected[0]] = resultdictfail.get(entryDisected[0], 0) + 1

    # Build output tuples
    for key, value in resultdictsuccess.items():
        succCounter = value["successCount"]  # Number of successful solves
        succScore = value["score"]           # Total score
        failCounter = resultdictfail[key] if key in resultdictfail else 0  # Failures if any

        output.append((int(key), succScore, succCounter, failCounter))

    # Sort output by total score descending
    sortedOutput = sorted(output, key=lambda x: x[1], reverse=True)

    return sortedOutput


# Example usage
logs = "1 solve 09:00 50, 2 solve 09:15 40, 1 solve 09:30 50, 3 fail 09:45 0, 2 solve 10:00 60"
print(analyze_competition(logs))
