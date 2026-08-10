import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace dark:text-on-primary-fixed with dark:text-white 
    # for the FixNex logo in the header
    pattern = r'(<a href="index\.html" class="[^"]*font-headline-sm[^"]*text-primary )dark:text-on-primary-fixed([^"]*".*?>\s*FixNex\s*</a>)'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, r'\1dark:text-white\2', content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Fixed logo color in {f}")
