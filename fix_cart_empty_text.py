import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the cart empty state text visibility in dark mode
    content = content.replace(
        '<p class="text-on-surface-variant text-sm mb-6">Looks like you haven\'t added anything to your cart yet.</p>',
        '<p class="text-on-surface-variant dark:text-gray-400 text-sm mb-6">Looks like you haven\'t added anything to your cart yet.</p>'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed empty cart text visibility in dark mode")
