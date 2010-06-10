#!/usr/bin/python

from urllib2 import urlopen
from csv import DictReader
from json import dump

DATAURL = "http://earthquake.usgs.gov/earthquakes/catalogs/eqs1day-M1.txt"
OUTPUTFILE = "earthquakes.json"

reader = DictReader(urlopen(DATAURL))

quakes = [q for q in reader]

dump(quakes, open(OUTPUTFILE, "w"))
