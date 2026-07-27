# verify_live.py

#  1. Explicitly import the clean_and_flatten functions from both files
from deep_sort_list import clean_and_flatten as iterative_clean
from deep_sort_list_recursion_version import clean_and_flatten as recursive_clean

# 2. Define our standard testing payload matrix
final_test_list = [
    55, 
    "Python_Dev!", 
    True, 
    {"z_key": 9, "a_key": {"inner_b": 2, "inner_a": 1}}, 
    ["1000", "banana", "@@@"],
    [88, [False, ["#", 200, "404"]]]  # Sweeps regular collections smoothly
]

print("--- > Dual Engine Validation Sweep: Iterative vs. Recursive ---\n")

# 3. Process the list through the new iterative layout engine
res_iterative = iterative_clean(final_test_list, convert_numeric_strings=True)

# 4. Process the exact same list through your old recursive engine
res_recursive = recursive_clean(final_test_list, convert_numeric_strings=True)

# 5. Print out both tracks side-by-side to visually inspect them
print("=== 🔢 NUMBERS TRACK COMPARISON ===")
print("Iterative Engine (New) :", res_iterative["numbers"])
print("Recursive Engine (Old) :", res_recursive["numbers"])

print("\n=== 🔤 WORDS TRACK COMPARISON ===")
print("Iterative Engine (New) :", res_iterative["words"])
print("Recursive Engine (Old) :", res_recursive["words"])

print("\n=== 🗂️ DICTIONARIES TRACK COMPARISON ===")
print("Iterative Engine (New) :", res_iterative["dictionaries"])
print("Recursive Engine (Old) :", res_recursive["dictionaries"])

print("\n" + "="*60 + "\n")

# 6. Use an automated assert equality sweep to verify they match perfectly!
assert res_iterative == res_recursive, "❌ Discrepancy Found! The structural tracking layouts do not match."
print("ARCHITECTURAL PARITY CONFIRMED! Both engines generated the exact same data outputs.")
