import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Navbar fixes
    content = content.replace('class="hidden lg:flex gap-2 lg:gap-3 items-center"', 'class="hidden xl:flex gap-2 xl:gap-3 items-center"')
    content = content.replace('class="hidden lg:block text-secondary', 'class="hidden xl:block text-secondary')
    content = content.replace('class="hidden lg:flex items-center space-x-2 ml-4"', 'class="hidden xl:flex items-center space-x-2 ml-4"')
    content = content.replace('id="mobile-menu-btn" class="lg:hidden', 'id="mobile-menu-btn" class="xl:hidden')
    
    # Hero section fixes for index.html
    if file == 'index.html':
        content = content.replace('<div class="relative z-10 grid grid-cols-1 md:grid-cols-2 gap-gutter items-center">', '<div class="relative z-10 grid grid-cols-1 xl:grid-cols-2 gap-gutter items-center">')
        content = content.replace('class="font-display-lg-mobile text-display-lg-mobile md:font-display-lg text-primary dark:text-on-primary"', 'class="font-display-lg-mobile text-display-lg-mobile xl:font-display-lg text-primary dark:text-on-primary"')
        # Also fix the image float at 1024px so it doesn't look weird if 1 column
        content = content.replace('class="relative flex justify-center items-center mt-12 md:mt-0 animate-float"', 'class="relative flex justify-center items-center mt-12 xl:mt-0 animate-float"')
        
    # Hero section fixes for home2.html
    if file == 'home2.html':
        content = content.replace('<div class="max-w-container-max mx-auto w-full grid grid-cols-1 md:grid-cols-2 gap-gutter items-center z-10">', '<div class="max-w-container-max mx-auto w-full grid grid-cols-1 xl:grid-cols-2 gap-gutter items-center z-10">')
        content = content.replace('class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-primary leading-tight dark:text-on-primary"', 'class="font-display-lg-mobile xl:font-display-lg text-display-lg-mobile xl:text-display-lg text-primary leading-tight dark:text-on-primary"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
