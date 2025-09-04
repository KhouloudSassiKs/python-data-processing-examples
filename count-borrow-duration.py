"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Process borrow/return logs and calculate total borrow time per book.

    Args:
        logs (str): Comma-separated log entries.
                    Each entry is "bookId action time", e.g., "1 borrow 09:00"

    Returns:
        list of tuples: [(bookId, total_time)], where total_time is formatted as 'HH:MM'
"""
from datetime import datetime
def solution(logs):
    output = []  # List to store final results

    # Split logs into individual entries
    bookEntries = logs.split(', ')
    
    borrowed = {}  # Dictionary to store borrow time for each book
    finalStat = {}  # Dictionary to accumulate total borrowed time per book
    timeFormat = '%H:%M'  # Format used for parsing times

    # Loop through each log entry
    for entry in bookEntries:  # Example: "1 borrow 09:00" or "1 return 12:00"
        dissectedEntry = entry.split()  # Split entry into [bookId, action, time]
        bookId = dissectedEntry[0]      # Book ID
        action = dissectedEntry[1]      # 'borrow' or 'return'
        timeStamp = dissectedEntry[2]   # Time as string

        if action == 'borrow':
            # Record the borrow time for the book
            borrowed[bookId] = timeStamp
        else:
            # Calculate time difference between return and borrow
            returntime = datetime.strptime(timeStamp, timeFormat)
            borrowedtime = datetime.strptime(borrowed[bookId], timeFormat)
            addedTime = returntime - borrowedtime  # timedelta object

            # Accumulate total time for this book
            if bookId in finalStat:
                finalStat[bookId] += addedTime
            else:
                finalStat[bookId] = addedTime

    # Format cumulative time for output
    for key, value in finalStat.items():
        # Convert timedelta to datetime object for formatting
        t = datetime.strptime(str(value), "%H:%M:%S")
        formatted = t.strftime(timeFormat)  # Format as 'HH:MM'
        output.append((int(key), formatted))  # Append tuple (bookId, formatted time)

    return output


# Example usage
logs = "1 borrow 09:00, 1 return 12:00, 2 borrow 10:00, 2 return 13:30, 1 borrow 14:00, 1 return 15:30"
print(solution(logs))
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Process borrow/return logs and return all books with the maximum borrow duration.

    Args:
        logs (str): Comma-separated log entries.
                    Each entry is in the format "bookId action time",
                    e.g., "1 borrow 09:00, 1 return 12:00"

    Returns:
        list of tuples: [(bookId, duration)], where duration is formatted as 'HH:MM'.
                        Includes all books that share the maximum duration.
"""
from datetime import datetime

def solution(logs):
    output = []  # List to store books with the maximum duration

    # Split the log string into individual entries
    bookEntries = logs.split(', ')

    borrowed = {}   # Dictionary to track borrow time for each book
    finalStat = {}  # Dictionary to accumulate total borrow time per book
    timeFormat = '%H:%M'

    # Process each log entry
    for entry in bookEntries:  # Example: "1 borrow 09:00" or "1 return 12:00"
        dissectedEntry = entry.split()
        bookId = dissectedEntry[0]       # Extract book ID
        action = dissectedEntry[1]       # 'borrow' or 'return'
        timeStamp = dissectedEntry[2]    # Time of the action

        if action == 'borrow':
            # Record borrow time
            borrowed[bookId] = timeStamp
        else:
            # Calculate duration between return and borrow
            returntime = datetime.strptime(timeStamp, timeFormat)
            borrowedtime = datetime.strptime(borrowed[bookId], timeFormat)
            addedTime = returntime - borrowedtime  # timedelta object

            # Accumulate total duration for the book
            if bookId in finalStat:
                finalStat[bookId] += addedTime
            else:
                finalStat[bookId] = addedTime  

    # Determine the maximum borrow duration
    maxDuration = max(finalStat.values())

    # Collect all books that share the maximum duration
    for key, value in finalStat.items():
        if value == maxDuration:
            # Convert timedelta to HH:MM format
            t = datetime.strptime(str(value), "%H:%M:%S")
            formatted = t.strftime(timeFormat)
            output.append((int(key), formatted))  # Append tuple (bookId, duration)

    return output


# Example usage

logs = "1 borrow 09:00, 1 return 12:00, 2 borrow 10:00, 2 return 13:30, 3 borrow 08:00, 3 return 11:30"
print(solution(logs))  # Example output: [(1, '03:00'), (3, '03:00')]
