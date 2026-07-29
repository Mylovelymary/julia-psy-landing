import re

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make all section titles uppercase and tracking-wider
content = content.replace('class="font-serif text-3xl sm:text-4xl font-medium text-slate-900 mb-4"', 'class="font-serif text-3xl sm:text-4xl font-light text-slate-900 mb-4 uppercase tracking-widest"')

# Make program titles uppercase and accent color
content = content.replace('h3 class="font-serif text-2xl font-medium text-slate-900 mb-2 leading-tight"', 'h3 class="font-serif text-2xl font-normal text-deep-blue-900 mb-2 leading-tight uppercase tracking-wider"')
# And the white one in the former dark card (now we made it light, so text is white -> change to accent)
content = content.replace('h3 class="font-serif text-2xl font-medium text-white mb-2 leading-tight"', 'h3 class="font-serif text-2xl font-normal text-deep-blue-900 mb-2 leading-tight uppercase tracking-wider"')

# Make "Кто мы" uppercase
content = content.replace('Кто мы</h2>', 'ОБ АВТОРАХ</h2>')

# Make "Наши программы" uppercase
content = content.replace('Наши программы</h2>', 'НАШИ ПРОГРАММЫ</h2>')

# Make text a bit lighter and softer
content = content.replace('text-slate-600', 'text-slate-700')

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
