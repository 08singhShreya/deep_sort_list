# deep_sort_list

A bulletproof data parsing library designed to safely unwrap, flatten, and sort messy, multi-nested collections (Lists and Dictionaries) without crashing.

## What This Solves
Python's native `.sort()` method immediately crashes with a `TypeError` if a list contains mixed data types (like strings and integers together), or if it contains nested structures. 

This library completely bypasses that limitation by automatically separating elements into distinct, sorted data streams.

## 🚀 How to Use

Save `deep_sort_list.py` in your project folder, import it, and pass your data payload into the `clean_and_flatten` function.

### 🔹 Scenario 1: Sorting a Complex, Mixed Input
You can pass completely mixed lists, nested sublists, or even single items directly without a crash.

```python
import deep_sort_list

# A chaotic list containing numbers, strings, symbols, and nested boxes
data = [44, [3, "@#%&"], "banana"]

result = deep_sort_list.clean_and_flatten(data)

print(result["numbers"]) # Output: [3, 44]
print(result["words"])   # Output: ['banana']
print(result["symbols"]) # Output: ['@#%&']
```

### 🔹 Scenario 2: Handling Nested Dictionaries (Locker Sorting)
If your list contains multi-layered dictionaries, the engine digs through every sub-layer, alphabetizes all keys, keeps the values safely locked to their pairs, and puts them into a dedicated track.

```python
nested_data = [{"sex": "Female", "name": {"last": "Singh", "first": "Shreya"}}]

result = deep_sort_list.clean_and_flatten(nested_data)
print(result["dictionaries"])
# Output: [{'name': {'first': 'Shreya', 'last': 'Singh'}, 'sex': 'Female'}]
```

### 🔹 Scenario 3: Smart Number Conversion
By default, text digits like `'100'` are kept in the words track. Set `convert_numeric_strings=True` to dynamically convert and sort them as math integers.

```python
result = deep_sort_list.clean_and_flatten(data, convert_numeric_strings=True)
```

## 📊 Return Format
The function returns a clean Python dictionary with four tracks:
- `result["numbers"]`: Sorted integers and floats.
- `result["words"]`: Sorted text strings.
- `result["symbols"]`: Sorted special punctuation marks (like `@`, `#`, `^`).
- `result["dictionaries"]`: Deeply key-sorted internal dictionary blocks.