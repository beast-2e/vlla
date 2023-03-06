#!/bin/python3

import random, time

flags = [
    'pride',
    'lesbian',
    'mlm',
    'transgender',
    'agender',
    'genderfluid',
    'genderqueer',
    'nonbinary',
    'polyamory',
    'pansexual',
    'bisexual',
    'aromantic',
    'asexual',
    'demisexual',
]

random.shuffle(flags)

for flag in flags:
    __import__(flag)
    time.sleep(1200)
