# -*- coding: utf-8 -*-
from lettuce import step
import ipi


# Store the current filename and the output of the parse command
FILENAME = None
OUTPUT = None


@step(u'Given the filename (\S+)')
def given_the_filename(step, filename):
    global FILENAME
    FILENAME = filename


@step(u'When I parse the filename')
def when_i_parse_the_filename(step):
    global OUTPUT
    OUTPUT = ipi._parse_filename(FILENAME)


@step(u'Then the package is (\S+)')
def then_the_package_is(step, package):
    actual = OUTPUT[0]
    assert package == actual, 'Got %s' % actual


@step(u'And the version is (\S+)')
def and_the_version_is(step, version):
    actual = OUTPUT[1]
    assert version == actual, 'Got %s' % actual
