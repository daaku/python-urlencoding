urlencoding
===========

A `python <http://python.org/>`_ library for query string parsing and
generation.

The code is hosted
`here at github <https://github.com/nshah/python-urlencoding/tree/master>`_.
The latest code can be downloaded as a
`zip file <http://github.com/nshah/python-urlencoding/zipball/master>`_ or a
`tarball <http://github.com/nshah/python-urlencoding/tarball/master>`_.

Requires Python 2.5 or newer.

Can be installed using `pip <http://pip.openplans.org/>`_::

    pip install -e 'git://github.com/nshah/python-urlencoding.git#egg=urlencoding'

.. toctree::

*********
Functions
*********

.. autofunction:: urlencoding.escape
.. autofunction:: urlencoding.parse_qs
.. autofunction:: urlencoding.compose_qs(params, sort=False)
