import re

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix middle card price text color
content = content.replace('<span class="text-4xl font-medium text-white">4 000 ₽</span>', '<span class="text-4xl font-medium text-slate-900">4 000 ₽</span>')

# Make the middle card button an outline button
old_middle_btn = 'bg-deep-blue-900 text-white px-6 py-4 rounded-xl font-medium hover:bg-blue-800 transition-colors shadow-sm'
new_middle_btn = 'bg-transparent border-2 border-deep-blue-900 text-deep-blue-900 px-6 py-4 rounded-xl font-medium hover:bg-deep-blue-900 hover:text-white transition-all shadow-sm'
content = content.replace(old_middle_btn, new_middle_btn)

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
