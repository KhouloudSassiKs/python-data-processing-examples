import json
 """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Parse a custom string format into nested dictionaries,
    and update a given user's field with a new value.

    Args:
        data (str): Input string, multiple users separated by newline.
        userid (str): The main key identifying the user (e.g., "001").
        key (str): The field to update (e.g., "Age" or "Address").
        new_value (str): The new value to update with. Can be a simple string or
                         a nested structure like "(Street=Main St;City=NY;Zip=10001)".

    Returns:
        list[dict]: List of parsed user dictionaries with the update applied.
    """
def solution(data, userid, key, new_value):
    # Split by newline to get multiple users
    lines = data.split('\n')
    finalOutput = []

    # If new_value is nested (contains parentheses), process it into a dict
    new_value_processed = processNestedValue(new_value[1:-1]) if '(' in new_value else new_value

    for line in lines:
        output = {}

        # Example: '001,Age=25,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com'
        items = line.split(',')
        mainkey = items[0]
        output[mainkey] = {}

        # Process each attribute of the user
        for item in items[1:]:
            if '(' in item:  # Nested field (like Address)
                subdict, subkey = processNestedElement(item)
                output[mainkey][subkey] = subdict
            else:  # Simple key=value
                key1, value = processSimpleElement(item)
                output[mainkey][key1] = value

        # Apply the update if this is the target user
        if mainkey == userid:
            output[mainkey][key] = new_value_processed

        finalOutput.append(output)

    return finalOutput

"""""""""""""""""""""""""""""""""""""""""""""""""""""
Parse a simple element like 'Age=25' → ('Age', '25')
"""
def processSimpleElement(element):
    items = element.split('=')
    return items[0], items[1]

"""""""""""""""""""""""""""""""""""""""""""""""""""""
Parse a nested element like:
'Address=(Street=Main St;City=NY;Zip=10001)'
to ({'Street': 'Main St', 'City': 'NY', 'Zip': '10001'}, 'Address')
"""
def processNestedElement(element):
   
    items = element[:-1].split('=(')  # Remove trailing ')'
    key1 = items[0]
    subdict = processNestedValue(items[1])
    return subdict, key1

"""""""""""""""""""""""""""""""""""""""""""""""""""""
Parse nested key-value pairs separated by semicolons:
'Street=Main St;City=NY;Zip=10001'
{'Street': 'Main St', 'City': 'NY', 'Zip': '10001'}
"""
def processNestedValue(element):
    subdict = {}
    for item in element.split(';'):
        key, value = processSimpleElement(item)
        subdict[key] = value
    return subdict


# ------------------------------
# Example Usage
# ------------------------------
data = (
        "001,Age=25,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n"
        "002,Age=30,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com"
    )
result = solution(data, "002", "Address", "(Street=3rd St;City=LA;Zip=90002)")
print(json.dumps(result, indent=4))
