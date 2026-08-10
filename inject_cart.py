import glob
import re

cart_html = """
<!-- Cart Sidebar -->
<div id="cart-sidebar" class="fixed inset-0 z-[100] hidden">
    <!-- Backdrop -->
    <div id="cart-backdrop" class="absolute inset-0 bg-surface/50 dark:bg-surface-container-high/80 backdrop-blur-sm opacity-0 transition-opacity duration-300"></div>
    
    <!-- Sidebar Panel -->
    <div id="cart-panel" class="absolute inset-y-0 right-0 w-full max-w-md bg-surface dark:bg-surface-container text-on-surface dark:text-on-surface-variant transform translate-x-full transition-transform duration-300 shadow-2xl flex flex-col">
        <!-- Header -->
        <div class="p-6 border-b border-outline-variant/20 flex justify-between items-center">
            <h2 class="font-headline-md text-headline-sm font-semibold text-primary dark:text-on-primary">Your Cart</h2>
            <button id="close-cart-btn" class="p-2 hover:bg-surface-container-high dark:hover:bg-primary-container rounded-full transition-colors text-on-surface-variant dark:text-on-surface-variant">
                <span class="material-symbols-outlined">close</span>
            </button>
        </div>
        
        <!-- Cart Items (Empty State) -->
        <div class="flex-grow flex flex-col items-center justify-center p-6 text-center">
            <span class="material-symbols-outlined text-[64px] text-outline mb-4">shopping_cart</span>
            <h3 class="font-label-lg font-semibold mb-2 text-on-surface dark:text-on-primary">Your cart is empty</h3>
            <p class="text-on-surface-variant text-sm mb-6">Looks like you haven't added anything to your cart yet.</p>
            <button id="continue-shopping-btn" class="bg-secondary text-on-secondary px-6 py-3 rounded-md font-label-md hover:bg-secondary-fixed-dim transition-colors">
                Continue Shopping
            </button>
        </div>
        
        <!-- Footer -->
        <div class="p-6 border-t border-outline-variant/20 bg-surface-container-lowest dark:bg-surface-container">
            <div class="flex justify-between mb-4 font-semibold text-on-surface dark:text-on-primary">
                <span>Subtotal</span>
                <span>$0.00</span>
            </div>
            <button class="w-full bg-primary text-on-primary py-4 rounded-md font-label-lg hover:bg-inverse-surface dark:hover:bg-inverse-on-surface transition-colors opacity-50 cursor-not-allowed">
                Checkout
            </button>
        </div>
    </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const cartBtns = document.querySelectorAll('button[aria-label="shopping_cart"]');
        const cartSidebar = document.getElementById('cart-sidebar');
        const cartBackdrop = document.getElementById('cart-backdrop');
        const cartPanel = document.getElementById('cart-panel');
        const closeCartBtn = document.getElementById('close-cart-btn');
        const continueShoppingBtn = document.getElementById('continue-shopping-btn');

        function openCart() {
            if(!cartSidebar) return;
            cartSidebar.classList.remove('hidden');
            // Small delay to allow display:block to apply before animation
            setTimeout(() => {
                cartBackdrop.classList.remove('opacity-0');
                cartPanel.classList.remove('translate-x-full');
            }, 10);
        }

        function closeCart() {
            if(!cartSidebar) return;
            cartBackdrop.classList.add('opacity-0');
            cartPanel.classList.add('translate-x-full');
            setTimeout(() => {
                cartSidebar.classList.add('hidden');
            }, 300); // match duration-300
        }

        cartBtns.forEach(btn => btn.addEventListener('click', openCart));
        if (closeCartBtn) closeCartBtn.addEventListener('click', closeCart);
        if (cartBackdrop) cartBackdrop.addEventListener('click', closeCart);
        if (continueShoppingBtn) continueShoppingBtn.addEventListener('click', closeCart);
    });
</script>
</body>"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="cart-sidebar"' in content:
        print(f"Cart already in {file}")
        continue
        
    content = content.replace('</body>', cart_html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added cart to {file}")

print("Done injecting cart.")
