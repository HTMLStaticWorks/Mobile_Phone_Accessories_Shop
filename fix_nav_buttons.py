import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change space-x-2 to gap-2
    content = content.replace('class="hidden xl:flex items-center space-x-2 ml-4"', 'class="hidden xl:flex items-center gap-2 ms-4"')
    content = content.replace('class="hidden xl:flex items-center space-x-2', 'class="hidden xl:flex items-center gap-2')

    # Add w-24 text-center to Login button in nav
    # The login button
    login_btn_search = r'(<button class=")(px-4 py-2 text-primary dark:text-on-primary font-label-md text-label-md border-2 border-primary dark:border-outline-variant hover:bg-surface-container-high dark:hover:bg-primary-container transition-colors rounded)(" onclick="window\.location\.href=\'login\.html\'">)'
    content = re.sub(login_btn_search, r'\1\2 w-24 text-center\3', content)

    # Add w-24 text-center to Sign Up button in nav
    signup_btn_search = r'(<button class=")(px-4 py-2 bg-secondary text-on-secondary font-label-md text-label-md hover:bg-secondary-fixed-dim transition-colors rounded)(" onclick="window\.location\.href=\'regitser\.html\'">)'
    content = re.sub(signup_btn_search, r'\1\2 w-24 text-center\3', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav buttons fixed in all HTML files.")
