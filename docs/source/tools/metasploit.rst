Metasploit
##########

.. note::

    Since Metasploit does not force the users to follow a specific syntax when
    writing a module, :class:`PTP` needs to know which ``plugin`` has
    generated the report in order to find the right signature.

Parser
******

.. automodule:: tools.metasploit.parser

.. autoclass:: MetasploitParser
    :members:
    :private-members:
    :special-members:

    .. autoattribute:: __tool__
    .. autoattribute:: __plugin__

Signatures
**********

.. automodule:: tools.metasploit.signatures
    :members:
