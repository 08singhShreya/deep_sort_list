import deep_sort_list

print("Running automated test suite...")

# 🔹 Scenario 1: Standalone Single Input (The entryway protection check)
res1 = deep_sort_list.clean_and_flatten(8)
assert res1["numbers"] == [8], f"Failed Scenario 1: Expected [8], got {res1['numbers']}"

# 🔹 Scenario 2: Standard Mixed List with Empty Containers & Booleans
weird_list = [2, [], True, False, "apple"]
res2 = deep_sort_list.clean_and_flatten(weird_list)
# Remember: False is 0, True is 1 mathematically!
assert res2["numbers"] == [False, True, 2], f"Failed Scenario 2 Numbers: Got {res2['numbers']}"
assert res2["words"] == ["apple"], f"Failed Scenario 2 Words"

# 🔹 Scenario 3: String Number Conversion Toggle (True vs False)
mixed_digits = ["100", "banana", 44]

# Test with Conversion OFF (Default)
res3_off = deep_sort_list.clean_and_flatten(mixed_digits)
assert res3_off["words"] == ["100", "banana"], "Failed Scenario 3 OFF"

# Test with Conversion ON
res3_on = deep_sort_list.clean_and_flatten(mixed_digits, convert_numeric_strings=True)
assert res3_on["numbers"] == [44, 100], f"Failed Scenario 3 ON Numbers: Got {res3_on['numbers']}"
assert res3_on["words"] == ["banana"], "Failed Scenario 3 ON Words"

# 🔹 Scenario 4: Deep Multi-Nested Dictionary Locker Sorting
nested_dict = [{"sex": "Female", "name": {"last": "Singh", "first": "Shreya"}}]
res4 = deep_sort_list.clean_and_flatten(nested_dict)

expected_dict = [{'name': {'first': 'Shreya', 'last': 'Singh'}, 'sex': 'Female'}]
assert res4["dictionaries"] == expected_dict, f"Failed Scenario 4 Locker Sort"

print("ALL SCENARIOS PASSED PERFECTLY! Your library is bulletproof.")
