import re

header_template = """<header class="fixed top-0 left-0 w-full z-50 flex justify-between items-center px-margin-mobile md:px-margin-desktop h-16 bg-surface/80 dark:bg-primary/80 backdrop-blur-md shadow-sm border-b border-outline-variant/20 transition-colors duration-300">
<div class="flex items-center gap-6">
<span class="font-headline-sm text-headline-sm font-bold text-primary dark:text-on-primary-fixed tracking-tight">FixNex</span>
<nav class="hidden md:flex gap-6 items-center">
            <a class="{cls_home}" href="index.html">Home</a>
            <a class="{cls_home2}" href="home2.html">Home2</a>
            <a class="{cls_services}" href="services.html">Services</a>
            <a class="{cls_product}" href="product.html">Product</a>
            <a class="{cls_gallery}" href="gallery.html">Gallery</a>
            <a class="{cls_blog}" href="blog.html">Blog</a>
            <a class="{cls_contact}" href="contact.html">Contact</a>
            <a class="{cls_signup}" href="regitser.html">SignUp</a>
        </nav>
</div>
<div class="flex items-center gap-4">
<div class="hidden lg:flex items-center border border-outline-variant rounded px-3 py-1 bg-surface-container-low dark:bg-surface-container-high focus-within:border-secondary transition-colors">
<span class="material-symbols-outlined text-on-surface-variant text-sm mr-2" data-icon="search">search</span>
<input class="bg-transparent border-none outline-none text-sm text-on-surface w-32 focus:ring-0 placeholder:text-on-surface-variant/50" placeholder="Search..." type="text">
</div>
<a class="hidden md:block font-label-md text-label-md text-on-surface-variant hover:text-secondary transition-colors" href="#">Login</a>
<a class="hidden md:block font-label-md text-label-md bg-secondary text-on-primary px-4 py-2 rounded scale-95 active:scale-90 transition-transform hover:bg-secondary-container hover:text-on-secondary-container" href="#">Sign Up</a>
<button class="hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded scale-95 active:scale-90 flex items-center justify-center">
<span class="material-symbols-outlined text-on-surface-variant dark:text-on-primary-container" data-icon="shopping_cart">shopping_cart</span>
</button>
<button class="hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded scale-95 active:scale-90 flex items-center justify-center" id="theme-toggle">
<span class="material-symbols-outlined text-on-surface-variant dark:text-on-primary-container dark:hidden" data-icon="dark_mode">dark_mode</span>
<span class="material-symbols-outlined text-on-surface-variant dark:text-on-primary-container hidden dark:block" data-icon="light_mode">light_mode</span>
</button>
<!-- Mobile Menu Toggle -->
<button class="md:hidden hover:bg-surface-container-high/50 dark:hover:bg-primary-container/50 transition-all p-2 rounded flex items-center justify-center">
<span class="material-symbols-outlined text-on-surface-variant dark:text-on-primary-container" data-icon="menu">menu</span>
</button>
</div>
</header>"""

files_to_fix = ['blog.html', 'product.html']
active_class = "font-label-md text-label-md text-secondary border-b-2 border-secondary pb-1"
normal_class = "font-label-md text-label-md text-on-surface-variant hover:text-secondary transition-colors"

for file in files_to_fix:
    with open('d:/project 2/Mobile Phone & Accessories Shop/' + file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Setup classes based on file
    classes = {
        'cls_home': normal_class,
        'cls_home2': normal_class,
        'cls_services': normal_class,
        'cls_product': normal_class,
        'cls_gallery': normal_class,
        'cls_blog': normal_class,
        'cls_contact': normal_class,
        'cls_signup': normal_class,
    }
    
    if file == 'blog.html':
        classes['cls_blog'] = active_class
    elif file == 'product.html':
        classes['cls_product'] = active_class
        
    header_html = header_template.format(**classes)
    
    # The broken <nav> block we need to replace is currently:
    # <nav class="... flex justify-between ..."> ... </nav>
    # Note that there are NO other <nav> blocks in the body of product.html and blog.html (except for this one)
    # So we can just use regex to find <nav ... > ... </nav>
    
    pattern = re.compile(r'<nav[^>]*>.*?</nav>', re.DOTALL)
    
    # Ensure we only replace the FIRST match (the header nav), just in case there are others
    content = pattern.sub(header_html, content, count=1)
    
    with open('d:/project 2/Mobile Phone & Accessories Shop/' + file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed header in {file}")

