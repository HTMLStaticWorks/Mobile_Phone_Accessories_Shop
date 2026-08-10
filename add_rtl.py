import os
import glob
import re

html_files = glob.glob('*.html')

desktop_button = """<button aria-label="rtl_toggle" class="hidden lg:block text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded-full scale-95 active:scale-90 transition-transform font-bold" onclick="document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl'">
RTL
</button>
"""

mobile_button = """            <button aria-label="rtl_toggle" class="text-secondary dark:text-secondary-fixed transition-all p-2 rounded-full font-bold text-xl" onclick="document.documentElement.dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl'">
                RTL
            </button>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Desktop RTL button
    desktop_search = r'(<button aria-label="dark_mode" class="hidden lg:block.*?>\s*<span class="material-symbols-outlined">dark_mode</span>\s*</button>)'
    if re.search(desktop_search, content) and "aria-label=\"rtl_toggle\"" not in content:
        content = re.sub(desktop_search, r'\1\n' + desktop_button, content)

    # Add Mobile RTL button
    mobile_search = r'(<button aria-label="dark_mode" class="text-secondary dark:text-secondary-fixed transition-all p-2 rounded-full" onclick="document\.getElementById\(\'themeToggle\'\)\.click\(\)">\s*<span class="material-symbols-outlined text-3xl theme-icon-mobile">dark_mode</span>\s*</button>)'
    if re.search(mobile_search, content) and mobile_button.strip() not in content:
        content = re.sub(mobile_search, r'\1\n' + mobile_button, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added RTL button to all HTML files.")
