import re

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix inline purple styles
content = content.replace('style="color: #b070c0;"', 'class="text-lg font-medium text-deep-blue-900 mb-4 uppercase tracking-wider"')
# Remove the old class that was split across lines and combine it
content = re.sub(r'class="text-lg font-semibold mb-4 drop-shadow\s*-sm"\s*class="text-lg font-medium text-deep-blue-900 mb-4 uppercase tracking-wider"', 'class="text-sm font-medium text-deep-blue-900 mb-4 uppercase tracking-wider"', content)
# Just clean it up cleanly with regex
content = re.sub(r'class="[^"]*drop-shadow-sm"\s*style="color: #b070c0;"', 'class="text-sm font-medium text-deep-blue-900 mb-6 uppercase tracking-wider"', content)

# Fix mobile menu button
old_menu_btn = """<svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h16M4 18h16" />
                        </svg>"""

new_menu_btn = """<svg id="menu-icon" class="h-6 w-6 block" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                        <svg id="close-icon" class="h-6 w-6 hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>"""

content = content.replace(old_menu_btn, new_menu_btn)

# Fix JS for mobile menu
old_js = """        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });"""

new_js = """        if (mobileMenuBtn && mobileMenu) {
            const menuIcon = document.getElementById('menu-icon');
            const closeIcon = document.getElementById('close-icon');

            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
                menuIcon.classList.toggle('hidden');
                menuIcon.classList.toggle('block');
                closeIcon.classList.toggle('hidden');
                closeIcon.classList.toggle('block');
            });"""

content = content.replace(old_js, new_js)

old_js_close = """                link.addEventListener('click', () => {
                    mobileMenu.classList.add('hidden');
                });"""
                
new_js_close = """                link.addEventListener('click', () => {
                    mobileMenu.classList.add('hidden');
                    menuIcon.classList.remove('hidden');
                    menuIcon.classList.add('block');
                    closeIcon.classList.add('hidden');
                    closeIcon.classList.remove('block');
                });"""
content = content.replace(old_js_close, new_js_close)

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
