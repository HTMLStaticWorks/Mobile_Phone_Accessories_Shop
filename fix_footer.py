import glob
import re

with open('blog.html', 'r', encoding='utf-8') as f:
    blog_content = f.read()

good_footer_match = re.search(r'(<footer.*?>.*?</footer>)', blog_content, re.DOTALL)
if not good_footer_match:
    print("Could not find good footer in blog.html")
    exit(1)
good_footer = good_footer_match.group(1)

for file in glob.glob('*.html'):
    if file == 'blog.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '<footer' not in content:
        continue
        
    # Extract the old footer
    old_footer_match = re.search(r'(<footer.*?>.*?</footer>)', content, re.DOTALL)
    if old_footer_match:
        old_footer = old_footer_match.group(1)
        content = content.replace(old_footer, good_footer)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer in {file}")

print("Done fixing footers.")
