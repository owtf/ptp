=====================
Write our own support
=====================

Here we explain how we can contribute to the project by hacking into
:mod:`ptp`'s source code and enhance its list of supported tools.

First of all, we have to write a parser for our target tool. In our case, let
us assume that the tool is named *MyTool* and that we want to parse its XML
formatted reports.

==============
MyParser class
==============

In order for :mod:`ptp` to correctly retrieve the information that are
contained in a tool report, it needs a specialized parser.

Let's start by writing the skeleton of our parser class. Since we are aiming to
support *MyTool*'s XML reports, :ref:`xmlparser-label` seems to be the best
class from which to inherit.

The :ref:`xmlparser-label` already defines
:meth:`libptpt.parser.XMLParser.handle_file` for us. This will initialize the
:attr:`MyParser.stream` instance variable with a handle on the root node of the
file.

The skeleton
============

Time to write this famous skeleton!

.. code-block:: python

    from libptp.parser import XMLParser


    class MyParser(XMLParser):
        """Specialized parser for MyTool."""

        def __init__(self, fullpath):
            """Self-explanatory."""
            XMLParser.__init__(self, fullpath)

The :meth:`__init__`'s `fullpath` parameter will be the path to the report file
plus its name. For instance `'full/path/to/myreport.xml'`.

.. note::

    The `fullpath` can be both relative or absolute.

Then we add a couple of class attributes in order to give some information
about what tool is parsed by our class and the supported versions.

Since our parser inherits from :ref:`xmlparser-label`, we do not have to
specify the `__format__` class attribute, which is already set to `.xml`.

.. code-block:: python

    class MyParser(XMLParser):
        """Specialized parser for MyTool."""

        __tool__ = 'mytool'
        __version__ = ['0.1']

        def __init__(self, fullpath):
            """Self-explanatory."""
            XMLParser.__init__(self, fullpath)

.. _toolname-conv-label:

.. note::

    In order to keep the tool name homogene with the rest of the code base,
    `__tool__` must be lowercased.

.. note::

    Both the `__format__` and the `__version__` attributes are optional.

    For instance `__version__` is optional because some tools don't provide
    such information (e.g. robots.txt).

Matching the supported reports
==============================

The next step is to write the :meth:`is_mine` class method which tells
:mod:`ptp` whether or not it can parse the report file.

Let us say that *MyTool*'s XML report has `<mytool version='x.x'>`
as the root XML tag.

Therefore, our :meth:`is_mine` function is:

.. code-block:: python

    class MyParser(XMLParser):
        """Specialized parser for MyTool."""

        __tool__ = 'mytool'
        __version__ = ['0.1']

        # Omitted unchanged code

        @classmethod
        def is_mine(cls, fullpath):
            """Check if it is a supported MyTool report.

            :param str fullpath: full path to the report file.

            :return: `True` if it supports the report, `False` otherwise.
            :rtype: :class:`bool`

            """
            try:
                stream = cls.handle_file(fullpath)
            except (ValueError, LxmlError):
                # If an error occurs when trying to open the file, then the
                # parser cannot deal with it.
                return False
            # The root tag must contain 'mytool'.
            if not cls.__tool__ in stream.tag:
                return False
            # Check if the root node has a 'version' attribute.
            if not 'version' in stream:
                return False
            # Check if the version is the one this parser supports.
            if not stream.get('version') in cls.__version__:
                return False
            return True

Parsing methods
===============

Each :ref:`AbstractParser <abstractparser-class-label>` class has to provide
two methods:

* :meth:`libptp.parser.AbstractParser.parse_metadata` which parses the metadata
  of the report and formats them into a :class:`dict`.
* :meth:`libptp.parser.AbstractParser.parse_report` which parses the
  discoveries that are listed in the report and formats them into a
  :class:`list` of :class:`dict`.

In order to keep it simple, we will not detail the implementations of these
methods for our fake tool.

.. code-block:: python

    from libptp.parser import XMLParser

    class MyParser(XMLParser):
        """Specialized parser for MyTool."""

        __tool__ = 'mytool'
        __version__ = ['0.1']

        def __init__(self, fullpath):
            """Self-explanatory."""
            XMLParser.__init__(self, fullpath)

        @classmethod
        def is_mine(cls, fullpath):
            """Check if it is a supported MyTool report.

            :param str fullpath: full path to the report file.

            :return: `True` if it supports the report, `False` otherwise.
            :rtype: :class:`bool`

            """
            try:
                stream = cls.handle_file(fullpath)
            except (ValueError, LxmlError):
                return False
            if not cls.__tool__ in stream.tag:
                return False
            if not 'version' in stream:
                return False
            if not stream.get('version') in cls.__version__:
                return False
            return True

        def parse_metadata(self):
            return {}  # The expected behavior is to return a dict.

        def parse_report(self):
            return []  # The expected behavior is to return a list.

==============
MyReport class
==============

The skeleton
============

In order to support a tool, :mod:`ptp` needs a report class that will describe
how the reports of the target tool behave. The `__tool__` attribute must follow
the same convention as when writing the parser (see. the :ref:`Skeleton
<toolname-conv-label>` section)

