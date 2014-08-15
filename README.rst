============
What is PTP?
============

The primary goal of ptp (Pentester's Tools Parser) is to enhance `OWASP - OWTF
project <https://www.owasp.org/index.php/OWASP_OWTF>`_ in order to provide an
automated ranking for each plugin. This will allow the user to focus attention
on the most likely weak areas of a web application or network first, which will
be valuable to efficiently use the remaining time in a penetration assessment.

Instead of evaluating every plugins run by OWASP - OWTF and defining the
rankings for each of them, thanks to `ptp`, the user will be able to focus
on the ones that have been ranked with the highest risks. The user is then able
to confirm or override the automated rankings since we estimate that she/he is
the only one that can accurately detect the false positives.

When developing the automated ranking system, `ptp`'s main goal was joined
with a secondary one.

Apart from its main feature which is **ranking the results from security tools
reports**, it also provides an **unified way to reuse these reports directly in
your python code**, without having to deal with complex parsing.

============
Installation
============


The first step is to clone the repository of the project:

.. code-block:: bash

    $ git clone https://github.com/owtf/ptp.git

Then the script `setup.py` must be run:

.. code-block:: bash

    $ ./setup.py install

=====
Usage
=====

.. code-block:: python

    from __future__ import print_function
    from ptp import PTP


    if __name__ == '__main__':
        ptp = PTP()
        ptp.parse('path/to/the/report/directory')
        print('Highest severity:', ptp.get_highest_ranking())

=============
Documentation
=============

The ptp's documentation is available online at the following address:
`http://owtf.github.io/ptp/ <http://owtf.github.io/ptp/>`_.

It explained how to use the library and even how to contribute. Plus it
contains the technical documentation of the project.

===============
Current support
===============

+ arachni (0.4.6) (XML report)
+ dirbuster (1.0-RC1)
+ metasploit
+ owasp
+ robots.txt
+ skipfish (2.10b)
+ w3af (1.6.0.2, 1.6.0.3) (XML report)
+ wapiti (2.2.1, 2.3.0) (XML report)
