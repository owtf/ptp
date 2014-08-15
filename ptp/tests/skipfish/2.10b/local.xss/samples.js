var mime_samples = [
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

