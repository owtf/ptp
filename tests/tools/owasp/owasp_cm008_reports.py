report_low = r"""HTTP/1.1 200 OK
Allow: OPTIONS, TRACE, GET, HEAD
Content-Length: 0
Server: Microsoft-IIS/6.0
Public: OPTIONS, TRACE, GET, HEAD, POST
X-Powered-By: ASP.NET
Date: Tue, 12 Aug 2014 20:26:16 GMT
"""


report_medium = r"""HTTP/1.1 200 OK
Allow: OPTIONS, CONNECT
Content-Length: 0
Server: Microsoft-IIS/6.0
Public: OPTIONS, CONNECT
X-Powered-By: ASP.NET
Date: Tue, 12 Aug 2014 20:26:16 GMT
"""


report_high = r"""HTTP/1.1 200 OK
Allow: OPTIONS, TRACE, GET, HEAD, DELETE
Content-Length: 0
Server: Microsoft-IIS/6.0
Public: OPTIONS, TRACE, GET, HEAD, POST, DELETE
X-Powered-By: ASP.NET
Date: Tue, 12 Aug 2014 20:26:16 GMT
"""


report_no_allow = r"""HTTP/1.1 200 OK
Content-Length: 0
Server: Microsoft-IIS/6.0
Public: OPTIONS, TRACE, GET, HEAD, POST, DELETE
X-Powered-By: ASP.NET
Date: Tue, 12 Aug 2014 20:26:16 GMT
"""
