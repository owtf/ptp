OWASP
#####

The OWASP tests are supported by PTP thanks to the following classes.

CM-008
******

`OWASP-CM-008
<https://www.owasp.org/index.php/Test_HTTP_Methods_(OTG-CONFIG-006)>`_ tests
the HTTP methods of a website that are available.

Report
------

.. automodule:: libptp.tools.owasp.cm008.report

.. autoclass:: OWASPCM008Report
    :members:
    :private-members:
    :special-members:

    .. autoattribute:: __tool__
    .. autoattribute:: __parsers__

Parser
------

.. automodule:: libptp.tools.owasp.cm008.parser

.. autoclass:: OWASPCM008Parser
    :members:
    :private-members:
    :special-members:

    .. autoattribute:: __tool__

Signatures
----------

.. automodule:: libptp.tools.owasp.cm008.signatures
    :members:
