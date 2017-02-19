from distutils.core import setup
import sys

requires = [
    'flask',
    'premailer',
    'requests',
    'sqlalchemy',
    'stripe',
    'mako',
    'psycopg2',
    'waitress',
    'mailchimp3',
]

if sys.version_info < (3, 5):
    requires.append('typing')

setup(
    name='uqcs-signup',
    version='0.2.0',
    packages=[
        'uqcs.models',
        'uqcs.app',
        'uqcs.__main__',
        'uqcs'
    ],
    install_requires=requires,
    package_dir={'uqcs.join': 'app'},
    url='https://join.uqcs.org.au',
    license='MIT',
    author='Tom Manderson',
    author_email='me@trm.io',
    description='The UQCS payment systems for membership signup'
)