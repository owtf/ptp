report_low = """<report xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/Arachni/arachni/v1.0.1/components/reporters/xml/schema.xsd">
  <version>1.0.1</version>
  <options>---
http:
  user_agent: Arachni/v1.0.1
  request_timeout: 50000
  request_redirect_limit: 5
  request_concurrency: 20
  request_queue_size: 500
  request_headers: {}
  cookies: {}
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
browser_cluster:
  pool_size: 6
  job_timeout: 120
  worker_time_to_live: 100
  ignore_images: false
  screen_width: 1600
  screen_height: 1200
datastore:
  report_path: "../"
session: {}
audit:
  exclude_vector_patterns: []
  include_vector_patterns: []
  link_templates: []
  links: true
  forms: true
  cookies: true
scope:
  redundant_path_patterns: {}
  dom_depth_limit: 10
  exclude_path_patterns: []
  exclude_content_patterns: []
  include_path_patterns: []
  restrict_paths: []
  extend_paths: []
  url_rewrites: {}
checks:
- code_injection_timing
- ldap_injection
- xss
- xss_dom_inputs
- response_splitting
- source_code_disclosure
- xss_script_context
- file_inclusion
- os_cmd_injection
- trainer
- no_sql_injection_differential
- sql_injection
- xss_dom_script_context
- os_cmd_injection_timing
- session_fixation
- path_traversal
- sql_injection_timing
- sql_injection_differential
- unvalidated_redirect
- no_sql_injection
- xss_tag
- code_injection_php_input_wrapper
- xss_path
- xpath_injection
- xss_event
- csrf
- xss_dom
- code_injection
- rfi
- xst
- http_put
- htaccess_limit
- backup_files
- directory_listing
- common_directories
- backup_directories
- interesting_responses
- origin_spoof_access_restriction_bypass
- allowed_methods
- common_files
- ssn
- emails
- form_upload
- cvs_svn_users
- cookie_set_for_parent_domain
- unencrypted_password_forms
- html_objects
- captcha
- mixed_resource
- hsts
- private_ip
- http_only_cookies
- insecure_cookies
- password_autocomplete
- credit_card
- backdoors
- webdav
- localstart_asp
platforms: []
plugins: {}
no_fingerprinting: false
authorized_by: 
url: http://192.168.1.24:9000/
</options>
  <start_datetime>2014-10-07T01:06:54+02:00</start_datetime>
  <finish_datetime>2014-10-07T01:07:05+02:00</finish_datetime>
  <sitemap>
    <entry url="http://192.168.1.24:9000/" code="200"/>
    <entry url="http://192.168.1.24:9000/choucroute" code="200"/>
    <entry url="http://192.168.1.24:9000/cake" code="200"/>
  </sitemap>
  <issues>
    <issue>
      <name>Private IP address disclosure</name>
      <description>
Private, or non-routable, IP addresses are generally used within a home or
company network and are typically unknown to anyone outside of that network.

Cyber-criminals will attempt to identify the private IP address range being used
by their victim, to aid in collecting further information that could then lead
to a possible compromise.

Arachni discovered that the affected page returned a RFC 1918 compliant private
IP address and therefore could be revealing sensitive information.

_This finding typically requires manual verification to ensure the context is
correct, as any private IP address within the HTML body will trigger it.
</description>
      <remedy_guidance>
Identifying the context in which the affected page displays a Private IP
address is necessary.

If the page is publicly accessible and displays the Private IP of the affected
server (or supporting infrastructure), then measures should be put in place to
ensure that the IP address is removed from any response.
</remedy_guidance>
      <remedy_code/>
      <severity>low</severity>
      <cwe>200</cwe>
      <digest>3594371297</digest>
      <references>
        <reference title="WebAppSec" url="http://projects.webappsec.org/w/page/13246936/Information%20Leakage"/>
      </references>
      <vector>
        <class>Arachni::Element::Header</class>
        <type>header</type>
        <url>http://192.168.1.24:9000/cake</url>
        <action>http://192.168.1.24:9000/cake</action>
        <affected_input_name/>
        <inputs>
          <input name="Host" value="192.168.1.24:9000"/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <seed/>
            <inputs>
              <input name="Host" value="192.168.1.24:9000"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>    &lt;h2&gt;Chocolate cake&lt;/h2&gt;

    &lt;ul&gt;
        &lt;li&gt;225g/8oz plain flour&lt;/li&gt;
        &lt;li&gt;350g/12&#xBD;oz caster sugar&lt;/li&gt;
        &lt;li&gt;85g/3oz cocoa powder&lt;/li&gt;
        &lt;li&gt;1&#xBD; tsp baking powder&lt;/li&gt;
        &lt;li&gt;1&#xBD; tsp bicarbonate of soda&lt;/li&gt;
        &lt;li&gt;2 free-range eggs&lt;/li&gt;
        &lt;li&gt;250ml/9fl oz milk&lt;/li&gt;
        &lt;li&gt;125ml/4&#xBD;fl oz vegetable oil&lt;/li&gt;
        &lt;li&gt;2 tsp vanilla extract&lt;/li&gt;
        &lt;li&gt;250ml/9fl oz boiling water&lt;/li&gt;
    &lt;/ul&gt;
    &lt;a href='/cake'&gt;reload the current page&lt;/a&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/cake</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /cake HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/cake</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0097</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;h2&gt;Chocolate cake&lt;/h2&gt;

    &lt;ul&gt;
        &lt;li&gt;225g/8oz plain flour&lt;/li&gt;
        &lt;li&gt;350g/12&#xBD;oz caster sugar&lt;/li&gt;
        &lt;li&gt;85g/3oz cocoa powder&lt;/li&gt;
        &lt;li&gt;1&#xBD; tsp baking powder&lt;/li&gt;
        &lt;li&gt;1&#xBD; tsp bicarbonate of soda&lt;/li&gt;
        &lt;li&gt;2 free-range eggs&lt;/li&gt;
        &lt;li&gt;250ml/9fl oz milk&lt;/li&gt;
        &lt;li&gt;125ml/4&#xBD;fl oz vegetable oil&lt;/li&gt;
        &lt;li&gt;2 tsp vanilla extract&lt;/li&gt;
        &lt;li&gt;250ml/9fl oz boiling water&lt;/li&gt;
    &lt;/ul&gt;
    &lt;a href='/cake'&gt;reload the current page&lt;/a&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/cake</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;h2&gt;Chocolate cake&lt;/h2&gt;

    &lt;ul&gt;
        &lt;li&gt;225g/8oz plain flour&lt;/li&gt;
        &lt;li&gt;350g/12&#xBD;oz caster sugar&lt;/li&gt;
        &lt;li&gt;85g/3oz cocoa powder&lt;/li&gt;
        &lt;li&gt;1&#xBD; tsp baking powder&lt;/li&gt;
        &lt;li&gt;1&#xBD; tsp bicarbonate of soda&lt;/li&gt;
        &lt;li&gt;2 free-range eggs&lt;/li&gt;
        &lt;li&gt;250ml/9fl oz milk&lt;/li&gt;
        &lt;li&gt;125ml/4&#xBD;fl oz vegetable oil&lt;/li&gt;
        &lt;li&gt;2 tsp vanilla extract&lt;/li&gt;
        &lt;li&gt;250ml/9fl oz boiling water&lt;/li&gt;
    &lt;/ul&gt;
    &lt;a href='/cake'&gt;reload the current page&lt;/a&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/cake</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /cake HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/cake</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0097</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;h2&gt;Chocolate cake&lt;/h2&gt;

    &lt;ul&gt;
        &lt;li&gt;225g/8oz plain flour&lt;/li&gt;
        &lt;li&gt;350g/12&#xBD;oz caster sugar&lt;/li&gt;
        &lt;li&gt;85g/3oz cocoa powder&lt;/li&gt;
        &lt;li&gt;1&#xBD; tsp baking powder&lt;/li&gt;
        &lt;li&gt;1&#xBD; tsp bicarbonate of soda&lt;/li&gt;
        &lt;li&gt;2 free-range eggs&lt;/li&gt;
        &lt;li&gt;250ml/9fl oz milk&lt;/li&gt;
        &lt;li&gt;125ml/4&#xBD;fl oz vegetable oil&lt;/li&gt;
        &lt;li&gt;2 tsp vanilla extract&lt;/li&gt;
        &lt;li&gt;250ml/9fl oz boiling water&lt;/li&gt;
    &lt;/ul&gt;
    &lt;a href='/cake'&gt;reload the current page&lt;/a&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/cake</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>192.168.1.24:9000</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Private IP address disclosure</name>
      <description>
Private, or non-routable, IP addresses are generally used within a home or
company network and are typically unknown to anyone outside of that network.

Cyber-criminals will attempt to identify the private IP address range being used
by their victim, to aid in collecting further information that could then lead
to a possible compromise.

Arachni discovered that the affected page returned a RFC 1918 compliant private
IP address and therefore could be revealing sensitive information.

_This finding typically requires manual verification to ensure the context is
correct, as any private IP address within the HTML body will trigger it.
</description>
      <remedy_guidance>
Identifying the context in which the affected page displays a Private IP
address is necessary.

If the page is publicly accessible and displays the Private IP of the affected
server (or supporting infrastructure), then measures should be put in place to
ensure that the IP address is removed from any response.
</remedy_guidance>
      <remedy_code/>
      <severity>low</severity>
      <cwe>200</cwe>
      <digest>188442206</digest>
      <references>
        <reference title="WebAppSec" url="http://projects.webappsec.org/w/page/13246936/Information%20Leakage"/>
      </references>
      <vector>
        <class>Arachni::Element::Header</class>
        <type>header</type>
        <url>http://192.168.1.24:9000/choucroute</url>
        <action>http://192.168.1.24:9000/choucroute</action>
        <affected_input_name/>
        <inputs>
          <input name="Host" value="192.168.1.24:9000"/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <seed/>
            <inputs>
              <input name="Host" value="192.168.1.24:9000"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>    &lt;h2&gt;Choucroute Garnie&lt;/h2&gt;

    &lt;ul&gt;
        &lt;li&gt;1/3 cup kosher salt, plus more for seasoning&lt;/li&gt;
        &lt;li&gt;2 tablespoons light brown sugar&lt;/li&gt;
        &lt;li&gt;3 pounds pork back ribs or baby back ribs, cut into 3 sections&lt;/li&gt;
        &lt;li&gt;6 pounds sauerkraut (in plastic bags), drained&lt;/li&gt;
        &lt;li&gt;1/4 cup duck or goose fat or peanut oil&lt;/li&gt;
        &lt;li&gt;1 large onion, coarsely chopped&lt;/li&gt;
        &lt;li&gt;4 large garlic cloves, coarsely chopped&lt;/li&gt;
        &lt;li&gt;20 juniper berries&lt;/li&gt;
        &lt;li&gt;3 large bay leaves&lt;/li&gt;
        &lt;li&gt;1/2 teaspoon caraway seeds&lt;/li&gt;
        &lt;li&gt;1 teaspoon freshly ground black pepper&lt;/li&gt;
        &lt;li&gt;3 cups chicken stock&lt;/li&gt;
        &lt;li&gt;1 1/2 cups Riesling or Pinot Gris&lt;/li&gt;
        &lt;li&gt;2 pounds Polish kielbasa, skinned and cut into 2-inch pieces&lt;/li&gt;
        &lt;li&gt;10 skinless hot dogs&lt;/li&gt;
        &lt;li&gt;One 2-pound piece of boneless boiled ham (3 to 4 inches wide), sliced 1/4 inch thick&lt;/li&gt;
        &lt;li&gt;2 pounds medium potatoes (about 10), peeled&lt;/li&gt;
        &lt;li&gt;Assorted mustards, for serving&lt;/li&gt;
    &lt;/ul&gt;

    &lt;a href='/choucroute'&gt;reload the current page&lt;/a&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/choucroute</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /choucroute HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/choucroute</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0097</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;h2&gt;Choucroute Garnie&lt;/h2&gt;

    &lt;ul&gt;
        &lt;li&gt;1/3 cup kosher salt, plus more for seasoning&lt;/li&gt;
        &lt;li&gt;2 tablespoons light brown sugar&lt;/li&gt;
        &lt;li&gt;3 pounds pork back ribs or baby back ribs, cut into 3 sections&lt;/li&gt;
        &lt;li&gt;6 pounds sauerkraut (in plastic bags), drained&lt;/li&gt;
        &lt;li&gt;1/4 cup duck or goose fat or peanut oil&lt;/li&gt;
        &lt;li&gt;1 large onion, coarsely chopped&lt;/li&gt;
        &lt;li&gt;4 large garlic cloves, coarsely chopped&lt;/li&gt;
        &lt;li&gt;20 juniper berries&lt;/li&gt;
        &lt;li&gt;3 large bay leaves&lt;/li&gt;
        &lt;li&gt;1/2 teaspoon caraway seeds&lt;/li&gt;
        &lt;li&gt;1 teaspoon freshly ground black pepper&lt;/li&gt;
        &lt;li&gt;3 cups chicken stock&lt;/li&gt;
        &lt;li&gt;1 1/2 cups Riesling or Pinot Gris&lt;/li&gt;
        &lt;li&gt;2 pounds Polish kielbasa, skinned and cut into 2-inch pieces&lt;/li&gt;
        &lt;li&gt;10 skinless hot dogs&lt;/li&gt;
        &lt;li&gt;One 2-pound piece of boneless boiled ham (3 to 4 inches wide), sliced 1/4 inch thick&lt;/li&gt;
        &lt;li&gt;2 pounds medium potatoes (about 10), peeled&lt;/li&gt;
        &lt;li&gt;Assorted mustards, for serving&lt;/li&gt;
    &lt;/ul&gt;

    &lt;a href='/choucroute'&gt;reload the current page&lt;/a&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/choucroute</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;h2&gt;Choucroute Garnie&lt;/h2&gt;

    &lt;ul&gt;
        &lt;li&gt;1/3 cup kosher salt, plus more for seasoning&lt;/li&gt;
        &lt;li&gt;2 tablespoons light brown sugar&lt;/li&gt;
        &lt;li&gt;3 pounds pork back ribs or baby back ribs, cut into 3 sections&lt;/li&gt;
        &lt;li&gt;6 pounds sauerkraut (in plastic bags), drained&lt;/li&gt;
        &lt;li&gt;1/4 cup duck or goose fat or peanut oil&lt;/li&gt;
        &lt;li&gt;1 large onion, coarsely chopped&lt;/li&gt;
        &lt;li&gt;4 large garlic cloves, coarsely chopped&lt;/li&gt;
        &lt;li&gt;20 juniper berries&lt;/li&gt;
        &lt;li&gt;3 large bay leaves&lt;/li&gt;
        &lt;li&gt;1/2 teaspoon caraway seeds&lt;/li&gt;
        &lt;li&gt;1 teaspoon freshly ground black pepper&lt;/li&gt;
        &lt;li&gt;3 cups chicken stock&lt;/li&gt;
        &lt;li&gt;1 1/2 cups Riesling or Pinot Gris&lt;/li&gt;
        &lt;li&gt;2 pounds Polish kielbasa, skinned and cut into 2-inch pieces&lt;/li&gt;
        &lt;li&gt;10 skinless hot dogs&lt;/li&gt;
        &lt;li&gt;One 2-pound piece of boneless boiled ham (3 to 4 inches wide), sliced 1/4 inch thick&lt;/li&gt;
        &lt;li&gt;2 pounds medium potatoes (about 10), peeled&lt;/li&gt;
        &lt;li&gt;Assorted mustards, for serving&lt;/li&gt;
    &lt;/ul&gt;

    &lt;a href='/choucroute'&gt;reload the current page&lt;/a&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/choucroute</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /choucroute HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/choucroute</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0097</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;h2&gt;Choucroute Garnie&lt;/h2&gt;

    &lt;ul&gt;
        &lt;li&gt;1/3 cup kosher salt, plus more for seasoning&lt;/li&gt;
        &lt;li&gt;2 tablespoons light brown sugar&lt;/li&gt;
        &lt;li&gt;3 pounds pork back ribs or baby back ribs, cut into 3 sections&lt;/li&gt;
        &lt;li&gt;6 pounds sauerkraut (in plastic bags), drained&lt;/li&gt;
        &lt;li&gt;1/4 cup duck or goose fat or peanut oil&lt;/li&gt;
        &lt;li&gt;1 large onion, coarsely chopped&lt;/li&gt;
        &lt;li&gt;4 large garlic cloves, coarsely chopped&lt;/li&gt;
        &lt;li&gt;20 juniper berries&lt;/li&gt;
        &lt;li&gt;3 large bay leaves&lt;/li&gt;
        &lt;li&gt;1/2 teaspoon caraway seeds&lt;/li&gt;
        &lt;li&gt;1 teaspoon freshly ground black pepper&lt;/li&gt;
        &lt;li&gt;3 cups chicken stock&lt;/li&gt;
        &lt;li&gt;1 1/2 cups Riesling or Pinot Gris&lt;/li&gt;
        &lt;li&gt;2 pounds Polish kielbasa, skinned and cut into 2-inch pieces&lt;/li&gt;
        &lt;li&gt;10 skinless hot dogs&lt;/li&gt;
        &lt;li&gt;One 2-pound piece of boneless boiled ham (3 to 4 inches wide), sliced 1/4 inch thick&lt;/li&gt;
        &lt;li&gt;2 pounds medium potatoes (about 10), peeled&lt;/li&gt;
        &lt;li&gt;Assorted mustards, for serving&lt;/li&gt;
    &lt;/ul&gt;

    &lt;a href='/choucroute'&gt;reload the current page&lt;/a&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/choucroute</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>192.168.1.24:9000</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Private IP address disclosure</name>
      <description>
Private, or non-routable, IP addresses are generally used within a home or
company network and are typically unknown to anyone outside of that network.

Cyber-criminals will attempt to identify the private IP address range being used
by their victim, to aid in collecting further information that could then lead
to a possible compromise.

Arachni discovered that the affected page returned a RFC 1918 compliant private
IP address and therefore could be revealing sensitive information.

_This finding typically requires manual verification to ensure the context is
correct, as any private IP address within the HTML body will trigger it.
</description>
      <remedy_guidance>
Identifying the context in which the affected page displays a Private IP
address is necessary.

If the page is publicly accessible and displays the Private IP of the affected
server (or supporting infrastructure), then measures should be put in place to
ensure that the IP address is removed from any response.
</remedy_guidance>
      <remedy_code/>
      <severity>low</severity>
      <cwe>200</cwe>
      <digest>3420875319</digest>
      <references>
        <reference title="WebAppSec" url="http://projects.webappsec.org/w/page/13246936/Information%20Leakage"/>
      </references>
      <vector>
        <class>Arachni::Element::Header</class>
        <type>header</type>
        <url>http://192.168.1.24:9000/</url>
        <action>http://192.168.1.24:9000/</action>
        <affected_input_name/>
        <inputs>
          <input name="Host" value="192.168.1.24:9000"/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <seed/>
            <inputs>
              <input name="Host" value="192.168.1.24:9000"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>    &lt;h1&gt;List of recipes&lt;/h1&gt;

    &lt;ul&gt;
        &lt;li&gt;&lt;a href="/choucroute"&gt;Choucroute garnie&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="/cake"&gt;Chocolate cake&lt;/a&gt;&lt;/li&gt;
        ... And more to come!
    &lt;/ul&gt;
    &lt;a href='/'&gt;reload the current page&lt;/a&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0094</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;h1&gt;List of recipes&lt;/h1&gt;

    &lt;ul&gt;
        &lt;li&gt;&lt;a href="/choucroute"&gt;Choucroute garnie&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="/cake"&gt;Chocolate cake&lt;/a&gt;&lt;/li&gt;
        ... And more to come!
    &lt;/ul&gt;
    &lt;a href='/'&gt;reload the current page&lt;/a&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;h1&gt;List of recipes&lt;/h1&gt;

    &lt;ul&gt;
        &lt;li&gt;&lt;a href="/choucroute"&gt;Choucroute garnie&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="/cake"&gt;Chocolate cake&lt;/a&gt;&lt;/li&gt;
        ... And more to come!
    &lt;/ul&gt;
    &lt;a href='/'&gt;reload the current page&lt;/a&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0094</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;h1&gt;List of recipes&lt;/h1&gt;

    &lt;ul&gt;
        &lt;li&gt;&lt;a href="/choucroute"&gt;Choucroute garnie&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="/cake"&gt;Chocolate cake&lt;/a&gt;&lt;/li&gt;
        ... And more to come!
    &lt;/ul&gt;
    &lt;a href='/'&gt;reload the current page&lt;/a&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>192.168.1.24:9000</proof>
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
          <with_issues>http://192.168.1.24:9000/</with_issues>
          <with_issues>http://192.168.1.24:9000/cake</with_issues>
          <with_issues>http://192.168.1.24:9000/choucroute</with_issues>
        </map>
        <total>3</total>
        <with_issues>3</with_issues>
        <without_issues>0</without_issues>
        <issue_percentage>100</issue_percentage>
      </results>
    </healthmap>
  </plugins>
</report>
"""


