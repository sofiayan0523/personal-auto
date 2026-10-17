import json
import os

template_path = '.omni/demo_template_latest.html'
index_path = 'from-carbon-to-metro/demo/index.html'

# Read template
html = open(template_path, 'r', encoding='utf-8').read()

# Serialize to JSON and replace '<' with '\u003c'
encoded = json.dumps(html).replace('<', '\\u003c')

# Read current index.html
index_content = open(index_path, 'r', encoding='utf-8').read()

# Find and replace the template tag without using re.sub (avoiding backslash escape issues)
start_tag = '<script type="__bundler/template">'
end_tag = '</script>'

start_idx = index_content.find(start_tag)
if start_idx != -1:
    end_idx = index_content.find(end_tag, start_idx)
    if end_idx != -1:
        new_index_content = index_content[:start_idx + len(start_tag)] + encoded + index_content[end_idx:]
        open(index_path, 'w', encoding='utf-8').write(new_index_content)
        print("Success: Repackaged demo index.html")
    else:
        print("Error: Could not find closing tag </script> after __bundler/template")
else:
    print("Error: Could not find <script type=\"__bundler/template\"> in index.html")
