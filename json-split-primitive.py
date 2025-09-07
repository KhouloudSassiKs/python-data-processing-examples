"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Primitive split-based solution to process a flat JSON or one-level nested JSON string.
    
Args:
    json_string (str): JSON-like string with flat or one-level nested elements
    update_value (str): value to update if key == 'key4'
    
Returns:
    dict: nested dictionary representation of the JSON-like string
"""
def solution(json_string, update_value):
    output = {}
    
    # Strip outer curly brackets
    without_outer_brackets = json_string[1:-1]
    
    # Split elements by comma
    elements = without_outer_brackets.split(',') 
    
    # Track if currently inside a nested element
    nested = False
    current_head_key = ""
    
    for element in elements:
        element = element.strip()
        if '{' in element:
            # Start of a nested element
            nested = True
            key1, key2, value = processHeadNestedElement(element, update_value)
            output.setdefault(key1, {})[key2] = value
            current_head_key = key1
        elif '}' in element:   
            # End of nested element
            nested = False
            key2, value = processSimplElement(element, update_value)
            output[current_head_key][key2] = value
            current_head_key = ""
        elif nested:
            # Inside a nested element
            key, value = processSimplElement(element, update_value)
            output[current_head_key][key] = value
        else:
            # Simple flat element
            key, value = processSimplElement(element, update_value)
            output[key] = value
            
    return output

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Process a simple key-value pair like: '"key1": "value1"'
"""
def processSimplElement(element, update_value):
    items = element.split(r'"')
    items = [x.strip(' :}') for x in items if x.strip(' :')]
    key, value = items[0], items[1]
    
    if key == "key4":
        value = update_value
    
    return key, value

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Process the head of a one-level nested element like: '"key2": {"key3": "value3"'
"""
def processHeadNestedElement(element, update_value):
    """
    Process the head of a one-level nested element like: '"key2": {"key3": "value3"'
    """
    print(element)
    items = element.split(r'"')
    items = [x.strip(' :{') for x in items if x.strip(' :{')]
    key1, key2, value = items[0], items[1], items[2]
    
    if key2 == "key4":
        value = update_value
    
    return key1, key2, value


# =====================
# Example usage
# =====================
json_string = '{"key1": "value1", "key2": {"key3": "value3", "key4": "value4"}, "key5": "value5"}'
update_value = "updated_value"
    
result = solution(json_string, update_value)
print("\nProcessed output:")
print(result)
