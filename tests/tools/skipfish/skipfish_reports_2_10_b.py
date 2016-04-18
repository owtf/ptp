report_high_samples = r"""var mime_samples = [
  { 'mime': 'application/javascript', 'samples': [
    { 'url': 'http://demo.testfire.net/bank/mozxpath.js', 'dir': '_m0/0', 'linked': 2, 'len': 1414 },
    { 'url': 'http://demo.testfire.net/pr/Draft.rtf', 'dir': '_m0/1', 'linked': 2, 'len': 11281 },
    { 'url': 'http://demo.testfire.net/pr/Q3_earnings.rtf', 'dir': '_m0/2', 'linked': 2, 'len': 187754 } ]
  },
  { 'mime': 'application/pdf', 'samples': [
    { 'url': 'http://demo.testfire.net/pr/communityannualreport.pdf', 'dir': '_m1/0', 'linked': 2, 'len': 63887 } ]
  },
  { 'mime': 'application/vnd.ms-excel', 'samples': [
    { 'url': 'http://demo.testfire.net/admin/clients.xls', 'dir': '_m2/0', 'linked': 2, 'len': 119296 } ]
  },
  { 'mime': 'application/x-shockwave-flash', 'samples': [
    { 'url': 'http://demo.testfire.net/subscribe.swf', 'dir': '_m3/0', 'linked': 2, 'len': 2484 } ]
  },
  { 'mime': 'application/xhtml+xml', 'samples': [
    { 'url': 'http://demo.testfire.net/', 'dir': '_m4/0', 'linked': 2, 'len': 9953 },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'dir': '_m4/1', 'linked': 2, 'len': 9040 },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/', 'dir': '_m4/2', 'linked': 2, 'len': 4169 },
    { 'url': 'http://demo.testfire.net/bank/members/', 'dir': '_m4/3', 'linked': 2, 'len': 1656 },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'dir': '_m4/4', 'linked': 5, 'len': 5451 },
    { 'url': 'http://demo.testfire.net/bank/servererror.aspx', 'dir': '_m4/5', 'linked': 2, 'len': 3479 },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'dir': '_m4/6', 'linked': 5, 'len': 7539 },
    { 'url': 'http://demo.testfire.net/notfound.aspx', 'dir': '_m4/7', 'linked': 2, 'len': 7695 },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_contact.htm', 'dir': '_m4/8', 'linked': 2, 'len': 10815 },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal_investments.htm', 'dir': '_m4/9', 'linked': 2, 'len': 8802 },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal.htm', 'dir': '_m4/10', 'linked': 2, 'len': 9167 },
    { 'url': 'http://demo.testfire.net/default.aspx?content=business_deposit.htm', 'dir': '_m4/11', 'linked': 0, 'len': 8365 },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_executives.htm', 'dir': '_m4/12', 'linked': 0, 'len': 10867 },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_jobs.htm', 'dir': '_m4/13', 'linked': 0, 'len': 11290 },
    { 'url': 'http://demo.testfire.net/default.aspx?content=privacy.htm', 'dir': '_m4/14', 'linked': 0, 'len': 13220 },
    { 'url': 'http://demo.testfire.net/default.aspx?content=security.htm', 'dir': '_m4/15', 'linked': 0, 'len': 11909 } ]
  },
  { 'mime': 'image/gif', 'samples': [
    { 'url': 'http://demo.testfire.net/images/adobe.gif', 'dir': '_m5/0', 'linked': 2, 'len': 1425 },
    { 'url': 'http://demo.testfire.net/images/altoro.gif', 'dir': '_m5/1', 'linked': 2, 'len': 4113 },
    { 'url': 'http://demo.testfire.net/images/logo.gif', 'dir': '_m5/2', 'linked': 2, 'len': 4989 },
    { 'url': 'http://demo.testfire.net/images/pf_lock.gif', 'dir': '_m5/3', 'linked': 2, 'len': 76 },
    { 'url': 'http://demo.testfire.net/images/spacer.gif', 'dir': '_m5/4', 'linked': 2, 'len': 43 } ]
  },
  { 'mime': 'image/jpeg', 'samples': [
    { 'url': 'http://demo.testfire.net/admin/captcha.aspx', 'dir': '_m6/0', 'linked': 2, 'len': 4290 },
    { 'url': 'http://demo.testfire.net/images/b_cards.jpg', 'dir': '_m6/1', 'linked': 2, 'len': 7235 },
    { 'url': 'http://demo.testfire.net/images/b_deposit.jpg', 'dir': '_m6/2', 'linked': 2, 'len': 6734 },
    { 'url': 'http://demo.testfire.net/images/b_insurance.jpg', 'dir': '_m6/3', 'linked': 2, 'len': 9195 },
    { 'url': 'http://demo.testfire.net/images/b_lending.jpg', 'dir': '_m6/4', 'linked': 2, 'len': 8481 },
    { 'url': 'http://demo.testfire.net/images/b_other.jpg', 'dir': '_m6/5', 'linked': 2, 'len': 5701 },
    { 'url': 'http://demo.testfire.net/images/b_retirement.jpg', 'dir': '_m6/6', 'linked': 2, 'len': 6848 },
    { 'url': 'http://demo.testfire.net/images/DownloadAppScanDemo_172x80.jpg', 'dir': '_m6/7', 'linked': 2, 'len': 6233 },
    { 'url': 'http://demo.testfire.net/images/header_pic.jpg', 'dir': '_m6/8', 'linked': 2, 'len': 16209 },
    { 'url': 'http://demo.testfire.net/images/home1.jpg', 'dir': '_m6/9', 'linked': 2, 'len': 7900 },
    { 'url': 'http://demo.testfire.net/images/home2.jpg', 'dir': '_m6/10', 'linked': 2, 'len': 5904 },
    { 'url': 'http://demo.testfire.net/images/home3.jpg', 'dir': '_m6/11', 'linked': 2, 'len': 10441 },
    { 'url': 'http://demo.testfire.net/images/inside1.jpg', 'dir': '_m6/12', 'linked': 2, 'len': 3697 },
    { 'url': 'http://demo.testfire.net/images/inside4.jpg', 'dir': '_m6/13', 'linked': 2, 'len': 5477 },
    { 'url': 'http://demo.testfire.net/images/inside5.jpg', 'dir': '_m6/14', 'linked': 2, 'len': 4869 },
    { 'url': 'http://demo.testfire.net/images/inside6.jpg', 'dir': '_m6/15', 'linked': 2, 'len': 6573 },
    { 'url': 'http://demo.testfire.net/images/p_cards.jpg', 'dir': '_m6/16', 'linked': 2, 'len': 9899 },
    { 'url': 'http://demo.testfire.net/images/p_loans.jpg', 'dir': '_m6/17', 'linked': 2, 'len': 7740 },
    { 'url': 'http://demo.testfire.net/images/p_main.jpg', 'dir': '_m6/18', 'linked': 2, 'len': 8193 } ]
  },
  { 'mime': 'image/x-ms-bmp', 'samples': [
    { 'url': 'http://demo.testfire.net/images/cancel.gif', 'dir': '_m7/0', 'linked': 2, 'len': 2598 } ]
  },
  { 'mime': 'text/css', 'samples': [
    { 'url': 'http://demo.testfire.net/style.css', 'dir': '_m8/0', 'linked': 2, 'len': 1198 } ]
  },
  { 'mime': 'text/html', 'samples': [
    { 'url': 'http://demo.testfire.net/', 'dir': '_m9/0', 'linked': 2, 'len': 42 },
    { 'url': 'http://demo.testfire.net/admin/', 'dir': '_m9/1', 'linked': 5, 'len': 218 },
    { 'url': 'http://demo.testfire.net/bank/', 'dir': '_m9/2', 'linked': 5, 'len': 2364 },
    { 'url': 'http://demo.testfire.net/bank/ws.asmx', 'dir': '_m9/3', 'linked': 2, 'len': 3794 },
    { 'url': 'http://demo.testfire.net/bank/ws.asmx?op=GetUserAccounts', 'dir': '_m9/4', 'linked': 2, 'len': 6773 },
    { 'url': 'http://demo.testfire.net/bank/default.aspx?content=inside_contact.htm', 'dir': '_m9/5', 'linked': 2, 'len': 174 },
    { 'url': 'http://demo.testfire.net/pr/', 'dir': '_m9/6', 'linked': 2, 'len': 584 },
    { 'url': 'http://demo.testfire.net/disclaimer.htm', 'dir': '_m9/7', 'linked': 2, 'len': 2083 },
    { 'url': 'http://demo.testfire.net/retirement.htm', 'dir': '_m9/8', 'linked': 2, 'len': 1123 },
    { 'url': 'http://demo.testfire.net/test.aspx', 'dir': '_m9/9', 'linked': 0, 'len': 558 } ]
  },
  { 'mime': 'text/xml', 'samples': [
    { 'url': 'http://demo.testfire.net/bank/ws.asmx?disco', 'dir': '_m10/0', 'linked': 2, 'len': 731 },
    { 'url': 'http://demo.testfire.net/bank/ws.asmx?WSDL', 'dir': '_m10/1', 'linked': 0, 'len': 8329 },
    { 'url': 'http://demo.testfire.net/pr/Docs.xml', 'dir': '_m10/2', 'linked': 2, 'len': 779 } ]
  }
];

var issue_samples = [
  { 'severity': 4, 'type': 50103, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'response to \x27\x27\x27\x27\x22\x22\x22\x22 different than to \x27\x22\x27\x22\x27\x22\x27\x22', 'sid': '0', 'dir': '_i0/0' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'response to \x27\x27\x27\x27\x22\x22\x22\x22 different than to \x27\x22\x27\x22\x27\x22\x27\x22', 'sid': '0', 'dir': '_i0/1' } ]
  },
  { 'severity': 3, 'type': 40501, 'samples': [
    { 'url': 'http://demo.testfire.net/default.aspx?content=./inside_contact.htm', 'extra': 'responses for ./val and .../val look different', 'sid': '0', 'dir': '_i1/0' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=.\x5cinside_contact.htm', 'extra': 'responses for .\x5cval and ...\x5cval look different', 'sid': '0', 'dir': '_i1/1' } ]
  },
  { 'severity': 3, 'type': 40402, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/0' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/1' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/2' } ]
  },
  { 'severity': 3, 'type': 40305, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i3/0' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i3/1' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i3/2' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i3/3' },
    { 'url': 'http://demo.testfire.net/notfound.aspx?aspxerrorpath=/Privacypolicy.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000162v391429\x3e', 'extra': '', 'sid': '0', 'dir': '_i3/4' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=skipfish.htm', 'extra': '', 'sid': '0', 'dir': '_i3/5' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=.../skipfish', 'extra': '', 'sid': '0', 'dir': '_i3/6' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i3/7' } ]
  },
  { 'severity': 3, 'type': 40201, 'samples': [
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal_investments.htm', 'extra': 'http://demo-analytics.testfire.net/urchin.js', 'sid': '0', 'dir': '_i4/0' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal_investments.htm', 'extra': 'http://demo-analytics.testfire.net/urchin.js', 'sid': '0', 'dir': '_i4/1' } ]
  },
  { 'severity': 3, 'type': 40101, 'samples': [
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': 'injected \x27\x3csfi...\x3e\x27 tag seen in HTML', 'sid': '0', 'dir': '_i5/0' },
    { 'url': 'http://demo.testfire.net/notfound.aspx?aspxerrorpath=/Privacypolicy.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000162v391429\x3e', 'extra': 'injected \x27\x3csfi...\x3e\x27 tag seen in HTML', 'sid': '0', 'dir': '_i5/1' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000031v391429\x3e', 'extra': 'injected \x27\x3csfi...\x3e\x27 tag seen in HTML', 'sid': '0', 'dir': '_i5/2' } ]
  },
  { 'severity': 2, 'type': 30601, 'samples': [
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/0' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/1' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/2' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/3' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/4' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/5' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/6' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/7' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/8' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/9' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/10' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/11' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/12' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/13' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/14' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/15' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/16' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/17' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/18' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/19' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/20' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/21' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/22' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/23' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/24' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/25' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/26' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/27' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/28' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/29' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/30' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/31' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/32' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/33' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/34' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/35' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/36' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/37' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i6/38' } ]
  },
  { 'severity': 2, 'type': 30501, 'samples': [
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_contact.htm', 'extra': 'http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0', 'sid': '0', 'dir': '_i7/0' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_benefits.htm', 'extra': 'http://www.exampledomainnotinuse.org/mybeacon.gif', 'sid': '0', 'dir': '_i7/1' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal.htm', 'extra': 'http://www.testfire.net/testfireappl/storefront/testfire_files/help_graphic.gif', 'sid': '0', 'dir': '_i7/2' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_benefits.htm', 'extra': 'http://www.exampledomainnotinuse.org/mybeacon.gif', 'sid': '0', 'dir': '_i7/3' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal.htm', 'extra': 'http://www.testfire.net/testfireappl/storefront/testfire_files/help_graphic.gif', 'sid': '0', 'dir': '_i7/4' },
    { 'url': 'http://demo.testfire.net/feedback.aspx', 'extra': 'http://www.altoromutual.com/bug.aspx', 'sid': '0', 'dir': '_i7/5' } ]
  },
  { 'severity': 1, 'type': 20205, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'Responses too slow for time sensitive tests', 'sid': '0', 'dir': '_i8/0' } ]
  },
  { 'severity': 1, 'type': 20101, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'during parameter brute-force tests', 'sid': '0', 'dir': '_i9/0' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'during parameter brute-force tests', 'sid': '0', 'dir': '_i9/1' } ]
  },
  { 'severity': 0, 'type': 10909, 'samples': [
    { 'url': 'http://demo.testfire.net/admin/clients.xls', 'extra': 'Microsoft Excel spreadsheet (mime)', 'sid': '41001', 'dir': '_i10/0' } ]
  },
  { 'severity': 0, 'type': 10901, 'samples': [
    { 'url': 'http://demo.testfire.net/%2Fnotfound.aspx%3Faspxerrorpath%3D%2Fsfi9876.aspx/', 'extra': '', 'sid': '0', 'dir': '_i11/0' },
    { 'url': 'http://demo.testfire.net/bank/20060308_bak/', 'extra': '', 'sid': '0', 'dir': '_i11/1' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/DownloadAppScanDemo_172x80.jpg/', 'extra': '', 'sid': '0', 'dir': '_i11/2' },
    { 'url': 'http://demo.testfire.net/pr/Q3_earnings.rtf', 'extra': '', 'sid': '0', 'dir': '_i11/3' } ]
  },
  { 'severity': 0, 'type': 10804, 'samples': [
    { 'url': 'http://demo.testfire.net/', 'extra': '', 'sid': '0', 'dir': '_i12/0' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/1' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/2' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/3' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/4' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/5' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/6' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/', 'extra': '', 'sid': '0', 'dir': '_i12/7' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/login.aspx/', 'extra': '', 'sid': '0', 'dir': '_i12/8' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/', 'extra': '', 'sid': '0', 'dir': '_i12/9' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/login.aspx/', 'extra': '', 'sid': '0', 'dir': '_i12/10' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/11' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/12' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/13' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/14' },
    { 'url': 'http://demo.testfire.net/bank/servererror.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/15' },
    { 'url': 'http://demo.testfire.net/comment.aspx/', 'extra': '', 'sid': '0', 'dir': '_i12/16' },
    { 'url': 'http://demo.testfire.net/comment.aspx/bank/', 'extra': '', 'sid': '0', 'dir': '_i12/17' },
    { 'url': 'http://demo.testfire.net/comment.aspx/default.aspx/', 'extra': '', 'sid': '0', 'dir': '_i12/18' },
    { 'url': 'http://demo.testfire.net/comment.aspx/default.aspx?content=9876sfi', 'extra': '', 'sid': '0', 'dir': '_i12/19' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/', 'extra': '', 'sid': '0', 'dir': '_i12/20' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/DownloadAppScanDemo_172x80.jpg/', 'extra': '', 'sid': '0', 'dir': '_i12/21' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/22' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/23' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/24' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/25' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/26' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/27' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/28' },
    { 'url': 'http://demo.testfire.net/notfound.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/29' },
    { 'url': 'http://demo.testfire.net/notfound.aspx?aspxerrorpath=9876sfi', 'extra': '', 'sid': '0', 'dir': '_i12/30' },
    { 'url': 'http://demo.testfire.net/default.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/31' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_contact.htm', 'extra': '', 'sid': '0', 'dir': '_i12/32' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=business.htm', 'extra': '', 'sid': '0', 'dir': '_i12/33' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=business_deposit.htm', 'extra': '', 'sid': '0', 'dir': '_i12/34' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=Default.htm', 'extra': '', 'sid': '0', 'dir': '_i12/35' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside.htm', 'extra': '', 'sid': '0', 'dir': '_i12/36' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_benefits.htm', 'extra': '', 'sid': '0', 'dir': '_i12/37' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_community.htm', 'extra': '', 'sid': '0', 'dir': '_i12/38' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_executives.htm', 'extra': '', 'sid': '0', 'dir': '_i12/39' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_jobs.htm', 'extra': '', 'sid': '0', 'dir': '_i12/40' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_trainee.htm', 'extra': '', 'sid': '0', 'dir': '_i12/41' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal.htm', 'extra': '', 'sid': '0', 'dir': '_i12/42' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal_investments.htm', 'extra': '', 'sid': '0', 'dir': '_i12/43' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=privacy.htm', 'extra': '', 'sid': '0', 'dir': '_i12/44' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=security.htm', 'extra': '', 'sid': '0', 'dir': '_i12/45' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_jobs.htm&job=ExecutiveAssistant:Administration', 'extra': '', 'sid': '0', 'dir': '_i12/46' },
    { 'url': 'http://demo.testfire.net/feedback.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/47' },
    { 'url': 'http://demo.testfire.net/search.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/48' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=9876sfi', 'extra': '', 'sid': '0', 'dir': '_i12/49' },
    { 'url': 'http://demo.testfire.net/servererror.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/50' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/51' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/52' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/53' },
    { 'url': 'http://demo.testfire.net/survey_questions.aspx', 'extra': '', 'sid': '0', 'dir': '_i12/54' },
    { 'url': 'http://demo.testfire.net/survey_questions.aspx?step=9876sfi', 'extra': '', 'sid': '0', 'dir': '_i12/55' } ]
  },
  { 'severity': 0, 'type': 10803, 'samples': [
    { 'url': 'http://demo.testfire.net/', 'extra': '', 'sid': '0', 'dir': '_i13/0' },
    { 'url': 'http://demo.testfire.net/%0A/', 'extra': '', 'sid': '0', 'dir': '_i13/1' },
    { 'url': 'http://demo.testfire.net/%2Fnotfound.aspx%3Faspxerrorpath%3D%2FPrivacypolicy.aspx/', 'extra': '', 'sid': '0', 'dir': '_i13/2' },
    { 'url': 'http://demo.testfire.net/%2Fnotfound.aspx%3Faspxerrorpath%3D%2Fsfi9876.aspx/', 'extra': '', 'sid': '0', 'dir': '_i13/3' },
    { 'url': 'http://demo.testfire.net/admin/', 'extra': '', 'sid': '0', 'dir': '_i13/4' },
    { 'url': 'http://demo.testfire.net/admin/CustomerServiceRepresentative:CustomerService.asmx/', 'extra': '', 'sid': '0', 'dir': '_i13/5' },
    { 'url': 'http://demo.testfire.net/admin/clients.xls', 'extra': '', 'sid': '0', 'dir': '_i13/6' },
    { 'url': 'http://demo.testfire.net/admin/captcha.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/7' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/8' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/9' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/10' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/11' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/12' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/13' },
    { 'url': 'http://demo.testfire.net/bank/', 'extra': '', 'sid': '0', 'dir': '_i13/14' },
    { 'url': 'http://demo.testfire.net/bank/20060308_bak/', 'extra': '', 'sid': '0', 'dir': '_i13/15' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000979v391429\x3e', 'extra': '', 'sid': '0', 'dir': '_i13/16' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/login.aspx/', 'extra': '', 'sid': '0', 'dir': '_i13/17' },
    { 'url': 'http://demo.testfire.net/bank/images/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000618v391429\x3e', 'extra': '', 'sid': '0', 'dir': '_i13/18' },
    { 'url': 'http://demo.testfire.net/bank/members/', 'extra': '', 'sid': '0', 'dir': '_i13/19' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/', 'extra': '', 'sid': '0', 'dir': '_i13/20' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/login.aspx/', 'extra': '', 'sid': '0', 'dir': '_i13/21' },
    { 'url': 'http://demo.testfire.net/bank/mozxpath.js', 'extra': '', 'sid': '0', 'dir': '_i13/22' },
    { 'url': 'http://demo.testfire.net/bank/ws.asmx', 'extra': '', 'sid': '0', 'dir': '_i13/23' },
    { 'url': 'http://demo.testfire.net/bank/ws.asmx?disco', 'extra': '', 'sid': '0', 'dir': '_i13/24' },
    { 'url': 'http://demo.testfire.net/bank/ws.asmx?op=GetUserAccounts', 'extra': '', 'sid': '0', 'dir': '_i13/25' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/26' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/27' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/28' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/29' },
    { 'url': 'http://demo.testfire.net/bank/servererror.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/30' },
    { 'url': 'http://demo.testfire.net/bank/default.aspx?content=inside_contact.htm', 'extra': '', 'sid': '0', 'dir': '_i13/31' },
    { 'url': 'http://demo.testfire.net/comment.aspx/', 'extra': '', 'sid': '0', 'dir': '_i13/32' },
    { 'url': 'http://demo.testfire.net/comment.aspx/bank/', 'extra': '', 'sid': '0', 'dir': '_i13/33' },
    { 'url': 'http://demo.testfire.net/comment.aspx/default.aspx/', 'extra': '', 'sid': '0', 'dir': '_i13/34' },
    { 'url': 'http://demo.testfire.net/comment.aspx/default.aspx?content=inside_contact.htm', 'extra': '', 'sid': '0', 'dir': '_i13/35' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/', 'extra': '', 'sid': '0', 'dir': '_i13/36' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/DownloadAppScanDemo_172x80.jpg/', 'extra': '', 'sid': '0', 'dir': '_i13/37' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/38' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/39' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/40' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/41' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/42' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/43' },
    { 'url': 'http://demo.testfire.net/images/', 'extra': '', 'sid': '0', 'dir': '_i13/44' },
    { 'url': 'http://demo.testfire.net/images/adobe.gif', 'extra': '', 'sid': '0', 'dir': '_i13/45' },
    { 'url': 'http://demo.testfire.net/images/altoro.gif', 'extra': '', 'sid': '0', 'dir': '_i13/46' },
    { 'url': 'http://demo.testfire.net/images/b_cards.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/47' },
    { 'url': 'http://demo.testfire.net/images/b_deposit.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/48' },
    { 'url': 'http://demo.testfire.net/images/b_insurance.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/49' },
    { 'url': 'http://demo.testfire.net/images/b_lending.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/50' },
    { 'url': 'http://demo.testfire.net/images/b_other.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/51' },
    { 'url': 'http://demo.testfire.net/images/b_retirement.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/52' },
    { 'url': 'http://demo.testfire.net/images/cancel.gif', 'extra': '', 'sid': '0', 'dir': '_i13/53' },
    { 'url': 'http://demo.testfire.net/images/DownloadAppScanDemo_172x80.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/54' },
    { 'url': 'http://demo.testfire.net/images/header_pic.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/55' },
    { 'url': 'http://demo.testfire.net/images/home1.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/56' },
    { 'url': 'http://demo.testfire.net/images/home2.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/57' },
    { 'url': 'http://demo.testfire.net/images/home3.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/58' },
    { 'url': 'http://demo.testfire.net/images/inside1.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/59' },
    { 'url': 'http://demo.testfire.net/images/inside4.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/60' },
    { 'url': 'http://demo.testfire.net/images/inside5.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/61' },
    { 'url': 'http://demo.testfire.net/images/inside6.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/62' },
    { 'url': 'http://demo.testfire.net/images/logo.gif/.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000577v391429\x3e', 'extra': '', 'sid': '0', 'dir': '_i13/63' },
    { 'url': 'http://demo.testfire.net/images/p_cards.jpg/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000402v391429\x3e', 'extra': '', 'sid': '0', 'dir': '_i13/64' },
    { 'url': 'http://demo.testfire.net/images/p_loans.jpg/.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000409v391429\x3e', 'extra': '', 'sid': '0', 'dir': '_i13/65' },
    { 'url': 'http://demo.testfire.net/images/p_main.jpg', 'extra': '', 'sid': '0', 'dir': '_i13/66' },
    { 'url': 'http://demo.testfire.net/images/pf_lock.gif', 'extra': '', 'sid': '0', 'dir': '_i13/67' },
    { 'url': 'http://demo.testfire.net/images/spacer.gif', 'extra': '', 'sid': '0', 'dir': '_i13/68' },
    { 'url': 'http://demo.testfire.net/jobs/', 'extra': '', 'sid': '0', 'dir': '_i13/69' },
    { 'url': 'http://demo.testfire.net/pr/.htaccess.aspx--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000349v391429\x3e', 'extra': '', 'sid': '0', 'dir': '_i13/70' },
    { 'url': 'http://demo.testfire.net/pr/communityannualreport.pdf', 'extra': '', 'sid': '0', 'dir': '_i13/71' },
    { 'url': 'http://demo.testfire.net/pr/Docs.xml', 'extra': '', 'sid': '0', 'dir': '_i13/72' },
    { 'url': 'http://demo.testfire.net/pr/Draft.rtf', 'extra': '', 'sid': '0', 'dir': '_i13/73' },
    { 'url': 'http://demo.testfire.net/pr/Q3_earnings.rtf', 'extra': '', 'sid': '0', 'dir': '_i13/74' },
    { 'url': 'http://demo.testfire.net/transfer/', 'extra': '', 'sid': '0', 'dir': '_i13/75' },
    { 'url': 'http://demo.testfire.net/transfer/transfer.asmx?disco', 'extra': '', 'sid': '0', 'dir': '_i13/76' },
    { 'url': 'http://demo.testfire.net/transfer/transfer.asmx?op=GetUserAccounts', 'extra': '', 'sid': '0', 'dir': '_i13/77' },
    { 'url': 'http://demo.testfire.net/disclaimer.htm', 'extra': '', 'sid': '0', 'dir': '_i13/78' },
    { 'url': 'http://demo.testfire.net/disclaimer.htm?url=http://www.netscape.com', 'extra': '', 'sid': '0', 'dir': '_i13/79' },
    { 'url': 'http://demo.testfire.net/high_yield_investments.htm', 'extra': '', 'sid': '0', 'dir': '_i13/80' },
    { 'url': 'http://demo.testfire.net/notfound.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/81' },
    { 'url': 'http://demo.testfire.net/notfound.aspx?aspxerrorpath=/Privacypolicy.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/82' },
    { 'url': 'http://demo.testfire.net/Privacypolicy.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/83' },
    { 'url': 'http://demo.testfire.net/Privacypolicy.aspx?sec=Careers&template=US', 'extra': '', 'sid': '0', 'dir': '_i13/84' },
    { 'url': 'http://demo.testfire.net/Privacypolicy.aspx?sec=Careers&template=US', 'extra': '', 'sid': '0', 'dir': '_i13/85' },
    { 'url': 'http://demo.testfire.net/retirement.htm', 'extra': '', 'sid': '0', 'dir': '_i13/86' },
    { 'url': 'http://demo.testfire.net/style.css', 'extra': '', 'sid': '0', 'dir': '_i13/87' },
    { 'url': 'http://demo.testfire.net/subscribe.swf', 'extra': '', 'sid': '0', 'dir': '_i13/88' },
    { 'url': 'http://demo.testfire.net/default.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/89' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_contact.htm', 'extra': '', 'sid': '0', 'dir': '_i13/90' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_jobs.htm&job=ExecutiveAssistant:Administration', 'extra': '', 'sid': '0', 'dir': '_i13/91' },
    { 'url': 'http://demo.testfire.net/feedback.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/92' },
    { 'url': 'http://demo.testfire.net/search.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/93' },
    { 'url': 'http://demo.testfire.net/search.aspx?txtSearch=skipfish', 'extra': '', 'sid': '0', 'dir': '_i13/94' },
    { 'url': 'http://demo.testfire.net/servererror.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/95' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/96' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/97' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/98' },
    { 'url': 'http://demo.testfire.net/survey_questions.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/99' },
    { 'url': 'http://demo.testfire.net/survey_questions.aspx?step=a', 'extra': '', 'sid': '0', 'dir': '_i13/100' },
    { 'url': 'http://demo.testfire.net/test.aspx', 'extra': '', 'sid': '0', 'dir': '_i13/101' } ]
  },
  { 'severity': 0, 'type': 10801, 'samples': [
    { 'url': 'http://demo.testfire.net/images/cancel.gif', 'extra': 'image/x-ms-bmp', 'sid': '0', 'dir': '_i14/0' },
    { 'url': 'http://demo.testfire.net/pr/Draft.rtf', 'extra': 'application/javascript', 'sid': '0', 'dir': '_i14/1' },
    { 'url': 'http://demo.testfire.net/pr/Q3_earnings.rtf', 'extra': 'application/javascript', 'sid': '0', 'dir': '_i14/2' } ]
  },
  { 'severity': 0, 'type': 10602, 'samples': [
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': '', 'sid': '0', 'dir': '_i15/0' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i15/1' } ]
  },
  { 'severity': 0, 'type': 10505, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'uid', 'sid': '0', 'dir': '_i16/0' } ]
  },
  { 'severity': 0, 'type': 10405, 'samples': [
    { 'url': 'http://demo.testfire.net/%0A/', 'extra': '', 'sid': '0', 'dir': '_i17/0' },
    { 'url': 'http://demo.testfire.net/admin/CustomerServiceRepresentative:CustomerService.asmx/', 'extra': '', 'sid': '0', 'dir': '_i17/1' },
    { 'url': 'http://demo.testfire.net/bank/ws.asmx?WSDL', 'extra': '', 'sid': '0', 'dir': '_i17/2' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i17/3' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i17/4' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=business.htm', 'extra': '', 'sid': '0', 'dir': '_i17/5' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=business_deposit.htm', 'extra': '', 'sid': '0', 'dir': '_i17/6' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=Default.htm', 'extra': '', 'sid': '0', 'dir': '_i17/7' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside.htm', 'extra': '', 'sid': '0', 'dir': '_i17/8' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_benefits.htm', 'extra': '', 'sid': '0', 'dir': '_i17/9' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_community.htm', 'extra': '', 'sid': '0', 'dir': '_i17/10' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_executives.htm', 'extra': '', 'sid': '0', 'dir': '_i17/11' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_jobs.htm', 'extra': '', 'sid': '0', 'dir': '_i17/12' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=inside_trainee.htm', 'extra': '', 'sid': '0', 'dir': '_i17/13' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal.htm', 'extra': '', 'sid': '0', 'dir': '_i17/14' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=personal_investments.htm', 'extra': '', 'sid': '0', 'dir': '_i17/15' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=privacy.htm', 'extra': '', 'sid': '0', 'dir': '_i17/16' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=security.htm', 'extra': '', 'sid': '0', 'dir': '_i17/17' },
    { 'url': 'http://demo.testfire.net/servererror.aspx', 'extra': '', 'sid': '0', 'dir': '_i17/18' },
    { 'url': 'http://demo.testfire.net/test.aspx', 'extra': '', 'sid': '0', 'dir': '_i17/19' } ]
  },
  { 'severity': 0, 'type': 10404, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/', 'extra': 'Directory listing', 'sid': '0', 'dir': '_i18/0' },
    { 'url': 'http://demo.testfire.net/pr/', 'extra': 'Directory listing', 'sid': '0', 'dir': '_i18/1' } ]
  },
  { 'severity': 0, 'type': 10403, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/', 'extra': '', 'sid': '0', 'dir': '_i19/0' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/login.aspx/', 'extra': '', 'sid': '0', 'dir': '_i19/1' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/', 'extra': '', 'sid': '0', 'dir': '_i19/2' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/login.aspx/', 'extra': '', 'sid': '0', 'dir': '_i19/3' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i19/4' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': '', 'sid': '0', 'dir': '_i19/5' },
    { 'url': 'http://demo.testfire.net/comment.aspx/', 'extra': '', 'sid': '0', 'dir': '_i19/6' },
    { 'url': 'http://demo.testfire.net/comment.aspx/bank/', 'extra': '', 'sid': '0', 'dir': '_i19/7' },
    { 'url': 'http://demo.testfire.net/comment.aspx/default.aspx/', 'extra': '', 'sid': '0', 'dir': '_i19/8' },
    { 'url': 'http://demo.testfire.net/comment.aspx/default.aspx?content=9876sfi', 'extra': '', 'sid': '0', 'dir': '_i19/9' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/', 'extra': '', 'sid': '0', 'dir': '_i19/10' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/DownloadAppScanDemo_172x80.jpg/', 'extra': '', 'sid': '0', 'dir': '_i19/11' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i19/12' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i19/13' },
    { 'url': 'http://demo.testfire.net/comment.aspx', 'extra': '', 'sid': '0', 'dir': '_i19/14' },
    { 'url': 'http://demo.testfire.net/default.aspx?content=.../inside_contact.htm', 'extra': '', 'sid': '0', 'dir': '_i19/15' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i19/16' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i19/17' },
    { 'url': 'http://demo.testfire.net/survey_questions.aspx?step=a', 'extra': '', 'sid': '0', 'dir': '_i19/18' } ]
  },
  { 'severity': 0, 'type': 10402, 'samples': [
    { 'url': 'http://demo.testfire.net/bank/members/', 'extra': '', 'sid': '0', 'dir': '_i20/0' } ]
  },
  { 'severity': 0, 'type': 10401, 'samples': [
    { 'url': 'http://demo.testfire.net/%0A/', 'extra': '', 'sid': '0', 'dir': '_i21/0' },
    { 'url': 'http://demo.testfire.net/%2Fnotfound.aspx%3Faspxerrorpath%3D%2FPrivacypolicy.aspx/', 'extra': '', 'sid': '0', 'dir': '_i21/1' },
    { 'url': 'http://demo.testfire.net/%2Fnotfound.aspx%3Faspxerrorpath%3D%2Fsfi9876.aspx/', 'extra': '', 'sid': '0', 'dir': '_i21/2' },
    { 'url': 'http://demo.testfire.net/admin/CustomerServiceRepresentative:CustomerService.asmx/', 'extra': '', 'sid': '0', 'dir': '_i21/3' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/', 'extra': '', 'sid': '0', 'dir': '_i21/4' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/login.aspx/', 'extra': '', 'sid': '0', 'dir': '_i21/5' },
    { 'url': 'http://demo.testfire.net/bank/members/', 'extra': '', 'sid': '0', 'dir': '_i21/6' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/', 'extra': '', 'sid': '0', 'dir': '_i21/7' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/login.aspx/', 'extra': '', 'sid': '0', 'dir': '_i21/8' },
    { 'url': 'http://demo.testfire.net/comment.aspx/', 'extra': '', 'sid': '0', 'dir': '_i21/9' },
    { 'url': 'http://demo.testfire.net/comment.aspx/bank/', 'extra': '', 'sid': '0', 'dir': '_i21/10' },
    { 'url': 'http://demo.testfire.net/comment.aspx/default.aspx/', 'extra': '', 'sid': '0', 'dir': '_i21/11' },
    { 'url': 'http://demo.testfire.net/comment.aspx/default.aspx?content=inside_contact.htm', 'extra': '', 'sid': '0', 'dir': '_i21/12' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/', 'extra': '', 'sid': '0', 'dir': '_i21/13' },
    { 'url': 'http://demo.testfire.net/comment.aspx/images/DownloadAppScanDemo_172x80.jpg/', 'extra': '', 'sid': '0', 'dir': '_i21/14' },
    { 'url': 'http://demo.testfire.net/notfound.aspx', 'extra': '', 'sid': '0', 'dir': '_i21/15' },
    { 'url': 'http://demo.testfire.net/notfound.aspx?aspxerrorpath=/Privacypolicy.aspx', 'extra': '', 'sid': '0', 'dir': '_i21/16' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i21/17' },
    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': '', 'sid': '0', 'dir': '_i21/18' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://demo.testfire.net/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i22/0' },
    { 'url': 'http://demo.testfire.net/sfi9876.aspx', 'extra': '', 'sid': '0', 'dir': '_i22/1' },
    { 'url': 'http://demo.testfire.net/bank/20060308_bak/sfi9876.asmx', 'extra': '', 'sid': '0', 'dir': '_i22/2' },
    { 'url': 'http://demo.testfire.net/images/sfi9876.asmx', 'extra': '', 'sid': '0', 'dir': '_i22/3' },
    { 'url': 'http://demo.testfire.net/pr/sfi9876.asmx', 'extra': '', 'sid': '0', 'dir': '_i22/4' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'http://demo.testfire.net/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i23/0' },
    { 'url': 'http://demo.testfire.net/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/1' },
    { 'url': 'http://demo.testfire.net/%0A/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i23/2' },
    { 'url': 'http://demo.testfire.net/%0A/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/3' },
    { 'url': 'http://demo.testfire.net/%2Fnotfound.aspx%3Faspxerrorpath%3D%2FPrivacypolicy.aspx/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/4' },
    { 'url': 'http://demo.testfire.net/%2Fnotfound.aspx%3Faspxerrorpath%3D%2Fsfi9876.aspx/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/5' },
    { 'url': 'http://demo.testfire.net/admin/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/6' },
    { 'url': 'http://demo.testfire.net/admin/captcha.aspx', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/7' },
    { 'url': 'http://demo.testfire.net/admin/Login.aspx', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/8' },
    { 'url': 'http://demo.testfire.net/bank/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/9' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/10' },
    { 'url': 'http://demo.testfire.net/bank/queryxpath.aspx/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/11' },
    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/12' },
    { 'url': 'http://demo.testfire.net/bank/servererror.aspx', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/13' },
    { 'url': 'http://demo.testfire.net/images/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/14' },
    { 'url': 'http://demo.testfire.net/pr/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/15' },
    { 'url': 'http://demo.testfire.net/transfer/', 'extra': 'X-AspNet-Version', 'sid': '0', 'dir': '_i23/16' } ]
  },
  { 'severity': 0, 'type': 10202, 'samples': [
    { 'url': 'http://demo.testfire.net/', 'extra': 'Microsoft-IIS/6.0', 'sid': '0', 'dir': '_i24/0' },
    { 'url': 'http://demo.testfire.net/%0A/', 'extra': '[none]', 'sid': '0', 'dir': '_i24/1' } ]
  },
  { 'severity': 0, 'type': 10201, 'samples': [
    { 'url': 'http://demo.testfire.net/', 'extra': 'ASP.NET_SessionId', 'sid': '0', 'dir': '_i25/0' },
    { 'url': 'http://demo.testfire.net/', 'extra': 'amSessionId', 'sid': '0', 'dir': '_i25/1' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx', 'extra': 'lang', 'sid': '0', 'dir': '_i25/2' },
    { 'url': 'http://demo.testfire.net/bank/customize.aspx/login.aspx', 'extra': 'lang', 'sid': '0', 'dir': '_i25/3' },
    { 'url': 'http://demo.testfire.net/bank/account.aspx', 'extra': 'amUserId', 'sid': '0', 'dir': '_i25/4' },
    { 'url': 'http://demo.testfire.net/bank/account.aspx', 'extra': 'amCreditOffer', 'sid': '0', 'dir': '_i25/5' } ]
  }
];

"""


