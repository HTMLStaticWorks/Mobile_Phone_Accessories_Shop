import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix existing wrong classes in services.html
    content = content.replace(
        'class="bg-surface dark:bg-surface-container text-on-surface dark:text-white"',
        'class="bg-surface dark:bg-primary-container text-on-surface dark:text-on-primary"'
    )

    # Function to add correct classes to options that don't have them
    def add_classes_to_option(match):
        option_tag = match.group(0)
        if 'class=' in option_tag:
            return option_tag
        # Add the class before the closing >
        return option_tag[:-1] + ' class="bg-surface dark:bg-primary-container text-on-surface dark:text-on-primary">'

    # Regex to find <option> or <option value="..."> tags
    # We use re.sub with a callback
    content = re.sub(r'<option[^>]*>', add_classes_to_option, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed options in {file}")

print("Done fixing options.")
