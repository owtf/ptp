========
Welcome!
========

Here we present the :mod:`ptp` (*Pentesters' Tools Parser*) project and answer
the *What is it? What does it do? Why does it do it? How does it do it?*
questions.

The project has been developed during the `Google Summer of Code 2014, 10th
edition <https://www.google-melange.com/gsoc/homepage/google/gsoc2014>`_, in
order to create an `automated ranking system
<https://www.owasp.org/index.php/GSoC2014_Ideas#OWASP_OWTF_-_Automated_Vulnerability_Severity_Rankings>`_
for the `OWASP - OWTF project <https://www.owasp.org/index.php/OWASP_OWTF>`_.

OWASP - OWTF in a word
======================

The `OWASP - OWTF project <https://www.owasp.org/index.php/OWASP_OWTF>`_
provides an efficient approach to combine the power of automation with the
out-of-the-box thinking that only the user can provide.

It gathers a complete set of plugins and merges their results into an
interactive report. The user has then the possibility to add notes, to change
details and to add media like screenshots in order to have a complete report.

The goals aimed by :mod:`ptp`
=============================

The primary goal of :mod:`ptp` is to enhance OWASP - OWTF in order to provide
an automated ranking for each plugin. This will allow the user to focus
attention on the most likely weak areas of a web application or network first,
which will be valuable to efficiently use the remaining time in a penetration
assessment.

Instead of evaluating every plugins run by OWASP - OWTF and defining the
rankings for each of them, thanks to :mod:`ptp`, the user will be able to focus
on the ones that have been ranked with the highest risks. The user is then able
to confirm or override the automated rankings since we estimate that she/he is
the only one that can accurately detect the false positives.

When developing the automated ranking system, :mod:`ptp`'s main goal was joined
with a secondary one.  Apart from its main feature which is **ranking the
results from security tools reports**, it also provides an **unified way to
reuse these reports directly in your python code**, without having to deal with
complex parsing.

.. note::

    The long-term objective for :mod:`ptp` is to support all security tools and
    tests. But :mod:`ptp` is in its early development phase and only supports
    the main ones for now.

============
Installation
============

:mod:`ptp` provides the :file:`ptp.pip` file which contains the required
dependencies of the project.

In order to properly configure :mod:`ptp`, the following command should be run:

.. code-block:: bash

    $ pip install -r ptp.pip

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
mode**. This mode tries to reduce as much as possible our work by
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
        'skipfish': [<class 'libptp.tools.skipfish.parser.SkipfishJSParser'>],
        'nmap': [<class 'libptp.tools.nmap.parser.NmapXMLParser'>],
        'dirbuster': [<class 'libptp.tools.dirbuster.parser.DirbusterParser'>],
        'wapiti': [
            <class 'libptp.tools.wapiti.parser.WapitiXMLParser'>,
            <class 'libptp.tools.wapiti.parser.Wapiti221XMLParser'>
        ],
        'owasp-cm-008': [<class 'libptp.tools.owasp.cm008.parser.OWASPCM008Parser'>],
        'w3af': [<class 'libptp.tools.w3af.parser.W3AFXMLParser'>],
        'arachni': [<class 'libptp.tools.arachni.parser.ArachniXMLParser'>],
        'metasploit': [<class
        'libptp.tools.metasploit.parser.MetasploitParser'>],
        'robots': [<class 'libptp.tools.robots.parser.RobotsParser'>]
    }


.. warning::

    The current support to Nmap does not provide any ranking yet.
    Refer to the :doc:`libptp/tools/nmap` section for more information.

Example:

.. code-block:: pycon

    >>> myptp = PTP('skipfish')
    >>> myptp.parse(pathname='my/other/directory')
    [{'ranking': 2}, {'ranking': 2}, {'ranking': 1}]
