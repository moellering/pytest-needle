"""pytest_needle.plugin

.. codeauthor:: John Lane <jlane@fanthreesixty.com>

"""

from __future__ import absolute_import
import pytest


def pytest_addoption(parser):
    """

    :param parser:
    :return:
    """

    group = parser.getgroup('needle')
    group.addoption('--needle-cleanup-on-success', action='store_true',
                    help='destroy all non-baseline screenshots')

    group.addoption('--needle-save-baseline', action='store_true',
                    help='save baseline screenshots to disk')

    group.addoption('--needle-engine', action='store', dest='needle_engine', metavar='engine',
                    default=DEFAULT_ENGINE, help='engine for compare screenshots')

    group.addoption('--needle-baseline-dir', action='store', dest='baseline_dir',
                    metavar='dir', default=DEFAULT_BASELINE_DIR,
                    help='where to store baseline images')

    group.addoption('--needle-output-dir', action='store', dest='output_dir',
                    metavar='dir', default=DEFAULT_OUTPUT_DIR,
                    help='where to store baseline images')

    group.addoption('--needle-viewport-size', action='store', dest='viewport_size', metavar='pixels',
                    default=DEFAULT_VIEWPORT_SIZE, help='size of window width (px) x height (px)')

