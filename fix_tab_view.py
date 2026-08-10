import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the huge font size breaking on tablet
    content = content.replace('md:font-display-lg', 'xl:font-display-lg')
    content = content.replace('md:text-display-lg', 'xl:text-display-lg')
    
    # Fix the buttons in index.html (and any other file) being constrained to 200px and breaking text
    content = content.replace('sm:w-[200px] px-8 py-3 bg-secondary', 'sm:w-auto whitespace-nowrap px-8 py-3 bg-secondary')
    content = content.replace('sm:w-[200px] px-8 py-3 border-2 border-primary', 'sm:w-auto whitespace-nowrap px-8 py-3 border-2 border-primary')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done applying Tab view fixes!')
