#!/usr/bin/env python

"""Generates random "fluff" news articles.

Usage: fluffy.py [topic] [company]

"""

import sys
import random
import textwrap


def main():

    if len(sys.argv) > 3:
        exit(__doc__)
    elif len(sys.argv) == 3:
        topic = sys.argv[-2]
        company = sys.argv[-1]
    elif len(sys.argv) == 2:
        topic = sys.argv[-1]
    else:
        topic = None
        company = None

    text = ' '.join(p for p in article(topic=topic, company=company))
    for paragraph in text.split('\n'):
        wrapped = textwrap.fill(paragraph.strip(), 80)
        print(wrapped, end='\n\n')


def article(topic=None, company=None):

    topic = topic or random.choice((
        'Hypervisor',
        'FPGA',
        'Embedded Systems',
        'Continuous Integration',
    ))
    company = company or "ACME"

    yield from intoduction(topic)
    yield "\n"
    for index in range(random.randint(2, 2)):
        if index % 2:
            paragraph = quote
        else:
            paragraph = fluff
        yield from paragraph(topic)
        yield "\n"
    yield from closing(topic, company)


def intoduction(topic):
    yield random.choice((
        "Despite the apparent trend,",
        "In spite of media reactions,",
    ))
    yield random.choice((
        "the medical industry",
        "the aerospace industry",
        "safety-critical application development",
        "automotive infotainment",
    ))
    yield random.choice((
        "is not a dying trend.",
        "continues to demand innovation.",
    ))
    yield random.choice((
        "Lots of disparate sets of data",
    ))
    yield "create complex engineering problems."
    yield "This is where " + topic + 's' " come in."


def fluff(topic):
    yield "Using a " + topic + ", engineers can leverage"
    yield random.choice((
        "the latest technology",
        "an innovative new technology",
        "a multifaceted solution",
    ))
    yield "to meet their customer's needs."


def quote(topic):
    yield "According to"
    yield random.choice((
        "Ned Flanders",
        "Lisa Simpson",
    ))
    yield "at"
    yield random.choice((
        "Competing Company,",
    ))
    yield '"A ' + topic + ' is a great way to synergize content."'


def closing(topic, company):
    yield company + " is"
    yield random.choice((
        "eager",
        "excited",
    ))
    yield "to help your company"
    yield random.choice((
        "exceed",
        "meet",
    ))
    yield "their goals"
    yield random.choice((
        "utilizing our skills with",
        "by taking advantage of",
    ))
    yield topic + 's.'


if __name__ == '__main__':
    main()