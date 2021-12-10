import os 

htmls = list(filter(lambda x: x.endswith('.html') and x!='index.html', os.listdir('Object Oriented Programming using Python')))


data = []
for html in htmls:
    data.append({
        'title': ' '.join(html.split(' ')[1:]).replace('.html', ''),
        'path': html
    })

html_string = '<ol>'
for entry in data:
    html_string = html_string + f'''<li><a href="./{entry['path']}" target="_blank">{entry['title']}</a></li>'''

html_string = html_string + '</ol>'

with open('list.html', 'w', encoding='utf8') as f:
    f.write(html_string)