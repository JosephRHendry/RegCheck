from bs4 import BeautifulSoup
import re
from regcheck import RegCheck

infile = open("Rules.xml","r", encoding='utf-16')
print(infile)
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
rules = soup.find_all('commandBlock')
pattern = "(?<=')[^']*"
#pattern = "docume"
match_list = []
#print(rules)
rule_list = []
for i, rule in enumerate(rules):
    #print(i, " ", rule.text)
    start_pos = rule.text.find('-Mode Audit')
    end_pos = rule.text.find('Except')
    if end_pos == 0:
        end_pos = rule.text.find("FromScope")
    if end_pos == 0:
        end_pos = rule.text.find('-SetAudit')
    rule_list.append(rule.text[start_pos:end_pos])
    #print(rule_list[i])

print("######")

for i, rule in enumerate(rule_list):
    print("List :", i)
    match_num = 0
    for match in re.finditer(pattern, rule):
        if str(match.group()) != ", ":
            if str(match.group()) != " -":
                match_num +=1
                match_list.append(match.group())
                print(match_num, " :", match.group())

print("######")

RegCheck("mail\mac1.txt", match_list)
