# RegCheck
Python program to check an xls of regexes against a text file and list which matches matched where<br>
Primarily to be used for evaluating and tuning Exchange mail flow rules<br>

# Requirements
Python3
re
Beautiful Soup

# Background
I created this program after implementing mail flow rules in exchange. These rules are regexes which block or flag suspect mail. After implementing this I monitored which items were getting flagged and saw that the rules list was capturing too many false positives. The problem was that there was no indication which of the mail rules has caused a given piece of mail to get flagged, so I created this program to compare the mail that was flagged against the rules list and see specifically which regex matches caused the mail to be flagged so that the regexes could be more finely tuned.

RegCheck.py - Used to perform the regex comparisons<br>
xml_sort.py - File for taking the exported mail rule list from ms-exchange and scraping the regex's into an array<br>
<br>
To use:
<ul>
  <li>Export your exchange mail flow rules list into "rules/Rules.xml" located in the program directory</li>
    <ul>
      <li>To export your rules list you can use powershell. First you'll need to install the Exchange Online Remote PowerShell Module. Instruction <a href="https://docs.microsoft.com/en-us/powershell/exchange/exchange-online/connect-to-exchange-online-powershell/mfa-connect-to-exchange-online-powershell?view=exchange-ps">here</a></li>
      <li>Once connected, you can export your rules list with the following powershell command: $file = Export-TransportRuleCollection; Set-Content -Path "C:\program_directory\Rules.xml" -Value $file.FileData -Encoding Byte</li></ul>
  <li>Place the text file to analyze in "mail/mail.txt"</li>
  <li>Run xml_sort.py</li>
