# PTP

Pentester's tools parser provides an unified way to retrieve the information
from all (final goal) automated pentesting tools.

# General

This standalone library is created in order to be used by
[OWTF](https://github.com/owtf) when it will try to retrieve the automated
rankings already provided by some pentesting tools.

# Usage

```python
from __future__ import print_function
from ptp import PTP


if __name__ == '__main__':
    ptp = PTP('arachni')
    ptp.parse(
        path_to_report='path/to/arachni/report/directory',
        filename='report_name.xml')
    print('Highest severity:', ptp.get_highest_ranking())
```

# Current support

+ skipfish (2.10b)
+ arachni (0.4.6) (XML report)
+ w3af (1.6.0.2) (XML report)
