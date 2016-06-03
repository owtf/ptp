report_high= r"""
{
  "version" : "1.2.1",
  "options" : {
    "input" : {
      "values" : {},
      "default_values" : {
        "(?i-mx:name)" : "arachni_name",
        "(?i-mx:user)" : "arachni_user",
        "(?i-mx:usr)" : "arachni_user",
        "(?i-mx:pass)" : "5543!%arachni_secret",
        "(?i-mx:txt)" : "arachni_text",
        "(?i-mx:num)" : "132",
        "(?i-mx:amount)" : "100",
        "(?i-mx:mail)" : "arachni@email.gr",
        "(?i-mx:account)" : "12",
        "(?i-mx:id)" : "1"
      },
      "without_defaults" : false,
      "force" : false
    },
    "audit" : {
      "parameter_values" : true,
      "exclude_vector_patterns" : [],
      "include_vector_patterns" : [],
      "link_templates" : [],
      "links" : true,
      "forms" : true,
      "cookies" : true,
      "jsons" : true,
      "xmls" : true
    },
    "browser_cluster" : {
      "wait_for_elements" : {},
      "pool_size" : 6,
      "job_timeout" : 25,
      "worker_time_to_live" : 100,
      "ignore_images" : false,
      "screen_width" : 1600,
      "screen_height" : 1200
    },
    "session" : {},
    "http" : {
      "user_agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
      "request_timeout" : 10000,
      "request_redirect_limit" : 5,
      "request_concurrency" : 20,
      "request_queue_size" : 100,
      "request_headers" : {},
      "response_max_size" : 500000,
      "cookies" : {}
    },
    "scope" : {
      "redundant_path_patterns" : {},
      "dom_depth_limit" : 5,
      "exclude_path_patterns" : [],
      "exclude_content_patterns" : [],
      "include_path_patterns" : [],
      "restrict_paths" : [],
      "extend_paths" : [],
      "url_rewrites" : {}
    },
    "datastore" : {
      "report_path" : "/root/Desktop/arachni.afr"
    },
    "checks" : [
      "htaccess_limit",
      "insecure_client_access_policy",
      "interesting_responses",
      "insecure_cross_domain_policy_access",
      "insecure_cross_domain_policy_headers",
      "backdoors",
      "directory_listing",
      "origin_spoof_access_restriction_bypass",
      "backup_directories",
      "http_put",
      "xst",
      "localstart_asp",
      "common_admin_interfaces",
      "common_files",
      "common_directories",
      "webdav",
      "backup_files",
      "captcha",
      "private_ip",
      "http_only_cookies",
      "x_frame_options",
      "unencrypted_password_forms",
      "insecure_cookies",
      "password_autocomplete",
      "cookie_set_for_parent_domain",
      "insecure_cors_policy",
      "credit_card",
      "ssn",
      "html_objects",
      "form_upload",
      "mixed_resource",
      "hsts",
      "cvs_svn_users",
      "emails",
      "allowed_methods",
      "sql_injection",
      "code_injection_timing",
      "no_sql_injection",
      "session_fixation",
      "path_traversal",
      "unvalidated_redirect",
      "trainer",
      "os_cmd_injection_timing",
      "response_splitting",
      "xxe",
      "file_inclusion",
      "csrf",
      "xss_event",
      "xss_path",
      "source_code_disclosure",
      "rfi",
      "xss_dom_script_context",
      "no_sql_injection_differential",
      "unvalidated_redirect_dom",
      "sql_injection_differential",
      "xpath_injection",
      "ldap_injection",
      "xss_tag",
      "xss_script_context",
      "xss",
      "code_injection_php_input_wrapper",
      "xss_dom",
      "os_cmd_injection",
      "code_injection",
      "sql_injection_timing",
      "xss_dom_inputs"
    ],
    "platforms" : [],
    "plugins" : {},
    "no_fingerprinting" : false,
    "authorized_by" : null,
    "url" : "http://elearnix.org/"
  },
  "sitemap" : {
    "http://elearnix.org/" : 200
  },
  "start_datetime" : "2016-06-07 09:37:38 -0400",
  "finish_datetime" : "2016-06-07 09:55:29 -0400",
  "delta_time" : "00:17:51",
  "issues" : [
    {
      "name" : "Cross-Site Request Forgery",
      "description" : "\nIn the majority of today's web applications, clients are required to submit forms\nwhich can perform sensitive operations.\n\nAn example of such a form being used would be when an administrator wishes to\ncreate a new user for the application.\n\nIn the simplest version of the form, the administrator would fill-in:\n\n* Name\n* Password\n* Role (level of access)\n\nContinuing with this example, Cross Site Request Forgery (CSRF) would occur when\nthe administrator is tricked into clicking on a link, which if logged into the\napplication, would automatically submit the form without any further interaction.\n\nCyber-criminals will look for sites where sensitive functions are performed in\nthis manner and then craft malicious requests that will be used against clients\nvia a social engineering attack.\n\nThere are 3 things that are required for a CSRF attack to occur:\n\n1. The form must perform some sort of sensitive action.\n2. The victim (the administrator the example above) must have an active session.\n3. Most importantly, all parameter values must be **known** or **guessable**.\n\nArachni discovered that all parameters within the form were known or predictable\nand therefore the form could be vulnerable to CSRF.\n\n_Manual verification may be required to check whether the submission will then\nperform a sensitive action, such as reset a password, modify user profiles, post\ncontent on a forum, etc._\n",
      "references" : {
        "Wikipedia" : "http://en.wikipedia.org/wiki/Cross-site_request_forgery",
        "OWASP" : "https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)",
        "CGI Security" : "http://www.cgisecurity.com/csrf-faq.html"
      },
      "tags" : [
        "csrf",
        "rdiff",
        "form",
        "token"
      ],
      "severity" : "high",
      "check" : {
        "name" : "CSRF",
        "description" : "\nIt uses differential analysis to determine which forms affect business logic and\nchecks them for lack of anti-CSRF tokens.\n\n(Works best with a valid session.)\n",
        "elements" : [
          "form"
        ],
        "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com> ",
        "version" : "0.3.5",
        "shortname" : "csrf"
      },
      "vector" : {
        "class" : "Arachni::Element::Form",
        "type" : "form",
        "url" : "http://elearnix.org/",
        "inputs" : {
          "recaptcha_challenge_field" : "",
          "recaptcha_response_field" : "manual_challenge",
          "origin_url" : "http://elearnix.org/"
        },
        "action" : "http://elearnix.org/verify.php",
        "method" : "post",
        "source" : "<form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\">\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\">\n                    <input type=\"submit\" value=\"Delist\">\n                </form>",
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Form",
            "inputs" : {
              "recaptcha_challenge_field" : "",
              "recaptcha_response_field" : "manual_challenge",
              "origin_url" : "http://elearnix.org/"
            },
            "method" : "post"
          },
          "trusted" : true,
          "proof" : "<form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\">\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\">\n                    <input type=\"submit\" value=\"Delist\">\n                </form>",
          "page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "response" : {
            "url" : "http://elearnix.org/",
            "code" : 200,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:38 GMT",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Server" : "Apache/2.2.16 (Debian)",
              "Content-Length" : "6557",
              "Connection" : "close"
            },
            "headers_string" : "HTTP/1.1 200 OK\r\nDate: Tue, 07 Jun 2016 13:37:38 GMT\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nServer: Apache/2.2.16 (Debian)\r\nContent-Length: 6557\r\nConnection: close\r\n\r\n",
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "time" : 0.983864,
            "app_time" : 0.6131759999999999,
            "total_time" : 0.983864,
            "return_code" : "ok",
            "return_message" : "No error"
          },
          "request" : {
            "url" : "http://elearnix.org/",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET / HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        }
      ],
      "cwe" : 352,
      "remedy_guidance" : "\nBased on the risk (determined by manual verification) of whether the form submission\nperforms a sensitive action, the addition of anti-CSRF tokens may be required.\n\nThese tokens can be configured in such a way that each session generates a new\nanti-CSRF token or such that each individual request requires a new token.\n\nIt is important that the server track and maintain the status of each token (in\norder to reject requests accompanied by invalid ones) and therefore prevent\ncyber-criminals from knowing, guessing or reusing them.\n\n_For examples of framework specific remediation options, please refer to the references._\n",
      "cwe_url" : "http://cwe.mitre.org/data/definitions/352.html",
      "digest" : 1606559286
    },
    {
      "name" : "HTTP TRACE",
      "description" : "\nThe `TRACE` HTTP method allows a client so send a request to the server, and\nhave the same request then send back in the server's response. This allows the\nclient to determine if the server is receiving the request as expected or if\nspecific parts of the request are not arriving as expected.\nFor example incorrect encoding or a load balancer has filtered or changed a value.\nOn many default installations the `TRACE` method is still enabled.\n\nWhile not vulnerable by itself, it does provide a method for cyber-criminals to\nbypass the `HTTPOnly` cookie flag, and therefore could allow a XSS attack to\nsuccessfully access a session token.\n\nArachni has discovered that the affected page permits the HTTP `TRACE` method.\n",
      "references" : {
        "CAPEC" : "http://capec.mitre.org/data/definitions/107.html",
        "OWASP" : "http://www.owasp.org/index.php/Cross_Site_Tracing"
      },
      "tags" : [
        "xst",
        "methods",
        "trace",
        "server"
      ],
      "severity" : "medium",
      "check" : {
        "name" : "XST",
        "description" : "Sends an HTTP TRACE request and checks if it succeeded.",
        "elements" : [
          "server"
        ],
        "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com>",
        "version" : "0.1.7",
        "shortname" : "xst"
      },
      "vector" : {
        "class" : "Arachni::Element::Server",
        "type" : "server",
        "url" : "http://elearnix.org/",
        "inputs" : null,
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Server"
          },
          "trusted" : true,
          "proof" : "HTTP/1.1 200 OK",
          "page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "response" : {
            "url" : "http://elearnix.org/",
            "code" : 200,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:43 GMT",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Server" : "Apache/2.2.16 (Debian)",
              "Content-Length" : "6557",
              "Connection" : "close"
            },
            "headers_string" : "HTTP/1.1 200 OK\r\nDate: Tue, 07 Jun 2016 13:37:43 GMT\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nServer: Apache/2.2.16 (Debian)\r\nContent-Length: 6557\r\nConnection: close\r\n\r\n",
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "time" : 2.353672,
            "app_time" : 0.969563,
            "total_time" : 2.353672,
            "return_code" : "ok",
            "return_message" : "No error",
            "status_line" : "HTTP/1.1 200 OK"
          },
          "request" : {
            "url" : "http://elearnix.org/",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "TRACE / HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "trace"
          }
        }
      ],
      "cwe" : 693,
      "remedy_guidance" : "\nThe HTTP `TRACE` method is normally not required within production sites and\nshould therefore be disabled.\n\nDepending on the function being performed by the web application, the risk\nlevel can start low and increase as more functionality is implemented.\n\nThe remediation is typically a very simple configuration change and in most cases\nwill not have any negative impact on the server or application.\n",
      "cwe_url" : "http://cwe.mitre.org/data/definitions/693.html",
      "digest" : 1441521763
    },
    {
      "name" : "Missing 'X-Frame-Options' header",
      "description" : "\nClickjacking (User Interface redress attack, UI redress attack, UI redressing)\nis a malicious technique of tricking a Web user into clicking on something different\nfrom what the user perceives they are clicking on, thus potentially revealing\nconfidential information or taking control of their computer while clicking on\nseemingly innocuous web pages.\n\nThe server didn't return an `X-Frame-Options` header which means that this website\ncould be at risk of a clickjacking attack.\n\nThe `X-Frame-Options` HTTP response header can be used to indicate whether or not\na browser should be allowed to render a page inside a frame or iframe. Sites can\nuse this to avoid clickjacking attacks, by ensuring that their content is not\nembedded into other sites.\n",
      "references" : {
        "MDN" : "https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options",
        "RFC" : "http://tools.ietf.org/html/rfc7034",
        "OWASP" : "https://www.owasp.org/index.php/Clickjacking"
      },
      "tags" : [],
      "severity" : "low",
      "check" : {
        "name" : "Missing X-Frame-Options header",
        "description" : "Checks the host for a missing `X-Frame-Options` header.",
        "author" : "Tasos Laskos <tasos.laskos@arachni-scanner.com>",
        "version" : "0.1.1",
        "elements" : [
          "server"
        ],
        "shortname" : "x_frame_options"
      },
      "vector" : {
        "class" : "Arachni::Element::Server",
        "type" : "server",
        "url" : "http://elearnix.org/",
        "inputs" : null,
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Server"
          },
          "trusted" : true,
          "proof" : "HTTP/1.1 200 OK\r\nDate: Tue, 07 Jun 2016 13:37:38 GMT\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nServer: Apache/2.2.16 (Debian)\r\nContent-Length: 6557\r\nConnection: close\r\n\r\n",
          "page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "response" : {
            "url" : "http://elearnix.org/",
            "code" : 200,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:38 GMT",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Server" : "Apache/2.2.16 (Debian)",
              "Content-Length" : "6557",
              "Connection" : "close"
            },
            "headers_string" : "HTTP/1.1 200 OK\r\nDate: Tue, 07 Jun 2016 13:37:38 GMT\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nServer: Apache/2.2.16 (Debian)\r\nContent-Length: 6557\r\nConnection: close\r\n\r\n",
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "time" : 0.983864,
            "app_time" : 0.6131759999999999,
            "total_time" : 0.983864,
            "return_code" : "ok",
            "return_message" : "No error"
          },
          "request" : {
            "url" : "http://elearnix.org/",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET / HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        }
      ],
      "cwe" : 693,
      "remedy_guidance" : "\nConfigure your web server to include an X-Frame-Options header.\n",
      "cwe_url" : "http://cwe.mitre.org/data/definitions/693.html",
      "digest" : 730375711
    },
    {
      "name" : "Interesting response",
      "description" : "\nThe server responded with a non 200 (OK) nor 404 (Not Found) status code.\nThis is a non-issue, however exotic HTTP response status codes can provide useful\ninsights into the behavior of the web application and assist with the penetration test.\n",
      "references" : {
        "w3.org" : "http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html"
      },
      "tags" : [
        "interesting",
        "response",
        "server"
      ],
      "severity" : "informational",
      "check" : {
        "name" : "Interesting responses",
        "description" : "Logs all non 200 (OK) server responses.",
        "elements" : [
          "server"
        ],
        "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com>",
        "version" : "0.2.1",
        "max_issues" : 25,
        "shortname" : "interesting_responses"
      },
      "vector" : {
        "class" : "Arachni::Element::Server",
        "type" : "server",
        "url" : "http://elearnix.org/.adm",
        "inputs" : null,
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Server"
          },
          "trusted" : true,
          "proof" : "HTTP/1.1 403 Forbidden",
          "page" : {
            "body" : "Invalid URI /.adm",
            "dom" : {
              "url" : "http://elearnix.org/.adm",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "response" : {
            "url" : "http://elearnix.org/.adm",
            "code" : 403,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:49 GMT",
              "Server" : "Apache/2.2.16 (Debian)",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Content-Type" : "text/plain",
              "Content-Length" : "17"
            },
            "headers_string" : "HTTP/1.1 403 Forbidden\r\nDate: Tue, 07 Jun 2016 13:37:49 GMT\r\nServer: Apache/2.2.16 (Debian)\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nContent-Type: text/plain\r\nContent-Length: 17\r\n\r\n",
            "body" : "Invalid URI /.adm",
            "time" : 7.42406,
            "app_time" : 7.223271,
            "total_time" : 7.42406,
            "return_code" : "ok",
            "return_message" : "No error",
            "status_line" : "HTTP/1.1 403 Forbidden"
          },
          "request" : {
            "url" : "http://elearnix.org/.adm",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET /.adm HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        }
      ],
      "digest" : 2686368332
    },
    {
      "name" : "CAPTCHA protected form",
      "description" : "\nTo prevent the automated abuse of a page, applications can implement what is\nknown as a CAPTCHA.\n\nThese are used to ensure human interaction with the application and are often\nused on forms where the application conducts sensitive actions. These typically\ninclude user registration, or submitting emails via \"Contact Us\" pages etc.\n\nArachni has flagged this not as a vulnerability, but as a prompt for the\npenetration tester to conduct further manual testing on the CAPTCHA function, as\nArachni cannot audit CAPTCHA protected forms.\n\nTesting for insecurely implemented CAPTCHA is a manual process, and an insecurely\nimplemented CAPTCHA could allow a cyber-criminal a means to abuse these sensitive\nactions.\n",
      "references" : {},
      "tags" : [],
      "severity" : "informational",
      "check" : {
        "name" : "CAPTCHA",
        "description" : "Greps pages for forms with CAPTCHAs.",
        "elements" : [
          "form"
        ],
        "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com>",
        "version" : "0.2",
        "max_issues" : 25,
        "shortname" : "captcha"
      },
      "vector" : {
        "class" : "Arachni::Element::Form",
        "type" : "form",
        "url" : "http://elearnix.org/",
        "inputs" : {
          "recaptcha_challenge_field" : "",
          "recaptcha_response_field" : "manual_challenge",
          "origin_url" : "http://elearnix.org/"
        },
        "action" : "http://elearnix.org/verify.php",
        "method" : "post",
        "source" : "<form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\">\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\">\n                    <input type=\"submit\" value=\"Delist\">\n                </form>",
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Form",
            "inputs" : {
              "recaptcha_challenge_field" : "",
              "recaptcha_response_field" : "manual_challenge",
              "origin_url" : "http://elearnix.org/"
            },
            "method" : "post"
          },
          "trusted" : true,
          "proof" : "<form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\">\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\">\n                    <input type=\"submit\" value=\"Delist\">\n                </form>",
          "page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "signature" : "captcha",
          "response" : {
            "url" : "http://elearnix.org/",
            "code" : 200,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:38 GMT",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Server" : "Apache/2.2.16 (Debian)",
              "Content-Length" : "6557",
              "Connection" : "close"
            },
            "headers_string" : "HTTP/1.1 200 OK\r\nDate: Tue, 07 Jun 2016 13:37:38 GMT\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nServer: Apache/2.2.16 (Debian)\r\nContent-Length: 6557\r\nConnection: close\r\n\r\n",
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "time" : 0.983864,
            "app_time" : 0.6131759999999999,
            "total_time" : 0.983864,
            "return_code" : "ok",
            "return_message" : "No error"
          },
          "request" : {
            "url" : "http://elearnix.org/",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET / HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        }
      ],
      "remedy_guidance" : "\nAlthough no remediation may be required based on this finding alone, manual\ntesting should ensure that:\n\n1. The server keeps track of CAPTCHA tokens in use and has the token terminated\n    after its first use or after a period of time. Therefore preventing replay attacks.\n2. The CAPTCHA answer is not hidden in plain text within the response that is\n    sent to the client.\n3. The CAPTCHA image should not be weak and easily solved.\n",
      "digest" : 1495184166
    },
    {
      "name" : "Interesting response",
      "description" : "\nThe server responded with a non 200 (OK) nor 404 (Not Found) status code.\nThis is a non-issue, however exotic HTTP response status codes can provide useful\ninsights into the behavior of the web application and assist with the penetration test.\n",
      "references" : {
        "w3.org" : "http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html"
      },
      "tags" : [
        "interesting",
        "response",
        "server"
      ],
      "severity" : "informational",
      "check" : {
        "name" : "Interesting responses",
        "description" : "Logs all non 200 (OK) server responses.",
        "elements" : [
          "server"
        ],
        "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com>",
        "version" : "0.2.1",
        "max_issues" : 25,
        "shortname" : "interesting_responses"
      },
      "vector" : {
        "class" : "Arachni::Element::Server",
        "type" : "server",
        "url" : "http://elearnix.org/.git/HEAD",
        "inputs" : null,
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Server"
          },
          "trusted" : true,
          "proof" : "HTTP/1.1 403 Forbidden",
          "page" : {
            "body" : "Invalid URI /.git/HEAD",
            "dom" : {
              "url" : "http://elearnix.org/.git/HEAD",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "response" : {
            "url" : "http://elearnix.org/.git/HEAD",
            "code" : 403,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:49 GMT",
              "Server" : "Apache/2.2.16 (Debian)",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Content-Type" : "text/plain",
              "Content-Length" : "22"
            },
            "headers_string" : "HTTP/1.1 403 Forbidden\r\nDate: Tue, 07 Jun 2016 13:37:49 GMT\r\nServer: Apache/2.2.16 (Debian)\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nContent-Type: text/plain\r\nContent-Length: 22\r\n\r\n",
            "body" : "Invalid URI /.git/HEAD",
            "time" : 7.371221,
            "app_time" : 7.172712,
            "total_time" : 7.371221,
            "return_code" : "ok",
            "return_message" : "No error",
            "status_line" : "HTTP/1.1 403 Forbidden"
          },
          "request" : {
            "url" : "http://elearnix.org/.git/HEAD",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET /.git/HEAD HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        }
      ],
      "digest" : 3783498189
    },
    {
      "name" : "Interesting response",
      "description" : "\nThe server responded with a non 200 (OK) nor 404 (Not Found) status code.\nThis is a non-issue, however exotic HTTP response status codes can provide useful\ninsights into the behavior of the web application and assist with the penetration test.\n",
      "references" : {
        "w3.org" : "http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html"
      },
      "tags" : [
        "interesting",
        "response",
        "server"
      ],
      "severity" : "informational",
      "check" : {
        "name" : "Interesting responses",
        "description" : "Logs all non 200 (OK) server responses.",
        "elements" : [
          "server"
        ],
        "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com>",
        "version" : "0.2.1",
        "max_issues" : 25,
        "shortname" : "interesting_responses"
      },
      "vector" : {
        "class" : "Arachni::Element::Server",
        "type" : "server",
        "url" : "http://elearnix.org/.admin",
        "inputs" : null,
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Server"
          },
          "trusted" : true,
          "proof" : "HTTP/1.1 403 Forbidden",
          "page" : {
            "body" : "Invalid URI /.admin",
            "dom" : {
              "url" : "http://elearnix.org/.admin",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "response" : {
            "url" : "http://elearnix.org/.admin",
            "code" : 403,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:43 GMT",
              "Server" : "Apache/2.2.16 (Debian)",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Content-Type" : "text/plain",
              "Content-Length" : "19"
            },
            "headers_string" : "HTTP/1.1 403 Forbidden\r\nDate: Tue, 07 Jun 2016 13:37:43 GMT\r\nServer: Apache/2.2.16 (Debian)\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nContent-Type: text/plain\r\nContent-Length: 19\r\n\r\n",
            "body" : "Invalid URI /.admin",
            "time" : 4.252556,
            "app_time" : 4.052006,
            "total_time" : 4.252556,
            "return_code" : "ok",
            "return_message" : "No error",
            "status_line" : "HTTP/1.1 403 Forbidden"
          },
          "request" : {
            "url" : "http://elearnix.org/.admin",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET /.admin HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        }
      ],
      "digest" : 680817867
    },
    {
      "name" : "E-mail address disclosure",
      "description" : "\nEmail addresses are typically found on \"Contact us\" pages, however, they can also\nbe found within scripts or code comments of the application. They are used to\nprovide a legitimate means of contacting an organisation.\n\nAs one of the initial steps in information gathering, cyber-criminals will spider\na website and using automated methods collect as many email addresses as possible,\nthat they may then use in a social engineering attack.\n\nUsing the same automated methods, Arachni was able to detect one or more email\naddresses that were stored within the affected page.\n",
      "references" : {},
      "tags" : [],
      "severity" : "informational",
      "check" : {
        "name" : "E-mail address",
        "description" : "Greps pages for disclosed e-mail addresses.",
        "elements" : [
          "body"
        ],
        "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com>",
        "version" : "0.2.1",
        "max_issues" : 25,
        "shortname" : "emails"
      },
      "vector" : {
        "class" : "Arachni::Element::Body",
        "type" : "body",
        "url" : "http://elearnix.org/",
        "inputs" : null,
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Body"
          },
          "trusted" : true,
          "proof" : "csapda@web-server.hu",
          "page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "signature" : "[A-Z0-9._%+-]+(?:@|\\s*\\[at\\]\\s*)[A-Z0-9.-]+(?:\\.|\\s*\\[dot\\]\\s*)[A-Z]{2,4}",
          "response" : {
            "url" : "http://elearnix.org/",
            "code" : 200,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:38 GMT",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Server" : "Apache/2.2.16 (Debian)",
              "Content-Length" : "6557",
              "Connection" : "close"
            },
            "headers_string" : "HTTP/1.1 200 OK\r\nDate: Tue, 07 Jun 2016 13:37:38 GMT\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nServer: Apache/2.2.16 (Debian)\r\nContent-Length: 6557\r\nConnection: close\r\n\r\n",
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "time" : 0.983864,
            "app_time" : 0.6131759999999999,
            "total_time" : 0.983864,
            "return_code" : "ok",
            "return_message" : "No error"
          },
          "request" : {
            "url" : "http://elearnix.org/",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET / HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        },
        {
          "vector" : {
            "class" : "Arachni::Element::Body"
          },
          "trusted" : true,
          "proof" : "csapda@astrohost.com",
          "page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "signature" : "[A-Z0-9._%+-]+(?:@|\\s*\\[at\\]\\s*)[A-Z0-9.-]+(?:\\.|\\s*\\[dot\\]\\s*)[A-Z]{2,4}",
          "response" : {
            "url" : "http://elearnix.org/",
            "code" : 200,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:38 GMT",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Server" : "Apache/2.2.16 (Debian)",
              "Content-Length" : "6557",
              "Connection" : "close"
            },
            "headers_string" : "HTTP/1.1 200 OK\r\nDate: Tue, 07 Jun 2016 13:37:38 GMT\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nServer: Apache/2.2.16 (Debian)\r\nContent-Length: 6557\r\nConnection: close\r\n\r\n",
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "time" : 0.983864,
            "app_time" : 0.6131759999999999,
            "total_time" : 0.983864,
            "return_code" : "ok",
            "return_message" : "No error"
          },
          "request" : {
            "url" : "http://elearnix.org/",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET / HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        }
      ],
      "cwe" : 200,
      "remedy_guidance" : "E-mail addresses should be presented in such\n                    a way that it is hard to process them automatically.",
      "cwe_url" : "http://cwe.mitre.org/data/definitions/200.html",
      "digest" : 4057954726
    },
    {
      "name" : "Interesting response",
      "description" : "\nThe server responded with a non 200 (OK) nor 404 (Not Found) status code.\nThis is a non-issue, however exotic HTTP response status codes can provide useful\ninsights into the behavior of the web application and assist with the penetration test.\n",
      "references" : {
        "w3.org" : "http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html"
      },
      "tags" : [
        "interesting",
        "response",
        "server"
      ],
      "severity" : "informational",
      "check" : {
        "name" : "Interesting responses",
        "description" : "Logs all non 200 (OK) server responses.",
        "elements" : [
          "server"
        ],
        "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com>",
        "version" : "0.2.1",
        "max_issues" : 25,
        "shortname" : "interesting_responses"
      },
      "vector" : {
        "class" : "Arachni::Element::Server",
        "type" : "server",
        "url" : "http://elearnix.org/.svn/all-wcprops",
        "inputs" : null,
        "affected_input_name" : null
      },
      "trusted" : true,
      "variation" : false,
      "variations" : [
        {
          "vector" : {
            "class" : "Arachni::Element::Server"
          },
          "trusted" : true,
          "proof" : "HTTP/1.1 403 Forbidden",
          "page" : {
            "body" : "Invalid URI /.svn/all-wcprops",
            "dom" : {
              "url" : "http://elearnix.org/.svn/all-wcprops",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "referring_page" : {
            "body" : "<html>\n    <head>\n        <title>Visitor anti-robot validation</title>\n        <meta charset=\"UTF-8\" />\n        <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\" />\n        <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />\n\n        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n<meta name=\"robots\" content=\"noindex, nofollow\" />\n<meta name=\"keywords\" content=\"joomla, Joomla, joomla 1.5, wordpress 2.5, Drupal\" />\n<meta name=\"description\" content=\"Joomla!\" />\n<meta name=\"generator\" content=\"Joomla! 1.5 - Open Source Content Management\" />\n<meta name=\"generator\" content=\"WordPress 2.5\" />\n\n\n\n    </head>\n    <body>\n\n        <div class=\"container\">\n            <div>\n                <h1>Dear visitor</h1>\n                <p>To reach the website securely, please fill in the characters shown below.</p>\n                <p><strong></strong></p>\n            </div>\n            <div class=\"left\">\n                <img src=\"/img/logo.png\" alt=\"\" />\n            </div>\n            <div class=\"right\">\n                <form method=\"post\" action=\"/verify.php\">\n                    <script type=\"text/javascript\" src=\"http://www.google.com/recaptcha/api/challenge?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\"></script>\n\n\t<noscript>\n  \t\t<iframe src=\"http://www.google.com/recaptcha/api/noscript?k=6LfRteUSAAAAAFQ4IlQQdjP_E7ek9ElCzSo5TDxC\" height=\"300\" width=\"500\" frameborder=\"0\"></iframe><br/>\n  \t\t<textarea name=\"recaptcha_challenge_field\" rows=\"3\" cols=\"40\"></textarea>\n  \t\t<input type=\"hidden\" name=\"recaptcha_response_field\" value=\"manual_challenge\"/>\n\t</noscript>\n                    <input type=\"hidden\" name=\"origin_url\" value=\"http://elearnix.org/\" />\n                    <input type=\"submit\" value=\"Delist\" />\n                </form>\n            </div>\t\n            <div class=\"clear\"></div>\n            <div>\n                <h1>Why is it necessary?</h1>\n                <p>Your IP address (125.18.48.110) has been blocked for security reason. Probably your IP address has been used for violation of server security rules before.</p>\n                <p>We have to make sure that this is not a malicious visit by an automated robot. Filling in the captcha is required to delist you IP address.</p>\n                <p>Thank you.</p>\n                <hr/>\n                <pre>\nRemote address: 125.18.48.110\nURI: /\nAgent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\n                </pre>\n            </div>\n        </div>\n    </body>\n\n    <!--\n<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>\n<a href='index.php?option=com_dshop'>This contact form is about /components/com_dshop/ </a><br>\n<a href='index.php?option=com_jobprofile'>This contact form is about /components/com_jobprofile/ </a><br>\n<a href='index.php?option=com_fckeditor'>This contact form is about /components/com_fckeditor/ </a><br>\n<a href='index.php?option=com_acajoom'>This contact form is about /components/com_acajoom/ </a><br>\n<a href='index.php?option=com_content'>This contact form is about /components/com_content/ </a><br>\n<a href='index.php?option=com_phocagallery'>This contact form is about /components/com_phocagallery/ </a><br>\n<a href='index.php?option=com_mailto'>This contact form is about /components/com_mailto/ </a><br>\n<a href='index.php?option=com_qcontacts'>This contact form is about /components/com_qcontacts/ </a><br>\n<a href='index.php?option=com_jevents'>This contact form is about /components/com_jevents/ </a><br>\n<a href='index.php?option=com_contact'>This contact form is about /components/com_contact/ </a><br>\n<a href='index.php?option=com_search'>This contact form is about /components/com_search/ </a><br>\n<a href='index.php?option=com_virtuemart'>This contact form is about /components/com_virtuemart/ </a><br>\n<a href='index.php?option=com_google'>This contact form is about /components/com_google/ </a><br>\n<a href='index.php?option=com_oziogallery2'>This contact form is about /components/com_oziogallery2/ </a><br>\n<a href='index.php?option=fckeditor/editor/filemanager/connectors/uploadtest.html'>This contact form is about /components/fckeditor/editor/filemanager/connectors/uploadtest.html/ </a><br>\n<a href='index.php?option=FCKeditor - Uploaders Tests'>This contact form is about /components/FCKeditor - Uploaders Tests/ </a><br>\n<a href='index.php?option=phpmyadmin'>This contact form is about /components/phpmyadmin/ </a><br>\n<a href='index.php?option=phpmyadmin2'>This contact form is about /components/phpmyadmin2/ </a><br>\n\n<a href=\"demo/GHH%20-%20Haxplorer/1.php\">GHDB Signature #833 (filetype:php HAXPLORER &quot;Server Files Browser&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Ping/php-ping.php\">GHDB Signature #733 (&quot;Enter ip&quot; inurl:&quot;php-ping.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHP%20Shell/phpshell.php\">GHDB Signature #365 (intitle:&quot;PHP Shell *&quot; &quot;Enable stderr&quot; filetype:php)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPBB%20Install/phpBB2/install/install.php\">GHDB Signature #935 (inurl:&quot;install/install.php&quot;)</a><br>\n<br>\n<a href=\"demo/GHH%20-%20PHPFM/index.php\">GHDB Signature #361 (&quot;Powered by PHPFM&quot; filetype:php -username)\n</a><br><br>\n<a href=\"demo/GHH%20-%20PhpSysInfo/index.php\">GHDB Signature #161 (inurl:phpSysInfo/ &quot;created by phpsysinfo&quot;)</a><br><br>\n<a href=\"demo/GHH%20-%20SquirrelMail/src/login.php\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7\">GHDB Signature #1013 (&quot;SquirrelMail version 1.4.4&quot; inurl:src ext:php)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .mdb/admin.mdb\">GHDB Signature #162 (allinurl: admin mdb)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - .sql/create.sql\">GHDB Signature #1064 (filetype:sql (\"passwd values\" | \"password values\" | \"pass values\" ))</a> <br><br>\n<a href=\"/demo/GHH v1.1 - AIM BuddyList/BuddyList.blt\">GHDB Signature #937 (filetype:blt \"buddylist\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - File Upload Manager/\">GHDB Signature #734 (\"File Upload Manager v1.3\" \"rename to\")</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passlist.txt/passlist.txt\">GHDB Signature #58 (inurl:passlist.txt)</a> <br><br>\n<a href=\"/demo/GHH v1.1 - passwd.txt/passwd.txt\">GHDB Signature #1122 (wwwboard WebAdmin inurl:passwd.txt</a> <br><br>\n<a href=\"/demo/GHH v1.1 - WebUtil 2.7/webutil.pl\">GHDB Signature #769 (inurl:webutil.pl)</a> <br><br>\n-->\n\n\n    <!--\n<a href=\"mailto:csapda@web-server.hu\"></a>\n<a href=\"mailto:csapda@astrohost.com\"></a>\n-->\n\n</html>\n\n",
            "dom" : {
              "url" : "http://elearnix.org/",
              "transitions" : [],
              "digest" : null,
              "data_flow_sinks" : [],
              "execution_flow_sinks" : []
            }
          },
          "remarks" : {},
          "variation" : true,
          "response" : {
            "url" : "http://elearnix.org/.svn/all-wcprops",
            "code" : 403,
            "ip_address" : "31.220.16.186",
            "headers" : {
              "Date" : "Tue, 07 Jun 2016 13:37:44 GMT",
              "Server" : "Apache/2.2.16 (Debian)",
              "Cache-Control" : "no-cache, no-store, must-revalidate",
              "Pragma" : "no-cache",
              "Expires" : "0",
              "Content-Type" : "text/plain",
              "Content-Length" : "29"
            },
            "headers_string" : "HTTP/1.1 403 Forbidden\r\nDate: Tue, 07 Jun 2016 13:37:44 GMT\r\nServer: Apache/2.2.16 (Debian)\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: 0\r\nContent-Type: text/plain\r\nContent-Length: 29\r\n\r\n",
            "body" : "Invalid URI /.svn/all-wcprops",
            "time" : 1.466338,
            "app_time" : 1.267606,
            "total_time" : 1.466338,
            "return_code" : "ok",
            "return_message" : "No error",
            "status_line" : "HTTP/1.1 403 Forbidden"
          },
          "request" : {
            "url" : "http://elearnix.org/.svn/all-wcprops",
            "parameters" : {},
            "headers" : {
              "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0"
            },
            "headers_string" : "GET /.svn/all-wcprops HTTP/1.1\r\nHost: elearnix.org\r\nAccept-Encoding: gzip, deflate\r\nUser-Agent: Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n\r\n",
            "effective_body" : null,
            "body" : null,
            "method" : "get"
          }
        }
      ],
      "digest" : 710586659
    }
  ],
  "plugins" : {
    "healthmap" : {
      "name" : "Health map",
      "description" : "Generates a simple list of safe/unsafe URLs.",
      "author" : "Tasos \"Zapotek\" Laskos <tasos.laskos@arachni-scanner.com>",
      "version" : "0.1.5",
      "results" : {
        "map" : [
          {
            "with_issues" : "http://elearnix.org/"
          },
          {
            "with_issues" : "http://elearnix.org/.adm"
          },
          {
            "with_issues" : "http://elearnix.org/.admin"
          },
          {
            "with_issues" : "http://elearnix.org/.git/HEAD"
          },
          {
            "with_issues" : "http://elearnix.org/.svn/all-wcprops"
          },
          {
            "with_issues" : "http://elearnix.org/verify.php"
          }
        ],
        "total" : 6,
        "without_issues" : 0,
        "with_issues" : 6,
        "issue_percentage" : 100
      }
    }
  }
}
"""
