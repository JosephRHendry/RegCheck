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
  <li>The program will output a list of all rules followed by the matches and locations</li>

# Sample Output (Mail rules list originally from @SwiftOnSecurity)
"C:\Users\JHendry\Dropbox (Connected California)\JH\python\RegCheck\venv\Scripts\python.exe" "C:/Users/JHendry/Dropbox (Connected California)/JH/python/RegCheck/xml_sort.py"
XML SORT

######


List #0: Suspicious Patterns
1  : \.top/
2  : \.joburg
3  : tiny\.cc/
4  : \.wix\.com
5  : \.weebly\.com
6  : is\.gd/
7  : \.000webhost(app)?\.com
8  : /https?/www/
9  : \w\.jar(?=\b)
10  : ownership\ validation\ (has\ )?expired
11  : \.xyz/
12  : contabo\.net
13  : mailowa
14  : \.myfreesites\.net
15  : \.tripod\.com
16  : \.ezweb123\.com
17  : \.sitey\.me
18  : \.freetemplate\.site
19  : //webmail(?!\.)
20  : \.yolasite\.com
21  : mail-?update
22  : \.my-free\.website
23  : //helpdesk(?!\.)
24  : (?<!gsm)-(un)?b?locked
25  : security-?warning
26  : simplefileupload
27  : /www/amazon
28  : /newdropbox/
29  : security-?err
30  : \.invoice\.php
31  : %20paypal
32  : /dro?pbo?x/
33  : /natwest/
34  : pay\Sa\S{0,2}login
35  : /helpdesk/
36  : /docu\S{0,3}sign\S{1,4}/
37  : pyapal
38  : /office\S{0,3}365/
39  : outlook\W365
40  : owaportal
41  : /\S{0,3}outloo\S{0,2}k\S{1,3}\W
42  : /uploadfile/
43  : myfreesites\.net
44  : sitey\.me
45  : limit\ (and\ suspend\ )?your\ account
46  : /Dropfile/
47  : /googledocs?/
48  : /GoogleDrive/
49  : (?<![\x00\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5A])appie\W
50  : chase\S{0,10}\.html"
51  : dear\ \w{3,8}(\ banking)?\ user
52  : Verify\ your\ ID\s
53  : sign\ in\S{0,7}(with\ )?\ your\ email\ address
54  : Securely\ \S{3,4}\ Google\ Drive
55  : Securely\ \S{3,4}\ drop(\ )?box
56  : Securely\ \S{3,4}\ one(\ )?drive
57  : updated?\ your\ account\ record
58  : suspicious\ activit
59  :  blocked\ your?\ online

List #1: Potential Links to Hacked Websites
1  : \/wp-includes\/
2  : \/wp-admin\/

List #2: Suspicious Phrases
1  : [Tt]ransfter [Pp]ayment
2  : verify and reactivate
3  : Account Was Limited
4  : update in our security
5  : update your account information
6  : informations on your account
7  : restricted if you fail to update
8  : suspend your account
9  : trying to access your account
10  : multiple login attempt
11  : that you validate your account
12  : urged to download
13  : was blocked for violation
14  : your apple id was used to sign in to
15  : your account will be closed
16  : FRAUD NOTICE
17  : has been compromised
18  : via Paypal
19  : submit your payment
20  : Update your payment
21  : activate your account
22  : delayed payment
23  : unable to verify
24  : failed to validate
25  : confirm your informations
26  : fallow our process
27  : informations has been
28  : prevent further unauthorised
29  : prevent further unauthorized
30  :  word must be installed

List #3: Suspicious Subjects
1  : verification\ required
2  : temporar(il)?y\ deactivated
3  : secure\ update
4  : wire\ transfer
5  : account\ (is\ )?on\ hold
6  : refund\ not\ approved
7  : Periodic\ Maintenance
8  : your\ (customer\ )?account\ was
9  : your\ (customer\ )?account\ has
10  : notifications\ pending
11  : unusual\ activity
12  : has\ been\ suspended
13  : We\ have\ locked
14  : has\ been\ limited

List #4: Quarantine-Content
1  : \|\s*Download.as.Excel
2  : \.com/\?[0-9]+\=
3  : You have new documents sent to you via
4  : will be deleted in few hours
5  : View Invoice in DOCx?\W
6  : used docu.?box to
7  : to share some document 
8  : shared?.a.secure.file
9  : shared a private document
10  : secured? files link
11  : Scan result: Clean
12  : Purchase Order for your kind reference
13  : Our courier attempted
14  : one drive team
15  : no emails reply: no emails
16  : new\W*documents\W*was\W*sent\W*to\W*you 
17  : MOVE.MESSAGE.TO.IN.?BOX
18  : invoice.?#.?[0-9]{3,}\.doc
19  : how to resolve your email
20  : File scanned by Avast antivirus
21  : dropbox file sent
22  : Download.\|.View
23  : clustered messages
24  : but there was nobody who could sign
25  : Antivirus.Status:\s*Clean
26  : a Secured File with you
27  : /New-invoice-
28  : /invoice-due-
29  : //bitly\.im/

List #5: Quarantine-VipSpoofing
1  : From
2  :  -HeaderMatchesPatterns 
3  : Lucia.*Villasana
4  : Sheryl.*Jones
5  : Gary.*Hoachlander

List #6: Quarantine-Sender
1  : \.ssl\.com$
2  : VoiceMessage@
3  : vmservice@
4  : mail365
5  : ffax.com
6  : efax@
7  : dropsign\.net
8  : docusign\-
9  : docusigns
10  : @dse\.com

