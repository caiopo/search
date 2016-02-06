search
======
Searches for keywords inside files

Usage
-----
Run `search.py` passing the keywords you want to search for.

The script will only open files with extensions defined using the flag `-e` or `--extension`. If extension is ommited, it defaults to the extensions in `extensions.txt`.

Examples
--------
```python
./search.py keyword1
./search.py keyword1 keyword2 -e ext1 ext2
```