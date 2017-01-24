# -*- coding: utf-8 -*-
report_high = """<?xml version="1.0"?>
<report type="security">
    <report_infos>
        <info name="generatorName">wapiti</info>
        <info name="generatorVersion">Wapiti 2.3.0</info>
        <info name="scope">folder</info>
        <info name="dateOfScan">Tue, 24 Jan 2017 05:29:07 +0000</info>
    </report_infos>
    <vulnerabilities>
        <vulnerability name="Cross Site Scripting">
            <description>
<![CDATA[Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications which allow code injection by malicious web users into the web pages viewed by other users. Examples of such code include HTML code and client-side scripts.]]>            </description>
            <solution>
<![CDATA[The best way to protect a web application from XSS attacks is ensure that the application performs validation of all headers, cookies, query strings, form fields, and hidden fields. Encoding user supplied output in the server side can also defeat XSS vulnerabilities by preventing inserted scripts from being transmitted to users in an executable form. Applications can gain significant protection from javascript based attacks by converting the following characters in all generated output to the appropriate HTML entity encoding:  &lt;, &gt;, &amp;, &quot;, ', (, ), #, %, ; , +, -.]]>            </solution>
            <references>
                <reference>
                    <title>CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')</title>
                    <url>http://cwe.mitre.org/data/definitions/79.html</url>
                </reference>
                <reference>
                    <title>http://en.wikipedia.org/wiki/Cross-site_scripting</title>
                    <url>http://en.wikipedia.org/wiki/Cross-site_scripting</url>
                </reference>
                <reference>
                    <title>VulneraNET wiki: Cross Site Scripting Flaw article</title>
                    <url>http://lab.gsi.dit.upm.es/semanticwiki/index.php/Cross_Site_Scripting_Flaw</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Cross_Site_Scripting</title>
                    <url>http://www.owasp.org/index.php/Cross_Site_Scripting</url>
                </reference>
            </references>
            <entries>
                <entry>
                    <method>GET</method>
                    <path>/listproducts.php</path>
                    <level>1</level>
                    <parameter>cat</parameter>
                    <info>XSS vulnerability found via injection in the parameter cat</info>
                    <http_request>
<![CDATA[GET /listproducts.php?cat=%3Cscript%3Ealert%28%27wdmxyf0wgy%27%29%3C%2Fscript%3E HTTP/1.1
Host: testphp.vulnweb.com
]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/listproducts.php?cat=%3Cscript%3Ealert%28%27wdmxyf0wgy%27%29%3C%2Fscript%3E"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>GET</method>
                    <path>/hpp/</path>
                    <level>1</level>
                    <parameter>pp</parameter>
                    <info>XSS vulnerability found via injection in the parameter pp</info>
                    <http_request>
<![CDATA[GET /hpp/?pp=%22%3E%3C%2Fa%3E%3Cscript%3Ealert%28%27w0ascsajs9%27%29%3C%2Fscript%3E HTTP/1.1
Host: testphp.vulnweb.com
]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/hpp/?pp=%22%3E%3C%2Fa%3E%3Cscript%3Ealert%28%27w0ascsajs9%27%29%3C%2Fscript%3E"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>GET</method>
                    <path>/listproducts.php</path>
                    <level>1</level>
                    <parameter>artist</parameter>
                    <info>XSS vulnerability found via injection in the parameter artist</info>
                    <http_request>
<![CDATA[GET /listproducts.php?artist=%3Cscript%3Ealert%28%27wzwh1hy34d%27%29%3C%2Fscript%3E HTTP/1.1
Host: testphp.vulnweb.com
]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/listproducts.php?artist=%3Cscript%3Ealert%28%27wzwh1hy34d%27%29%3C%2Fscript%3E"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>GET</method>
                    <path>/hpp/params.php</path>
                    <level>1</level>
                    <parameter>p</parameter>
                    <info>XSS vulnerability found via injection in the parameter p</info>
                    <http_request>
<![CDATA[GET /hpp/params.php?p=%3Cscript%3Ealert%28%27wky5rp0g7i%27%29%3C%2Fscript%3E&pp=12 HTTP/1.1
Host: testphp.vulnweb.com
]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/hpp/params.php?p=%3Cscript%3Ealert%28%27wky5rp0g7i%27%29%3C%2Fscript%3E&pp=12"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>GET</method>
                    <path>/hpp/params.php</path>
                    <level>1</level>
                    <parameter>pp</parameter>
                    <info>XSS vulnerability found via injection in the parameter pp</info>
                    <http_request>
<![CDATA[GET /hpp/params.php?p=valid&pp=%3Cscript%3Ealert%28%27wchs3retc4%27%29%3C%2Fscript%3E HTTP/1.1
Host: testphp.vulnweb.com
]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=%3Cscript%3Ealert%28%27wchs3retc4%27%29%3C%2Fscript%3E"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/search.php</path>
                    <level>1</level>
                    <parameter>searchFor</parameter>
                    <info>XSS vulnerability found via injection in the parameter searchFor</info>
                    <http_request>
<![CDATA[POST /search.php?test=query HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/
Content-Type: application/x-www-form-urlencoded

searchFor=%3Cscript%3Ealert%28%27wi1e1dnwq4%27%29%3C%2Fscript%3E&goButton=go]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/search.php?test=query" -e "http://testphp.vulnweb.com/" -d "searchFor=%3Cscript%3Ealert%28%27wi1e1dnwq4%27%29%3C%2Fscript%3E&goButton=go"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/guestbook.php</path>
                    <level>1</level>
                    <parameter>name</parameter>
                    <info>XSS vulnerability found via injection in the parameter name</info>
                    <http_request>
<![CDATA[POST /guestbook.php HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/guestbook.php
Content-Type: application/x-www-form-urlencoded

name=%3Cscript%3Ealert%28%27wma0n2rar3%27%29%3C%2Fscript%3E&text=on&submit=add%20message]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/guestbook.php" -e "http://testphp.vulnweb.com/guestbook.php" -d "name=%3Cscript%3Ealert%28%27wma0n2rar3%27%29%3C%2Fscript%3E&text=on&submit=add%20message"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/guestbook.php</path>
                    <level>1</level>
                    <parameter>text</parameter>
                    <info>XSS vulnerability found via injection in the parameter text</info>
                    <http_request>
<![CDATA[POST /guestbook.php HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/guestbook.php
Content-Type: application/x-www-form-urlencoded

name=anonymous%20user&text=%3Cscript%3Ealert%28%27wma3tchvh3%27%29%3C%2Fscript%3E&submit=add%20message]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/guestbook.php" -e "http://testphp.vulnweb.com/guestbook.php" -d "name=anonymous%20user&text=%3Cscript%3Ealert%28%27wma3tchvh3%27%29%3C%2Fscript%3E&submit=add%20message"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/secured/newuser.php</path>
                    <level>1</level>
                    <parameter>uuname</parameter>
                    <info>XSS vulnerability found via injection in the parameter uuname</info>
                    <http_request>
<![CDATA[POST /secured/newuser.php HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/signup.php
Content-Type: application/x-www-form-urlencoded

uuname=%3Cscript%3Ealert%28%22wanbvx5m1k%22%29%3C%2Fscript%3E&upass=letmein&upass2=letmein&urname=default&ucc=default&uemail=default&uphone=default&uaddress=on&signup=signup]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/secured/newuser.php" -e "http://testphp.vulnweb.com/signup.php" -d "uuname=%3Cscript%3Ealert%28%22wanbvx5m1k%22%29%3C%2Fscript%3E&upass=letmein&upass2=letmein&urname=default&ucc=default&uemail=default&uphone=default&uaddress=on&signup=signup"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/secured/newuser.php</path>
                    <level>1</level>
                    <parameter>urname</parameter>
                    <info>XSS vulnerability found via injection in the parameter urname</info>
                    <http_request>
<![CDATA[POST /secured/newuser.php HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/signup.php
Content-Type: application/x-www-form-urlencoded

uuname=default&upass=letmein&upass2=letmein&urname=%3Cscript%3Ealert%28%27wx0ispy38v%27%29%3C%2Fscript%3E&ucc=default&uemail=default&uphone=default&uaddress=on&signup=signup]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/secured/newuser.php" -e "http://testphp.vulnweb.com/signup.php" -d "uuname=default&upass=letmein&upass2=letmein&urname=%3Cscript%3Ealert%28%27wx0ispy38v%27%29%3C%2Fscript%3E&ucc=default&uemail=default&uphone=default&uaddress=on&signup=signup"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/secured/newuser.php</path>
                    <level>1</level>
                    <parameter>ucc</parameter>
                    <info>XSS vulnerability found via injection in the parameter ucc</info>
                    <http_request>
<![CDATA[POST /secured/newuser.php HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/signup.php
Content-Type: application/x-www-form-urlencoded

uuname=default&upass=letmein&upass2=letmein&urname=default&ucc=%3Cscript%3Ealert%28%27w7un4hc6zj%27%29%3C%2Fscript%3E&uemail=default&uphone=default&uaddress=on&signup=signup]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/secured/newuser.php" -e "http://testphp.vulnweb.com/signup.php" -d "uuname=default&upass=letmein&upass2=letmein&urname=default&ucc=%3Cscript%3Ealert%28%27w7un4hc6zj%27%29%3C%2Fscript%3E&uemail=default&uphone=default&uaddress=on&signup=signup"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/secured/newuser.php</path>
                    <level>1</level>
                    <parameter>uemail</parameter>
                    <info>XSS vulnerability found via injection in the parameter uemail</info>
                    <http_request>
<![CDATA[POST /secured/newuser.php HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/signup.php
Content-Type: application/x-www-form-urlencoded

uuname=default&upass=letmein&upass2=letmein&urname=default&ucc=default&uemail=%3Cscript%3Ealert%28%27wdt1faisd7%27%29%3C%2Fscript%3E&uphone=default&uaddress=on&signup=signup]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/secured/newuser.php" -e "http://testphp.vulnweb.com/signup.php" -d "uuname=default&upass=letmein&upass2=letmein&urname=default&ucc=default&uemail=%3Cscript%3Ealert%28%27wdt1faisd7%27%29%3C%2Fscript%3E&uphone=default&uaddress=on&signup=signup"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/secured/newuser.php</path>
                    <level>1</level>
                    <parameter>uphone</parameter>
                    <info>XSS vulnerability found via injection in the parameter uphone</info>
                    <http_request>
<![CDATA[POST /secured/newuser.php HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/signup.php
Content-Type: application/x-www-form-urlencoded

uuname=default&upass=letmein&upass2=letmein&urname=default&ucc=default&uemail=default&uphone=%3Cscript%3Ealert%28%27wyga5ilg7u%27%29%3C%2Fscript%3E&uaddress=on&signup=signup]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/secured/newuser.php" -e "http://testphp.vulnweb.com/signup.php" -d "uuname=default&upass=letmein&upass2=letmein&urname=default&ucc=default&uemail=default&uphone=%3Cscript%3Ealert%28%27wyga5ilg7u%27%29%3C%2Fscript%3E&uaddress=on&signup=signup"]]>                    </curl_command>
                </entry>
                <entry>
                    <method>POST</method>
                    <path>/secured/newuser.php</path>
                    <level>1</level>
                    <parameter>uaddress</parameter>
                    <info>XSS vulnerability found via injection in the parameter uaddress</info>
                    <http_request>
<![CDATA[POST /secured/newuser.php HTTP/1.1
Host: testphp.vulnweb.com
Referer: http://testphp.vulnweb.com/signup.php
Content-Type: application/x-www-form-urlencoded

uuname=default&upass=letmein&upass2=letmein&urname=default&ucc=default&uemail=default&uphone=default&uaddress=%3Cscript%3Ealert%28%27wamj9dqgvs%27%29%3C%2Fscript%3E&signup=signup]]>                    </http_request>
                    <curl_command>
<![CDATA[curl "http://testphp.vulnweb.com/secured/newuser.php" -e "http://testphp.vulnweb.com/signup.php" -d "uuname=default&upass=letmein&upass2=letmein&urname=default&ucc=default&uemail=default&uphone=default&uaddress=%3Cscript%3Ealert%28%27wamj9dqgvs%27%29%3C%2Fscript%3E&signup=signup"]]>                    </curl_command>
                </entry>
            </entries>
        </vulnerability>
        <vulnerability name="Htaccess Bypass">
            <description>
<![CDATA[htaccess files are used to restrict access to some files or HTTP method. In some case it may be possible to bypass this restriction and access the files.]]>            </description>
            <solution>
<![CDATA[Make sure every HTTP method is forbidden if the credentials are bad.]]>            </solution>
            <references>
                <reference>
                    <title>http://blog.teusink.net/2009/07/common-apache-htaccess-misconfiguration.html</title>
                    <url>http://blog.teusink.net/2009/07/common-apache-htaccess-misconfiguration.html</url>
                </reference>
                <reference>
                    <title>CWE-538: File and Directory Information Exposure</title>
                    <url>http://cwe.mitre.org/data/definitions/538.html</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Backup file">
            <description>
<![CDATA[It may be possible to find backup files of scripts on the webserver that the web-admin put here to save a previous version or backup files that are automaticallygenerated by the software editor used (like for example Emacs). These copies may reveal interesting informations like source code or credentials]]>            </description>
            <solution>
<![CDATA[The webadmin must manually delete the backup files or remove it from the web root. He should also reconfigure its editor to deactivate automatic backups.]]>            </solution>
            <references>
                <reference>
                    <title>Testing for Old, Backup and Unreferenced Files (OWASP-CM-006)</title>
                    <url>http://www.owasp.org/index.php/Testing_for_Old,_Backup_and_Unreferenced_Files_(OWASP-CM-006)</url>
                </reference>
                <reference>
                    <title>CWE-530: Exposure of Backup File to an Unauthorized Control Sphere</title>
                    <url>http://cwe.mitre.org/data/definitions/530.html</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="SQL Injection">
            <description>
<![CDATA[SQL injection vulnerabilities allow an attacker to alter the queries executed on the backend database. An attacker may then be able to extract or modify informations stored in the database or even escalate his privileges on the system.]]>            </description>
            <solution>
<![CDATA[To protect against SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.]]>            </solution>
            <references>
                <reference>
                    <title>http://www.owasp.org/index.php/SQL_Injection</title>
                    <url>http://www.owasp.org/index.php/SQL_Injection</url>
                </reference>
                <reference>
                    <title>http://en.wikipedia.org/wiki/SQL_injection</title>
                    <url>http://en.wikipedia.org/wiki/SQL_injection</url>
                </reference>
                <reference>
                    <title>CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')</title>
                    <url>http://cwe.mitre.org/data/definitions/89.html</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Blind SQL Injection">
            <description>
<![CDATA[Blind SQL injection is a technique that exploits a vulnerability occurring in the database of an application. This kind of vulnerability is harder to detect than basic SQL injections because no error message will be displayed on the webpage.]]>            </description>
            <solution>
<![CDATA[To protect against SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.]]>            </solution>
            <references>
                <reference>
                    <title>CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')</title>
                    <url>http://cwe.mitre.org/data/definitions/89.html</url>
                </reference>
                <reference>
                    <title>http://www.imperva.com/resources/adc/blind_sql_server_injection.html</title>
                    <url>http://www.imperva.com/resources/adc/blind_sql_server_injection.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Blind_SQL_Injection</title>
                    <url>http://www.owasp.org/index.php/Blind_SQL_Injection</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="File Handling">
            <description>
<![CDATA[This attack is also known as Path or Directory Traversal, its aim is the access to files and directories that are stored outside the web root folder. The attacker tries to explore the directories stored in the web server. The attacker uses some techniques, for instance, the manipulation of variables that reference files with 'dot-dot-slash (../)' sequences and its variations to move up to root directory to navigate through the file system.]]>            </description>
            <solution>
<![CDATA[Prefer working without user input when using file system calls. Use indexes rather than actual portions of file names when templating or using language files (eg: value 5 from the user submission = Czechoslovakian, rather than expecting the user to return 'Czechoslovakian'). Ensure the user cannot supply all parts of the path - surround it with your path code. Validate the user's input by only accepting known good - do not sanitize the data. Use chrooted jails and code access policies to restrict where the files can be obtained or saved to.]]>            </solution>
            <references>
                <reference>
                    <title>http://www.owasp.org/index.php/Path_Traversal</title>
                    <url>http://www.owasp.org/index.php/Path_Traversal</url>
                </reference>
                <reference>
                    <title>http://www.acunetix.com/websitesecurity/directory-traversal.htm</title>
                    <url>http://www.acunetix.com/websitesecurity/directory-traversal.htm</url>
                </reference>
                <reference>
                    <title>CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')</title>
                    <url>http://cwe.mitre.org/data/definitions/22.html</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Potentially dangerous file">
            <description>
<![CDATA[A file with potential vulnerabilities has been found on the website.]]>            </description>
            <solution>
<![CDATA[Make sure the script is up-to-date and restrict access to it if possible]]>            </solution>
            <references>
                <reference>
                    <title>The Open Source Vulnerability Database</title>
                    <url>http://osvdb.org/</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="CRLF Injection">
            <description>
<![CDATA[The term CRLF refers to Carriage Return (ASCII 13, \r) Line Feed (ASCII 10, \n). They're used to note the termination of a line, however, dealt with differently in today's popular Operating Systems. For example: in Windows both a CR and LF are required to note the end of a line, whereas in Linux/UNIX a LF is only required. This combination of CR and LR is used for example when pressing 'Enter' on the keyboard. Depending on the application being used, pressing 'Enter' generally instructs the application to start a new line, or to send a command.]]>            </description>
            <solution>
<![CDATA[Check the submitted parameters and do not allow CRLF to be injected by filtering CRLF]]>            </solution>
            <references>
                <reference>
                    <title>CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')</title>
                    <url>http://cwe.mitre.org/data/definitions/93.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/CRLF_Injection</title>
                    <url>http://www.owasp.org/index.php/CRLF_Injection</url>
                </reference>
                <reference>
                    <title>http://www.acunetix.com/websitesecurity/crlf-injection.htm</title>
                    <url>http://www.acunetix.com/websitesecurity/crlf-injection.htm</url>
                </reference>
                <reference>
                    <title>VulneraNET wiki: CRLF Injection article</title>
                    <url>http://lab.gsi.dit.upm.es/semanticwiki/index.php/CRLF_Injection</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Commands execution">
            <description>
<![CDATA[This attack consists in executing system commands on the server. The attacker tries to inject this commands in the request parameters]]>            </description>
            <solution>
<![CDATA[Prefer working without user input when using file system calls]]>            </solution>
            <references>
                <reference>
                    <title>CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')</title>
                    <url>http://cwe.mitre.org/data/definitions/78.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Command_Injection</title>
                    <url>http://www.owasp.org/index.php/Command_Injection</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
    </vulnerabilities>
    <anomalies>
        <anomaly name="Resource consumption">
            <description>
<![CDATA[Resource consumption description]]>            </description>
            <solution>
<![CDATA[The involved script is maybe using the server resources (CPU, memory, network, file access...) in a non-efficient way]]>            </solution>
            <references>
                <reference>
                    <title>CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')</title>
                    <url>http://cwe.mitre.org/data/definitions/400.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Asymmetric_resource_consumption_(amplification)</title>
                    <url>http://www.owasp.org/index.php/Asymmetric_resource_consumption_(amplification)</url>
                </reference>
            </references>
            <entries/>
        </anomaly>
        <anomaly name="Internal Server Error">
            <description>
<![CDATA[Internal server error description]]>            </description>
            <solution>
<![CDATA[More information about the error should be found in the server logs.]]>            </solution>
            <references>
                <reference>
                    <title>Wikipedia article for 5xx HTTP error codes</title>
                    <url>https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error</url>
                </reference>
            </references>
            <entries/>
        </anomaly>
    </anomalies>
</report>
"""


