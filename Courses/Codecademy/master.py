"""MyTest."""

excerpt = """ \
it is a long passage about something. \
it is just a test text that we are going to use in our code.\
it is beneficial to use python strings methods like .find(), title(), .replace(), .strip() \
.join(), .format()\
"""

lower_excerpt = excerpt.lower()
upper_excerpt = excerpt.upper()
title_excerpt = excerpt.title()

strip_excerpt = excerpt.strip()

word_find = excerpt.find("it")
word_index = excerpt.index("it")

index_search_mult = [index for index in range(len(excerpt)) if excerpt.startswith("it", index)]

print(word_find)
print(word_index)
print(index_search_mult)

user_name = "::::::::Eloise :::::::::::"

stripped = user_name.strip(":").strip()
print(stripped)
