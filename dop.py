import re
import string

str = 'gluy1gluy2134q3.ysd jhg23'
new_str = re.sub("[1|2|3|4|5|6|7|8|9|0|.| ]", "", str)
print(new_str)

glossary = '0123456789,. '
n = ''.join([ch for ch in str if ch in glossary])
print(n)