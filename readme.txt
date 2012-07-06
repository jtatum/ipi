ipi allows you to store archived third party dependencies inside your
application and install them at runtime. This differs slightly from pip
where the installation generally happens prior to runtime and typically the
packages are downloaded from the Internet on execution of pip.

Example:

You want to install BeautifulSoup and use it in your application. Copy
ipi and the BeautifulSoup source tarball from PyPi into your application
like so:

MyApp
 - ipi
 |- (ipi files)
 |- BeautifulSoup-1.2.3.tar.gz

Your application should import ipi first. This will install or update
BeautifulSoup:

# MyApp.py

import ipi
import BeautifulSoup

Note that ipi essentially calls easy_install on the file. Your application
will either need to be inside a virtualenv or run as root for easy_install
to work.

To run unit tests, lettuce must be installed. Call lettuce in the ipi
directory.