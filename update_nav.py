import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the specific navigation link text
    content = content.replace('href="product.html">Product</a>', 'href="product.html">Products</a>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated nav link in {file}")

print("Done updating nav links.")
