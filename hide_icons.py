import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Shopping cart button replacement
    old_cart = '<button aria-label="shopping_cart" class="text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded-full scale-95 active:scale-90 transition-transform">'
    new_cart = '<button aria-label="shopping_cart" class="hidden lg:block text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded-full scale-95 active:scale-90 transition-transform">'
    
    # Theme toggle button replacement
    old_theme = '<button aria-label="dark_mode" class="text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded-full scale-95 active:scale-90 transition-transform" id="themeToggle">>'
    new_theme = '<button aria-label="dark_mode" class="hidden lg:block text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded-full scale-95 active:scale-90 transition-transform" id="themeToggle">'

    old_theme2 = '<button aria-label="dark_mode" class="text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded-full scale-95 active:scale-90 transition-transform" id="themeToggle">'
    new_theme2 = '<button aria-label="dark_mode" class="hidden lg:block text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded-full scale-95 active:scale-90 transition-transform" id="themeToggle">'
    
    if old_cart in content:
        content = content.replace(old_cart, new_cart)
    
    if old_theme in content:
        content = content.replace(old_theme, new_theme)
    elif old_theme2 in content:
        content = content.replace(old_theme2, new_theme2)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Icons hidden on mobile.")
