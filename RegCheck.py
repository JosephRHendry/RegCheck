import re
import pandas as pd
from docx import Document

def RegCheck(file_name_text, rules_list):
    """
    Function to check a text against a set or regular expression rules and return the match
    :param file_name_text:
    :param rules_list: An array o
    :return:
    """
    print("Reg Check")

    rules = []

    rules = rules_list

    for i, rule in enumerate(rules):
        if "\z" in rule['match']: # Currently this is an invalid escape character, so replacing with nothing
            temp_string = str(rule['match'])
            temp_string = temp_string.replace("\z", "")
            rules[i]['match']=temp_string

    f = open(file_name_text, 'r', encoding='utf-8')  # Loads the text file to scan
    message = f.read()  # The text as a string variable

    for i, line in enumerate(open(file_name_text, encoding='utf-8')):  # Loop through every line of the text file
        for v in range(len(rules)):  # Loop through every line of the rules
            for match in re.finditer(rules[v]['match'], line):  # Check for a match
                print("List : {}".format(rules[v]['list']))
                print("Match #{} : {}".format(rules[v]['match_num'], str(rules[v]['match'])))
                print('Found on line %s: %s' % (i + 1, match.group()))
                print("Line : ", str(line))  # Print line which matched

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
