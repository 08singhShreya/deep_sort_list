import deep_sort_list

print("Running Iterative & Set-Safe Test Passes...")

# 🔹 Test 1: Infinite Depth List Parsing (Bypassing the 1,000 recursion ceiling)
nested_bomb = "Breakthrough"
for _ in range(1200):
    nested_bomb = [nested_bomb]

res1 = deep_sort_list.clean_and_flatten(nested_bomb)
assert res1["words"] == ["Breakthrough"], "Failed Recursion Stack Test!"

# 🔹 Test 2: Unhashable Set Safety Check 
set_data = {44, "banana", (1, 2)} 
res2 = deep_sort_list.clean_and_flatten(set_data)
assert res2["numbers"] == [1, 2, 44]
assert res2["words"] == ["banana"]

# 🔹 Test 3: Multiple Dictionary Ordering Check (Verifying Left-to-Right Order)
mixed_dicts = [{"z": 1}, {"a": 2}]
res3 = deep_sort_list.clean_and_flatten(mixed_dicts)
assert res3["dictionaries"] == [{"z": 1}, {"a": 2}], "Failed Left-to-Right structural alignment!"

print("ALL TESTS PASSED! The new iterative logic works.")
