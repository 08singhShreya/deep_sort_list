def clean_and_flatten(any_input, convert_numeric_strings = False):
    """
    Flattens any list and returns a DICTIONARY of sorted tracks.
    If convert_numeric_strings is True, text like '100' becomes an integer.
    """
    numbers = []
    words = []
    symbols = []
    
    dict_tracks = []

    # THE FIX FOR ACCIDENTAL INPUTS:
    # If the user passed a single item (not a list and not a dict), 
    # wrap it inside a list box automatically so the loop doesn't crash!

    if type(any_input) is list:
        any_list = any_input
    else:
        any_list = [any_input]    

    def unpack(box):

        for item in box:
            if type(item) is list:
                unpack(item)  

            # Find any dictionary inside the list box
            elif type(item) is dict:
                def deep_sort_dict(input_dict):
                        """
                        Takes any dictionary, sorts its keys alphabetically, 
                        and checks if any of its values are ALSO dictionaries to sort them too!
                        """
                        sorted_dict = {}
                
                        sorted_keys = sorted(input_dict.keys(), key=str)    # Grab all keys and sort them alphabetically
                
                        for key in sorted_keys:
                            value = input_dict[key]
                
                            # RECURSION CHECK: If the value inside this key is ANOTHER dictionary,call deep_sort_dict
                            if type(value) is dict:
                                sorted_dict[key] = deep_sort_dict(value)
                            else:
                                sorted_dict[key] = value
                
                        return sorted_dict 
                clean_dict = deep_sort_dict(item) 
                dict_tracks.append(clean_dict)

            elif type(item) in (int, float, bool):
                numbers.append(item)
            else:
                text_item = str(item)

                if text_item.isalnum() == False:  # Check for special characters first
                    symbols.append(text_item)
                else:
                    # User requirement check: Should we turn string numbers into integers?
                    if convert_numeric_strings and text_item.isdigit():
                        numbers.append(int(text_item))
                    else:
                        words.append(text_item)   

    # Start the engine using the dynamic argument variable
    unpack(any_list) 

                   
    # Sort each individual track cleanly
    numbers.sort()
    words.sort()
    symbols.sort()

    # RETURN A DICTIONARY: This hands the clean data back to the user!
    
    return {
        "numbers": numbers,
        "symbols": symbols,
        "words": words,
        "dictionaries": dict_tracks
    }


