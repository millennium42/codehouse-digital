#!/usr/bin/env python3
# html_validate.py — lint basico de index.html
import re, sys

path = 'site/index.html'
with open(path, encoding='utf-8') as f:
    html = f.read()

issues = []

# 1. Tags unclosed obvias (a/div/p/span/img sem /> ou </...)
SELF_CLOSE_IMPLICIT = re.compile(r'<(area|base|br|col|embed|hr|img|input|link|meta|source|track|wbr)\b[^>]*/?>', re.I)
TAG_OPEN = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)\b([^>]*)>', re.I)
TAG_CLOSE = re.compile(r'</([a-zA-Z][a-zA-Z0-9]*)>', re.I)

opens = []
for m in TAG_OPEN.finditer(html):
    tag = m.group(1).lower()
    attrs = m.group(2)
    if tag in ('script', 'style', 'textarea', 'pre'):
        # nao tratamos bloco por bloco aqui para nao falsos positivos
        continue
    if SELF_CLOSE_IMPLICIT.match('<' + tag + ' ' + attrs) or attrs.strip().endswith('/'):
        continue
    opens.append((m.start(), tag))

closes = [(m.start(), m.group(1).lower()) for m in TAG_CLOSE.finditer(html)]

# Conta so para warning de desbalanceamento global
from collections import Counter
open_counter = Counter(t for _, t in opens)
close_counter = Counter(t for _, t in closes)
for tag in set(open_counter) | set(close_counter):
    o = open_counter.get(tag, 0)
    c = close_counter.get(tag, 0)
    if o != c:
        issues.append(f'Desbalanceamento {tag}: open={o} close={c}')

# 2. IDs duplicados
ids = re.findall(r'id="([^"]+)"', html)
seen = set()
for i in ids:
    if i in seen:
        issues.append(f'ID duplicado: id="{i}"')
    seen.add(i)

# 3. Duplicacao de comentarios de seção (stack, faq etc)
sec_comments = re.findall(r'<!--\s*=\s*=\s*=\s*([^\s=]+)', html)
from collections import Counter as C
dup = [(k, v) for k, v in C(sec_comments).items() if v > 1]
for k, v in dup:
    issues.append(f'Comentario de seção duplicado ({v}x): {k}')

# 4. Script externo referenciado mas nao existe
refs = re.findall(r'src="([^"]+)"', html)
import os
for r in refs:
    full = os.path.join(os.path.dirname(os.path.abspath(path)), r)
    if not os.path.exists(full):
        issues.append(f'Referencia a script/asset inexistente: {r}')

# 5. Javascript com sintaxes potencialmente quebradas (paren/brace mismatch) 
js_blocks = re.findall(r'<script[^>]*>(.*?)</script>', html, re.S)
for idx, block in enumerate(js_blocks):
    # conta parenteses e chaves
    if block.count('(') != block.count(')'):
        issues.append(f'Script #{idx}: parenteses desbalanceados')
    if block.count('{') != block.count('}'):
        issues.append(f'Script #{idx}: chaves desbalanceadas')

# 6. alt vazio em img
imgs = re.findall(r'<img\b([^>]*)>', html, re.I)
for attrs in imgs:
    if 'alt=""' in attrs or 'alt=\'\'' in attrs:
        issues.append('img com alt="" (vazio)')

print('=== VALIDAÇÃO index.html ===')
print('issues encontrados:', len(issues))
for i in issues:
    print(' -', i)
if not issues:
    print('Nenhum problema obviano detectado.')
