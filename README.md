# RegCheck
Python program to check an xls of regexes against a text file and list which matches matched where<br>
Primarily to be used for evaluating and tuning Exchange mail flow rules<br>

# Requirements
Python3<br>
re<br>
Beautiful Soup<br>

# Background
I created this program after implementing mail flow rules in exchange. These rules are regexes which block or flag suspect mail. After implementing this I monitored which items were getting flagged and saw that the rules list was capturing too many false positives. The problem was that there was no indication which of the mail rules has caused a given piece of mail to get flagged, so I created this program to compare the mail that was flagged against the rules list and see specifically which regex matches caused the mail to be flagged so that the regexes could be more finely tuned.

RegCheck.py - Used to perform the regex comparisons<br>
xml_sort.py - File for taking the exported mail rule list from ms-exchange and scraping the regex's into an array<br>
<br>
# To use:
<ul>
  <li>Export your exchange mail flow rules list into "rules/Rules.xml" located in the program directory</li>
    <ul>
      <li>To export your rules list you can use powershell. First you'll need to install the Exchange Online Remote PowerShell Module. Instruction <a href="https://docs.microsoft.com/en-us/powershell/exchange/exchange-online/connect-to-exchange-online-powershell/mfa-connect-to-exchange-online-powershell?view=exchange-ps">here</a></li>
      <li>Once connected, you can export your rules list with the following powershell command: $file = Export-TransportRuleCollection; Set-Content -Path "C:\program_directory\Rules.xml" -Value $file.FileData -Encoding Byte</li></ul>
  <li>Place the text file to analyze in "mail/mail.txt"</li>
  <li>Run xml_sort.py</li>
  <li>The program will output a list of all rules followed by the matches and locations</li></ul>

(Mail rules list originally from @SwiftOnSecurity)
# Sample Output 

XML SORT

######
<br><br>

List #0: Suspicious Patterns<br>
1  : \.top/<br>
2  : \.joburg<br>
3  : tiny\.cc/<br>
4  : \.wix\.com<br>
5  : \.weebly\.com<br>
6  : is\.gd/<br>
7  : \.000webhost(app)?\.com<br>
8  : /https?/www/<br>
9  : \w\.jar(?=\b)<br>
10  : ownership\ validation\ (has\ )?expired<br>
11  : \.xyz/<br>
12  : contabo\.net<br>
13  : mailowa<br>
14  : \.myfreesites\.net<br>
15  : \.tripod\.com<br>
16  : \.ezweb123\.com<br>
17  : \.sitey\.me<br>
18  : \.freetemplate\.site<br>
etc. etc.<br>
######

Reg Check
List : WarnAudit-PhishingPatterns-Subject<br>
Match #6 : suspicious.*sign.*[io]n<br>
Found on line 7: suspicious email subject. Please use caution before clicking any links or following instructions below. Do not sign-in<br>
Line :  <span style="color:#9C6500; font-weight:bold;">CAUTION:</span> This email originated from outside of the organization and has a suspicious email subject. Please use caution before clicking any links or following instructions below. Do not sign-in with your<br>
 <br>
<br>

etc. etc.
