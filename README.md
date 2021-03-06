search
======
Searches for keywords inside files

Usage
-----
Run `search.py` passing the keywords you want to search for.

The script will only open files with extensions defined using the flag `-e` or `--extension`. If extension is ommited, it defaults to the extensions in `extensions.txt`.

Note: `-e \0` evaluates to _no extension_.

You can also specify the root directory of the search (it will walk through all sub-directories recursively) using the `-d` flag. If ommited, it defaults to the current directory.

Examples
--------
```python
./search.py keyword1
./search.py keyword1 keyword2 -e ext1 ext2
./search.py keyword1 keyword2 -d /path/to/root/
./search.py keyword1 keyword2 -e ext1 ext2 -d /path/to/root/
```