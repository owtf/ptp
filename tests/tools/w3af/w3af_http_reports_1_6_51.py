# -*- coding: UTF-8 -*-
report_http = r"""
========================================Request 1 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 1 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 2 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 2 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=99
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 3 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 3 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=98
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 4 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 4 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=97
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 5 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 5 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=96
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 6 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 6 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=95
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 7 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 7 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=94
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 8 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 8 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=93
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 9 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 9 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=92
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
=====================================================================================================================
========================================Request 10 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 10 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=91
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 11 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 11 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=90
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 12 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 12 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=89
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 13 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 13 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=88
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 14 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 14 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=87
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 15 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 15 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=86
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 16 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 16 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=85
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 17 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 17 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=84
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 18 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 18 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 23 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/nDspn8nu.htm HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 23 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 285
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /nDspn8nu.htm was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 20 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/LCdZPsMg.cgi HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 20 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 285
keep-alive: timeout=5, max=83
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /LCdZPsMg.cgi was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 21 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/wgz8ZcrT.do HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 21 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 284
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /wgz8ZcrT.do was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 22 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/VQr0QeRW.asp HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 22 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 285
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /VQr0QeRW.asp was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 19 - Wed Apr 13 07:59:01 2016 ========================================
GET http://127.0.0.1/cuzjmpTs.foobar HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 19 - Wed Apr 13 07:59:01 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 288
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /cuzjmpTs.foobar was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 24 - Wed Apr 13 07:59:02 2016 ========================================
GET http://127.0.0.1/YMkKyTWY.py HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 24 - Wed Apr 13 07:59:02 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 284
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:02 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /YMkKyTWY.py was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 25 - Wed Apr 13 07:59:03 2016 ========================================
GET http://127.0.0.1/dA19MTZ6.gif HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 25 - Wed Apr 13 07:59:03 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 285
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:03 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /dA19MTZ6.gif was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 26 - Wed Apr 13 07:59:03 2016 ========================================
GET http://127.0.0.1/AXTHm5sQ.htmls HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 26 - Wed Apr 13 07:59:03 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 287
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:03 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /AXTHm5sQ.htmls was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 27 - Wed Apr 13 07:59:04 2016 ========================================
GET http://127.0.0.1/7xpvduaC.jsp HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 27 - Wed Apr 13 07:59:04 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 285
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:04 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /7xpvduaC.jsp was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 29 - Wed Apr 13 07:59:04 2016 ========================================
GET http://127.0.0.1/b9ROfy4C.php HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 29 - Wed Apr 13 07:59:04 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 285
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:04 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /b9ROfy4C.php was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 28 - Wed Apr 13 07:59:04 2016 ========================================
GET http://127.0.0.1/9zdHD8Az.rb HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 28 - Wed Apr 13 07:59:04 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 284
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:04 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /9zdHD8Az.rb was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 30 - Wed Apr 13 07:59:04 2016 ========================================
GET http://127.0.0.1/rSOzbaX6.xhtml HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 30 - Wed Apr 13 07:59:04 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 287
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:04 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /rSOzbaX6.xhtml was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 31 - Wed Apr 13 07:59:05 2016 ========================================
GET http://127.0.0.1/0VyFRjBd.aspx HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 31 - Wed Apr 13 07:59:05 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 286
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:05 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /0VyFRjBd.aspx was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 32 - Wed Apr 13 07:59:05 2016 ========================================
GET http://127.0.0.1/LhKJLL1W.pl HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 32 - Wed Apr 13 07:59:05 2016 =======================================
HTTP/1.1 404 Not Found
content-length: 284
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
connection: Keep-Alive
date: Wed, 13 Apr 2016 11:59:05 GMT
content-type: text/html; charset=iso-8859-1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /LhKJLL1W.pl was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at 127.0.0.1 Port 80</address>
</body></html>
======================================================================================================================
========================================Request 33 - Wed Apr 13 07:59:05 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 33 - Wed Apr 13 07:59:05 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 34 - Wed Apr 13 07:59:06 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 34 - Wed Apr 13 07:59:06 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=82
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:06 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 37 - Wed Apr 13 07:59:06 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 37 - Wed Apr 13 07:59:06 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
======================================================================================================================
========================================Request 46 - Wed Apr 13 07:59:06 2016 ========================================
GET http://127.0.0.1/ HTTP/1.1
Accept-encoding: gzip, deflate
User-agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/15.0
Host: 127.0.0.1
Accept: */*
========================================Response 46 - Wed Apr 13 07:59:06 2016 =======================================
HTTP/1.1 200 OK
content-length: 3078
content-encoding: gzip
accept-ranges: bytes
vary: Accept-Encoding
keep-alive: timeout=5, max=100
server: Apache/2.4.10 (Debian)
last-modified: Sun, 09 Aug 2015 02:53:20 GMT
connection: Keep-Alive
etag: "2b60-51cd7f8b96800-gzip"
date: Wed, 13 Apr 2016 11:59:01 GMT
content-type: text/html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Debian Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  body, html {
    padding: 3px 3px 3px 3px;
    background-color: #D8DBE2;
    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  div.main_page {
    position: relative;
    display: table;
    width: 800px;
    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;
    border-width: 2px;
    border-color: #212738;
    border-style: solid;
    background-color: #FFFFFF;
    text-align: center;
  div.page_header {
    height: 99px;
    width: 100%;
    background-color: #F5F6F7;
  div.page_header span {
    margin: 15px 0px 0px 50px;
    font-size: 180%;
    font-weight: bold;
  div.page_header img {
    margin: 3px 0px 0px 40px;
    border: 0px 0px 0px;
  div.table_of_contents {
    clear: left;
    min-width: 200px;
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.table_of_contents_item {
    clear: left;
    width: 100%;
    margin: 4px 0px 0px 0px;
    background-color: #FFFFFF;
    color: #000000;
    text-align: left;
  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  div.content_section {
    margin: 3px 3px 3px 3px;
    background-color: #FFFFFF;
    text-align: left;
  div.content_section_text {
    padding: 4px 8px 4px 8px;
    color: #000000;
    font-size: 100%;
  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;
    border-width: 1px;
    border-style: dotted;
    border-color: #000000;
    background-color: #F5F6F7;
    font-style: italic;
  div.content_section_text p {
    margin-bottom: 6px;
  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  div.section_header {
    padding: 3px 6px 3px 6px;
    background-color: #8E9CB2;
    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  div.section_header_red {
    background-color: #CD214F;
  div.section_header_grey {
    background-color: #9F9386;
  .floating_element {
    position: relative;
    float: left;
  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  div.table_of_contents_item a:hover {
    background-color: #000000;
    color: #FFFFFF;
  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;
    color: #000000;
  div.content_section_text a:hover {
    background-color: #000000;
    color: #DCDFE6;
  div.validator {
    </style>
  </head>
  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache2 Debian Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
      <div class="content_section floating_element">
        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Debian systems.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>
          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>
        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Debian's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Debian tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.
          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Debian systems is as follows:
          </p>
          <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>
                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>
                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>
                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>
                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>
        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>
        <div class="content_section_text">
            <p>
                By default, Debian does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Debian document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>
        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>reportbug</tt> tool to report bugs in the
                Apache2 package with Debian. However, check <a
                href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>
      </div>
    </div>
    <div class="validator">
    </div>
  </body>
</html>
========================================================================================================================
"""
