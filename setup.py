from setuptools import setup

long_description = (open('README.rst').read() + '\n' +
                    open('CHANGES.rst').read())

setup(
    name='mobile-codes',
    version='0.7',
    description='Library of ISO 3166, MCC and MNC codes',
    long_description=long_description,
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
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
