# !/usr/bin/env python
# -*- coding: utf-8 -*-

from playwright.sync_api import sync_playwright

__author__ = "@britodfbr"  # pragma: no cover


def example_oficial():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http:playwright.dev')
        print(page.title())
        browser.close()


def example01():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http:playwright.dev')
        print(page.title())
        browser.close()


def example02():
    """

    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://google.com')
        print(page.title())
        page.fill('input[name=q]', value='python')
        page.click('input[name=btnK]')
        page.wait_for_timeout(5000)


def run():
    example02()
    # example01()
    # example_oficial()


if __name__ == '__main__':    # pragma: no cover
    run()
