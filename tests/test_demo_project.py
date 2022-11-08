#!/usr/bin/env python
"""Tests for `demo_project` package."""

import pytest
from demo_project.main import custom_add, custom_reduce


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    del response


def test_custom_add():
    a = 1
    b = 2
    assert 3 == custom_add(a, b)


def test_custom_reduce():
    a = 1
    b = 2
    assert 1 == custom_reduce(b, a)
