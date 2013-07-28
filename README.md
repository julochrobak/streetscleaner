streetscleaner
==============

simple street names cleaner within the city of Zürich

## web interface ##
Download and open the `index.html` file in your browser and follow the instructions. Or test it online on http://julochrobak.github.io/streetscleaner

## command line utility ##
The `streetscleaner.py` is a command line utility which reads the names from the `stdin` (one street name per line) and returns comma separated
values in the `stdout`. Errors are printed to the `stderr`.

Example:

    echo -e 'bahnofstr\nlimaqua' | python streetscleaner.py
