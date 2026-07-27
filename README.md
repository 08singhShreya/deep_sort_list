# 📦 deep_sort_list_parser

A lightweight, bulletproof utility library to flatten and sort mixed data arrays (Lists, Tuples, Sets, and Dictionaries) without crashing. 

It handles everything inside a single loop stack, meaning it will never crash from memory limits even if your data is nested thousands of layers deep.

## ✨ Key Features
- **Infinite Flattening:** Automatically drills through nested layers like `[[[]]]` to pull out elements.
- **Type-Safe Tracking:** Splits data into four clean, sorted tracks: Numbers, Words, Symbols, and Dictionaries.
- **Boolean Safe:** Keeps `True` / `False` inside the words track so they don't break your mathematical number sorting.
- **Locker Key Sorting:** Alphabetizes keys inside nested dictionaries down to any depth without losing their original key-value pairs.
- **String-to-Int Conversion:** Optional flag converts numeric text like `'100'` into real integers on command.

## 🚀 How to Use

### 🔹 Example 1: Standard Mixed Input (With Sentences & Booleans)
```python
import deep_sort_list

data = [44, [3, "banana!"], "Hello World", True]
result = deep_sort_list.clean_and_flatten(data)

print(result["numbers"])      # [3, 44]
print(result["words"])        # ['Hello World', 'True', 'banana!']
print(result["symbols"])      # []
print(result["dictionaries"]) # []
```

### 🔹 Example 2: Handling Nested Dictionaries
```python
nested_data = [{"sex": "Female", "name": "Shreya"}]
result = deep_sort_list.clean_and_flatten(nested_data)

print(result["dictionaries"]) 
# Output: [{'name': 'Shreya', 'sex': 'Female'}]
```

### 🔹 Example 3: String Number Conversion ON
```python
data = [44, "100", "banana"]
# Set convert_numeric_strings to True to change text digits into real math integers
result = deep_sort_list.clean_and_flatten(data, convert_numeric_strings=True)

print(result["numbers"]) # [44, 100]
print(result["words"])   # ['banana']
```

## 📊 Output Schema Layout
The library always returns a standard dictionary map containing:
- `result["numbers"]`: Perfectly sorted integers and floats.
- `result["words"]`: Perfectly sorted alphanumeric words, sentences, and booleans.
- `result["symbols"]`: Perfectly sorted pure punctuation strings (like `@`, `#`, `^`).
- `result["dictionaries"]`: Isolated dictionary blocks with internal alphabetical keys.
