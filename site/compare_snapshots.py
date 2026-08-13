#!/usr/bin/env python3
# compare_snapshots.py — compara site/index.html com a string HTML_CONTENT de build_site.py
import re, html as html_mod, ast

def tokenize(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    without_comments = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    text = re.sub(r'<[^>]+>', ' ', without_comments)
    text = html_mod.unescape(text)
    words = re.findall(r'\S+', text.lower())
    return set(words), len(words)

s1, n1 = tokenize('site/index.html')

with open('site/build_site.py', encoding='utf-8') as f:
    bcode = f.read()

import ast
try:
    ast.parse(bcode)
    ok = True
except SyntaxError as e:
    ok = False
    print('build_site.py NAO eh Python sintaticamente valido:', e)

print('=== build_site.py vs index.html ===')
print('build_site.py sintaticamente valido:', ok)

if ok:
    m = re.search(r'HTML_CONTENT\s*=\s*[""]{3}(.*?)[""]{3}', bcode, re.S)
    if m:
        snap_text = re.sub(r'<[^>]+>', ' ', m.group(1))
        snap_text = html_mod.unescape(snap_text)
        snap_words = set(re.findall(r'\S+', snap_text.lower()))
        inter = s1 & snap_words
        print('overlap palavras textuais build_site.py snapshot vs index.html:', len(inter), 'de', len(snap_words))
    else:
        print('build_site.py NAO contem bloco HTML_CONTENT tipo triple-quoted')

print()
print('Conclusao:')
if not ok:
    print('-> build_site.py NAO é Python sintaticamente valido')
    print('-> nao pode ser o gerador do index.html atual')
elif not re.search(r'HTML_CONTENT\s*=\s*[""]{3}', bcode):
    print('-> build_site.py nao contem HTML em string triple-quoted visivel')
    print('-> provavelmente NAO eh o gerador do index.html atual')
else:
    print('-> build_site.py contem HTML em string, mas texto difere do index.html atual')
    print('-> provavelmente snapshot de outro ponto no tempo / outro design')
