#!/usr/bin/python

# Copyright (c) 2013 Julius Chronak. You can use this source code
# under the terms of the MIT License found in the LICENSE file:
#
# https://raw.github.com/julochrobak/streetscleaner/master/LICENSE

import fileinput
import json
import sys
import urllib2

streets = []

for line in fileinput.input():
        streets.append(line.strip())

request = {
    "expr": "[ {input: b, " +
            "   street: a.LOK_TEXT, " +
            "   match: fuzzy(lower(a.LOK_TEXT), lower(b))} | " +
            "   a <~ ch_zh_strassennamenverzeichnis, " +
            "   b <- input, " +
            "   fuzzy(lower(a.LOK_TEXT), lower(b)) > confidence ]",

    "input": streets,
    "confidence": 0.2
}

try:
    f = urllib2.urlopen("https://data.mingle.io", json.dumps(request))
    response = f.read()
    f.close()

    data = json.loads(response)
    sys.stdout.write("input,street,match\n")

    # FIXME: properly qoute the values to allow commas in the street names
    for item in data["result"]:
        sys.stdout.write(item["input"].encode("utf-8") + ',' + 
                         item["street"].encode("utf-8") + ',' +
                         '%.8f' % item["match"] + '\n')

except Exception, e:
    sys.stderr.write(str(e))
