from __future__ import annotations

import importlib.metadata

import data_bootcamp_project as m


def test_version():
    assert importlib.metadata.version("data_bootcamp_project") == m.__version__
