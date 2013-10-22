Contains the country codes from ISO 3166-1 based on the code based on:

https://github.com/deactivated/python-iso3166/

But also has the MCC codes based on the Wikipedia page:

http://en.wikipedia.org/wiki/List_of_mobile_country_codes

Note that MCC codes for a country can be:

* None (no MCC code)
* a string (where a country has one code)
* a tuple of strings (where a country has more than one code)

Installation
============

::

    $ pip install mobile-codes

Usage
=====

::

    >>> import mobile_codes
    >>> mobile_codes.mcc("648")
    Country(name=u'Zimbabwe', alpha2='ZW', alpha3='ZWE', numeric='716', mcc='648')
    >>> mobile_codes.mcc("310")
    Country(name=u'United States', alpha2='US', alpha3='USA', numeric='840', mcc=('310', '311', '313', '316'))
    >>> mobile_codes.mcc("313")
    Country(name=u'United States', alpha2='US', alpha3='USA', numeric='840', mcc=('310', '311', '313', '316'))
    >>> mobile_codes.alpha3("CAN")
    Country(name=u'Canada', alpha2='CA', alpha3='CAN', numeric='124', mcc='302')

Changes
=======

0.1: From the original.

- Added in MCC codes and a lookup.

- Made completely lazy, no records generated or indexed until first asked for.
