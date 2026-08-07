import re

with open('d:/project 2/Mobile Phone & Accessories Shop/services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract class attributes
class_strings = re.findall(r'class="([^"]+)"', content)
all_classes = set()
for cstr in class_strings:
    for c in cstr.split():
        all_classes.add(c)

# We want to find classes that lack a dark: equivalent in the same tag.
# Let's just output the body class to see
print("Body class:")
print(re.search(r'<body class="([^"]+)"', content).group(1))

print("Header classes:")
for header in re.findall(r'<header class="([^"]+)"', content):
    print(header)

