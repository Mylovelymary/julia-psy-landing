import re

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Tailwind config
new_config = """                    // Цветовая палитра "Элегантный голубой" (по новому референсу)
                    colors: {
                        'ice-50': '#f8fafc', 
                        'deep-blue-900': '#729cb3', // Более насыщенный и читаемый голубой акцент
                        'lilac-300': '#9ebcd1', 
                        'lilac-100': '#eef3f7', 
                        blue: {
                            50: '#f8fafc',
                            100: '#eef3f7',
                            200: '#dbe5ee',
                            300: '#9ebcd1',
                            800: '#5a8298', 
                        },
                        purple: {
                            50: '#eef3f7', 
                        },
                        slate: {
                            600: '#475569',
                            800: '#1e293b', 
                            900: '#0f172a', 
                        }
                    }"""
content = re.sub(r'// Цветовая палитра "Пыльно-голубой".*?slate: \{.*?\n\s+\}\n\s+\}', new_config, content, flags=re.DOTALL)

# 2. Change font weights of headings from font-bold to font-medium or font-normal for elegance
content = content.replace('font-bold text-slate-800', 'font-medium text-slate-900')
content = content.replace('font-bold text-white', 'font-medium text-white')
content = content.replace('font-bold text-deep-blue-900', 'font-medium text-deep-blue-900')

# 3. Change solid buttons to outline buttons
# Find main solid buttons: bg-deep-blue-900 text-white
old_btn = 'bg-deep-blue-900 text-white px-8 py-4 rounded-xl font-medium hover:bg-blue-800 transition-colors shadow-sm'
new_btn = 'bg-transparent border-2 border-deep-blue-900 text-deep-blue-900 px-8 py-4 rounded-xl font-medium hover:bg-deep-blue-900 hover:text-white transition-all shadow-sm'
content = content.replace(old_btn, new_btn)

old_btn2 = 'bg-deep-blue-900 text-white px-6 py-2.5 rounded-full font-medium hover:bg-blue-800 transition-colors shadow-md'
new_btn2 = 'bg-transparent border border-deep-blue-900 text-deep-blue-900 px-6 py-2.5 rounded-full font-medium hover:bg-deep-blue-900 hover:text-white transition-all'
content = content.replace(old_btn2, new_btn2)

old_btn_hero = 'bg-deep-blue-900 text-white px-8 py-4 rounded-full font-medium hover:bg-blue-800 transition-all shadow-lg hover:shadow-xl'
new_btn_hero = 'bg-white border border-deep-blue-900 text-deep-blue-900 px-8 py-4 rounded-full font-medium hover:bg-deep-blue-900 hover:text-white transition-all shadow-md hover:shadow-lg tracking-wide uppercase text-sm'
content = content.replace(old_btn_hero, new_btn_hero)

old_btn_mobile = 'bg-deep-blue-900 text-white px-6 py-3 rounded-full font-medium hover:bg-blue-800 transition-colors shadow-md'
new_btn_mobile = 'bg-transparent border border-deep-blue-900 text-deep-blue-900 px-6 py-3 rounded-full font-medium hover:bg-deep-blue-900 hover:text-white transition-all'
content = content.replace(old_btn_mobile, new_btn_mobile)

# Tariffs dark card -> light card
dark_card = 'bg-deep-blue-900/95 backdrop-blur-sm p-8 sm:p-10 rounded-3xl shadow-xl flex flex-col relative border border-blue-800'
new_dark_card = 'bg-ice-50 p-8 sm:p-10 rounded-3xl shadow-xl flex flex-col relative border border-deep-blue-900/20'
content = content.replace(dark_card, new_dark_card)

# Dark card text colors
content = content.replace('text-blue-200 text-sm', 'text-slate-600 text-sm')
content = content.replace('text-blue-300', 'text-slate-500')
content = content.replace('text-blue-50 mb-10', 'text-slate-700 mb-10')
content = content.replace('bg-blue-800 text-lilac-100', 'bg-deep-blue-900 text-white')
content = content.replace('bg-white text-deep-blue-900 px-6 py-4 rounded-xl font-semibold hover:bg-gray-50 transition-colors shadow-sm', 'bg-deep-blue-900 text-white px-6 py-4 rounded-xl font-medium hover:bg-blue-800 transition-colors shadow-sm')

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
