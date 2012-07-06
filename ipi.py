###
# Copyright (c) 2012, James Tatum
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###

from setuptools.command import easy_install
import glob
import sys
import os


def _parse_filename(filename):
    """Take an archive filename and parse out the package name and version

       Returns (package, version)
       If passed BeautifulSoup-3.2.1.tar.gz, will return a tuple:
       ('BeautifulSoup', '3.2.1')
    """
    (package, version) = filename.rsplit('.tar.gz')[0].rsplit('-',1)
    return (package, version)


def install():
    """Install all archives in this directory

       This code searches the current working directory for all files ending
       in .tar.gz and installs/updates them
    """
    import pkg_resources
    this_dir = os.path.split(os.path.abspath(__file__))[0]

    # Find package archives
    files = glob.glob('%s/*.tar.gz' % this_dir)

    for filename in files:
        # strip directory
        base_filename = os.path.basename(filename)

        (package, version) = _parse_filename(base_filename)

        try:
            # Ask pkg_resources to find a package/egg with the right name
            # and version. If this works, there's no reason to do anything
            # more.
            pkg_resources.require('%s==%s' % package, version)
        except (pkg_resources.VersionConflict, pkg_resources.DistributionNotFound):
            # This is where the magic happens. Install or update the pkg.
            easy_install.main(['-U', filename])

            # Scan sys.path for this package
            old_paths = [i for i in sys.path if package in i]
            if len(old_paths) > 1:
                # I can't think of any conditions that would put us here.
                # If people do wind up here, I'd like to see what their
                # sys.paths look like and get details so this can be handled
                # properly.
                assert('No code to handle the current sys.path.')
            elif len(old_paths) == 1:
                sys.path.remove(old_paths[0])
                # Time to reload pkg_resources
                del pkg_resources, sys.modules['pkg_resources']
                import pkg_resources

            # Update sys.path with newly installed/updated pkg
            pkg_resources.require('%s==%s' % package, version)
