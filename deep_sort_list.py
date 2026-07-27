import collections

def deep_sort_dict(input_dict):
    """
    Safely sorts dictionary keys alphabetically using an iterative stack approach
    to avoid any recursive stack depth limitations.
    """
    root_sorted = {}
    stack = [(input_dict, root_sorted)]

    while stack:

        curr_dict, target_dict = stack.pop()

        sorted_keys = sorted(curr_dict.keys(), key=str)

        for key in sorted_keys:
            value = curr_dict[key]

            # Use isinstance to support OrderedDict, Counter, and sub-dicts

            if isinstance(value, dict):    # Create the nested skeleton and push it to our work stack
                target_dict[key] = {}
                stack.append((value, target_dict[key]))
            else:
                target_dict[key] = value   
    return root_sorted

def clean_and_flatten(any_input, convert_numeric_strings = False):
    """
    Iteratively flattens nested data structures and segregates types into sorted streams.
    Bypasses Python's 1000 recursion limit using a manual array processing stack.
    """
    numbers = []
    words = []
    symbols = []
    dict_tracks = []       

    # Normalization: Force structural wrappers.

    if isinstance(any_input, (list, tuple)):
        # We make a shallow copy or cast to a list so we can freely mutate our working stack
        processing_stack = list(any_input)
    elif isinstance(any_input, set):    
        processing_stack = list(any_input)
    else:
        processing_stack = [any_input]    

    # Reverse to maintain original left-to-right processing order since we pop from the end
    processing_stack.reverse()

    while processing_stack:
        item = processing_stack.pop()    

        # Scenario A: Nested containers (Lists, Tuples, Sets)
        if isinstance(item, (list, tuple, set)):
            # Convert to list and extend backwards onto the stack to keep structural alignment
            inner_items = list(item)
            inner_items.reverse()
            processing_stack.extend(inner_items)

        # Scenario B: Dictionaries
        elif isinstance(item, dict):
            clean_dict = deep_sort_dict(item)  #call global_helper_function
            dict_tracks.append(clean_dict)

        # Scenario C: True Booleans
        elif type(item) is bool:
            if item is True:
                words.append("True")
            else:
                words.append("False")

        # Scenario D: Numbers
        elif isinstance(item, (int, float)):
            numbers.append(item)

        # Scenario E: Strings and Custom Type fallbacks
        else:
            text_item = str(item)

            # Smart word evaluation check.
            # If a string has letters or digits (even with spaces/exclamations), it's a word track item.
            # If it is only pure punctuation characters (like "@@@"), it goes to symbols.

            if any(char.isalnum() for char in text_item):
                if convert_numeric_strings and text_item.isdigit():
                    numbers.append(int(text_item))
                else:
                    words.append(text_item)    

            else:
                symbols.append(text_item)
                
    # Sort each individual track cleanly
    numbers.sort()
    words.sort()
    symbols.sort()
    
    return {
        "numbers": numbers,
        "symbols": symbols,
        "words": words,
        "dictionaries": dict_tracks
    }


