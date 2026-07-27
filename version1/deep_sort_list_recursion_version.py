import collections

def deep_sort_dict(input_dict):
        """
        Takes any dictionary, sorts its keys alphabetically, 
        and checks if any of its values are ALSO dictionaries to sort them too!
        """
        sorted_dict = {}
        sorted_keys = sorted(input_dict.keys(), key=str)

        for key in sorted_keys:
            value = input_dict[key]

            # Use isinstance to support OrderedDict, Counter, and sub-dicts

            if isinstance(value, dict):    # RECURSION CHECK: If the value inside this key is ANOTHER dictionary,call deep_sort_dict
                sorted_dict[key] = deep_sort_dict(value)
            else:
                sorted_dict[key] = value   
        return sorted_dict

def clean_and_flatten(any_input, convert_numeric_strings = False):
    """
    Recursively flattens nested data structures and segregates types into sorted streams.

    This function drills down into infinitely nested lists, tuples, sets, and 
    dictionaries. It separates loose elements into type-safe buckets, safely 
    alphabetizes internal dictionary configurations without losing key-value mappings, 
    and handles booleans and complex strings without pipeline crashes.

    Parameters:
    -----------
    any_input : any
        The entry-level data element or container (list, tuple, set, dict, 
        int, float, bool, or str) to parse.
    convert_numeric_strings : bool, default False
        If True, text strings containing pure digits (e.g., '100') will be 
        dynamically converted into integers and sorted into the numbers track.

    Returns:
    --------
    dict
        A structured dictionary map holding four cleanly sorted data streams:
        - "numbers": Sorted integers and floats.
        - "symbols": Sorted pure punctuation marks.
        - "words": Sorted alphanumeric text strings and standalone booleans.
        - "dictionaries": Sorted dictionaries with internal alphabetical keys.    
    """
    numbers = []
    words = []
    symbols = []
    dict_tracks = []       

    # HANDLE ACCIDENTAL INPUTS at entry level:
    # Supports custom lists/tuples/sets safely via Sequence checks

    if isinstance(any_input, (list, tuple, set)):
        any_list = any_input
    else:
        any_list = [any_input]    


    def unpack(box):
        for item in box:
            if isinstance(item, (list, tuple, set)):
                unpack(item)  

            # Find any dictionary inside the list box
            elif isinstance(item, dict):
                clean_dict = deep_sort_dict(item)  #call global_helper_function
                dict_tracks.append(clean_dict)

            elif type(item) is bool:
                if item is True:
                    words.append("True")
                else:
                    words.append("False")        

            elif isinstance(item, (int, float)):
                numbers.append(item)

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

    # Start the engine using the dynamic argument variable
    unpack(any_list) 

                   
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


