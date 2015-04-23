#!/usr/bin/env python3
# Note, you'll need python3.3 or greater

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
        company = None
    else:
        topic = None
        company = None

    text = ' '.join(p for p in article(topic=topic, company=company))
    for paragraph in text.split('\n'):
        wrapped = textwrap.fill(paragraph.strip(), 80)
        print(wrapped, end='\n\n')


def article(topic=None, company=None):

    topic = topic or random.choice((
        "Hypervisor",
        "FPGA",
        "Embedded Systems",
        "Continuous Integration",
    ))
    company = company or "ACME"

    yield from introduction(topic, company)
    yield "\n"
    for index in range(random.randint(2, 2)):
        if index % 2:
            paragraph = quote
        else:
            paragraph = fluff
        yield from paragraph(topic)
        yield "\n"
    yield from closing(topic, company)


def introduction(topic, company):

    yield random.choice((
        "Despite the apparent trend,",
        "In spite of media reactions,",
        "In this highly advanced technological age,",
        "There will always come a time when a product becomes obsolete, but",
    ))
    yield random.choice((
        "the experience carried by our high-quality workers",
        "the range of services " + company + " can provide",
        "the medical industry",
        "the aerospace industry",
        "safety-critical application development",
        "automotive infotainment",
    ))
    yield random.choice((
        "has shown significant improvement.",
        "has proven to be an effective step in business inovation.",
        "has gathered behind " + company + " to spearhead inovation.",
        "is not a dying trend.",
        "continues to demand innovation.",
    ))
    yield random.choice((
        "Lots of disparate sets of data",
    ))
    yield "create complex engineering problems."
    yield "This is where " + topic + 's' " come in."


def fluff(topic):

    yield random.choice((
        "Using a " + topic + ",",

    ))
    yield random.choice((
        "engineers can leverage",
        "companies can include",
        "businesses are able to benefit from",
    ))
    yield random.choice((
        "the latest technology",
        "an innovative new technology",
        "a multifaceted solution",
    ))
    yield random.choice ((
        "to meet their customer's needs.",
        "to solve the challenging problems they face.",
        "to satisfy market demands.",
    ))


def quote(topic):

    yield "According to"
    yield random.choice((
        "Ned Flanders,",
        "Lisa Simpson,",
        "Mr. Bill,",
        "Bill Nye,",
        "Dr. Doofenshmirtz,",
        "Columbo,",
        "the most honorable sheriff of Nottingham,",
    ))
    yield random.choice((
        "at",
        "a representative from",
        "the president of",
        "a regarded efficiency expert from",
    ))
    yield random.choice((
        "a competing company,",
        "a promising startup,",
        "a respected sales firm,",
    ))
    yield random.choice((
        "A " + topic + " is a great way to synergize content.",
        "Implementing a " + topic + " can be quite a challenging task.",
        "Companies often struggle to develop a well thought out " + topic + ".",
    ))
    yield random.choice((
        "This is why collaboration is important when managing a limited resource set,",
        "This concept is a critical challenge from a consumers' perspective,",
        "Product lifecycles don't always match consumer expectations,",
    ))
    yield random.choice((
        "as customers want their products to continue working smoothly despite any disruptions.",
        "as engineers challenge themselves to push their product to an all new level.",
        "as companies continue to deliver hard-hitting solutions.",
    ))


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
        "surpass",
    ))
    yield "their goals"
    yield random.choice((
        "utilizing our skills with",
        "by taking advantage of",
    ))
    yield topic + 's.'


if __name__ == '__main__':
    main()
