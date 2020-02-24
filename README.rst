.. image:: https://github.com/adonmo/trajectory/workflows/Tests/badge.svg
   :target: https://github.com/adonmo/trajectory/actions
   :alt: Test Status

.. image:: https://img.shields.io/pypi/dm/trajectory.svg
   :target: https://pypistats.org/packages/trajectory
   :alt: PyPI downloads

.. image:: https://img.shields.io/github/license/adonmo/trajectory.svg
   :target: https://github.com/adonmo/trajectory/blob/master/LICENSE
   :alt: MIT License

trajectory
============

``trajectory`` is a library for lossy compression of trajectory data based on Google's Encoded Polyline Algorithm Format (http://goo.gl/PvXf8Y). It is heavily based on (in fact forked from) https://github.com/hicsail/polyline.

Installation
============

``trajectory`` can be installed using ``pip`` or ``easy_install``

.. code-block:: sh

    $ pip install trajectory
    or
    $ easy_install trajectory

API Documentation
=================

Encoding
--------

To serialize a trajectory (set of (lat, lon, unix time in seconds) tuples)

.. code-block:: py

    import trajectory
    trajectory.encode([
        (38.500, -120.200, 1582482601),
        (40.700, -120.950, 1582482611),
        (43.252, -126.453, 1582482627)
    ], 5)

This should return ``_p~iF~ps|U_ynpijgz~G_ulLnnqC_c`|@_mqNvxq`@__t`B``.

You can set the required precision with the optional ``precision`` parameter. The default value is 5.

Decoding
--------

To deserialize a trajectory (set of (lat, lon, unix time in seconds) tuples) represented by an encoded string

.. code-block:: py

    import trajectory
    trajectory.decode('_p~iF~ps|U_ynpijgz~G_ulLnnqC_c`|@_mqNvxq`@__t`B', 5)

This should return the following:

.. code-block:: py

    [
        (38.500, -120.200, 1582482601),
        (40.700, -120.950, 1582482611),
        (43.252, -126.453, 1582482627)
    ]

You can set the required precision with the optional ``precision`` parameter. The default value is 5.


Development
===========

Setup Dependencies
------------------

.. code-block:: sh

    $ poetry install

Running Tests
-------------

.. code-block:: sh

    $ poetry run pytest

Contributing
------------

Issues and pull requests are welcome.

* For proposing new features/improvements or reporting bugs, `create an issue <https://github.com/adonmo/trajectory/issues/new/choose>`_.
* Check `open issues <https://github.com/adonmo/trajectory/issues>`_ for viewing existing ideas, verify if it is already proposed/being worked upon.
* When implementing new features make sure to add relavant tests and documentation before sending pull requests.
