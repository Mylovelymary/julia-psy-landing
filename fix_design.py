import re

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Header logo
# The logo is probably `text-xl`. Let's change to `text-lg`. 
# And ensure it's left aligned on mobile. Currently it might be flex-center or justify-between.
html = html.replace('font-serif text-xl font-bold text-slate-800 tracking-tight', 'font-serif text-lg font-medium text-slate-800 tracking-tight text-left')
# Also the footer logo
html = html.replace('font-serif text-xl font-bold text-white tracking-tight', 'font-serif text-lg font-medium text-white tracking-tight text-left')

# 2. Hero Margin
# Hero section is probably `<section class="relative pt-20 pb-32...` or similar
# Let's reduce padding top.
html = re.sub(r'(<section[^>]*class="[^"]*)pt-24 sm:pt-32', r'\1pt-12 sm:pt-20', html)

# 3. Typography: Non-breaking spaces for prepositions
def replace_prepositions(match):
    prep = match.group(1)
    return f' {prep}&nbsp;'
    
# Apply to text outside of HTML tags (rough approximation)
# Actually, just doing a global replace for common prepositions with spaces around them is usually safe enough if we avoid attributes.
prepositions = r'(?i)(?<=\s)(в|без|до|из|к|на|по|о|от|перед|при|через|с|у|и|нет|за|над|для|об|под|про|чтобы|что|как|не|же|ли|или|а|но)(?=\s)'
# We only want to apply this to text nodes. A simple way in Python without beautifulsoup:
# Split by > and <, process only text outside tags
parts = re.split(r'(<[^>]+>)', html)
for i in range(len(parts)):
    if not parts[i].startswith('<'):
        parts[i] = re.sub(prepositions, replace_prepositions, parts[i])
        # Specific fixes from screenshots:
        parts[i] = parts[i].replace('быть «удобной»', 'быть&nbsp;«удобной»')
        parts[i] = parts[i].replace('ожидания общества', 'ожидания&nbsp;общества')
        parts[i] = parts[i].replace('вернуть контроль', 'вернуть&nbsp;контроль')
html = ''.join(parts)

# 4. Buttons -> rounded-full
html = html.replace('rounded-xl', 'rounded-full')
html = html.replace('rounded-2xl', 'rounded-3xl') # Keep cards 3xl or 2xl, but button was rounded-xl

# 5. Quote icons in "Об Авторах"
# There are probably SVGs or decorative elements. Let's find them.
# In the HTML they look like:
# <div class="absolute top-0 left-0 -translate-x-4 -translate-y-4 text-lilac-300 opacity-30">
# <svg class="w-16 h-16" fill="currentColor" viewBox="0 0 24 24">...
quote_regex = r'<div class="absolute[^>]*text-lilac-300 opacity-30[^>]*>.*?</div>'
html = re.sub(quote_regex, '', html, flags=re.DOTALL)

# 6. "Наш подход" numbers
# <div class="w-12 h-12 rounded-full bg-ice-50 flex items-center justify-center text-deep-blue-900 font-bold text-xl mr-6 shrink-0 shadow-sm border border-blue-50">1</div>
html = re.sub(r'bg-ice-50([^>]*)text-deep-blue-900', r'bg-deep-blue-900\1text-white', html)

# 7. Move the big quote "Терапия — это не волшебная пилюля..."
# Find the section containing it.
quote_section_regex = r'(<section[^>]*bg-ice-50/50[^>]*>.*?Терапия — это не волшебная пилюля.*?</section>)'
match = re.search(quote_section_regex, html, flags=re.DOTALL)
if match:
    quote_section = match.group(1)
    html = html.replace(quote_section, '')
    # Insert it before the footer (or after FAQ)
    # Let's insert it before <footer
    html = html.replace('<footer', quote_section + '\n    <footer')

# 8. Gradient Blob in "Знакомо ли вам?"
# Usually an absolute div with bg-gradient, blur, etc.
blob_regex = r'<div class="absolute top-0 left-1/2 -translate-x-1/2 w-64 h-64 bg-purple-50 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-blob"></div>'
html = html.replace(blob_regex, '')
html = re.sub(r'<div class="absolute[^>]*animate-blob[^>]*></div>', '', html)

# 9. Telegram Icon
old_tg_svg = r'<path d="M12 2C6\.48 2 2 6\.48 2 12s4\.48 10 10 10 10-4\.48 10-10S17\.52 2 12 2zm4\.64 6\.8c-\.15 1\.58-\.8 5\.42-1\.13 7\.19-\.14\.75-\.42 1-\.68 1\.03-\.58\.05-1\.02-\.38-1\.58-\.75-\.88-\.58-1\.38-\.94-2\.23-1\.5-\.99-\.65-\.35-1\.01\.22-1\.59\.15-\.15 2\.71-2\.48 2\.76-2\.69a\.2\.2 0 00-\.05-\.18c-\.06-\.05-\.14-\.03-\.21-\.02-\.09\.02-1\.49\.95-4\.22 2\.79-\.4\.27-\.76\.41-1\.08\.4-\.36-\.01-1\.04-\.2-1\.55-\.37-\.63-\.2-1\.12-\.31-1\.08-\.66\.02-\.18\.27-\.36\.74-\.55 2\.92-1\.27 4\.86-2\.11 5\.83-2\.51 2\.78-1\.16 3\.35-1\.36 3\.73-1\.36\.08 0 \.27\.02\.39\.12\.1\.08\.13\.19\.14\.27-\.01\.06\.01\.24 0 \.38z" />'
# Outline Telegram icon (Send icon)
new_tg_svg = r'<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>'
# We also need to change fill="currentColor" to fill="none" stroke="currentColor" for outline icons if we swap path.
# Actually let's just inject the exact SVG for outline telegram (feather icons style):
tg_outline = '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>'

# Find the Telegram links and replace the SVG inside
tg_regex = r'<a href="https://t\.me/[^"]+"[^>]*>.*?<span class="sr-only">Telegram</span>.*?<svg[^>]*>.*?</svg>\s*</a>'

def replace_tg(match):
    original = match.group(0)
    replaced = re.sub(r'<svg.*?</svg>', tg_outline, original, flags=re.DOTALL)
    return replaced

html = re.sub(tg_regex, replace_tg, html, flags=re.DOTALL)

with open('/home/maris.vigulis/Desktop/julia_psy_landing/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
