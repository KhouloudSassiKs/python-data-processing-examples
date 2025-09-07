import json
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
As in the json-split-primitive.py algo we are trying to load a JSON string, 
update all occurrences of "key4" with the provided value, and return the 
resulting dictionary.
This time I am demonstrating how the use of loads() method by json library can be
a life changer.
And with recursion, searching could not be easier :)!
Args:
    json_string (str): JSON string to process
    update_value: Value to assign to "key4"

Returns:
    dict: Updated dictionary
"""
def solution(json_string, update_value):
    output = json.loads(json_string)
    findAndUpdateValue(output, "key4", update_value)
    return output


def findAndUpdateValue(data, searchedKey, update_value):
    """
    Recursively search for a key in a nested dictionary and update its value.

    Args:
        data (dict): Nested dictionary to search
        searchedKey (str): Key to search for
        update_value: Value to assign if key is found

    Returns:
        The updated value if found, else None
    """
    for key, value in data.items():
        if key == searchedKey:
            data[key] = update_value  # update the dictionary directly
            return update_value
        elif isinstance(value, dict):
            result = findAndUpdateValue(value, searchedKey, update_value)
            if result is not None:
                return result
    return None  # key not found


# =====================
# Example usage
# =====================

# Deeply nested JSON string
json_string = '{"key1": {"key2": {"key3": {"key4": "value4"}}}}'
new_value = "deepValue"

updated_dict = solution(json_string, new_value)

print("Updated dictionary:")
print(json.dumps(updated_dict, indent=4))
