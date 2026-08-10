import glob, re

classes = set()
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        for m in re.findall(r'class="([^"]+)"', content):
            for cls in m.split():
                if 'bg-' in cls or 'text-' in cls:
                    classes.add(cls)

dark_bgs = [c for c in classes if 'bg-primary' in c or 'midnight' in c or 'black' in c or 'dark:bg-' in c]
white_texts = [c for c in classes if 'text-white' in c or 'text-on-primary' in c]
print('Dark BGs:', sorted(dark_bgs))
print('White Texts:', sorted(white_texts))
