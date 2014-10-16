Changes
=======

0.6 - 2014-10-14
----------------

- Move network and country constants into JSON files
- Incorporate ITU data for operators

0.5 - unreleased
----------------


0.4 - 2014-06-13
----------------

- Declare compatibility with Python 3.4.
- Fix a number of country to mcc mappings.
- Issue #9: Fix typo in mcc for Yemen.
- Issue #10: Allow 310 as a mcc value for Puerto Rico.

0.3 - 2014-05-14
----------------

- Changed mcc API to always return a list, possibly empty, possibly
  containing multiple countries.

0.2.2 - 2014-04-22
------------------

- Some tests, docs changes and updates to the records, thanks hannosch.

0.2 - 2013-10-26
----------------

- Added in MNC codes and a script to scrape them.

0.1 - 2013-10-22
----------------

- Added in MCC codes and a lookup.

- Made completely lazy, no records generated or indexed until first asked for.
