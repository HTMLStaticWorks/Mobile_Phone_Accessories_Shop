import os
import glob
import re

html_files = glob.glob('*.html')

onclick_old = "document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl'"
onclick_new = "const newDir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl'; document.documentElement.dir = newDir; localStorage.setItem('dir', newDir);"

init_rtl_logic = """
        // Init dir
        const savedDir = localStorage.getItem('dir');
        if (savedDir) {
            document.documentElement.dir = savedDir;
        }
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update onclick handlers
    content = content.replace(onclick_old, onclick_new)

    # 2. Add Init dir logic right before Init theme, if not already there
    if "const savedDir = localStorage.getItem('dir');" not in content:
        content = content.replace("// Init theme", init_rtl_logic + "\n        // Init theme")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("RTL persistence added to all HTML files.")
