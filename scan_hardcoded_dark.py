import glob
import re

html_files = glob.glob('*.html')
problematic_classes = ['bg-mc-dark', 'bg-midnight-graphite', 'text-white', 'text-gray-400']

results = {}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        line_clean = line.strip()
        
        for pclass in problematic_classes:
            # We want to find the class if it's NOT prefixed by dark:
            # We can use regex: look for the class not preceded by 'dark:'
            pattern = r'(?<!dark:)\b' + re.escape(pclass) + r'\b'
            if re.search(pattern, line_clean):
                if file not in results:
                    results[file] = []
                results[file].append((i+1, pclass, line_clean[:100]))

for file, matches in results.items():
    print(f"\n--- {file} ---")
    for match in matches:
        print(f"Line {match[0]} [{match[1]}]: {match[2]}")
