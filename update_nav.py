import glob
import os

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace('<nav class="hidden md:flex gap-2 lg:gap-3 items-center">', '<nav class="hidden lg:flex gap-2 lg:gap-3 items-center">')
    content = content.replace('<div class="hidden md:flex items-center space-x-2 ml-4">', '<div class="hidden lg:flex items-center space-x-2 ml-4">')
    content = content.replace('<button aria-label="menu" class="md:hidden text-primary dark:text-on-primary p-2">', '<button aria-label="menu" class="lg:hidden text-primary dark:text-on-primary p-2">')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated navigation classes in all HTML files.')
