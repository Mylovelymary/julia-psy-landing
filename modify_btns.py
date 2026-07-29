import re

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make all buttons consistent outline buttons
old_btn = 'class="w-full bg-deep-blue-900 text-white px-6 py-4 rounded-full font-semibold hover:bg-lilac-100 transition-colors border border-blue-100"'
new_btn = 'class="w-full bg-transparent border-2 border-deep-blue-900 text-deep-blue-900 px-6 py-4 rounded-full font-medium hover:bg-deep-blue-900 hover:text-white transition-all shadow-sm"'
content = content.replace(old_btn, new_btn)

# Make sure all Buttons in Tariffs are outline.
content = content.replace('w-full bg-ice-50 text-deep-blue-900 px-6 py-4 rounded-full font-semibold hover:bg-lilac-100 transition-colors border border-blue-100', 'w-full bg-transparent border-2 border-deep-blue-900 text-deep-blue-900 px-6 py-4 rounded-full font-medium hover:bg-deep-blue-900 hover:text-white transition-all shadow-sm')

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
