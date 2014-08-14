========
Welcome!
========

Here we present the :mod:`ptp` (*Pentesters' Tools Parser*) project.

Before coding anything, let us start with some brief explanation about the
project, its context and its aims.

The project has been developed during the `Google Summer of Code 2014, 10th
edition <https://www.google-melange.com/gsoc/homepage/google/gsoc2014>`_, in
order to create an `automated ranking system
<https://www.owasp.org/index.php/GSoC2014_Ideas#OWASP_OWTF_-_Automated_Vulnerability_Severity_Rankings>`_
for the `OWASP - OWTF project <https://www.owasp.org/index.php/OWASP_OWTF>`_.

But :mod:`ptp` tries to go even beyond the original idea.

Apart from its main feature which is **ranking the results from any security
reports**, it also provides an **unified way to reuse these reports directly in
your python code**, without having to deal with complexe parsing.

.. note::

    When we say **any**, we mean that it is our ultimate goal. For now,
    :mod:`ptp` is in its early development phase and *only* supports a small
    amount of tools.

Let us now see how to install and use :mod:`ptp`!

============
Installation
============

:mod:`ptp` provides the :file:`ptp.pip` file which contains the required
dependencies of the project.

In order to properly configure :mod:`ptp`, the following command should be run:

.. code-block:: bash

    $ pip install -r ptp.pip

Now that :mod:`ptp` is correctly installed, let us see what it offers as basic
usages.

============
Basic usages
============

In this section, we see what we can expect from the library for basic purposes.

First we use the simplest mode a.k.a the **auto-detection mode** in which we do
not even have to specify the tool.
Then, the **explicit mode** in which we specify what tool generated our report.

Auto-detection mode
===================

The simplest way to use :mod:`ptp` library is by using its **auto-detection
mode**. This mode try to reduce as much as possible the usages for us by
auto-detecting which tool has generated a given report.

That way, we do not have to bother knowing if the report we want to parse comes
from `W3AF <http://w3af.org/>`_, `DirBuster
<https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project>`_ or even
`Skipfish <https://code.google.com/p/skipfish/>`_.

Example:

.. code-block:: pycon

    >>> from ptp import PTP
    >>> myptp = PTP()
    >>> myptp.parse(pathname='my/directory', filename='my_report')
    [{'ranking': 4}, ..., {'ranking': 3}, ..., {'ranking': 1}]

.. note::

    In the example above, the filename could have been omitted. In that case,
    :class:`ptp.PTP` would have recursively walked into the directory
    `pathname` until a file would have matched one supported tool.

    For instance, we could have done:

    >>> from ptp import PTP
    >>> myptp = PTP()
    >>> myptp.parse(pathname='my/directory')
    [{'ranking': 4}, ..., {'ranking': 3}, ..., {'ranking': 1}]

    Be careful though, when omitting the `filename` parameter, :class:`ptp.PTP`
    will stop as soon as a supported report file will be found! (i.e.
    :class:`ptp.PTP` will not parse all the files in the `pathname` directory.)

If we are only looking for the highest risk that is listed in the report, we
can use the following function:

.. code-block:: pycon

    >>> myptp.get_highest_ranking()
    4
    >>> from libptp.constants import HIGH
    >>> myptp.get_highest_ranking() == HIGH
    True

.. note::

    To know the possible ranking values, please refer to the
    :doc:`libptp/constants` section.

If we are interested in the name of the tool that generated the report, it is
stored in the :class:`ptp.PTP` class and can be retrieved like below:

.. code-block:: pycon

    >>> print(myptp.tool_name)
    arachni  # In our case, it is Arachni that has generated our report.

The big advantage in using the auto-detection mode is that :class:`ptp.PTP`
does all the job for us.

One possible drawback would be that it is slower than if :class:`ptp.PTP` knew
which tool had generated the report. Indeed :class:`ptp.PTP` has to go through
all its supported tool classes and asked them if it supports the current file.

Explicit mode
=============

If we already know which tool has generated the report, we can explicitly give
that information to :class:`ptp.PTP`. That will even speed up the whole process
since it will not have to lookup for the right parser.

The list of the supported tools can be found like below:

.. code-block:: pycon

    >>> PTP.supported
    {
        'metasploit': <class 'libptp.tools.metasploit.report.MetasploitReport'>,
        'w3af': <class 'libptp.tools.w3af.report.W3AFReport'>,
        'nmap': <class 'libptp.tools.nmap.report.NmapReport'>,
        'owasp-cm-008': <class 'libptp.tools.owasp.cm008.report.OWASPCM008Report'>,
        'arachni': <class 'libptp.tools.arachni.report.ArachniReport'>,
        'robots': <class 'libptp.tools.robots.report.RobotsReport'>,
        'wapiti': <class 'libptp.tools.wapiti.report.WapitiReport'>,
        'skipfish': <class 'libptp.tools.skipfish.report.SkipfishReport'>,
        'dirbuster': <class 'libptp.tools.dirbuster.report.DirbusterReport'>
    }

.. warning::

    The current support to Nmap does not provide any ranking yet.
    Refer to the :doc:`libptp/tools/nmap` section for more information.

Example:

.. code-block:: pycon

    >>> myptp = PTP('skipfish')
    >>> myptp.parse(pathname='my/other/directory')
    [{'ranking': 2}, {'ranking': 2}, {'ranking': 1}]
