# test_suite.py
import collections
import version1.deep_sort_list_recursion_version as deep_sort_list_recursion_version

print("Running optimized automated test suite...")

# 🔹 1. Test Sentence Spaces and Punctuation (Word vs Symbol Fix)
mixed_text = ["banana!", "Hello World", "@@@"]
res1 = deep_sort_list_recursion_version.clean_and_flatten(mixed_text)
assert res1["words"] == ["Hello World", "banana!"], f"Failed Word Fix: Got {res1['words']}"
assert res1["symbols"] == ["@@@"], f"Failed Symbol Fix: Got {res1['symbols']}"

# 🔹 2. Test Boolean Separation (Boolean Sorting Fix)
bool_list = [44, True, 0, False, 1]
res2 = deep_sort_list_recursion_version.clean_and_flatten(bool_list)
# Booleans should be completely absent from numbers and cleanly isolated in words!
assert res2["numbers"] == [0, 1, 44], f"Failed Number Separation: Got {res2['numbers']}"
assert res2["words"] == ["False", "True"], f"Failed Boolean Extraction: Got {res2['words']}"

# 🔹 3. Test Specialized Dictionary Support (OrderedDict Fix)
ordered_data = collections.OrderedDict([("z", 1), ("a", 2)])
res3 = deep_sort_list_recursion_version.clean_and_flatten(ordered_data)
# The engine should catch it via isinstance and process it natively into dictionaries!
assert res3["dictionaries"] == [{"a": 2, "z": 1}], f"Failed Sub-dict Handling: Got {res3['dictionaries']}"

print("ALL ARCHITECTURAL PASSES OK!")