report_high = """<report xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/Arachni/arachni/v1.0.1/components/reporters/xml/schema.xsd">
  <version>1.0.1</version>
  <options>---
http:
  user_agent: Arachni/v1.0.1
  request_timeout: 50000
  request_redirect_limit: 5
  request_concurrency: 20
  request_queue_size: 500
  request_headers: {}
  cookies: {}
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
browser_cluster:
  pool_size: 6
  job_timeout: 120
  worker_time_to_live: 100
  ignore_images: false
  screen_width: 1600
  screen_height: 1200
datastore:
  report_path: "../"
session: {}
audit:
  exclude_vector_patterns: []
  include_vector_patterns: []
  link_templates: []
  links: true
  forms: true
  cookies: true
scope:
  redundant_path_patterns: {}
  dom_depth_limit: 10
  exclude_path_patterns: []
  exclude_content_patterns: []
  include_path_patterns: []
  restrict_paths: []
  extend_paths: []
  url_rewrites: {}
checks:
- code_injection_timing
- ldap_injection
- xss
- xss_dom_inputs
- response_splitting
- source_code_disclosure
- xss_script_context
- file_inclusion
- os_cmd_injection
- trainer
- no_sql_injection_differential
- sql_injection
- xss_dom_script_context
- os_cmd_injection_timing
- session_fixation
- path_traversal
- sql_injection_timing
- sql_injection_differential
- unvalidated_redirect
- no_sql_injection
- xss_tag
- code_injection_php_input_wrapper
- xss_path
- xpath_injection
- xss_event
- csrf
- xss_dom
- code_injection
- rfi
- xst
- http_put
- htaccess_limit
- backup_files
- directory_listing
- common_directories
- backup_directories
- interesting_responses
- origin_spoof_access_restriction_bypass
- allowed_methods
- common_files
- ssn
- emails
- form_upload
- cvs_svn_users
- cookie_set_for_parent_domain
- unencrypted_password_forms
- html_objects
- captcha
- mixed_resource
- hsts
- private_ip
- http_only_cookies
- insecure_cookies
- password_autocomplete
- credit_card
- backdoors
- webdav
- localstart_asp
platforms: []
plugins: {}
no_fingerprinting: false
authorized_by: 
url: http://192.168.1.24:9000/
</options>
  <start_datetime>2014-10-07T01:08:49+02:00</start_datetime>
  <finish_datetime>2014-10-07T01:10:49+02:00</finish_datetime>
  <sitemap>
    <entry url="http://192.168.1.24:9000/" code="200"/>
    <entry url="http://192.168.1.24:9000/post" code="200"/>
  </sitemap>
  <issues>
    <issue>
      <name>Blind SQL Injection (timing attack)</name>
      <description>
Due to the requirement for dynamic content of today's web applications, many
rely on a database backend to store data that will be called upon and processed
by the web application (or other programs).
Web applications retrieve data from the database by using Structured Query Language
(SQL) queries.

To meet demands of many developers, database servers (such as MSSQL, MySQL,
Oracle etc.) have additional built-in functionality that can allow extensive
control of the database and interaction with the host operating system itself.

An SQL injection occurs when a value originating from the client's request is used
within a SQL query without prior sanitisation. This could allow cyber-criminals
to execute arbitrary SQL code and steal data or use the additional functionality
of the database server to take control of more server components.

The successful exploitation of a SQL injection can be devastating to an
organisation and is one of the most commonly exploited web application vulnerabilities.

This injection was detected as Arachni was able to inject specific SQL queries,
that if vulnerable, result in the responses for each request being delayed before
being sent by the server.
This is known as a time-based blind SQL injection vulnerability.
</description>
      <remedy_guidance>
The only proven method to prevent against SQL injection attacks while still
maintaining full application functionality is to use parameterized queries
(also known as prepared statements).
When utilising this method of querying the database, any value supplied by the
client will be handled as a string value rather than part of the SQL query.

Additionally, when utilising parameterized queries, the database engine will
automatically check to make sure the string being used matches that of the column.
For example, the database engine will check that the user supplied input is an
integer if the database column is configured to contain integers.
</remedy_guidance>
      <remedy_code/>
      <severity>high</severity>
      <cwe>89</cwe>
      <digest>2091028636</digest>
      <references>
        <reference title="OWASP" url="http://www.owasp.org/index.php/Blind_SQL_Injection"/>
        <reference title="MITRE - CAPEC" url="http://capec.mitre.org/data/definitions/7.html"/>
        <reference title="WASC" url="http://projects.webappsec.org/w/page/13246963/SQL%20Injection"/>
        <reference title="W3 Schools" url="http://www.w3schools.com/sql/sql_injection.asp"/>
      </references>
      <vector>
        <class>Arachni::Element::Form</class>
        <type>form</type>
        <url>http://192.168.1.24:9000/post</url>
        <action>http://192.168.1.24:9000/post</action>
        <html>&lt;form action="/post" method="post"&gt;
        &lt;input type="text" name="pseudo"&gt;
        &lt;input type="textarea" name="message"&gt;
        &lt;input type="submit" value="ok"&gt;
    &lt;/form&gt;</html>
        <method>post</method>
        <affected_input_name/>
        <inputs>
          <input name="pseudo" value=""/>
          <input name="message" value=""/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <method>post</method>
            <seed>' and sleep(16)='</seed>
            <inputs>
              <input name="pseudo" value="1' and sleep(16)='"/>
              <input name="message" value="1"/>
            </inputs>
          </vector>
          <remarks>
            <commenter>meta_analysis</commenter>
            <remark>This issue was discovered using a timing-attack but the audited page was exhibiting unusually high response times to begin with. This could be an indication that the logged issue is a false positive.</remark>
          </remarks>
          <page>
            <body/>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>post</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body>pseudo=1%27%20and%20sleep%2816%29%3D%27&amp;message=1</body>
              <raw>POST /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
Content-Length: 49&#xD;
Content-Type: application/x-www-form-urlencoded&#xD;
&#xD;
pseudo=1%27%20and%20sleep%2816%29%3D%27&amp;message=1</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>0</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.2005</time>
              <return_code>operation_timedout</return_code>
              <return_message>Timeout was reached</return_message>
              <headers/>
              <body/>
              <raw_headers/>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0122</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof/>
          <trusted>false</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>SQL Injection</name>
      <description>
Due to the requirement for dynamic content of today's web applications, many
rely on a database backend to store data that will be called upon and processed
by the web application (or other programs).
Web applications retrieve data from the database by using Structured Query Language
(SQL) queries.

To meet demands of many developers, database servers (such as MSSQL, MySQL,
Oracle etc.) have additional built-in functionality that can allow extensive
control of the database and interaction with the host operating system itself.

An SQL injection occurs when a value originating from the client's request is used
within a SQL query without prior sanitisation. This could allow cyber-criminals
to execute arbitrary SQL code and steal data or use the additional functionality
of the database server to take control of more server components.

The successful exploitation of a SQL injection can be devastating to an
organisation and is one of the most commonly exploited web application vulnerabilities.

This injection was detected as Arachni was able to cause the server to respond to
the request with a database related error.
</description>
      <remedy_guidance>
The only proven method to prevent against SQL injection attacks while still
maintaining full application functionality is to use parameterized queries
(also known as prepared statements).
When utilising this method of querying the database, any value supplied by the
client will be handled as a string value rather than part of the SQL query.

Additionally, when utilising parameterized queries, the database engine will
automatically check to make sure the string being used matches that of the column.
For example, the database engine will check that the user supplied input is an
integer if the database column is configured to contain integers.
</remedy_guidance>
      <remedy_code/>
      <severity>high</severity>
      <cwe>89</cwe>
      <digest>1191919315</digest>
      <references>
        <reference title="UnixWiz" url="http://unixwiz.net/techtips/sql-injection.html"/>
        <reference title="Wikipedia" url="http://en.wikipedia.org/wiki/SQL_injection"/>
        <reference title="SecuriTeam" url="http://www.securiteam.com/securityreviews/5DP0N1P76E.html"/>
        <reference title="OWASP" url="http://www.owasp.org/index.php/SQL_Injection"/>
        <reference title="WASC" url="http://projects.webappsec.org/w/page/13246963/SQL%20Injection"/>
        <reference title="W3 Schools" url="http://www.w3schools.com/sql/sql_injection.asp"/>
      </references>
      <vector>
        <class>Arachni::Element::Form</class>
        <type>form</type>
        <url>http://192.168.1.24:9000/post</url>
        <action>http://192.168.1.24:9000/post</action>
        <html>&lt;form action="/post" method="post"&gt;
        &lt;input type="text" name="pseudo"&gt;
        &lt;input type="textarea" name="message"&gt;
        &lt;input type="submit" value="ok"&gt;
    &lt;/form&gt;</html>
        <method>post</method>
        <affected_input_name/>
        <inputs>
          <input name="pseudo" value=""/>
          <input name="message" value=""/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <method>post</method>
            <seed>'`--</seed>
            <inputs>
              <input name="pseudo" value="1'`--"/>
              <input name="message" value="1"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '`--', '1')' at line 1
Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>post</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body>pseudo=1%27%60--&amp;message=1</body>
              <raw>POST /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
Content-Length: 26&#xD;
Content-Type: application/x-www-form-urlencoded&#xD;
&#xD;
pseudo=1%27%60--&amp;message=1</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>2.0992</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '`--', '1')' at line 1
Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0122</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature>(?i-mx:You have an error in your SQL syntax;)</signature>
          <proof>You have an error in your SQL syntax;</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>SQL Injection</name>
      <description>
Due to the requirement for dynamic content of today's web applications, many
rely on a database backend to store data that will be called upon and processed
by the web application (or other programs).
Web applications retrieve data from the database by using Structured Query Language
(SQL) queries.

To meet demands of many developers, database servers (such as MSSQL, MySQL,
Oracle etc.) have additional built-in functionality that can allow extensive
control of the database and interaction with the host operating system itself.

An SQL injection occurs when a value originating from the client's request is used
within a SQL query without prior sanitisation. This could allow cyber-criminals
to execute arbitrary SQL code and steal data or use the additional functionality
of the database server to take control of more server components.

The successful exploitation of a SQL injection can be devastating to an
organisation and is one of the most commonly exploited web application vulnerabilities.

This injection was detected as Arachni was able to cause the server to respond to
the request with a database related error.
</description>
      <remedy_guidance>
The only proven method to prevent against SQL injection attacks while still
maintaining full application functionality is to use parameterized queries
(also known as prepared statements).
When utilising this method of querying the database, any value supplied by the
client will be handled as a string value rather than part of the SQL query.

Additionally, when utilising parameterized queries, the database engine will
automatically check to make sure the string being used matches that of the column.
For example, the database engine will check that the user supplied input is an
integer if the database column is configured to contain integers.
</remedy_guidance>
      <remedy_code/>
      <severity>high</severity>
      <cwe>89</cwe>
      <digest>364363564</digest>
      <references>
        <reference title="UnixWiz" url="http://unixwiz.net/techtips/sql-injection.html"/>
        <reference title="Wikipedia" url="http://en.wikipedia.org/wiki/SQL_injection"/>
        <reference title="SecuriTeam" url="http://www.securiteam.com/securityreviews/5DP0N1P76E.html"/>
        <reference title="OWASP" url="http://www.owasp.org/index.php/SQL_Injection"/>
        <reference title="WASC" url="http://projects.webappsec.org/w/page/13246963/SQL%20Injection"/>
        <reference title="W3 Schools" url="http://www.w3schools.com/sql/sql_injection.asp"/>
      </references>
      <vector>
        <class>Arachni::Element::Form</class>
        <type>form</type>
        <url>http://192.168.1.24:9000/post</url>
        <action>http://192.168.1.24:9000/post</action>
        <html>&lt;form action="/post" method="post"&gt;
        &lt;input type="text" name="pseudo"&gt;
        &lt;input type="textarea" name="message"&gt;
        &lt;input type="submit" value="ok"&gt;
    &lt;/form&gt;</html>
        <method>post</method>
        <affected_input_name/>
        <inputs>
          <input name="pseudo" value=""/>
          <input name="message" value=""/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <method>post</method>
            <seed>'`--</seed>
            <inputs>
              <input name="pseudo" value="1"/>
              <input name="message" value="1'`--"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '`--')' at line 1
Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>post</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body>pseudo=1&amp;message=1%27%60--</body>
              <raw>POST /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
Content-Length: 26&#xD;
Content-Type: application/x-www-form-urlencoded&#xD;
&#xD;
pseudo=1&amp;message=1%27%60--</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>2.1076</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '`--')' at line 1
Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0122</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature>(?i-mx:You have an error in your SQL syntax;)</signature>
          <proof>You have an error in your SQL syntax;</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Cross-Site Scripting (XSS)</name>
      <description>
Client-side scripts are used extensively by modern web applications.
They perform from simple functions (such as the formatting of text) up to full
manipulation of client-side data and Operating System interaction.

Cross Site Scripting (XSS) allows clients to inject scripts into a request and
have the server return the script to the client in the response. This occurs
because the application is taking untrusted data (in this example, from the client)
and reusing it without performing any validation or sanitisation.

If the injected script is returned immediately this is known as reflected XSS.
If the injected script is stored by the server and returned to any client visiting
the affected page, then this is known as persistent XSS (also stored XSS).

Arachni has discovered that it is possible to insert script content directly into
HTML element content.
</description>
      <remedy_guidance>
To remedy XSS vulnerabilities, it is important to never use untrusted or unfiltered
data within the code of a HTML page.

Untrusted data can originate not only form the client but potentially a third
party or previously uploaded file etc.

Filtering of untrusted data typically involves converting special characters to
their HTML entity encoded counterparts (however, other methods do exist, see references).
These special characters include:

* `&amp;`
* `&lt;`
* `&gt;`
* `"`
* `'`
* `/`

An example of HTML entity encoding is converting `&lt;` to `&amp;lt;`.

Although it is possible to filter untrusted input, there are five locations
within an HTML page where untrusted input (even if it has been filtered) should
never be placed:

1. Directly in a script.
2. Inside an HTML comment.
3. In an attribute name.
4. In a tag name.
5. Directly in CSS.

Each of these locations have their own form of escaping and filtering.

_Because many browsers attempt to implement XSS protection, any manual verification
of this finding should be conducted using multiple different browsers and browser
versions._
</remedy_guidance>
      <remedy_code/>
      <severity>high</severity>
      <cwe>79</cwe>
      <digest>354116623</digest>
      <references>
        <reference title="ha.ckers" url="http://ha.ckers.org/xss.html"/>
        <reference title="Secunia" url="http://secunia.com/advisories/9716/"/>
        <reference title="WASC" url="http://projects.webappsec.org/w/page/13246920/Cross%20Site%20Scripting"/>
        <reference title="OWASP" url="www.owasp.org/index.php/XSS_%28Cross_Site_Scripting%29_Prevention_Cheat_Sheet"/>
      </references>
      <vector>
        <class>Arachni::Element::Form</class>
        <type>form</type>
        <url>http://192.168.1.24:9000/post</url>
        <action>http://192.168.1.24:9000/post</action>
        <html>&lt;form action="/post" method="post"&gt;
        &lt;input type="text" name="pseudo"&gt;
        &lt;input type="textarea" name="message"&gt;
        &lt;input type="submit" value="ok"&gt;
    &lt;/form&gt;</html>
        <method>post</method>
        <affected_input_name/>
        <inputs>
          <input name="pseudo" value=""/>
          <input name="message" value=""/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <method>post</method>
            <seed>()"&amp;%1'-;&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;'</seed>
            <inputs>
              <input name="pseudo" value="1()&quot;&amp;%1'-;&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;'"/>
              <input name="message" value="1"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ';&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;'', '1')' at line 1
Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>post</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body>pseudo=1%28%29%22%26%251%27-%3B%3Csome_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3%2F%3E%27&amp;message=1</body>
              <raw>POST /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
Content-Length: 106&#xD;
Content-Type: application/x-www-form-urlencoded&#xD;
&#xD;
pseudo=1%28%29%22%26%251%27-%3B%3Csome_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3%2F%3E%27&amp;message=1</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.4274</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ';&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;'', '1')' at line 1
Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0122</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Cross-Site Scripting (XSS)</name>
      <description>
Client-side scripts are used extensively by modern web applications.
They perform from simple functions (such as the formatting of text) up to full
manipulation of client-side data and Operating System interaction.

Cross Site Scripting (XSS) allows clients to inject scripts into a request and
have the server return the script to the client in the response. This occurs
because the application is taking untrusted data (in this example, from the client)
and reusing it without performing any validation or sanitisation.

If the injected script is returned immediately this is known as reflected XSS.
If the injected script is stored by the server and returned to any client visiting
the affected page, then this is known as persistent XSS (also stored XSS).

Arachni has discovered that it is possible to insert script content directly into
HTML element content.
</description>
      <remedy_guidance>
To remedy XSS vulnerabilities, it is important to never use untrusted or unfiltered
data within the code of a HTML page.

Untrusted data can originate not only form the client but potentially a third
party or previously uploaded file etc.

Filtering of untrusted data typically involves converting special characters to
their HTML entity encoded counterparts (however, other methods do exist, see references).
These special characters include:

* `&amp;`
* `&lt;`
* `&gt;`
* `"`
* `'`
* `/`

An example of HTML entity encoding is converting `&lt;` to `&amp;lt;`.

Although it is possible to filter untrusted input, there are five locations
within an HTML page where untrusted input (even if it has been filtered) should
never be placed:

1. Directly in a script.
2. Inside an HTML comment.
3. In an attribute name.
4. In a tag name.
5. Directly in CSS.

Each of these locations have their own form of escaping and filtering.

_Because many browsers attempt to implement XSS protection, any manual verification
of this finding should be conducted using multiple different browsers and browser
versions._
</remedy_guidance>
      <remedy_code/>
      <severity>high</severity>
      <cwe>79</cwe>
      <digest>2592092553</digest>
      <references>
        <reference title="ha.ckers" url="http://ha.ckers.org/xss.html"/>
        <reference title="Secunia" url="http://secunia.com/advisories/9716/"/>
        <reference title="WASC" url="http://projects.webappsec.org/w/page/13246920/Cross%20Site%20Scripting"/>
        <reference title="OWASP" url="www.owasp.org/index.php/XSS_%28Cross_Site_Scripting%29_Prevention_Cheat_Sheet"/>
      </references>
      <vector>
        <class>Arachni::Element::Form</class>
        <type>form</type>
        <url>http://192.168.1.24:9000/post</url>
        <action>http://192.168.1.24:9000/post</action>
        <html>&lt;form action="/post" method="post"&gt;
        &lt;input type="text" name="pseudo"&gt;
        &lt;input type="textarea" name="message"&gt;
        &lt;input type="submit" value="ok"&gt;
    &lt;/form&gt;</html>
        <method>post</method>
        <affected_input_name/>
        <inputs>
          <input name="pseudo" value=""/>
          <input name="message" value=""/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <method>post</method>
            <seed>()"&amp;%1'-;&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;'</seed>
            <inputs>
              <input name="pseudo" value="1"/>
              <input name="message" value="1()&quot;&amp;%1'-;&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;'"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ';&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;'')' at line 1
Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>post</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body>pseudo=1&amp;message=1%28%29%22%26%251%27-%3B%3Csome_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3%2F%3E%27</body>
              <raw>POST /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
Content-Length: 106&#xD;
Content-Type: application/x-www-form-urlencoded&#xD;
&#xD;
pseudo=1&amp;message=1%28%29%22%26%251%27-%3B%3Csome_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3%2F%3E%27</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.4364</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ';&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;'')' at line 1
Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0122</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>&lt;some_dangerous_input_ac898b180e96cdae4202d7a942d1c1e3/&gt;</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Private IP address disclosure</name>
      <description>
Private, or non-routable, IP addresses are generally used within a home or
company network and are typically unknown to anyone outside of that network.

Cyber-criminals will attempt to identify the private IP address range being used
by their victim, to aid in collecting further information that could then lead
to a possible compromise.

Arachni discovered that the affected page returned a RFC 1918 compliant private
IP address and therefore could be revealing sensitive information.

_This finding typically requires manual verification to ensure the context is
correct, as any private IP address within the HTML body will trigger it.
</description>
      <remedy_guidance>
Identifying the context in which the affected page displays a Private IP
address is necessary.

If the page is publicly accessible and displays the Private IP of the affected
server (or supporting infrastructure), then measures should be put in place to
ensure that the IP address is removed from any response.
</remedy_guidance>
      <remedy_code/>
      <severity>low</severity>
      <cwe>200</cwe>
      <digest>1990503729</digest>
      <references>
        <reference title="WebAppSec" url="http://projects.webappsec.org/w/page/13246936/Information%20Leakage"/>
      </references>
      <vector>
        <class>Arachni::Element::Header</class>
        <type>header</type>
        <url>http://192.168.1.24:9000/post</url>
        <action>http://192.168.1.24:9000/post</action>
        <affected_input_name/>
        <inputs>
          <input name="Host" value="192.168.1.24:9000"/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <seed/>
            <inputs>
              <input name="Host" value="192.168.1.24:9000"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0122</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0122</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;Type your pseudonyme and message!&lt;/p&gt;
    &lt;form action='/post' method='post'&gt;
        &lt;input type='text' name='pseudo' /&gt;
        &lt;input type='textarea' name='message' /&gt;
        &lt;input type='submit' value='ok' /&gt;
    &lt;/form&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>192.168.1.24:9000</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
        <variation>
          <vector>
            <seed/>
            <inputs>
              <input name="Host" value="192.168.1.24:9000"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>post</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body>pseudo=&amp;message=</body>
              <raw>POST /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
Content-Length: 16&#xD;
Content-Type: application/x-www-form-urlencoded&#xD;
&#xD;
pseudo=&amp;message=</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.2438</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
            <request>
              <url>http://192.168.1.24:9000/post</url>
              <method>post</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body>pseudo=&amp;message=</body>
              <raw>POST /post HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
Content-Length: 16&#xD;
Content-Type: application/x-www-form-urlencoded&#xD;
&#xD;
pseudo=&amp;message=</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/post</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.2438</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>Message added successfullygo back to &lt;a href='/'&gt;messages&lt;/a&gt;</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/post</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>192.168.1.24:9000</proof>
          <trusted>true</trusted>
          <platform_type/>
          <platform_name/>
        </variation>
      </variations>
    </issue>
    <issue>
      <name>Private IP address disclosure</name>
      <description>
Private, or non-routable, IP addresses are generally used within a home or
company network and are typically unknown to anyone outside of that network.

Cyber-criminals will attempt to identify the private IP address range being used
by their victim, to aid in collecting further information that could then lead
to a possible compromise.

Arachni discovered that the affected page returned a RFC 1918 compliant private
IP address and therefore could be revealing sensitive information.

_This finding typically requires manual verification to ensure the context is
correct, as any private IP address within the HTML body will trigger it.
</description>
      <remedy_guidance>
Identifying the context in which the affected page displays a Private IP
address is necessary.

If the page is publicly accessible and displays the Private IP of the affected
server (or supporting infrastructure), then measures should be put in place to
ensure that the IP address is removed from any response.
</remedy_guidance>
      <remedy_code/>
      <severity>low</severity>
      <cwe>200</cwe>
      <digest>3420875319</digest>
      <references>
        <reference title="WebAppSec" url="http://projects.webappsec.org/w/page/13246936/Information%20Leakage"/>
      </references>
      <vector>
        <class>Arachni::Element::Header</class>
        <type>header</type>
        <url>http://192.168.1.24:9000/</url>
        <action>http://192.168.1.24:9000/</action>
        <affected_input_name/>
        <inputs>
          <input name="Host" value="192.168.1.24:9000"/>
        </inputs>
      </vector>
      <variations>
        <variation>
          <vector>
            <seed/>
            <inputs>
              <input name="Host" value="192.168.1.24:9000"/>
            </inputs>
          </vector>
          <remarks/>
          <page>
            <body>    &lt;p&gt;&lt;a href='/post'&gt;leave a message!&lt;/a&gt;&lt;/p&gt;
    &lt;hr /&gt;
        &lt;p&gt;manny&lt;/p&gt;
        &lt;p&gt;beautiful website!&lt;/p&gt;
        &lt;hr /&gt;
        &lt;p&gt;manny&lt;/p&gt;
        &lt;p&gt;i've got nothing else to do&lt;/p&gt;
        &lt;hr /&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0429</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;&lt;a href='/post'&gt;leave a message!&lt;/a&gt;&lt;/p&gt;
    &lt;hr /&gt;
        &lt;p&gt;manny&lt;/p&gt;
        &lt;p&gt;beautiful website!&lt;/p&gt;
        &lt;hr /&gt;
        &lt;p&gt;manny&lt;/p&gt;
        &lt;p&gt;i've got nothing else to do&lt;/p&gt;
        &lt;hr /&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </page>
          <referring_page>
            <body>    &lt;p&gt;&lt;a href='/post'&gt;leave a message!&lt;/a&gt;&lt;/p&gt;
    &lt;hr /&gt;
        &lt;p&gt;manny&lt;/p&gt;
        &lt;p&gt;beautiful website!&lt;/p&gt;
        &lt;hr /&gt;
        &lt;p&gt;manny&lt;/p&gt;
        &lt;p&gt;i've got nothing else to do&lt;/p&gt;
        &lt;hr /&gt;
</body>
            <request>
              <url>http://192.168.1.24:9000/</url>
              <method>get</method>
              <parameters/>
              <headers>
                <header name="Accept" value="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"/>
                <header name="User-Agent" value="Arachni/v1.0.1"/>
              </headers>
              <body/>
              <raw>GET / HTTP/1.1&#xD;
Host: 192.168.1.24:9000&#xD;
Accept-Encoding: gzip, deflate&#xD;
User-Agent: Arachni/v1.0.1&#xD;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8&#xD;
&#xD;
</raw>
            </request>
            <response>
              <url>http://192.168.1.24:9000/</url>
              <code>200</code>
              <ip_address>192.168.1.24</ip_address>
              <time>0.0429</time>
              <return_code>ok</return_code>
              <return_message>No error</return_message>
              <headers>
                <header name="Host" value="192.168.1.24:9000"/>
                <header name="Connection" value="close"/>
                <header name="X-Powered-By" value="PHP/5.6.0"/>
                <header name="Content-Type" value="text/html;charset=UTF-8"/>
              </headers>
              <body>    &lt;p&gt;&lt;a href='/post'&gt;leave a message!&lt;/a&gt;&lt;/p&gt;
    &lt;hr /&gt;
        &lt;p&gt;manny&lt;/p&gt;
        &lt;p&gt;beautiful website!&lt;/p&gt;
        &lt;hr /&gt;
        &lt;p&gt;manny&lt;/p&gt;
        &lt;p&gt;i've got nothing else to do&lt;/p&gt;
        &lt;hr /&gt;
</body>
              <raw_headers>HTTP/1.1 200 OK&#xD;
Host: 192.168.1.24:9000&#xD;
Connection: close&#xD;
X-Powered-By: PHP/5.6.0&#xD;
Content-type: text/html;charset=UTF-8&#xD;
&#xD;
</raw_headers>
            </response>
            <dom>
              <url>http://192.168.1.24:9000/</url>
              <transitions/>
              <data_flow_sinks/>
              <execution_flow_sinks/>
            </dom>
          </referring_page>
          <signature/>
          <proof>192.168.1.24:9000</proof>
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
          <with_issues>http://192.168.1.24:9000/</with_issues>
          <with_issues>http://192.168.1.24:9000/post</with_issues>
        </map>
        <total>2</total>
        <with_issues>2</with_issues>
        <without_issues>0</without_issues>
        <issue_percentage>100</issue_percentage>
      </results>
    </healthmap>
    <uniformity>
      <name>Uniformity (Lack of central sanitization)</name>
      <description>
Analyzes the scan results and logs issues which persist across different pages.

This is usually a sign for a lack of a central/single point of input sanitization,
a bad coding practise.
</description>
      <results>
        <digests>1191919315 364363564</digests>
        <digests>354116623 2592092553</digests>
      </results>
    </uniformity>
  </plugins>
</report>
"""
