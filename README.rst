========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/rapid-models/badge/?style=flat
    :target: https://readthedocs.org/projects/rapid-models
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/simeld/rapid-models.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/simeld/rapid-models

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/simeld/rapid-models?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/simeld/rapid-models

.. |requires| image:: https://requires.io/github/simeld/rapid-models/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/simeld/rapid-models/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/simeld/rapid-models/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/simeld/rapid-models

.. |version| image:: https://img.shields.io/pypi/v/rapid-models.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/rapid-models

.. |wheel| image:: https://img.shields.io/pypi/wheel/rapid-models.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/rapid-models

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/rapid-models.svg
    :alt: Supported versions
    :target: https://pypi.org/project/rapid-models

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/rapid-models.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/rapid-models

.. |commits-since| image:: https://img.shields.io/github/commits-since/simeld/rapid-models/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/simeld/rapid-models/compare/v0.0.0...master



.. end-badges

Package to support more specific, accurate and timely decision support in operation of safety-critical systems, by
combining physics-based modelling with data-driven machine learning and probabilistic uncertainty assessment.

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Installation
============

::

    pip install rapid-models

You can also install the in-development version with::

    pip install https://github.com/simeld/rapid-models/archive/master.zip


Documentation
=============


https://rapid-models.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
