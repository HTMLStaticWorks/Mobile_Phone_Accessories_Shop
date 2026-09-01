import re

files = ['index.html', 'home2.html', 'product.html', 'services.html', 'gallery.html', 'blog.html', 'contact.html']

old_pattern = re.compile(
    r'<!-- Actions -->\s*<div class="flex items-center space-x-unit md:space-x-4">.*?<!-- Mobile Menu Toggle -->\s*<button aria-label="menu" id="mobile-menu-btn".*?</button>\s*</div>',
    re.DOTALL
)

new_block = '''<!-- Actions Bar with Uniform Height (h-10 / 40px) & Baseline Alignment -->
<div class="flex items-center gap-2">
<button aria-label="shopping_cart" class="hidden xl:inline-flex items-center justify-center h-10 w-10 text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/60 dark:hover:bg-primary-container/60 transition-all rounded-full" title="Cart">
<span class="material-symbols-outlined text-[20px]">shopping_cart</span>
</button>
<button aria-label="dark_mode" id="themeToggle" class="hidden xl:inline-flex items-center justify-center h-10 w-10 text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/60 dark:hover:bg-primary-container/60 transition-all rounded-full" title="Toggle Theme">
<span class="material-symbols-outlined text-[20px]">dark_mode</span>
</button>
<button aria-label="rtl_toggle" class="hidden xl:inline-flex items-center justify-center h-10 px-3 text-secondary dark:text-secondary-fixed hover:bg-surface-container-high/60 dark:hover:bg-primary-container/60 transition-all rounded-full font-bold text-xs tracking-wider" onclick="const newDir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl'; document.documentElement.dir = newDir; localStorage.setItem('dir', newDir);" title="Toggle RTL">
RTL
</button>
<div class="hidden xl:inline-flex items-center gap-2 ms-2">
<button class="h-10 px-5 inline-flex items-center justify-center text-primary dark:text-on-primary font-label-md text-sm font-semibold border-2 border-primary/30 dark:border-outline-variant hover:bg-surface-container-high dark:hover:bg-primary-container transition-all rounded-lg" onclick="window.location.href='login.html'">
                    Login
                </button>
<button class="h-10 px-5 inline-flex items-center justify-center bg-secondary text-on-secondary font-label-md text-sm font-semibold hover:bg-secondary-fixed-dim shadow-sm hover:shadow transition-all rounded-lg" onclick="window.location.href='regitser.html'">
                    Sign Up
                </button>
</div>
<!-- Mobile Menu Toggle -->
<button aria-label="menu" id="mobile-menu-btn" class="xl:hidden h-10 w-10 inline-flex items-center justify-center text-primary dark:text-on-primary rounded-full hover:bg-surface-container-high dark:hover:bg-primary-container z-50 relative">
<span class="material-symbols-outlined">menu</span>
</button>
</div>'''

for f in files:
    content = open(f, encoding='utf-8').read()
    if old_pattern.search(content):
        new_content = old_pattern.sub(new_block, content)
        open(f, 'w', encoding='utf-8').write(new_content)
        print(f'Updated {f}')
    else:
        print(f'Pattern NOT matched in {f}')