List #7: Quarantine-Subject
1  : Your password has been compromised
2  : Your document Settlement
3  : You have notifications pending
4  : Unrecognized login attempt,
5  : secured pdf
6  : secured files
7  : RingCentral
8  : REQUIRED: Completed Docusign
9  : Fwd: Due invoice paid
10  : FreeFax
11  : document has been sent to you via Docusign
12  : document for you
13  : docu sign
14  : detected suspicious actvity
15  : detected suspicious
16  : Delivery stopped for shipment
17  : Closing Statement Invoice Payment For PO
18  : bankofamerica
19  : Banking is temporarily unavailable
20  : Attached File to Docusign
21  : ACTION REQUIRED: Completed: Docusign
22  : account Has Been Limited
23  : .com Document is Ready for Signature

List #8: WarnAudit-PhishingPatterns-Subject
1  : temporar[il1]{2,}y disab[li]ed
2  : temporarily.*lock
3  : temporar(il)?y deactivate
4  : Susp[il1]+c[il1]+ous.*Act[il1]+v[il1]+ty
5  : Suspicious.Activit
6  : suspicious.*sign.*[io]n
7  : status of your .{3,14}? ?delivery
8  : Signed.*delivery
9  : securlty
10  : security breach
11  : secured?.update
12  : scanned.?invoice
13  : refund not approved
14  : potential(ly)? unauthorized
15  : Periodic Maintenance
16  : password.*compromised
17  : on\ google\ docs\ with\ you
18  : online doc
19  : office365
20  : office.*3.*6.*5.*suspend
21  : notifications?.pending
22  : new [sl][io]g?[nig][ -]?in from
23  : new voice ?-?mail
24  : Must.Update.Your.Account
25  : Missed.shipment.notification
26  : missed.*shipping.*notification
27  : ma[il1]{2,}[ -]?box.*fu[il1]
28  : Ma[il1]{2,}box\ Stor
29  : ma[il1]{2,}box.*[il1]{2,}mit
30  : ma[il1]{1,}[ -]?box.*quo
31  : mails.pending
32  : mail.update.required
33  : mail.*de-?activat
34  : mail.*box.*Migration
35  : mail on.?hold
36  : lock.*security
37  : i[il]iega[il]
38  : incoming.*Fax
39  : incoming e?mail
40  : ii[il]ega[il]
41  : he[li]p ?Desk Upgrade
42  : heipdesk
43  : have.locked
44  : has.been.limited
45  : has.been.*suspended
46  : fu[il1]{2,}.*ma[il1]+[ -]?box
47  : from.helpdesk
48  : fraud(ulent)?.*charge
49  : faxed you
50  : (?<!Sign up for.)email.update[^s]
51  : e.?ma[il1]{2,}.{0,50}suspend
52  : e.?ma[il1]{2,}.{50}server
53  : e-?ma[il1]{2,}.*up.?grade
54  : e-?ma[il1]{2,} acc
55  : e-?ma[il1]{1,} user
56  : e-?ma[il1]+ .{0,10}suspen
57  : dropbox.*document
58  : documented.*shared.*with.*you
59  : document.received
60  : Delivery.*Attempt.*Failed
61  : courier.*unable
62  : confirm.your.account
63  : Clos.*Of.*Account.*processed
64  : been.*suspend
65  : authenticate.*account
66  : app[li]e.[il]d
67  : almost.full
68  : activity.{0,20}acc(oun)?t
69  : account\ V[il]o[li]at
70  : account.will.be.blocked
71  : account.has.expired
72  : account.has.been
73  : account.*suspension
74  : account.*Security
75  : account.*re-verification
76  : account.*locked
77  : account.*de-?activat
78  : account (will be )?block
79  : access.*limitation
80  : acc(oun)?t.{50}[il1]{2,}mitation
81  : acc(ou)?n?t.{0,50}terminat
82  : acc(ou)?n?t (is )?on ho[li]d
83  : about.your.account
84  : abandon.*package
85  : :completed
86  : 3 6 5
87  : (?<!lease )termination.*notice
88  :  scam

List #9: WarnAudit-PhishingPatterns-Subject-2
1  : un-?usua[li].activity
2  : unable.*deliver
3  : unauthorized.*activit
4  : unauthorized.device
5  : undelivered message
6  : unread.*doc
7  : \bITS \s
8  : \bhoid\b
9  : \Aaction.*required\z
10  : [ng]-?[io]n .{50}disabl
11  : [ng]-?[io]n .{50}deactiv
12  : [ng]-?[io]n .{50}cancel
13  : [ng]-?[io]n .{50}block
14  : [li][li][li]ega[li] Attempt
15  : [il][il][il]egai[ -]
16  : [il1]{2,}mit.*ma[il1]{2,} ?bo?x
17  : your.online.access
18  : Your.Office.365
19  : your (customer )?account .as
20  : Will.Be.Suspended
21  : v[il1]o[li1]at[il1]on security
22  : verify.your?.account
23  : verification( )?-?need
24  : verification ?-?require
25  : va[il1]{1,}date.*ma[il1]{2,}[ -]?box
26  : urgent.verification
27  : urgent message
28  : UPGRADE.NOTICE
29  : upgrade.*account
30  : unusual.activity

######

Reg Check
List : WarnAudit-PhishingPatterns-Subject
Match #6 : suspicious.*sign.*[io]n
Found on line 7: suspicious email subject. Please use caution before clicking any links or following instructions below. Do not sign-in
Line :  <span style="color:#9C6500; font-weight:bold;">CAUTION:</span> This email originated from outside of the organization and has a suspicious email subject. Please use caution before clicking any links or following instructions below. Do not sign-in with your
 

List : Quarantine-VipSpoofing
Match #1 : From
Found on line 70: From
Line :  <div id="divRplyFwdMsg" dir="ltr"><font face="Calibri, sans-serif" style="font-size:11pt" color="#000000"><b>From:</b> Muhammad Umer<br>
 


Process finished with exit code 0
