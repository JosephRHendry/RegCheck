# RegCheck
Python program to check an xls of regexes against a text file and list what matches matched where<br>

RegCheck.py - Actual RegEx checking program<br>
xml_sort.py - File for taking the exported mail rule list from ms-exchange and scraping the regex's into an array<br>
<br>
To use:
<ul>
  <li>Export your exchange mail flow rules list into "rules/Rules.xml" located in the program directory</li>
  <li>Place the text file to analyze in "mail/<name.txt>"</li>
  <li>Edit the text file name at the bottom of xml_sort.py</li>
  <li>Run xml_sort.py</li>
