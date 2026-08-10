import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the cart checkout button in dark mode
    content = content.replace(
        '<button class="w-full bg-primary text-on-primary py-4 rounded-md font-label-lg hover:bg-inverse-surface dark:hover:bg-inverse-on-surface transition-colors opacity-50 cursor-not-allowed">',
        '<button class="w-full bg-primary dark:bg-white text-on-primary dark:text-black py-4 rounded-md font-label-lg hover:bg-inverse-surface dark:hover:bg-gray-200 transition-colors opacity-50 cursor-not-allowed">'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed Checkout button visibility in dark mode")
