# !/usr/bin/env python
# -*- coding: utf-8 -*-

from playwright.sync_api import sync_playwright
import toml
from pathlib import Path
__author__ = "@britodfbr"  # pragma: no cover
conf = Path(__file__).parents[3] / 'configure.toml'


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


def example03():
    """

    :return:
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://instagram.com')
        page.fill('//*[@id=\"loginForm\"]/div/div[1]/div/label/input', value=toml.load(conf)['instagram']['user'])
        page.fill('//*[@id=\"loginForm\"]/div/div[2]/div/label/input', value=toml.load(conf)['instagram']['pw'])
        page.click('//*[@id=\"loginForm\"]/div/div[3]/button')
        page.wait_for_timeout(2000)
        page.click('/html/body/div[5]/div/div/div/div[3]/button[2]')
        print(page.title())
        page.wait_for_timeout(10000)


def run():
    example03()
    # example02()
    # example01()
    # example_oficial()


if __name__ == '__main__':    # pragma: no cover
    run()
