"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""

from icecream import ic


def generate_hashtag(s):
    if not s:
        return False
    s = s.split()
    li = [i.capitalize() for i in s]
    result = '#' + ''.join(li)
    if len(result) > 140:
        return False
    else:
        return result


li = [" Hello there thanks for trying my Kata",
      "    Hello     World   ",
      ""]

for i in li:
    ic(generate_hashtag(i))