report_no_vulns = """<?xml version="1.0"?>
<report type="security">
    <report_infos>
        <info name="generatorName">wapiti</info>
        <info name="generatorVersion">Wapiti 2.3.0</info>
        <info name="scope">folder</info>
        <info name="dateOfScan">Tue, 24 Jan 2017 05:29:07 +0000</info>
    </report_infos>
    <vulnerabilities>
        <vulnerability name="Cross Site Scripting">
            <description>
<![CDATA[Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications which allow code injection by malicious web users into the web pages viewed by other users. Examples of such code include HTML code and client-side scripts.]]>            </description>
            <solution>
<![CDATA[The best way to protect a web application from XSS attacks is ensure that the application performs validation of all headers, cookies, query strings, form fields, and hidden fields. Encoding user supplied output in the server side can also defeat XSS vulnerabilities by preventing inserted scripts from being transmitted to users in an executable form. Applications can gain significant protection from javascript based attacks by converting the following characters in all generated output to the appropriate HTML entity encoding:  &lt;, &gt;, &amp;, &quot;, ', (, ), #, %, ; , +, -.]]>            </solution>
            <references>
                <reference>
                    <title>CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')</title>
                    <url>http://cwe.mitre.org/data/definitions/79.html</url>
                </reference>
                <reference>
                    <title>http://en.wikipedia.org/wiki/Cross-site_scripting</title>
                    <url>http://en.wikipedia.org/wiki/Cross-site_scripting</url>
                </reference>
                <reference>
                    <title>VulneraNET wiki: Cross Site Scripting Flaw article</title>
                    <url>http://lab.gsi.dit.upm.es/semanticwiki/index.php/Cross_Site_Scripting_Flaw</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Cross_Site_Scripting</title>
                    <url>http://www.owasp.org/index.php/Cross_Site_Scripting</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Htaccess Bypass">
            <description>
<![CDATA[htaccess files are used to restrict access to some files or HTTP method. In some case it may be possible to bypass this restriction and access the files.]]>            </description>
            <solution>
<![CDATA[Make sure every HTTP method is forbidden if the credentials are bad.]]>            </solution>
            <references>
                <reference>
                    <title>http://blog.teusink.net/2009/07/common-apache-htaccess-misconfiguration.html</title>
                    <url>http://blog.teusink.net/2009/07/common-apache-htaccess-misconfiguration.html</url>
                </reference>
                <reference>
                    <title>CWE-538: File and Directory Information Exposure</title>
                    <url>http://cwe.mitre.org/data/definitions/538.html</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Backup file">
            <description>
<![CDATA[It may be possible to find backup files of scripts on the webserver that the web-admin put here to save a previous version or backup files that are automaticallygenerated by the software editor used (like for example Emacs). These copies may reveal interesting informations like source code or credentials]]>            </description>
            <solution>
<![CDATA[The webadmin must manually delete the backup files or remove it from the web root. He should also reconfigure its editor to deactivate automatic backups.]]>            </solution>
            <references>
                <reference>
                    <title>Testing for Old, Backup and Unreferenced Files (OWASP-CM-006)</title>
                    <url>http://www.owasp.org/index.php/Testing_for_Old,_Backup_and_Unreferenced_Files_(OWASP-CM-006)</url>
                </reference>
                <reference>
                    <title>CWE-530: Exposure of Backup File to an Unauthorized Control Sphere</title>
                    <url>http://cwe.mitre.org/data/definitions/530.html</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="SQL Injection">
            <description>
<![CDATA[SQL injection vulnerabilities allow an attacker to alter the queries executed on the backend database. An attacker may then be able to extract or modify informations stored in the database or even escalate his privileges on the system.]]>            </description>
            <solution>
<![CDATA[To protect against SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.]]>            </solution>
            <references>
                <reference>
                    <title>http://www.owasp.org/index.php/SQL_Injection</title>
                    <url>http://www.owasp.org/index.php/SQL_Injection</url>
                </reference>
                <reference>
                    <title>http://en.wikipedia.org/wiki/SQL_injection</title>
                    <url>http://en.wikipedia.org/wiki/SQL_injection</url>
                </reference>
                <reference>
                    <title>CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')</title>
                    <url>http://cwe.mitre.org/data/definitions/89.html</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Blind SQL Injection">
            <description>
<![CDATA[Blind SQL injection is a technique that exploits a vulnerability occurring in the database of an application. This kind of vulnerability is harder to detect than basic SQL injections because no error message will be displayed on the webpage.]]>            </description>
            <solution>
<![CDATA[To protect against SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.]]>            </solution>
            <references>
                <reference>
                    <title>CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')</title>
                    <url>http://cwe.mitre.org/data/definitions/89.html</url>
                </reference>
                <reference>
                    <title>http://www.imperva.com/resources/adc/blind_sql_server_injection.html</title>
                    <url>http://www.imperva.com/resources/adc/blind_sql_server_injection.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Blind_SQL_Injection</title>
                    <url>http://www.owasp.org/index.php/Blind_SQL_Injection</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="File Handling">
            <description>
<![CDATA[This attack is also known as Path or Directory Traversal, its aim is the access to files and directories that are stored outside the web root folder. The attacker tries to explore the directories stored in the web server. The attacker uses some techniques, for instance, the manipulation of variables that reference files with 'dot-dot-slash (../)' sequences and its variations to move up to root directory to navigate through the file system.]]>            </description>
            <solution>
<![CDATA[Prefer working without user input when using file system calls. Use indexes rather than actual portions of file names when templating or using language files (eg: value 5 from the user submission = Czechoslovakian, rather than expecting the user to return 'Czechoslovakian'). Ensure the user cannot supply all parts of the path - surround it with your path code. Validate the user's input by only accepting known good - do not sanitize the data. Use chrooted jails and code access policies to restrict where the files can be obtained or saved to.]]>            </solution>
            <references>
                <reference>
                    <title>http://www.owasp.org/index.php/Path_Traversal</title>
                    <url>http://www.owasp.org/index.php/Path_Traversal</url>
                </reference>
                <reference>
                    <title>http://www.acunetix.com/websitesecurity/directory-traversal.htm</title>
                    <url>http://www.acunetix.com/websitesecurity/directory-traversal.htm</url>
                </reference>
                <reference>
                    <title>CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')</title>
                    <url>http://cwe.mitre.org/data/definitions/22.html</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Potentially dangerous file">
            <description>
<![CDATA[A file with potential vulnerabilities has been found on the website.]]>            </description>
            <solution>
<![CDATA[Make sure the script is up-to-date and restrict access to it if possible]]>            </solution>
            <references>
                <reference>
                    <title>The Open Source Vulnerability Database</title>
                    <url>http://osvdb.org/</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="CRLF Injection">
            <description>
<![CDATA[The term CRLF refers to Carriage Return (ASCII 13, \r) Line Feed (ASCII 10, \n). They're used to note the termination of a line, however, dealt with differently in today's popular Operating Systems. For example: in Windows both a CR and LF are required to note the end of a line, whereas in Linux/UNIX a LF is only required. This combination of CR and LR is used for example when pressing 'Enter' on the keyboard. Depending on the application being used, pressing 'Enter' generally instructs the application to start a new line, or to send a command.]]>            </description>
            <solution>
<![CDATA[Check the submitted parameters and do not allow CRLF to be injected by filtering CRLF]]>            </solution>
            <references>
                <reference>
                    <title>CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')</title>
                    <url>http://cwe.mitre.org/data/definitions/93.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/CRLF_Injection</title>
                    <url>http://www.owasp.org/index.php/CRLF_Injection</url>
                </reference>
                <reference>
                    <title>http://www.acunetix.com/websitesecurity/crlf-injection.htm</title>
                    <url>http://www.acunetix.com/websitesecurity/crlf-injection.htm</url>
                </reference>
                <reference>
                    <title>VulneraNET wiki: CRLF Injection article</title>
                    <url>http://lab.gsi.dit.upm.es/semanticwiki/index.php/CRLF_Injection</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
        <vulnerability name="Commands execution">
            <description>
<![CDATA[This attack consists in executing system commands on the server. The attacker tries to inject this commands in the request parameters]]>            </description>
            <solution>
<![CDATA[Prefer working without user input when using file system calls]]>            </solution>
            <references>
                <reference>
                    <title>CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')</title>
                    <url>http://cwe.mitre.org/data/definitions/78.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Command_Injection</title>
                    <url>http://www.owasp.org/index.php/Command_Injection</url>
                </reference>
            </references>
            <entries/>
        </vulnerability>
    </vulnerabilities>
    <anomalies>
        <anomaly name="Resource consumption">
            <description>
<![CDATA[Resource consumption description]]>            </description>
            <solution>
<![CDATA[The involved script is maybe using the server resources (CPU, memory, network, file access...) in a non-efficient way]]>            </solution>
            <references>
                <reference>
                    <title>CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')</title>
                    <url>http://cwe.mitre.org/data/definitions/400.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Asymmetric_resource_consumption_(amplification)</title>
                    <url>http://www.owasp.org/index.php/Asymmetric_resource_consumption_(amplification)</url>
                </reference>
            </references>
            <entries/>
        </anomaly>
        <anomaly name="Internal Server Error">
            <description>
<![CDATA[Internal server error description]]>            </description>
            <solution>
<![CDATA[More information about the error should be found in the server logs.]]>            </solution>
            <references>
                <reference>
                    <title>Wikipedia article for 5xx HTTP error codes</title>
                    <url>https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error</url>
                </reference>
            </references>
            <entries/>
        </anomaly>
    </anomalies>
</report>
"""


