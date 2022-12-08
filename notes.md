# Notes from initial investigation

`test.py` fails on twint.run.Profile, commented it for now
`test.py` runs after modification, does it do what is expected?
why does cli.py exist instead of a `__main__.py`?

rename `master` branch to `main` branch

Went through all of the example command lines and checked if each works.  Reordered them by 
 * working
 * need to test
 * need to test but think fails
 * fails

Go through the PRs in twint (linking back to the original) and make a table of number | name | status
The status options:
 * to include
 * included
 * won't include
 * duplicate

Build a distribution.  The setup was changed to use the new main file, but has not been tested yet.
