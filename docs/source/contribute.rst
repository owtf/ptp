=====================
Write our own support
=====================

Here we explain how we can contribute to the project by hacking into
:mod:`ptp`'s source code and enhance its list of supported tools.

First of all, we have to write a parser for our target tool. In our case, let
us assume that the tool is named *MyTool* and that we want to parse its XML
formatted reports.

The parser source code must be saved into the `tools/<tool name>/` and
be named `parser.py`. Therefore, the parser for *MyTool* will be saved under
the name `tools/mytool/parser.py`.

=================
MyXMLParser class
=================

In order for :mod:`ptp` to correctly retrieve the information that are
contained in a tool report, it needs a specialized parser.

Let's start by writing the skeleton of our parser class. Since we are aiming to
support *MyTool*'s XML reports, :ref:`xmlparser-label` seems to be the best
class from which to inherit.

The :ref:`xmlparser-label` already defines
:meth:`ptp.libptp.parser.XMLParser.handle_file` for us. This will initialize
the :attr:`MyXMLParser.stream` instance variable with a handle on the root node
of the file.

The skeleton
============

By convention, the class name must contain the format it parses (in our case
`XML`).

.. code-block:: python

    from ptp.libptp.parser import XMLParser


    class MyXMLParser(XMLParser):
        """Specialized parser for MyTool."""

        __tool__ = 'mytool'
        __version__ = r'0\.1'

        def __init__(self, pathname, filename='*.xml', first=True):
            """Initialize MyXMLParser.

            :param str pathname: Path to the report directory.
            :param str filename: Regex matching the report file.
            :param bool first: Only process first file (``True``) or each file
                that matched (``False``).

            """
            XMLParser.__init__(self, pathname, filename, first=first)

We added a couple of class attributes in order to give some information
about what tool is parsed by our class and the supported versions.

Since our parser inherits from :ref:`xmlparser-label`, we do not have to
specify the `__format__` class attribute, which is already set to `xml`.

.. note::

    In order to keep the tool name homogene with the rest of the code base,
    `__tool__` must be lowercased.

    Also, both the `__format__` and the `__version__` attributes are optional.

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

    class MyXMLParser(XMLParser):
        """Specialized parser for MyTool."""

        __tool__ = 'mytool'
        __version__ = r'0\.1'

        # Omitted unchanged code

        @classmethod
        def is_mine(cls, pathname, filename='*.xml', first=True):
            """Check if it is a supported MyTool report.

            :param str pathname: Path to the report directory.
            :param str filename: Regex matching the report file.
            :param bool first: Only process first file (``True``) or each file
                that matched (``False``).

            :return: `True` if it supports the report, `False` otherwise.
            :rtype: :class:`bool`

            """
            try:
                stream = cls.handle_file(pathname, filename, first=first)
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
            if not re.findall(cls.__version__, stream.get('version')):
                return False
            return True

Parsing methods
===============

Each :ref:`AbstractParser <abstractparser-class-label>` class has to provide
two methods:

* :meth:`ptp.libptp.parser.AbstractParser.parse_metadata` which parses the
  metadata of the report and formats them into a :class:`dict`.
* :meth:`ptp.libptp.parser.AbstractParser.parse_report` which parses the
  discoveries that are listed in the report and formats them into a
  :class:`list` of :class:`dict`.

In order to keep it simple, we will not detail the implementations of these
methods for our fake tool.

.. code-block:: python

    import re

    from ptp.libptp.parser import XMLParser


    class MyXMLParser(XMLParser):
        """Specialized parser for MyTool."""

        __tool__ = 'mytool'
        __version__ = r'0\.1'

        def __init__(self, pathname, filename='*.xml', first=True):
            """Initialize MyXMLParser.

            :param str pathname: Path to the report directory.
            :param str filename: Regex matching the report file.
            :param bool first: Only process first file (``True``) or each file
                that matched (``False``).

            """
            XMLParser.__init__(self, pathname, filename, first=first)

        @classmethod
        def is_mine(cls, pathname, filename='*.xml', first=True):
            """Check if it is a supported MyTool report.

            :param str pathname: Path to the report directory.
            :param str filename: Regex matching the report file.
            :param bool first: Only process first file (``True``) or each file
                that matched (``False``).

            :return: `True` if it supports the report, `False` otherwise.
            :rtype: :class:`bool`

            """
            try:
                stream = cls.handle_file(pathname, filename, first=first)
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
            if not re.findall(cls.__version__, stream.get('version')):
                return False
            return True

        def parse_metadata(self):
            return {}  # The expected behavior is to return a dict.

        def parse_report(self):
            return []  # The expected behavior is to return a list.

===============
Tell :mod:`ptp`
===============

Now that *MyTool* is supported thanks to our implementation of `MyXMLParser`,
we only have one more thing to do in order to finish.

We need to update the :attr:`ptp.PTP.supported` list attribute by inserting our
`MyXMLParser` inside like shown below:

.. code-block:: python

    # Omitted imports

    from ptp.tools.mytool.parser import MyXMLParser

    class PTP(object):

        # Omitted lines

        supported = {

            # Omitted supported tools.

            'w3af': [W3AFXMLParser],

            # Omitted supported tools.

            'mytool': [MyXMLParser]}

We have done it! We have written our own support to the tool *MyTool* and
integrated that into :mod:`ptp`!

Congratulations!
