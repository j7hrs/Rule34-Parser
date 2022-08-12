# Rule34-Parser
An Rule 34 Parser that uses [@kurozenzen's R34 API.](https://github.com/kurozenzen/r34-json-api)

(why did i make this)

# Installation
1. Open cmd.exe and enter the following:
```
pip install tqdm
```
2. Clone the folder somewhere
3. Done!

# Usage
## Seperating tags
Tags are seperated with an plus symbol (`+`) or an vertical bar with space surrounding it (`  |  `)
Example:
```
Download: dark skin | female
```
Or
```
Download: dark skin+female
```
Expected output: a file that has a female with dark skin.
## Searching by score
Tags can be used to search by score (`score:>[NUMBA HERE]`) or other post parameters.
Example:
```
Download: score:>100
```
Expected output: a file that belongs to a post having 100 likes or more
> NOTE: same can be done for `height`, `width`, `source`, `user`, however `score` is the most useful.