.. code-block:: python

    from libptp.report import AbstractReport


    class MyReport(AbstractReport):
        """Specialized report for MyTool."""

        __tool__ = 'mytool'

        def __init__(self):
            """Self-explanatory."""
            AbstractReport.__init__(self)

Default :meth:`is_mine` method
==============================

:class:`libptp.report.AbstractReport` already defines the default behavior
of the :meth:`libptp.report.AbstractReport.is_mine` class method. It consists
in finding the first file matching the `filename` regex parameter and go
through each of its parsers in order to find the right one.

What we need to do is specify such filename regex and which parsers are
availables.

.. code-block:: python

    from libptp.report import AbstractReport
    # We don't forget to import the parser we just wrote.
    from libptp.tools.mytool.parser import MyParser


    class MyReport(AbstractReport):
        """Specialized report for MyTool."""

        # We link the report with the parser we have written before.
        __parsers__ = [MyParser]

        # Omitted unchanged code

        @classmethod
        def is_mine(cls, pathname, filename='*.xml'):
            """Check if it is a MyTool report and if it can handle it.

            :param str pathname: Path to the report directory.
            :param str filename: Regex matching the report file.

            :return: `True` if it supports the report, `False` otherwise.
            :rtype: :class:`bool`

            """
            return AbstractReport.is_mine(
                cls.__parsers__,  # Our parser.
                pathname=pathname,
                filename=filename)  # The regex will match XML files.

Parse method
============

we need to override the :meth:`libptp.report.AbstractReport.parse` method. That
will specify how to deal with the data that was retrieved by our parser.

The first step is to first retrieve the report. Here we follow the simplest
idea that is using the `filename` regex in order to retrieve the first report
file that matches.

.. code-block:: python

    class MyReport(AbstractReport):
        """Specialized report for MyTool."""

        # Omitted unchanged code

        def parse(self, pathname, filename='*.xml'):
            # Reconstruct the path to the report if any.
            self.fullpath = self._recursive_find(pathname, filename)
            if not self.fullpath:
                return []
            self.fullpath = self.fullpath[0]

Then we need to initialize the correct parser using the
:meth:`libptp.report.AbstractReport._init_parser` method.

.. code-block:: python

    class MyReport(AbstractReport):
        """Specialized report for MyTool."""

        # Omitted unchanged code

        def parse(self, pathname, filename='*.xml'):
            # Omitted unchanged code

            # Find the corresponding parser.
            self._init_parser(self.fullpath)

And finally retrieve the data we want. In our case, we will retrieve both the
metadata and the discoveries listed in the XML report.

.. code-block:: python

    class MyReport(AbstractReport):
        """Specialized report for MyTool."""

        # Omitted unchanged code

        def parse(self, pathname, filename='*.xml'):
            # Omitted unchanged code

            # Parse specific data.
            self.metadata = self.parser.parse_metadata()
            self.vulns = self.parser.parse_report()
            return self.vulns

.. note::

    The :meth:`parse` method must always return a :class:`list` of the
    discoveries.

If we put all the pieces together, we end up with the following
:class:`MyReport` implementation.

.. code-block:: python

    from libptp.report import AbstractReport
    from libptp.tools.mytool.parser import MyParser


    class MyReport(AbstractReport):
        """Specialized report for MyTool."""

        __tool__ = 'mytool'
        __parsers__ = [MyParser]

        @classmethod
        def is_mine(cls, pathname, filename='*.xml'):
            """Check if it is a MyTool report and if it can handle it.

            :param str pathname: Path to the report directory.
            :param str filename: Regex matching the report file.

            :return: `True` if it supports the report, `False` otherwise.
            :rtype: :class:`bool`

            """
            return AbstractReport.is_mine(
                cls.__parsers__,
                pathname=pathname,
                filename=filename)


        def parse(self, pathname, filename='*.xml'):
            """Parse a MyTool report.

            :param str pathname: Path to the report directory.
            :param str filename: Regex matching the report file.

            :return: List of dicts where each one represents a discovery from
                the report.
            :rtype: :class:`list`

            """
            # Reconstruct the path to the report if any.
            self.fullpath = self._recursive_find(pathname, filename)
            if not self.fullpath:
                return []
            self.fullpath = self.fullpath[0]
            # Find the corresponding parser.
            self._init_parser(self.fullpath)
            # Parse specific data.
            self.metadata = self.parser.parse_metadata()
            self.vulns = self.parser.parse_report()
            return self.vulns

===============
Tell :mod:`ptp`
===============

Now that *MyTool* is supported thanks to our implementation of `MyParser` and
`MyReport`, we only have one more thing to do in order to finish.

We need to update the :attr:`ptp.supported` list attribute by inserting our
`MyReport` inside like shown below:

.. code-block:: python

    # Omitted imports

    from libptp.tools.mytool.report import MyReport

    class PTP(object):

        # Omitted lines

        supported = {

            # Omitted supported tools.

            'w3af': W3AFReport,

            # Omitted supported tools.

            'mytool': MyReport}

We have done it! We have written our own support to the tool *MyTool* and
integrated that into :mod:`ptp`!

Congratulations!
