import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix cart panel background and text color in dark mode
    content = content.replace(
        'bg-surface dark:bg-surface-container text-on-surface dark:text-on-surface-variant transform',
        'bg-surface dark:bg-primary-container text-on-surface dark:text-on-primary-container transform'
    )
    
    # Fix close button hover color
    content = content.replace(
        'hover:bg-surface-container-high dark:hover:bg-primary-container rounded-full transition-colors text-on-surface-variant dark:text-on-surface-variant',
        'hover:bg-surface-container-high dark:hover:bg-primary rounded-full transition-colors text-on-surface-variant dark:text-on-primary-container'
    )

    # Fix cart footer background
    content = content.replace(
        'bg-surface-container-lowest dark:bg-surface-container',
        'bg-surface-container-lowest dark:bg-primary'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed cart colors in {file}")

print("Done fixing cart colors.")
