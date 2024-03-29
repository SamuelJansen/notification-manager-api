from distutils.core import setup
import os

print('''Installation on linux, run:
sudo apt install libpq-dev python3-dev
pip3.9 install --no-cache-dir python-framework --force --upgrade

Aliases:
sudo rm /usr/bin/python
sudo ln -s /usr/local/bin/pythonX.Y /usr/bin/python

sudo rm /usr/bin/pip
sudo ln -s /usr/local/bin/pipX.Y /usr/bin/pip
''')

VERSION = '0.0.14'

SNAKE_CASE_NAME = 'notification_manager_api'
PACKAGE_NAME = SNAKE_CASE_NAME
REPOSITORY_NAME = SNAKE_CASE_NAME.replace('_', '-')
API = 'api'
SRC = 'src'
RESOURCE = 'resource'
PROVIDER = 'provider'
URL = f'https://github.com/SamuelJansen/{REPOSITORY_NAME}/'

OS_SEPARATOR = os.path.sep

setup(
    name = SNAKE_CASE_NAME,
    packages = [
        PACKAGE_NAME,
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}config',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}constant',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}converter',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}converter{OS_SEPARATOR}static',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}dto',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}enumeration',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}manager',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}{PROVIDER}',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}{PROVIDER}{OS_SEPARATOR}service',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}{PROVIDER}{OS_SEPARATOR}client',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}{PROVIDER}{OS_SEPARATOR}client{OS_SEPARATOR}emitter',
        f'{PACKAGE_NAME}{OS_SEPARATOR}{API}{OS_SEPARATOR}{SRC}{OS_SEPARATOR}{PROVIDER}{OS_SEPARATOR}validator'
    ],
    # data_files = [
    #     (STATIC_PACKAGE_PATH, [
    #         f'{RELATIVE_PATH}{OS_SEPARATOR}resource_1.extension',
    #         f'{RELATIVE_PATH}{OS_SEPARATOR}resource_2.extension'
    #     ])
    # ],
    version = VERSION,
    license = 'MIT',
    description = 'Queue Manager',
    author = 'Samuel Jansen',
    author_email = 'samuel.jansenn@gmail.com',
    url = URL,
    download_url = f'{URL}archive/v{VERSION}.tar.gz',
    keywords = ['queue', 'topic'],
    install_requires = [
        'python-framework<1.0.0,>=0.4.8',
        'queue-manager-api<1.0.0,>=0.1.41',
        'globals<1.0,>=0.3.34',
        'python-helper<1.0,>=0.3.51'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    python_requires='>=3.7'
)
