with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix heading text color
content = content.replace(
    '<h2 class="font-display-lg-mobile text-display-lg-mobile md:font-headline-md text-mc-dark mb-4">Build Your Bundle</h2>',
    '<h2 class="font-display-lg-mobile text-display-lg-mobile md:font-headline-md text-mc-dark dark:text-white mb-4">Build Your Bundle</h2>'
)

# Fix subheadings in the cards
content = content.replace(
    '<h3 class="font-headline-sm text-headline-sm mb-2 text-mc-dark">Select Device</h3>',
    '<h3 class="font-headline-sm text-headline-sm mb-2 text-mc-dark dark:text-white">Select Device</h3>'
)
content = content.replace(
    '<h3 class="font-headline-sm text-headline-sm mb-2 text-mc-dark">Add Accessories</h3>',
    '<h3 class="font-headline-sm text-headline-sm mb-2 text-mc-dark dark:text-white">Add Accessories</h3>'
)
content = content.replace(
    '<h3 class="font-headline-sm text-headline-sm mb-2 text-mc-dark">Save & Checkout</h3>',
    '<h3 class="font-headline-sm text-headline-sm mb-2 text-mc-dark dark:text-white">Save & Checkout</h3>'
)

# Fix card backgrounds
content = content.replace(
    '<div class="bg-surface border border-outline-variant/30 rounded-xl p-6 text-center spring-hover cursor-pointer shadow-sm hover:shadow-xl hover:border-mc-blue/50 transition-all">',
    '<div class="bg-surface dark:bg-primary-container border border-outline-variant/30 rounded-xl p-6 text-center spring-hover cursor-pointer shadow-sm hover:shadow-xl hover:border-mc-blue/50 transition-all">'
)
content = content.replace(
    '<div class="bg-surface border border-outline-variant/30 rounded-xl p-6 text-center spring-hover cursor-pointer shadow-sm hover:shadow-xl hover:border-mc-orange/50 transition-all relative overflow-hidden">',
    '<div class="bg-surface dark:bg-primary-container border border-outline-variant/30 rounded-xl p-6 text-center spring-hover cursor-pointer shadow-sm hover:shadow-xl hover:border-mc-orange/50 transition-all relative overflow-hidden">'
)

# Fix gray circles in the cards (dark mode support)
content = content.replace(
    '<div class="w-32 h-32 mx-auto bg-gray-100 rounded-full mb-6 flex items-center justify-center">',
    '<div class="w-32 h-32 mx-auto bg-gray-100 dark:bg-white/10 rounded-full mb-6 flex items-center justify-center">'
)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed dark mode issues in home2.html Bundle Section")
