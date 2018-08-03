import re
import pandas as pd
from docx import Document

file_name="Rules\PhishingRegex.xlsx"
#file_name="Rules\WarnAudit-PhishingPatterns-Subject.xlsx"
#file_name="Rules\Suspicious Patterns.xlsx"

file_name_text = "mail\mac1.txt"

xl_file = pd.read_excel(file_name) # Read the excel file as a Pandas dataframe
rules = []
f = open(file_name_text,'r', encoding='utf-8') # Loads the text file to scan
message = f.read() # The text as a string variable

for index, row in xl_file.iterrows(): # Loop through the excel sheet and add each row to an array
    print(index, row[0])
    rules.append(str(row[0]))

for i, line in enumerate(open(file_name_text, encoding='utf-8')): # Loop through every line of the text file
    for v in range(len(rules)): # Loop through every line of the rules
        for match in re.finditer(rules[v], line): # Check for a match
            print("Match #{} : {}".format(v, str(rules[v])))
            print('Found on line %s: %s' % (i+1, match.groups()))
            print(str(line)) # Print line which matched

def RegCheck(file_name_text, rules_list):
    """
    Function to check a text against a set or regular expression rules and return the match
    :param file_name_text:
    :param rules:
    :return:
    """
    print("Reg Check")

    rules = []

    if isinstance(rules_list, str):
        xl_file = pd.read_excel(rules)  # Read the excel file as a Pandas dataframe
        for index, row in xl_file.iterrows():  # Loop through the excel sheet and add each row to an array
            print(index, row[0])
        rules.append(str(row[0]))

    else:
        rules = rules_list

    for i, rule in enumerate(rules):
        if "\z" in rule:
            print("Rule :", rule)
            rules[i]=(rule.replace("\z", ""))

    f = open(file_name_text, 'r', encoding='utf-8')  # Loads the text file to scan
    message = f.read()  # The text as a string variable

    for i, line in enumerate(open(file_name_text, encoding='utf-8')):  # Loop through every line of the text file
        for v in range(len(rules)):  # Loop through every line of the rules
            for match in re.finditer(rules[v], line):  # Check for a match
                print("Match #{} : {}".format(v, str(rules[v])))
                print('Found on line %s: %s' % (i + 1, match.groups()))
                print(str(line))  # Print line which matched


# print("###")
#
# """
# Alternate method of scanning by the whole document rather than by line, with the idea that some matches may
# be broken up over multiple lines
# """
# info = []
# for i in range(len(rules)):
#     print(rules[i])
#     if re.search(rules[i], message):
#         info.append((i, rules[i], re.search(rules[i], message), re.search(rules[i],message).group()))
#
# for i in info:
#     print("Matched Line: {} Match: {}".format(i[0],i[1]))
#     print("With :{}".format(i[3]))