report_invalid_no_vulns = """<?xml version="1.0"?>
<report type="security">
    <report_infos>
        <info name="generatorName">wapiti</info>
        <info name="generatorVersion">Wapiti 2.3.0</info>
        <info name="scope">folder</info>
        <info name="dateOfScan">Tue, 24 Jan 2017 05:29:07 +0000</info>
    </report_infos>
    <anomalies>
        <anomaly name="Resource consumption">
            <description>
<![CDATA[Resource consumption description]]>            </description>
            <solution>
<![CDATA[The involved script is maybe using the server resources (CPU, memory, network, file access...) in a non-efficient way]]>            </solution>
            <references>
                <reference>
                    <title>CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')</title>
                    <url>http://cwe.mitre.org/data/definitions/400.html</url>
                </reference>
                <reference>
                    <title>http://www.owasp.org/index.php/Asymmetric_resource_consumption_(amplification)</title>
                    <url>http://www.owasp.org/index.php/Asymmetric_resource_consumption_(amplification)</url>
                </reference>
            </references>
            <entries/>
        </anomaly>
        <anomaly name="Internal Server Error">
            <description>
<![CDATA[Internal server error description]]>            </description>
            <solution>
<![CDATA[More information about the error should be found in the server logs.]]>            </solution>
            <references>
                <reference>
                    <title>Wikipedia article for 5xx HTTP error codes</title>
                    <url>https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error</url>
                </reference>
            </references>
            <entries/>
        </anomaly>
    </anomalies>
</report>
"""
