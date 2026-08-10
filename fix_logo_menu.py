import glob
import re
import os

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip files that don't have the standard header
    if '<!-- Brand Logo -->' not in content:
        continue
        
    print(f"Processing {file}...")

    # 1. Fix Logo
    content = re.sub(
        r'<div class="font-headline-sm text-headline-sm font-bold text-primary dark:text-on-primary-fixed">\s*FixNex\s*</div>',
        r'<a href="index.html" class="font-headline-sm text-headline-sm font-bold text-primary dark:text-on-primary-fixed hover:opacity-80 transition-opacity flex items-center">\n            FixNex\n        </a>',
        content
    )

    # 2. Fix Hamburger Button
    old_btn = '<button aria-label="menu" class="lg:hidden text-primary dark:text-on-primary p-2">'
    new_btn = '<button aria-label="menu" id="mobile-menu-btn" class="lg:hidden text-primary dark:text-on-primary p-2 z-50 relative">'
    content = content.replace(old_btn, new_btn)
    
    # 3. Insert Mobile Menu
    mobile_menu_html = '''
<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="fixed inset-0 bg-surface/95 dark:bg-primary/95 backdrop-blur-lg z-40 hidden flex-col pt-24 px-margin-mobile overflow-y-auto pb-10">
    <div class="flex flex-col gap-4">
        <a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="index.html">Home</a>
        <a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="home2.html">Home2</a>
        <a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="services.html">Services</a>
        <a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="product.html">Product</a>
        <a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="gallery.html">Gallery</a>
        <a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="blog.html">Blog</a>
        <a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="contact.html">Contact</a>
        <div class="flex flex-col gap-3 mt-4">
            <button class="px-4 py-3 text-primary dark:text-on-primary font-label-md text-label-md border-2 border-primary dark:border-outline-variant hover:bg-surface-container-high dark:hover:bg-primary-container transition-colors rounded w-full" onclick="window.location.href='login.html'">Login</button>
            <button class="px-4 py-3 bg-secondary text-on-secondary font-label-md text-label-md hover:bg-secondary-fixed-dim transition-colors rounded w-full" onclick="window.location.href='regitser.html'">Sign Up</button>
        </div>
    </div>
</div>
'''
    if 'id="mobile-menu"' not in content:
        content = content.replace('</header>', '</header>' + mobile_menu_html)
        
    # 4. Insert Script
    script_html = '''
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
                mobileMenu.classList.toggle('flex');
                const icon = mobileMenuBtn.querySelector('.material-symbols-outlined');
                if (icon) {
                    icon.textContent = mobileMenu.classList.contains('hidden') ? 'menu' : 'close';
                }
            });
        }
    });
</script>
</body>'''
    if 'const mobileMenuBtn' not in content:
        content = content.replace('</body>', script_html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done fixing logo and mobile menu across all files.')
