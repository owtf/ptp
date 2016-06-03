report_high = r"""<?xml version="1.0"?>
<report xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/Arachni/arachni/v1.2.1/components/reporters/xml/schema.xsd">
  <version>1.2.1</version>
  <options>---
input:
  values: {}
  default_values:
    "(?i-mx:name)": arachni_name
    "(?i-mx:user)": arachni_user
    "(?i-mx:usr)": arachni_user
    "(?i-mx:pass)": 5543!%arachni_secret
    "(?i-mx:txt)": arachni_text
    "(?i-mx:num)": '132'
    "(?i-mx:amount)": '100'
    "(?i-mx:mail)": arachni@email.gr
    "(?i-mx:account)": '12'
    "(?i-mx:id)": '1'
  without_defaults: false
  force: false
audit:
  parameter_values: true
  exclude_vector_patterns: []
  include_vector_patterns: []
  link_templates: []
  links: true
  forms: true
  cookies: true
  jsons: true
  xmls: true
browser_cluster:
  wait_for_elements: {}
  pool_size: 6
  job_timeout: 25
  worker_time_to_live: 100
  ignore_images: false
  screen_width: 1600
  screen_height: 1200
session: {}
http:
  user_agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
  request_timeout: 10000
  request_redirect_limit: 5
  request_concurrency: 20
  request_queue_size: 100
  request_headers: {}
  response_max_size: 500000
  cookies: {}
scope:
  redundant_path_patterns: {}
  dom_depth_limit: 5
  exclude_path_patterns: []
  exclude_content_patterns: []
  include_path_patterns: []
  restrict_paths: []
  extend_paths: []
  url_rewrites: {}
datastore:
  report_path: "/root/Desktop/arachni.afr"
checks:
- htaccess_limit
- insecure_client_access_policy
- interesting_responses
- insecure_cross_domain_policy_access
- insecure_cross_domain_policy_headers
- backdoors
- directory_listing
- origin_spoof_access_restriction_bypass
- backup_directories
- http_put
- xst
- localstart_asp
- common_admin_interfaces
- common_files
- common_directories
- webdav
- backup_files
- captcha
- private_ip
- http_only_cookies
- x_frame_options
- unencrypted_password_forms
- insecure_cookies
- password_autocomplete
- cookie_set_for_parent_domain
- insecure_cors_policy
- credit_card
- ssn
- html_objects
- form_upload
- mixed_resource
- hsts
- cvs_svn_users
- emails
- allowed_methods
- sql_injection
- code_injection_timing
- no_sql_injection
- session_fixation
- path_traversal
- unvalidated_redirect
- trainer
- os_cmd_injection_timing
- response_splitting
- xxe
- file_inclusion
- csrf
- xss_event
- xss_path
- source_code_disclosure
- rfi
- xss_dom_script_context
- no_sql_injection_differential
- unvalidated_redirect_dom
- sql_injection_differential
- xpath_injection
- ldap_injection
- xss_tag
- xss_script_context
- xss
- code_injection_php_input_wrapper
- xss_dom
- os_cmd_injection
- code_injection
- sql_injection_timing
- xss_dom_inputs
platforms: []
plugins: {}
no_fingerprinting: false
authorized_by: 
url: http://elearnix.org/
</options>
  <start_datetime>2016-06-07T09:37:38-04:00</start_datetime>
  <finish_datetime>2016-06-07T09:55:29-04:00</finish_datetime>
  <sitemap>
    <entry url="http://elearnix.org/" code="200"/>
  </sitemap>
  <issues>
    <issue>
      <name>Cross-Site Request Forgery</name>
      <description>
In the majority of today's web applications, clients are required to submit forms
which can perform sensitive operations.

An example of such a form being used would be when an administrator wishes to
create a new user for the application.

In the simplest version of the form, the administrator would fill-in:

* Name
* Password
* Role (level of access)

Continuing with this example, Cross Site Request Forgery (CSRF) would occur when
the administrator is tricked into clicking on a link, which if logged into the
application, would automatically submit the form without any further interaction.

Cyber-criminals will look for sites where sensitive functions are performed in
this manner and then craft malicious requests that will be used against clients
via a social engineering attack.

There are 3 things that are required for a CSRF attack to occur:

1. The form must perform some sort of sensitive action.
2. The victim (the administrator the example above) must have an active session.
3. Most importantly, all parameter values must be **known** or **guessable**.

Arachni discovered that all parameters within the form were known or predictable
and therefore the form could be vulnerable to CSRF.

_Manual verification may be required to check whether the submission will then
perform a sensitive action, such as reset a password, modify user profiles, post
content on a forum, etc._
</description>
      <remedy_guidance>
Based on the risk (determined by manual verification) of whether the form submission
performs a sensitive action, the addition of anti-CSRF tokens may be required.

These tokens can be configured in such a way that each session generates a new
anti-CSRF token or such that each individual request requires a new token.

It is important that the server track and maintain the status of each token (in
order to reject requests accompanied by invalid ones) and therefore prevent
cyber-criminals from knowing, guessing or reusing them.

_For examples of framework specific remediation options, please refer to the references._
</remedy_guidance>
      <remedy_code/>
      <severity>high</severity>
      <check>
        <name>CSRF</name>
        <description>
It uses differential analysis to determine which forms affect business logic and
checks them for lack of anti-CSRF tokens.

(Works best with a valid session.)
</description>
        <author>Tasos "Zapotek" Laskos &lt;tasos.laskos@arachni-scanner.com&gt; </author>
        <version>0.3.5</version>
        <shortname>csrf</shortname>
      </check>
      <cwe>352</cwe>
      <digest>1606559286</digest>
      <references>
        <reference title="Wikipedia" url="http://en.wikipedia.org/wiki/Cross-site_request_forgery"/>
        <reference title="OWASP" url="https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)"/>
        <reference title="CGI Security" url="http://www.cgisecurity.com/csrf-faq.html"/>
      </references>
      <vector>
        <class>Arachni::Element::Form</class>
        <type>form</type>
        <url>http://elearnix.org/</url>
        <action>http://elearnix.org/verify.php</action>
        <source>&lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/"&gt;
                    &lt;input type="submit" value="Delist"&gt;
                &lt;/form&gt;</source>
        <affected_input_name/>
        <inputs>
          <input name="recaptcha_challenge_field" value=""/>
          <input name="recaptcha_response_field" value="manual_challenge"/>
          <input name="origin_url" value="http://elearnix.org/"/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <seed/>
            <inputs>
              <input name="recaptcha_challenge_field" value=""/>
              <input name="recaptcha_response_field" value="manual_challenge"/>
              <input name="origin_url" value="http://elearnix.org/"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>&lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/"&gt;
                    &lt;input type="submit" value="Delist"&gt;
                &lt;/form&gt;</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>HTTP TRACE</name>
      <description>
The `TRACE` HTTP method allows a client so send a request to the server, and
have the same request then send back in the server's response. This allows the
client to determine if the server is receiving the request as expected or if
specific parts of the request are not arriving as expected.
For example incorrect encoding or a load balancer has filtered or changed a value.
On many default installations the `TRACE` method is still enabled.

While not vulnerable by itself, it does provide a method for cyber-criminals to
bypass the `HTTPOnly` cookie flag, and therefore could allow a XSS attack to
successfully access a session token.

Arachni has discovered that the affected page permits the HTTP `TRACE` method.
</description>
      <remedy_guidance>
The HTTP `TRACE` method is normally not required within production sites and
should therefore be disabled.

Depending on the function being performed by the web application, the risk
level can start low and increase as more functionality is implemented.

The remediation is typically a very simple configuration change and in most cases
will not have any negative impact on the server or application.
</remedy_guidance>
      <remedy_code/>
      <severity>medium</severity>
      <check>
        <name>XST</name>
        <description>Sends an HTTP TRACE request and checks if it succeeded.</description>
        <author>Tasos "Zapotek" Laskos &lt;tasos.laskos@arachni-scanner.com&gt;</author>
        <version>0.1.7</version>
        <shortname>xst</shortname>
      </check>
      <cwe>693</cwe>
      <digest>1441521763</digest>
      <references>
        <reference title="CAPEC" url="http://capec.mitre.org/data/definitions/107.html"/>
        <reference title="OWASP" url="http://www.owasp.org/index.php/Cross_Site_Tracing"/>
      </references>
      <vector>
        <class>Arachni::Element::Server</class>
        <type>server</type>
        <url>http://elearnix.org/</url>
        <action>http://elearnix.org/</action>
      </vector>
      <variations>
        <variation>
          <vector/>
          <remarks/>
          <page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>trace</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>TRACE / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>2.3537</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:43 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:43 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>HTTP/1.1 200 OK</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Missing 'X-Frame-Options' header</name>
      <description>
Clickjacking (User Interface redress attack, UI redress attack, UI redressing)
is a malicious technique of tricking a Web user into clicking on something different
from what the user perceives they are clicking on, thus potentially revealing
confidential information or taking control of their computer while clicking on
seemingly innocuous web pages.

The server didn't return an `X-Frame-Options` header which means that this website
could be at risk of a clickjacking attack.

The `X-Frame-Options` HTTP response header can be used to indicate whether or not
a browser should be allowed to render a page inside a frame or iframe. Sites can
use this to avoid clickjacking attacks, by ensuring that their content is not
embedded into other sites.
</description>
      <remedy_guidance>
Configure your web server to include an X-Frame-Options header.
</remedy_guidance>
      <remedy_code/>
      <severity>low</severity>
      <check>
        <name>Missing X-Frame-Options header</name>
        <description>Checks the host for a missing `X-Frame-Options` header.</description>
        <author>Tasos Laskos &lt;tasos.laskos@arachni-scanner.com&gt;</author>
        <version>0.1.1</version>
        <shortname>x_frame_options</shortname>
      </check>
      <cwe>693</cwe>
      <digest>730375711</digest>
      <references>
        <reference title="MDN" url="https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options"/>
        <reference title="RFC" url="http://tools.ietf.org/html/rfc7034"/>
        <reference title="OWASP" url="https://www.owasp.org/index.php/Clickjacking"/>
      </references>
      <vector>
        <class>Arachni::Element::Server</class>
        <type>server</type>
        <url>http://elearnix.org/</url>
        <action>http://elearnix.org/</action>
      </vector>
      <variations>
        <variation>
          <vector/>
          <remarks/>
          <page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Interesting response</name>
      <description>
The server responded with a non 200 (OK) nor 404 (Not Found) status code.
This is a non-issue, however exotic HTTP response status codes can provide useful
insights into the behavior of the web application and assist with the penetration test.
</description>
      <remedy_guidance/>
      <remedy_code/>
      <severity>informational</severity>
      <check>
        <name>Interesting responses</name>
        <description>Logs all non 200 (OK) server responses.</description>
        <author>Tasos "Zapotek" Laskos &lt;tasos.laskos@arachni-scanner.com&gt;</author>
        <version>0.2.1</version>
        <shortname>interesting_responses</shortname>
      </check>
      <digest>2686368332</digest>
      <references>
        <reference title="w3.org" url="http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html"/>
      </references>
      <vector>
        <class>Arachni::Element::Server</class>
        <type>server</type>
        <url>http://elearnix.org/.adm</url>
        <action>http://elearnix.org/.adm</action>
      </vector>
      <variations>
        <variation>
          <vector/>
          <remarks/>
          <page>
            <body>Invalid URI /.adm</body>
            <request>
              <url>http://elearnix.org/.adm</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET /.adm HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/.adm</url>
              <code>403</code>
              <ip_address>31.220.16.186</ip_address>
              <time>7.4241</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:49 GMT"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Content-Type" value="text/plain"/>
                <header name="Content-Length" value="17"/>
              </headers>
              <body>Invalid URI /.adm</body>
              <raw_headers>HTTP/1.1 403 Forbidden&#xD;
Date: Tue, 07 Jun 2016 13:37:49 GMT&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Content-Type: text/plain&#xD;
Content-Length: 17&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/.adm</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>HTTP/1.1 403 Forbidden</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>CAPTCHA protected form</name>
      <description>
To prevent the automated abuse of a page, applications can implement what is
known as a CAPTCHA.

These are used to ensure human interaction with the application and are often
used on forms where the application conducts sensitive actions. These typically
include user registration, or submitting emails via "Contact Us" pages etc.

Arachni has flagged this not as a vulnerability, but as a prompt for the
penetration tester to conduct further manual testing on the CAPTCHA function, as
Arachni cannot audit CAPTCHA protected forms.

Testing for insecurely implemented CAPTCHA is a manual process, and an insecurely
implemented CAPTCHA could allow a cyber-criminal a means to abuse these sensitive
actions.
</description>
      <remedy_guidance>
Although no remediation may be required based on this finding alone, manual
testing should ensure that:

1. The server keeps track of CAPTCHA tokens in use and has the token terminated
    after its first use or after a period of time. Therefore preventing replay attacks.
2. The CAPTCHA answer is not hidden in plain text within the response that is
    sent to the client.
3. The CAPTCHA image should not be weak and easily solved.
</remedy_guidance>
      <remedy_code/>
      <severity>informational</severity>
      <check>
        <name>CAPTCHA</name>
        <description>Greps pages for forms with CAPTCHAs.</description>
        <author>Tasos "Zapotek" Laskos &lt;tasos.laskos@arachni-scanner.com&gt;</author>
        <version>0.2</version>
        <shortname>captcha</shortname>
      </check>
      <digest>1495184166</digest>
      <references/>
      <vector>
        <class>Arachni::Element::Form</class>
        <type>form</type>
        <url>http://elearnix.org/</url>
        <action>http://elearnix.org/verify.php</action>
        <source>&lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/"&gt;
                    &lt;input type="submit" value="Delist"&gt;
                &lt;/form&gt;</source>
        <affected_input_name/>
        <inputs>
          <input name="recaptcha_challenge_field" value=""/>
          <input name="recaptcha_response_field" value="manual_challenge"/>
          <input name="origin_url" value="http://elearnix.org/"/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <seed/>
            <inputs>
              <input name="recaptcha_challenge_field" value=""/>
              <input name="recaptcha_response_field" value="manual_challenge"/>
              <input name="origin_url" value="http://elearnix.org/"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature>captcha</signature>
          <proof>&lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/"&gt;
                    &lt;input type="submit" value="Delist"&gt;
                &lt;/form&gt;</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Interesting response</name>
      <description>
The server responded with a non 200 (OK) nor 404 (Not Found) status code.
This is a non-issue, however exotic HTTP response status codes can provide useful
insights into the behavior of the web application and assist with the penetration test.
</description>
      <remedy_guidance/>
      <remedy_code/>
      <severity>informational</severity>
      <check>
        <name>Interesting responses</name>
        <description>Logs all non 200 (OK) server responses.</description>
        <author>Tasos "Zapotek" Laskos &lt;tasos.laskos@arachni-scanner.com&gt;</author>
        <version>0.2.1</version>
        <shortname>interesting_responses</shortname>
      </check>
      <digest>3783498189</digest>
      <references>
        <reference title="w3.org" url="http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html"/>
      </references>
      <vector>
        <class>Arachni::Element::Server</class>
        <type>server</type>
        <url>http://elearnix.org/.git/HEAD</url>
        <action>http://elearnix.org/.git/HEAD</action>
      </vector>
      <variations>
        <variation>
          <vector/>
          <remarks/>
          <page>
            <body>Invalid URI /.git/HEAD</body>
            <request>
              <url>http://elearnix.org/.git/HEAD</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET /.git/HEAD HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/.git/HEAD</url>
              <code>403</code>
              <ip_address>31.220.16.186</ip_address>
              <time>7.3712</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:49 GMT"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Content-Type" value="text/plain"/>
                <header name="Content-Length" value="22"/>
              </headers>
              <body>Invalid URI /.git/HEAD</body>
              <raw_headers>HTTP/1.1 403 Forbidden&#xD;
Date: Tue, 07 Jun 2016 13:37:49 GMT&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Content-Type: text/plain&#xD;
Content-Length: 22&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/.git/HEAD</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>HTTP/1.1 403 Forbidden</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Interesting response</name>
      <description>
The server responded with a non 200 (OK) nor 404 (Not Found) status code.
This is a non-issue, however exotic HTTP response status codes can provide useful
insights into the behavior of the web application and assist with the penetration test.
</description>
      <remedy_guidance/>
      <remedy_code/>
      <severity>informational</severity>
      <check>
        <name>Interesting responses</name>
        <description>Logs all non 200 (OK) server responses.</description>
        <author>Tasos "Zapotek" Laskos &lt;tasos.laskos@arachni-scanner.com&gt;</author>
        <version>0.2.1</version>
        <shortname>interesting_responses</shortname>
      </check>
      <digest>680817867</digest>
      <references>
        <reference title="w3.org" url="http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html"/>
      </references>
      <vector>
        <class>Arachni::Element::Server</class>
        <type>server</type>
        <url>http://elearnix.org/.admin</url>
        <action>http://elearnix.org/.admin</action>
      </vector>
      <variations>
        <variation>
          <vector/>
          <remarks/>
          <page>
            <body>Invalid URI /.admin</body>
            <request>
              <url>http://elearnix.org/.admin</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET /.admin HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/.admin</url>
              <code>403</code>
              <ip_address>31.220.16.186</ip_address>
              <time>4.2526</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:43 GMT"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Content-Type" value="text/plain"/>
                <header name="Content-Length" value="19"/>
              </headers>
              <body>Invalid URI /.admin</body>
              <raw_headers>HTTP/1.1 403 Forbidden&#xD;
Date: Tue, 07 Jun 2016 13:37:43 GMT&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Content-Type: text/plain&#xD;
Content-Length: 19&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/.admin</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>HTTP/1.1 403 Forbidden</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>E-mail address disclosure</name>
      <description>
Email addresses are typically found on "Contact us" pages, however, they can also
be found within scripts or code comments of the application. They are used to
provide a legitimate means of contacting an organisation.

As one of the initial steps in information gathering, cyber-criminals will spider
a website and using automated methods collect as many email addresses as possible,
that they may then use in a social engineering attack.

Using the same automated methods, Arachni was able to detect one or more email
addresses that were stored within the affected page.
</description>
      <remedy_guidance>E-mail addresses should be presented in such
                    a way that it is hard to process them automatically.</remedy_guidance>
      <remedy_code/>
      <severity>informational</severity>
      <check>
        <name>E-mail address</name>
        <description>Greps pages for disclosed e-mail addresses.</description>
        <author>Tasos "Zapotek" Laskos &lt;tasos.laskos@arachni-scanner.com&gt;</author>
        <version>0.2.1</version>
        <shortname>emails</shortname>
      </check>
      <cwe>200</cwe>
      <digest>4057954726</digest>
      <references/>
      <vector>
        <class>Arachni::Element::Body</class>
        <type>body</type>
        <url>http://elearnix.org/</url>
        <action>http://elearnix.org/</action>
      </vector>
      <variations>
        <variation>
          <vector/>
          <remarks/>
          <page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature>[A-Z0-9._%+-]+(?:@|\s*\[at\]\s*)[A-Z0-9.-]+(?:\.|\s*\[dot\]\s*)[A-Z]{2,4}</signature>
          <proof>csapda@web-server.hu</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
        <variation>
          <vector/>
          <remarks/>
          <page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature>[A-Z0-9._%+-]+(?:@|\s*\[at\]\s*)[A-Z0-9.-]+(?:\.|\s*\[dot\]\s*)[A-Z]{2,4}</signature>
          <proof>csapda@astrohost.com</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Interesting response</name>
      <description>
The server responded with a non 200 (OK) nor 404 (Not Found) status code.
This is a non-issue, however exotic HTTP response status codes can provide useful
insights into the behavior of the web application and assist with the penetration test.
</description>
      <remedy_guidance/>
      <remedy_code/>
      <severity>informational</severity>
      <check>
        <name>Interesting responses</name>
        <description>Logs all non 200 (OK) server responses.</description>
        <author>Tasos "Zapotek" Laskos &lt;tasos.laskos@arachni-scanner.com&gt;</author>
        <version>0.2.1</version>
        <shortname>interesting_responses</shortname>
      </check>
      <digest>710586659</digest>
      <references>
        <reference title="w3.org" url="http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html"/>
      </references>
      <vector>
        <class>Arachni::Element::Server</class>
        <type>server</type>
        <url>http://elearnix.org/.svn/all-wcprops</url>
        <action>http://elearnix.org/.svn/all-wcprops</action>
      </vector>
      <variations>
        <variation>
          <vector/>
          <remarks/>
          <page>
            <body>Invalid URI /.svn/all-wcprops</body>
            <request>
              <url>http://elearnix.org/.svn/all-wcprops</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET /.svn/all-wcprops HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/.svn/all-wcprops</url>
              <code>403</code>
              <ip_address>31.220.16.186</ip_address>
              <time>1.4663</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:44 GMT"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Content-Type" value="text/plain"/>
                <header name="Content-Length" value="29"/>
              </headers>
              <body>Invalid URI /.svn/all-wcprops</body>
              <raw_headers>HTTP/1.1 403 Forbidden&#xD;
Date: Tue, 07 Jun 2016 13:37:44 GMT&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Content-Type: text/plain&#xD;
Content-Length: 29&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/.svn/all-wcprops</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
            <request>
              <url>http://elearnix.org/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: elearnix.org&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://elearnix.org/</url>
              <code>200</code>
              <ip_address>31.220.16.186</ip_address>
              <time>0.9839</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Date" value="Tue, 07 Jun 2016 13:37:38 GMT"/>
                <header name="Cache-Control" value="no-cache, no-store, must-revalidate"/>
                <header name="Pragma" value="no-cache"/>
                <header name="Expires" value="0"/>
                <header name="Server" value="Apache/2.2.16 (Debian)"/>
                <header name="Content-Length" value="6557"/>
                <header name="Connection" value="close"/>
              </headers>
              <body>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Visitor anti-robot validation&lt;/title&gt;
        &lt;meta charset="UTF-8" /&gt;
        &lt;meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /&gt;
        &lt;link rel="stylesheet" type="text/css" href="/css/style.css" /&gt;

        &lt;meta http-equiv="content-type" content="text/html; charset=utf-8" /&gt;
&lt;meta name="robots" content="noindex, nofollow" /&gt;
&lt;meta name="keywords" content="joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal" /&gt;
&lt;meta name="description" content="Joomla!" /&gt;
&lt;meta name="generator" content="Joomla! 1.5 - Open Source Content Management" /&gt;
&lt;meta name="generator" content="WordPress 2.5" /&gt;



    &lt;/head&gt;
    &lt;body&gt;

        &lt;div class="container"&gt;
            &lt;div&gt;
                &lt;h1&gt;Dear visitor&lt;/h1&gt;
                &lt;p&gt;To reach the website securely, please fill in the characters shown below.&lt;/p&gt;
                &lt;p&gt;&lt;strong&gt;&lt;/strong&gt;&lt;/p&gt;
            &lt;/div&gt;
            &lt;div class="left"&gt;
                &lt;img src="/img/logo.png" alt="" /&gt;
            &lt;/div&gt;
            &lt;div class="right"&gt;
                &lt;form method="post" action="/verify.php"&gt;
                    &lt;script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC"&gt;&lt;/script&gt;

	&lt;noscript&gt;
  		&lt;iframe src="http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC" height="300" width="500" frameborder="0"&gt;&lt;/iframe&gt;&lt;br/&gt;
  		&lt;textarea name="recaptcha_challenge_field" rows="3" cols="40"&gt;&lt;/textarea&gt;
  		&lt;input type="hidden" name="recaptcha_response_field" value="manual_challenge"/&gt;
	&lt;/noscript&gt;
                    &lt;input type="hidden" name="origin_url" value="http://elearnix.org/" /&gt;
                    &lt;input type="submit" value="Delist" /&gt;
                &lt;/form&gt;
            &lt;/div&gt;	
            &lt;div class="clear"&gt;&lt;/div&gt;
            &lt;div&gt;
                &lt;h1&gt;Why is it necessary?&lt;/h1&gt;
                &lt;p&gt;Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.&lt;/p&gt;
                &lt;p&gt;We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.&lt;/p&gt;
                &lt;p&gt;Thank you.&lt;/p&gt;
                &lt;hr/&gt;
                &lt;pre&gt;
Remote address: 125.18.48.110
URI: /
Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0
                &lt;/pre&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;

    &lt;!--
&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;
&lt;a href='index.php?option=com_dshop'&gt;This contact form is about /components/com_dshop/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jobprofile'&gt;This contact form is about /components/com_jobprofile/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_fckeditor'&gt;This contact form is about /components/com_fckeditor/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_acajoom'&gt;This contact form is about /components/com_acajoom/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_content'&gt;This contact form is about /components/com_content/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_phocagallery'&gt;This contact form is about /components/com_phocagallery/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_mailto'&gt;This contact form is about /components/com_mailto/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_qcontacts'&gt;This contact form is about /components/com_qcontacts/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_jevents'&gt;This contact form is about /components/com_jevents/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_contact'&gt;This contact form is about /components/com_contact/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_search'&gt;This contact form is about /components/com_search/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_virtuemart'&gt;This contact form is about /components/com_virtuemart/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_google'&gt;This contact form is about /components/com_google/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=com_oziogallery2'&gt;This contact form is about /components/com_oziogallery2/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'&gt;This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=FCKeditor - Uploaders Tests'&gt;This contact form is about /components/FCKeditor - Uploaders Tests/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin'&gt;This contact form is about /components/phpmyadmin/ &lt;/a&gt;&lt;br&gt;
&lt;a href='index.php?option=phpmyadmin2'&gt;This contact form is about /components/phpmyadmin2/ &lt;/a&gt;&lt;br&gt;

&lt;a href="demo/GHH%20-%20Haxplorer/1.php"&gt;GHDB Signature #833 (filetype:php HAXPLORER &amp;quot;Server Files Browser&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Ping/php-ping.php"&gt;GHDB Signature #733 (&amp;quot;Enter ip&amp;quot; inurl:&amp;quot;php-ping.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHP%20Shell/phpshell.php"&gt;GHDB Signature #365 (intitle:&amp;quot;PHP Shell *&amp;quot; &amp;quot;Enable stderr&amp;quot; filetype:php)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php"&gt;GHDB Signature #935 (inurl:&amp;quot;install/install.php&amp;quot;)&lt;/a&gt;&lt;br&gt;
&lt;br&gt;
&lt;a href="demo/GHH%20-%20PHPFM/index.php"&gt;GHDB Signature #361 (&amp;quot;Powered by PHPFM&amp;quot; filetype:php -username)
&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20PhpSysInfo/index.php"&gt;GHDB Signature #161 (inurl:phpSysInfo/ &amp;quot;created by phpsysinfo&amp;quot;)&lt;/a&gt;&lt;br&gt;&lt;br&gt;
&lt;a href="demo/GHH%20-%20SquirrelMail/src/login.php"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7"&gt;GHDB Signature #1013 (&amp;quot;SquirrelMail version 1.4.4&amp;quot; inurl:src ext:php)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .mdb/admin.mdb"&gt;GHDB Signature #162 (allinurl: admin mdb)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - .sql/create.sql"&gt;GHDB Signature #1064 (filetype:sql ("passwd values" | "password values" | "pass values" ))&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt"&gt;GHDB Signature #937 (filetype:blt "buddylist")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - File Upload Manager/"&gt;GHDB Signature #734 ("File Upload Manager v1.3" "rename to")&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passlist.txt/passlist.txt"&gt;GHDB Signature #58 (inurl:passlist.txt)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - passwd.txt/passwd.txt"&gt;GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt&lt;/a&gt; &lt;br&gt;&lt;br&gt;
&lt;a href="/demo/GHH v1.1 - WebUtil 2.7/webutil.pl"&gt;GHDB Signature #769 (inurl:webutil.pl)&lt;/a&gt; &lt;br&gt;&lt;br&gt;
--&gt;


    &lt;!--
&lt;a href="mailto:csapda@web-server.hu"&gt;&lt;/a&gt;
&lt;a href="mailto:csapda@astrohost.com"&gt;&lt;/a&gt;
--&gt;

&lt;/html&gt;

</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Date: Tue, 07 Jun 2016 13:37:38 GMT&#xD;
Cache-Control: no-cache, no-store, must-revalidate&#xD;
Pragma: no-cache&#xD;
Expires: 0&#xD;
Server: Apache/2.2.16 (Debian)&#xD;
Content-Length: 6557&#xD;
Connection: close&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://elearnix.org/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>HTTP/1.1 403 Forbidden</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
  </issues>
  <plugins>
    <healthmap>
      <name>Health map</name>
      <description>Generates a simple list of safe/unsafe URLs.</description>
      <results>
        <map>
          <with_issues>http://elearnix.org/</with_issues>
          <with_issues>http://elearnix.org/.adm</with_issues>
          <with_issues>http://elearnix.org/.admin</with_issues>
          <with_issues>http://elearnix.org/.git/HEAD</with_issues>
          <with_issues>http://elearnix.org/.svn/all-wcprops</with_issues>
          <with_issues>http://elearnix.org/verify.php</with_issues>
        </map>
        <total>6</total>
        <with_issues>6</with_issues>
        <without_issues>0</without_issues>
        <issue_percentage>100</issue_percentage>
      </results>
    </healthmap>
  </plugins>
</report>
"""
