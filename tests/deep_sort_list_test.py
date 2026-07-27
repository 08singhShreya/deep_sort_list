import sys
import os
# Force Python to include the parent root folder in its search radar
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import collections
import version1.deep_sort_list_recursion_version as deep_sort_list_recursion_version

crazy_list = [44, [3, "apple", "@#%&"], {"name": "Aadhya", "sex": "Female", "personal_details": {"is_married": False, "address": {"house_no": 448, "plot_no": 403, "strret": 'abc', "locality": "janki_nagar_extension", "pincode": 452010}, "is_employed": True}, "religion": "Hindu"}, "banana", "100", "^^^", '&', '101','222','1000', 589, [445,[28,'%','828',[45,54],'*']]]

my_list = [44, '404', 88, 100, '100', '101', "Shreya@08singh","hey, buddy",'#', '^', {"subject": "english", "marks": {"internal_marks": 75, "internal_marks_2": 88}}, 'bjbj', 22545,[44, '404', 88, 100, '100', '101','#', '^', 'bjbj', 22545, 56, [44, '404', 88, 100, '100', '101','#', '^', 'bjbj', 22545,[44,"Hello David", '404', 88, 100, '100', '101','#', '^', 'bjbj', 22545]]]]

print("------Testing List--------")


print("=== REQUIREMENT 1: Standard Dictionary Return ===")
result_crazy_list = deep_sort_list_recursion_version.clean_and_flatten(crazy_list)
result_my_list = deep_sort_list_recursion_version.clean_and_flatten(my_list)

print("--- CRAZY LIST ---")
print("Words:", result_crazy_list["words"])
print("Numbers:", result_crazy_list["numbers"])
print("Symbols:", result_crazy_list["symbols"])

print("\n--- MY LIST ----")
print("Words:", result_my_list["words"])
print("Numbers:", result_my_list["numbers"])
print("Symbols:", result_my_list["symbols"])
print("Dictionaries:", result_my_list["dictionaries"])


print("=== REQUIREMENT 2: Convert String Numbers to Ints ===")
r_crazy_list = deep_sort_list_recursion_version.clean_and_flatten(crazy_list, convert_numeric_strings=True)
r_my_list = deep_sort_list_recursion_version.clean_and_flatten(my_list, convert_numeric_strings=True)

print("Words", r_crazy_list["words"])
print("Numbers", r_crazy_list["numbers"])
print("Symbols", r_crazy_list["symbols"])
print("Dictionaries", r_crazy_list["dictionaries"])

print("--- MY LIST WITH CONVERSION ON ---")
print("Words:", r_my_list["words"])
print("Numbers:", r_my_list["numbers"])
print("Symbols:", r_my_list["symbols"])