from setuptools import setup


setup(
    name='mobile-codes',
    version='0.2.2',
    description='Library of ISO 3166, MCC and MNC codes',
    long_description=open('README.rst').read(),
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    url='https://github.com/andymckay/mobile-codes',
    include_package_data=True,
    packages=['mobile_codes'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ]
)
