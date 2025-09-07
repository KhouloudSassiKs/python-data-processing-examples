import json
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Converts a semi-structured user string into a dictionary, 
and updates a specific preference value for a given user.

Parameters:
    - input_string (str): Original semi-structured string.
      Example: "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian; Sport1=Fencing};
                User2:Age2=30; Location2=Canada; Preferences2={Music2=Jazz; Color2=Blue}"
    - user_index (int): 1-based index of the user to update (1 for first user).
    - pref_key (str): Key inside the user's preferences to update.
    - new_value (str): New value for the specified preference key.

Returns:
    - dict: Updated dictionary representing all users and their info.
"""
def solution(input_string, user_index, pref_key, new_value):
    # Step 1: Replace ':' with ':{"' to start key-value pairs
    processedData0 = input_string.replace(':', '":{"')

    # Step 2: Replace closing braces with double braces to preserve structure
    processedData1 = processedData0.replace('}', '"}}')

    # Step 3: Replace '=' with '":"', converting assignments to JSON-style key-value pairs
    processedData2 = processedData1.replace('=', '":"')

    # Step 4: Correct the opening brace formatting
    processedData3 = processedData2.replace(':"{', ':{"')

    # Step 5: Replace ';' with '","' to separate key-value pairs
    processedData4 = processedData3.replace(';', '","')

    # Step 6: Clean up any incorrectly added quotes around braces
    processedData5 = processedData4.replace('}"', '}')

    # Step 7: Wrap the entire string in outer braces to make it valid JSON
    ultraProcessed = '{"' + processedData5.strip() + '}'

    # Step 8: Parse the string into a Python dictionary
    data = json.loads(ultraProcessed)

    # Step 9: Adjust for 1-based user_index (Python lists are 0-based)
    correspondingKey = list(data.keys())[user_index - 1]

    # Step 10: Construct the preference key based on the user index
    correspondingPref = "Preferences" + str(user_index)

    # Step 11: Update the desired preference value
    data[correspondingKey][correspondingPref][pref_key] = new_value

    return data
  
# =========================
# Example Usage
# =========================
input_string = (
   "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian; Sport1=Fencing};"
   "User2:Age2=30;Location2=Canada;Preferences2={Music2=Jazz; Color2=Blue}"
  )

# Example 1: Update Food1 for User1
result1 = solution(input_string, user_index=1, pref_key="Food1", new_value="Mexican")
print("Updated User1 Preferences:", result1["User1"]["Preferences1"])
# Output: {'Food1': 'Mexican', 'Sport1': 'Fencing'}

# Example 2: Update Music2 for User2
result2 = solution(input_string, user_index=2, pref_key="Music2", new_value="Rock")
print("Updated User2 Preferences:", result2["User2"]["Preferences2"])
# Output: {'Music2': 'Rock', 'Color2': 'Blue'}
