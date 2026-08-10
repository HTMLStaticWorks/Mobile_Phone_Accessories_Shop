import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    target_div = '<a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="contact.html">Contact</a>\n        <div class="flex flex-col gap-3 mt-4">'
        
    icons_html = '<a class="font-headline-sm text-headline-sm text-on-surface dark:text-on-primary border-b border-outline-variant/20 pb-4 hover:text-secondary dark:hover:text-secondary-fixed transition-colors" href="contact.html">Contact</a>\n        <div class="flex items-center justify-center gap-8 py-4 border-b border-outline-variant/20 mb-2">\n            <button aria-label="shopping_cart" class="text-secondary dark:text-secondary-fixed transition-all p-2 rounded-full">\n                <span class="material-symbols-outlined text-3xl">shopping_cart</span>\n            </button>\n            <button aria-label="dark_mode" class="text-secondary dark:text-secondary-fixed transition-all p-2 rounded-full" onclick="document.getElementById(\'themeToggle\').click()">\n                <span class="material-symbols-outlined text-3xl theme-icon-mobile">dark_mode</span>\n            </button>\n        </div>\n        <div class="flex flex-col gap-3 mt-4">'

    if target_div in content:
        content = content.replace(target_div, icons_html)
    else:
        # Check without newlines just in case formatting is slightly different
        print(f"Checking alternative formatting in {file}")

    script_html = '''
<script>
    // Keep mobile theme icon in sync
    document.addEventListener('click', (e) => {
        if (e.target.closest('#themeToggle') || e.target.closest('.theme-icon-mobile')) {
            setTimeout(() => {
                const mobileIcon = document.querySelector('.theme-icon-mobile');
                const htmlClasses = document.documentElement.classList;
                if (mobileIcon) {
                    mobileIcon.textContent = htmlClasses.contains('dark') ? 'light_mode' : 'dark_mode';
                }
            }, 50);
        }
    });
</script>
</body>'''
    
    if 'theme-icon-mobile' not in content[content.rfind('<script'):] and '</body>' in content:
        content = content.replace('</body>', script_html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Added mobile icons to all files.")
