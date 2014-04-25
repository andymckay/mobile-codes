Contains the country codes from ISO 3166-1 based on the code based on:

https://github.com/deactivated/python-iso3166/

But also has the MCC and MNC codes based on the Wikipedia page:

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

Lookup by Mobile Country Code (MCC)::

    >>> mobile_codes.mcc("648")
    [Country(name=u'Zimbabwe', alpha2='ZW', alpha3='ZWE', numeric='716', mcc='648')]
    >>> mobile_codes.mcc("311")
    [Country(name=u'Guam', alpha2='GU', alpha3='GUM', numeric='316', mcc=('310', '311')),
     Country(name=u'United States', alpha2='US', alpha3='USA', numeric='840', mcc=('310', '311', '313', '316'))]
    >>> mobile_codes.mcc("313")
    [Country(name=u'United States', alpha2='US', alpha3='USA', numeric='840', mcc=('310', '311', '313', '316'))]

Lookup by name, alpha2, alpha3 (all case insensitive)::

    >>> mobile_codes.alpha3("CAN")
    Country(name=u'Canada', alpha2='CA', alpha3='CAN', numeric='124', mcc='302')
    >>> mobile_codes.alpha2("CA")
    Country(name=u'Canada', alpha2='CA', alpha3='CAN', numeric='124', mcc='302')
    >>> mobile_codes.name('canada')
    Country(name=u'Canada', alpha2='CA', alpha3='CAN', numeric='124', mcc='302')

Lookup operators by mcc (returns a list of all operators)::

    >>> mobile_codes.operators('302')
    [Operator(mcc='302', mnc='220', brand='Telus', operator=u'Telus'),
     Operator(mcc='302', mnc='221', brand='Telus', operator=u'Telus'),...

Lookup operator by mcc and Mobile Network Code (MNC)::

    >>> mobile_codes.mcc_mnc('722', '070')
    Operator(mcc='722', mnc='070', brand='Movistar', operator=u'Movistar')

All lookups raise a KeyError if the requested value is not found.

Development
===========

If you want to do development on the library, follow these steps:

* Create a virtualenv
* bin/pip install -r requirements/tests.txt
* bin/nosetests -s mobile_codes

Changes
=======

0.3
---

- Changed mcc API to always return a list, possibly empty, possibly
  containing multiple countries.

0.2.2
-----

- Some tests, docs changes and updates to the records, thanks hannosch.

0.2
---

- Added in MNC codes and a script to scrape them.

0.1
---

- Added in MCC codes and a lookup.

- Made completely lazy, no records generated or indexed until first asked for.

Contributors
============

* hannosch
