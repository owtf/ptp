# PTP

Pentester's tools parser provides an unified way to retrieve the information
from all (final goal) automated pentesting tools.

# General

This standalone library is created in order to be used by
[OWTF](https://github.com/owtf) when it will try to retrieve the automated
rankings already provided by some pentesting tools.

# Features

+ Auto-detection of the tool that generated the report.

# Usage

```python
from __future__ import print_function
from ptp import PTP


if __name__ == '__main__':
    ptp = PTP()
    ptp.parse('path/to/the/report/directory')
    print('Highest severity:', ptp.get_highest_ranking())
```

# Current support

+ arachni (0.4.6) (XML report)
    + Metadata
    + Rankings
+ dirbuster (1.0-RC1)
    + Rankings
+ metasploit
    + Rankings
        + Scanner modules
+ nmap (XML report)
    + Metadata
+ skipfish (2.10b)
    + Metadata
    + Rankings
+ w3af (1.6.0.2, 1.6.0.3) (XML report)
    + Metadata
    + Rankings
+ wapiti (2.2.1, 2.3.0) (XML report)
    + Metadata
    + Rankings
    + Names
    + Descriptions
