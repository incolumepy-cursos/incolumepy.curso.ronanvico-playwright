# !/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from tempfile import gettempdir
import rstr
from string import ascii_letters, digits

__author__ = "@britodfbr"


def example_rstr():
    print('\nendereçamento postal')
    yield """{0} {1}
    {2} {3}
{4}, {5} {6}""".format(rstr.letters(4, 8).title(),
                       rstr.letters(4, 8).title(),
                       rstr.digits(3, 5),
                       rstr.letters(4, 10).title(),
                       rstr.letters(4, 15).title(),
                       rstr.uppercase(2),
                       rstr.digits(5),
                       )
    print('\nURL:')
    yield 'http://{0}.{1}/{2}/?{3}'.format(rstr.domainsafe(),
                                           rstr.letters(3),
                                           rstr.urlsafe(),
                                           rstr.urlsafe())

    print('\nEmail:')
    yield '{0}@{1}.{2}'.format(rstr.letters(exclude='@'),
                               rstr.domainsafe(),
                               rstr.letters(3))
    print('\nFilename:')
    yield rstr.xeger(r'[a-zA-Z]{10}\d{3}[A-Z]{2}\.csv')

    print('\n15 letters:')
    yield rstr.rstr(rstr.letters(), 15)


def filegen(suffix: str = ''):
    suffix = suffix or 'txt'
    suffix = f".{suffix.lstrip('.')}"
    while True:
        filename = Path(gettempdir()).joinpath(
            'move_files', rstr.xeger(r'[a-zA-Z]{10}\d{3}[A-Z]{2}')).with_suffix(suffix)
        filename.parent.mkdir(exist_ok=True, parents=True)
        filename.write_text('')
        yield filename


def movefile(file: Path = None) -> bool:
    if not isinstance(file, Path):
        raise TypeError('Not pathlib.Path')
    nfile = file.parent.joinpath(file.suffix.lstrip('.').casefold(), file.name)
    nfile.parent.mkdir(exist_ok=True, parents=True)
    file.rename(nfile)
    logging.info(f'moved [{file.parent} => {file.parent.joinpath(file.suffix.lstrip("."))}]{file.name}')
    return True


def move_files(directory):
    files = list(directory.glob('*'))
    for file in files:
        movefile(file)


def run():
    # print(rstr(ascii_letters, 10))

    e = example_rstr()
    for i in e:
        print(i)

    fileg = filegen('csv')
    f = filegen()
    g = filegen('js')
    h = filegen('json')
    i = filegen('docx')
    for _ in range(10):
        print(next(fileg))
        print(next(f))
        print(next(g))
        print(next(h))
        print(next(i))

    move_files(Path(gettempdir())/'move_files')


if __name__ == '__main__':
    run()
