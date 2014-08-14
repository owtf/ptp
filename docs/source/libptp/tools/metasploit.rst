Metasploit
##########

The tool Metasploit is supported by PTP thanks to the following classes.

.. note::

    Since Metasploit does not force the users to follow a specific syntax when
    writing a module, :class:`ptp.PTP` needs to know which ``plugin`` has
    generated the report in order to find the right signature.

Report
******

.. automodule:: libptp.tools.metasploit.report

.. autoclass:: MetasploitReport
    :members:
    :private-members:
    :special-members:

    .. autoattribute:: __tool__
    .. autoattribute:: __parsers__

Parser
******

.. automodule:: libptp.tools.metasploit.parser

.. autoclass:: MetasploitParser
    :members:
    :private-members:
    :special-members:

    .. autoattribute:: __tool__
    .. autoattribute:: __plugin__

Signatures
**********

.. automodule:: libptp.tools.metasploit.signatures
    :members:
