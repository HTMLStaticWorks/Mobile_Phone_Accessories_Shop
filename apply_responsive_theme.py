import re
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic background replacements
    content = content.replace('bg-mc-dark text-white', 'bg-surface-container dark:bg-mc-dark text-on-surface dark:text-white transition-colors')
    content = content.replace('bg-mc-dark overflow-hidden', 'bg-surface-container dark:bg-mc-dark text-on-surface dark:text-white overflow-hidden transition-colors')
    content = content.replace('bg-mc-dark/80 backdrop-blur-md', 'bg-surface-container/80 dark:bg-mc-dark/80 backdrop-blur-md')
    
    content = content.replace('bg-midnight-graphite rounded-xl', 'bg-surface-container dark:bg-midnight-graphite rounded-xl transition-colors text-on-surface dark:text-white')
    content = content.replace('bg-midnight-graphite visible', 'bg-surface-container dark:bg-midnight-graphite visible transition-colors text-on-surface dark:text-white')
    content = content.replace('bg-midnight-graphite/90', 'bg-surface/90 dark:bg-midnight-graphite/90 text-on-surface dark:text-white')
    content = content.replace('bg-midnight-graphite/80', 'bg-surface/80 dark:bg-midnight-graphite/80 text-on-surface dark:text-white')
    content = content.replace('bg-midnight-graphite/70', 'bg-surface/70 dark:bg-midnight-graphite/70')
    content = content.replace('bg-midnight-graphite rounded-full', 'bg-surface-container-high dark:bg-midnight-graphite rounded-full')
    
    content = content.replace('bg-primary-container/80 backdrop-blur-lg border border-white/10', 'bg-surface/80 dark:bg-primary-container/80 backdrop-blur-lg border border-outline-variant/30 dark:border-white/10 transition-colors text-on-surface dark:text-white')
    content = content.replace('tech-card bg-primary-container border border-white/10', 'tech-card bg-surface dark:bg-primary-container border border-outline-variant/30 dark:border-white/10 transition-colors text-on-surface dark:text-white')

    content = content.replace('bg-primary border border-mc-blue/30', 'bg-surface dark:bg-primary border border-outline-variant/30 dark:border-mc-blue/30 transition-colors')

    # Specific text color replacements
    content = content.replace('text-gray-400 font-body', 'text-on-surface-variant dark:text-gray-400 font-body')
    content = content.replace('text-gray-300 font-body', 'text-on-surface-variant dark:text-gray-300 font-body')
    content = content.replace('text-white text-4xl', 'text-primary dark:text-white text-4xl')
    
    # Bundle Builder specifics
    content = content.replace('bg-white/5 rounded-full', 'bg-surface-container-high dark:bg-white/5 rounded-full')
    content = content.replace('text-gray-300">Step', 'text-on-surface-variant dark:text-gray-300">Step')
    content = content.replace('text-gray-300">From', 'text-on-surface-variant dark:text-gray-300">From')
    content = content.replace('text-gray-400">Bundle Status', 'text-on-surface-variant dark:text-gray-400">Bundle Status')
    content = content.replace('text-3xl text-white mb-4 md:mb-0', 'text-3xl text-primary dark:text-white mb-4 md:mb-0')

    # General text-white replacements (careful not to break buttons)
    # The trick is to replace text-white inside typography tags only
    content = re.sub(r'<h([1-6])[^>]*?(text-white)[^>]*>', lambda m: m.group(0).replace('text-white', 'text-primary dark:text-white'), content)
    content = re.sub(r'<p[^>]*?(text-white)[^>]*>', lambda m: m.group(0).replace('text-white', 'text-on-surface dark:text-white'), content)
    content = re.sub(r'<p[^>]*?(text-white/80)[^>]*>', lambda m: m.group(0).replace('text-white/80', 'text-on-surface-variant dark:text-white/80'), content)
    content = re.sub(r'<p[^>]*?(text-white/70)[^>]*>', lambda m: m.group(0).replace('text-white/70', 'text-on-surface-variant dark:text-white/70'), content)
    content = re.sub(r'<span[^>]*?(text-white/80)[^>]*>', lambda m: m.group(0).replace('text-white/80', 'text-on-surface-variant dark:text-white/80'), content)
    content = re.sub(r'<span[^>]*?(text-white/60)[^>]*>', lambda m: m.group(0).replace('text-white/60', 'text-on-surface-variant dark:text-white/60'), content)

    # Some missed text-white in services.html
    content = content.replace('text-white/80 mb-2', 'text-on-surface-variant dark:text-white/80 mb-2')
    content = content.replace('border-white/20 rounded', 'border-outline-variant/30 dark:border-white/20 rounded text-on-surface dark:text-white')
    content = content.replace('text-white/50 text-center', 'text-on-surface-variant dark:text-white/50 text-center')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for file in glob.glob('*.html'):
    process_file(file)

print("Applied responsive themes across HTML files.")
