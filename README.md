# 📦 deep_sort_list_parser

A data parsing library designed to safely unwrap, flatten, and sort messy, multi-nested collections (Lists, Tuples, Sets, and Dictionaries) without crashing.

## 🌟 Enhanced Features
- **Infinite Flattening:** Recursively drills through any number of nested list layouts `[[[]]]` to extract loose data.
- **Advanced Type-Safe Tracking:** Automatically isolates items into distinct sorted categories: Numbers, Words, and Symbols.
- **Smart Text Analysis:** Intelligently tracks sentences with spaces and punctuation (like `"Hello World!"`) inside the words track instead of breaking them apart.
- **Boolean Guarding:** Standard booleans (`True` / `False`) are trapped safely and sorted inside the words track instead of corrupting mathematical numbers.
- **Deep Locker Sorting:** Alphabetizes keys inside nested dictionaries down to any depth while keeping values safely paired. Fully supports specialized dictionaries like `OrderedDict` and `Counter`.
- **On-the-Fly Conversion:** Dynamically casts numeric text strings (like `'100'`) into math integers upon request.

## 🚀 How to Use

Save `deep_sort_list.py` in your project folder, import it, and pass your data payload into the `clean_and_flatten` function.

### 🔹 Scenario 1: Standard Mixed Input (With Sentences & Booleans)
You can pass completely mixed lists, nested containers, or even single loose items safely.

```python
import deep_sort_list

# A chaotic list containing numbers, strings with punctuation, and booleans
data = [44, [3, "@#%&"], "Hello World!", True]

result = deep_sort_list.clean_and_flatten(data)

print(result["numbers"])      # [3, 44]
print(result["words"])        # ['Hello World!', 'True']
print(result["symbols"])      # ['@#%&']
```

### 🔹 Scenario 2: Handling Nested Dictionaries (Locker Sorting)
If your input contains complex dictionary blocks, the engine alphabetizes all internal keys at every sub-layer while keeping values locked to their pairs.

```python
nested_data = [{"sex": "Female", "name": {"last": "Singh", "first": "Aadhya"}}]

result = deep_sort_list.clean_and_flatten(nested_data)
print(result["dictionaries"])
# Output: [{'name': {'first': 'Aadhya', 'last': 'Singh'}, 'sex': 'Female'}]
```

### 🔹 Scenario 3: Smart Number Conversion
By default, text digits like `'100'` are kept in the words track. Set `convert_numeric_strings=True` to dynamically convert and sort them as math integers.

```python
result = deep_sort_list.clean_and_flatten(data, convert_numeric_strings=True)
```

## 📊 Return Format
The function returns a clean Python dictionary with four distinct tracks:
- `result["numbers"]`: Sorted integers and floats.
- `result["words"]`: Sorted alphanumeric text words, sentences, and booleans.
- `result["symbols"]`: Sorted pure punctuation strings (like `@`, `#`, `^`).
- `result["dictionaries"]`: Isolated dictionary blocks with fully alphabetized internal key layouts.