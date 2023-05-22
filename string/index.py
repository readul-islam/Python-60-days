# Slice String
a = 'Hello, world'

print(a[2:5])
# Slice From the Start
print(a[:5])
# Slice To the End
print(a[2:])
# Negative Indexing
print(a[-5:-2])


# Modify Strings

b = ' md readul islam'
c = (b.upper())
print(c.lower())

# Remove Whitespace
print(b.strip())


# Replace String
print(b.replace('j', 'J'))


# Split String

print(a.split(','))


# String Format

age = 16
title = 'my name is readul , and I am {1} {0}'

print(title.format(age, 20))