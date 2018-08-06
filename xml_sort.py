from bs4 import BeautifulSoup
import re
from regcheck import RegCheck

print("XML SORT\n")
infile = open("rules/Rules.xml","r", encoding='utf-16')
#rint(infile)
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
rules = soup.find_all('commandBlock')
rule_name_list = []

# print("list names :")
pattern = r'(?<=rule name=")[^"]*'
#data_soup.find_all(attrs={"data-foo": "value"})

for match in re.finditer(pattern, contents):
    rule_name_list.append(match.group())
    # print(match.group())


pattern = "(?<=')[^']*"
match_list = []
#print(rules)
rule_list = []


for i, rule in enumerate(rules): # Search for starting location for regex search
    #print(i, " ", rule.text)
    start_pos = rule.text.find('-Mode Audit')
    #print("Start position :", start_pos)
    if start_pos < 0:
        start_pos = rule.text.find('-Mode Enforce')

    end_pos = rule.text.find('Except') # Search for ending location for regex search
    if end_pos == 0:
        end_pos = rule.text.find("FromScope")
    if end_pos == 0:
        end_pos = rule.text.find('-SetAudit')
    rule_list.append(rule.text[start_pos:end_pos])
    #print(rule_list[i])

print("######\n")
complete_list = []

for i, rule in enumerate(rule_list):
    print("\nList #{}: {}".format(i,rule_name_list[i]))
    match_num = 0
    for match in re.finditer(pattern, rule):
        if str(match.group()) != ", ": # Eliminate erroneous non-regexes
            if str(match.group()) != " -":
                if str(match.group()) != " -FromScope NotInOrganization -":
                    match_num +=1
                    match_list.append(match.group())
                    print(match_num, " :", match.group())
                    match_info={'list': rule_name_list[i], 'match':match.group(), 'match_num':match_num}
                    complete_list.append(match_info)


print("\n######\n")

RegCheck(r"mail/you1.txt", complete_list)
