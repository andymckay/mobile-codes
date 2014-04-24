from unittest import TestCase

import mobile_codes


class TestCountries(TestCase):

    def test_mcc(self):
        countries = mobile_codes.mcc('302')
        self.assertEqual(len(countries), 1)
        self.assertEqual(countries[0].mcc, '302')

    def test_mcc_multiple_codes(self):
        countries = mobile_codes.mcc('313')
        self.assertEqual(len(countries), 1)
        self.assertEqual(countries[0].mcc, ('310', '311', '313', '316'))

        # We even get multiple countries with multiple MCC each
        countries = mobile_codes.mcc('310')
        self.assertTrue(len(countries) > 1)
        for country in countries:
            self.assertTrue(len(country.mcc) > 1)

    def test_mcc_multiple_countries(self):
        countries = mobile_codes.mcc('505')
        self.assertEqual(len(countries), 2)

    def test_mcc_fail(self):
        countries = mobile_codes.mcc('000')
        self.assertEqual(len(countries), 0)

    def test_alpha2(self):
        country = mobile_codes.alpha2('CA')
        self.assertEqual(country.alpha2, 'CA')

    def test_alpha2_fail(self):
        self.assertRaises(KeyError, mobile_codes.alpha2, 'XX')

    def test_alpha3(self):
        country = mobile_codes.alpha3('CAN')
        self.assertEqual(country.alpha3, 'CAN')

    def test_alpha3_fail(self):
        self.assertRaises(KeyError, mobile_codes.alpha3, 'XYZ')

    def test_name(self):
        country = mobile_codes.name('canada')
        self.assertEqual(country.name, 'Canada')

    def test_name_fail(self):
        self.assertRaises(KeyError, mobile_codes.name, 'Neverland')

    def test_numeric(self):
        country = mobile_codes.numeric('124')
        self.assertEqual(country.numeric, '124')

    def test_numeric_fail(self):
        self.assertRaises(KeyError, mobile_codes.numeric, '000')


class TestCountriesNoMCC(TestCase):

    def test_alpha2(self):
        country = mobile_codes.alpha2('AQ')
        self.assertEqual(country.mcc, None)

    def test_alpha3(self):
        country = mobile_codes.alpha3('ATA')
        self.assertEqual(country.mcc, None)

    def test_name(self):
        country = mobile_codes.name('antarctica')
        self.assertEqual(country.mcc, None)

    def test_numeric(self):
        country = mobile_codes.numeric('010')
        self.assertEqual(country.mcc, None)


class TestOperators(TestCase):

    def test_mcc(self):
        operators = mobile_codes.operators('302')
        mccs = set([o.mcc for o in operators])
        self.assertEqual(mccs, set(['302']))

    def test_mcc_fail(self):
        operators = mobile_codes.operators('000')
        self.assertEqual(len(operators), 0)

    def test_mcc_mnc(self):
        operator = mobile_codes.mcc_mnc('722', '070')
        self.assertEqual(operator.mcc, '722')
        self.assertEqual(operator.mnc, '070')

    def test_mcc_mnc_fail(self):
        self.assertRaises(KeyError, mobile_codes.mcc_mnc, '000', '001')
