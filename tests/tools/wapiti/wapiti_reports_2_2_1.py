# -*- coding: utf-8 -*-
report_high = """<?xml version="1.0"?>
<report type="security">
    <generatedBy id="Wapiti 2.2.1"/>
    <bugTypeList>
        <bugType name="SQL Injection">
            <bugList/>
            <description>
<![CDATA[SQL injection is a technique that exploits a vulnerability occurring in the database of an application.]]>            </description>
            <solution>
<![CDATA[To protect against SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.]]>            </solution>
            <references>
                <reference>
                    <title>
                        http://www.owasp.org/index.php/SQL_Injection
                    </title>
                    <url>
                        http://www.owasp.org/index.php/SQL_Injection
                    </url>
                </reference>
                <reference>
                    <title>
                        http://en.wikipedia.org/wiki/SQL_injection
                    </title>
                    <url>
                        http://en.wikipedia.org/wiki/SQL_injection
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="Blind SQL Injection">
            <bugList/>
            <description>
<![CDATA[Blind SQL injection is a technique that exploits a vulnerability occurring in the database of an application. This kind of vulnerability is harder to detect than basic SQL injections because no error message will be displayed on the webpage.]]>            </description>
            <solution>
<![CDATA[To protect against SQL injection, user input must not directly be embedded in SQL statements. Instead, user input must be escaped or filtered or parameterized statements must be used.]]>            </solution>
            <references>
                <reference>
                    <title>
                        http://www.imperva.com/resources/adc/blind_sql_server_injection.html
                    </title>
                    <url>
                        http://www.imperva.com/resources/adc/blind_sql_server_injection.html
                    </url>
                </reference>
                <reference>
                    <title>
                        http://www.owasp.org/index.php/Blind_SQL_Injection
                    </title>
                    <url>
                        http://www.owasp.org/index.php/Blind_SQL_Injection
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="File Handling">
            <bugList>
                <bug level="1">
                    <url>
                        http://10.1.1.6/chyrp_v2.1b2/?action=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00
                    </url>
                    <parameter>
                        action=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00
                    </parameter>
                    <info>
                        Unix include/fread (action)
                    </info>
                </bug>
                <bug level="1">
                    <url>
                        http://10.1.1.6/chyrp_v2.1b2/?action=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00&amp;year=2011&amp;month=03
                    </url>
                    <parameter>
                        action=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00&amp;year=2011&amp;month=03
                    </parameter>
                    <info>
                        Unix include/fread (action)
                    </info>
                </bug>
                <bug level="1">
                    <url>
                        http://10.1.1.6/chyrp_v2.1b2/?action=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00&amp;name=post1tag
                    </url>
                    <parameter>
                        action=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00&amp;name=post1tag
                    </parameter>
                    <info>
                        Unix include/fread (action)
                    </info>
                </bug>
                <bug level="1">
                    <url>
                        http://10.1.1.6/chyrp_v2.1b2/?action=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00&amp;url=post1
                    </url>
                    <parameter>
                        action=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%00&amp;url=post1
                    </parameter>
                    <info>
                        Unix include/fread (action)
                    </info>
                </bug>
            </bugList>
            <description>
<![CDATA[This attack is also known as Path Transversal or Directory Transversal, its aim is the access to files and directories that are stored outside the web root folder. The attacker tries to explore the directories stored in the web server. The attacker uses some techniques, for instance, the manipulation of variables that reference files with 'dot-dot-slash (../)' sequences and its variations to move up to root directory to navigate through the file system.]]>            </description>
            <solution>
<![CDATA[Prefer working without user input when using file system calls<br>Use indexes rather than actual portions of file names when templating or using language files (ie value 5 from the user submission = Czechoslovakian, rather than expecting the user to return 'Czechoslovakian').<br>Ensure the user cannot supply all parts of the path – surround it with your path code.<br>Validate the user’s input by only accepting known good – do not sanitize the data.<br>Use chrooted jails and code access policies to restrict where the files can be obtained or saved to.]]>            </solution>
            <references>
                <reference>
                    <title>
                        http://www.owasp.org/index.php/Path_Traversal
                    </title>
                    <url>
                        http://www.owasp.org/index.php/Path_Traversal
                    </url>
                </reference>
                <reference>
                    <title>
                        http://www.acunetix.com/websitesecurity/directory-traversal.htm
                    </title>
                    <url>
                        http://www.acunetix.com/websitesecurity/directory-traversal.htm
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="Cross Site Scripting">
            <bugList>
                <bug level="1">
                    <url>
                        http://10.1.1.6/chyrp_v2.1b2/?action=%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%28%27kwjufljfsg%27%29%3C%2Fscript%3E
                    </url>
                    <parameter>
                        action=%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%28%27kwjufljfsg%27%29%3C%2Fscript%3E
                    </parameter>
                    <info>
                        XSS (action)
                    </info>
                </bug>
                <bug level="1">
                    <url>
                        http://10.1.1.6/chyrp_v2.1b2/?action=%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%28%27jad3jql5qd%27%29%3C%2Fscript%3E&amp;month=03&amp;year=2011
                    </url>
                    <parameter>
                        action=%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%28%27jad3jql5qd%27%29%3C%2Fscript%3E&amp;month=03&amp;year=2011
                    </parameter>
                    <info>
                        XSS (action)
                    </info>
                </bug>
                <bug level="1">
                    <url>
                        http://10.1.1.6/chyrp_v2.1b2/?action=%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%28%27j9ukfmupb9%27%29%3C%2Fscript%3E&amp;name=post1tag
                    </url>
                    <parameter>
                        action=%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%28%27j9ukfmupb9%27%29%3C%2Fscript%3E&amp;name=post1tag
                    </parameter>
                    <info>
                        XSS (action)
                    </info>
                </bug>
                <bug level="1">
                    <url>
                        http://10.1.1.6/chyrp_v2.1b2/?action=%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%28%27mb7kjvdyjo%27%29%3C%2Fscript%3E&amp;url=post1
                    </url>
                    <parameter>
                        action=%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%28%27mb7kjvdyjo%27%29%3C%2Fscript%3E&amp;url=post1
                    </parameter>
                    <info>
                        XSS (action)
                    </info>
                </bug>
            </bugList>
            <description>
<![CDATA[Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications which allow code injection by malicious web users into the web pages viewed by other users. Examples of such code include HTML code and client-side scripts.]]>            </description>
            <solution>
<![CDATA[The best way to protect a web application from XSS attacks is ensure that the application performs validation of all headers, cookies, query strings, form fields, and hidden fields. Encoding user supplied output in the server side can also defeat XSS vulnerabilities by preventing inserted scripts from being transmitted to users in an executable form. Applications can gain significant protection from javascript based attacks by converting the following characters in all generated output to the appropriate HTML entity encoding:  &lt;, &gt;, &amp;, &quot;, ', (, ), #, %, ; , +, -.]]>            </solution>
            <references>
                <reference>
                    <title>
                        http://en.wikipedia.org/wiki/Cross-site_scripting
                    </title>
                    <url>
                        http://en.wikipedia.org/wiki/Cross-site_scripting
                    </url>
                </reference>
                <reference>
                    <title>
                        http://www.owasp.org/index.php/Cross_Site_Scripting
                    </title>
                    <url>
                        http://www.owasp.org/index.php/Cross_Site_Scripting
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="CRLF">
            <bugList/>
            <description>
<![CDATA[The term CRLF refers to Carriage Return (ASCII 13, \r) Line Feed (ASCII 10, \n). They're used to note the termination of a line, however, dealt with differently in today’s popular Operating Systems. For example: in Windows both a CR and LF are required to note the end of a line, whereas in Linux/UNIX a LF is only required. This combination of CR and LR is used for example when pressing 'Enter' on the keyboard. Depending on the application being used, pressing 'Enter' generally instructs the application to start a new line, or to send a command.]]>            </description>
            <solution>
<![CDATA[Check the submitted parameters and do not allow CRLF to be injected by filtering CRLF]]>            </solution>
            <references>
                <reference>
                    <title>
                        http://www.owasp.org/index.php/CRLF_Injection
                    </title>
                    <url>
                        http://www.owasp.org/index.php/CRLF_Injection
                    </url>
                </reference>
                <reference>
                    <title>
                        http://www.acunetix.com/websitesecurity/crlf-injection.htm
                    </title>
                    <url>
                        http://www.acunetix.com/websitesecurity/crlf-injection.htm
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="Commands execution">
            <bugList/>
            <description>
<![CDATA[This attack consists in executing system commands on the server. The attacker tries to inject this commands in the request parameters]]>            </description>
            <solution>
<![CDATA[Prefer working without user input when using file system calls]]>            </solution>
            <references>
                <reference>
                    <title>
                        http://www.owasp.org/index.php/Command_Injection
                    </title>
                    <url>
                        http://www.owasp.org/index.php/Command_Injection
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="Resource consumption">
            <bugList/>
            <description>
<![CDATA[An attacker can force a victim to consume more resources than should be allowed for the attacker's level of access. The program can potentially fail to release or incorrectly release a system resource. A resource is not properly cleared and made available for re-use. It can also be a false-positive due to a too short timeout used for the scan.]]>            </description>
            <solution>
<![CDATA[Configure properly the software giving the ressource to avoid memory consumption or system load.]]>            </solution>
            <references>
                <reference>
                    <title>
                        http://www.owasp.org/index.php/Asymmetric_resource_consumption_(amplification)
                    </title>
                    <url>
                        http://www.owasp.org/index.php/Asymmetric_resource_consumption_(amplification)
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="Htaccess Bypass">
            <bugList/>
            <description>
<![CDATA[htaccess files are used to restrict access to some files or HTTP method. In some case it may be possible to bypass this restriction and access the files.]]>            </description>
            <solution>
<![CDATA[Make sure every HTTP method is forbidden if the credentials are bad.]]>            </solution>
            <references>
                <reference>
                    <title>
                        http://blog.teusink.net/2009/07/common-apache-htaccess-misconfiguration.html
                    </title>
                    <url>
                        http://blog.teusink.net/2009/07/common-apache-htaccess-misconfiguration.html
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="Backup file">
            <bugList/>
            <description>
<![CDATA[It may be possible to find backup files of scripts on the webserver that thewebadmin put here to save a previous version or backup files that are automaticallygenerated by the software editor used (like for example Emacs). These copies may revealinteresting informations like source code or credentials]]>            </description>
            <solution>
<![CDATA[The webadmin must manually delete the backup files or remove it from the web root. He shouldalso reconfigure its editor to deactivate automatic backups]]>            </solution>
            <references>
                <reference>
                    <title>
                        Testing for Old, Backup and Unreferenced Files (OWASP-CM-006)
                    </title>
                    <url>
                        http://www.owasp.org/index.php/Testing_for_Old,_Backup_and_Unreferenced_Files_(OWASP-CM-006)
                    </url>
                </reference>
            </references>
        </bugType>
        <bugType name="Potentially dangerous file">
            <bugList/>
            <description>
<![CDATA[Some scripts are known to be vulnerable or dangerous. Databases of such files exists and attackers often scan websites to find such vulnerabilities and exploit them. ]]>            </description>
            <solution>
<![CDATA[The administrator should frequently check for new version of the scripts used on his server and keep informed of vulnerabilities in the software programs he uses by reading security-list or specialised RSS.]]>            </solution>
            <references>
                <reference>
                    <title>
                        The Open Source Vulnerability Database
                    </title>
                    <url>
                        http://osvdb.org/
                    </url>
                </reference>
            </references>
        </bugType>
    </bugTypeList>
</report>
"""