report_high_summary = r"""var sf_version = '2.10b';
var scan_date  = 'Mon May 19 20:32:47 2014';
var scan_seed  = '0x4491d352';
var scan_ms    = 2494666;
"""


report_medium_samples = r"""var mime_samples = [
  { 'mime': 'text/html', 'samples': [
    { 'url': 'http://127.0.0.1:9000/', 'dir': '_m0/0', 'linked': 2, 'len': 236 },
    { 'url': 'http://127.0.0.1:9000/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000000v993478\x3e', 'dir': '_m0/1', 'linked': 2, 'len': 239 },
    { 'url': 'http://127.0.0.1:9000/cake', 'dir': '_m0/2', 'linked': 2, 'len': 497 },
    { 'url': 'http://127.0.0.1:9000/choucroute', 'dir': '_m0/3', 'linked': 2, 'len': 1112 } ]
  }
];

var issue_samples = [
  { 'severity': 3, 'type': 40304, 'samples': [
    { 'url': 'http://127.0.0.1:9000/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000000v993478\x3e', 'extra': '', 'sid': '0', 'dir': '_i0/0' },
    { 'url': 'http://127.0.0.1:9000/cake/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000004v993478\x3e', 'extra': '', 'sid': '0', 'dir': '_i0/1' },
    { 'url': 'http://127.0.0.1:9000/choucroute/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000008v993478\x3e', 'extra': '', 'sid': '0', 'dir': '_i0/2' } ]
  },
  { 'severity': 3, 'type': 40101, 'samples': [
    { 'url': 'http://127.0.0.1:9000/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000000v993478\x3e', 'extra': 'injected \x27\x3csfi...\x3e\x27 tag seen in HTML', 'sid': '0', 'dir': '_i1/0' },
    { 'url': 'http://127.0.0.1:9000/cake/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000004v993478\x3e', 'extra': 'injected \x27\x3csfi...\x3e\x27 tag seen in HTML', 'sid': '0', 'dir': '_i1/1' },
    { 'url': 'http://127.0.0.1:9000/choucroute/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000008v993478\x3e', 'extra': 'injected \x27\x3csfi...\x3e\x27 tag seen in HTML', 'sid': '0', 'dir': '_i1/2' } ]
  },
  { 'severity': 0, 'type': 10803, 'samples': [
    { 'url': 'http://127.0.0.1:9000/', 'extra': '', 'sid': '0', 'dir': '_i2/0' },
    { 'url': 'http://127.0.0.1:9000/cake', 'extra': '', 'sid': '0', 'dir': '_i2/1' },
    { 'url': 'http://127.0.0.1:9000/choucroute', 'extra': '', 'sid': '0', 'dir': '_i2/2' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://127.0.0.1:9000/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i3/0' },
    { 'url': 'http://127.0.0.1:9000/sfi9876.zip', 'extra': '', 'sid': '0', 'dir': '_i3/1' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'http://127.0.0.1:9000/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i4/0' } ]
  }
];

"""


report_medium_summary = r"""var sf_version = '2.10b';
var scan_date  = 'Tue May 27 11:31:14 2014';
var scan_seed  = '0x5b37a9a3';
var scan_ms    = 44836;
"""
