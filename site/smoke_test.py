#!/usr/bin/env python3
"""
Smoke test for CodeHouse site/ directory.
Validates: file existence, HTML well-formedness, internal links,
CSS brace balance, CSS variable definitions, JS balance, Formspree,
and WhatsApp number consistency.

Usage: python site/smoke_test.py
Exit code: 0 if all OK, 1 if any FAIL.
"""

import os
import re
import sys
from html.parser import HTMLParser

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SITE_DIR = os.path.dirname(os.path.abspath(__file__))
REQUIRED_FILES = [
    "index.html",
    "exemplos.html",
    "politica-privacidade.html",
    "css/tokens.css",
    "css/layout.css",
    "css/components.css",
    "css/examples.css",
    "js/nav.js",
    "js/scroll.js",
    "js/theme.js",
    "js/examples.js",
    "js/faq.js",
    "og-image.png",
    "robots.txt",
    "sitemap.xml",
    "_headers",
    "render.yaml",
    "CNAME",
]

# Self-closing / void HTML tags (no closing tag expected)
VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

# ---------------------------------------------------------------------------
# Helper: read file
# ---------------------------------------------------------------------------
def read_file(rel_path):
    path = os.path.join(SITE_DIR, rel_path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

# ---------------------------------------------------------------------------
# TEST 1 — File existence
# ---------------------------------------------------------------------------
def test_file_existence():
    missing = []
    for rel in REQUIRED_FILES:
        path = os.path.join(SITE_DIR, rel)
        if not os.path.isfile(path):
            missing.append(rel)
    if missing:
        return False, f"Missing files: {', '.join(missing)}"
    return True, f"All {len(REQUIRED_FILES)} required files present"

# ---------------------------------------------------------------------------
# TEST 2 — HTML well-formedness (tag matching)
# ---------------------------------------------------------------------------
class TagValidator(HTMLParser):
    """Tracks open tags and reports unclosed ones."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in VOID_TAGS:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in VOID_TAGS:
            return
        # Find matching opener
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack.pop(i)
                return
        self.errors.append(f"Unexpected closing </{tag}> at line {self.getpos()[0]}")

    def error(self, message):
        pass  # suppress default error printing


def test_html_well_formedness():
    html_files = ["index.html", "exemplos.html", "politica-privacidade.html"]
    all_errors = []
    for rel in html_files:
        content = read_file(rel)
        if content is None:
            all_errors.append(f"{rel}: cannot read")
            continue
        # Strip content inside <script> and <style> to avoid false positives
        # (JS/CSS content is not HTML)
        cleaned = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        cleaned = re.sub(r'<style[^>]*>.*?</style>', '', cleaned, flags=re.DOTALL)
        parser = TagValidator()
        try:
            parser.feed(cleaned)
        except Exception as e:
            all_errors.append(f"{rel}: parse error: {e}")
            continue
        if parser.errors:
            for err in parser.errors:
                all_errors.append(f"{rel}: {err}")
        if parser.stack:
            for tag, pos in parser.stack:
                all_errors.append(f"{rel}: unclosed <{tag}> at line {pos[0]}")
    if all_errors:
        return False, "; ".join(all_errors[:5])
    return True, "All HTML files well-formed"


# ---------------------------------------------------------------------------
# TEST 3 — Internal links not broken
# ---------------------------------------------------------------------------
def test_internal_links():
    """Check that all href="*.html" and href="#id" point to existing resources."""
    html_files = ["index.html", "exemplos.html", "politica-privacidade.html"]
    # Collect all IDs in each file
    file_ids = {}
    for rel in html_files:
        content = read_file(rel)
        if content is None:
            continue
        ids = set(re.findall(r'id="([^"]+)"', content))
        file_ids[rel] = ids
    # Also check for anchor/name attributes
    for rel in html_files:
        content = read_file(rel)
        if content is None:
            continue
        ids = re.findall(r'name="([^"]+)"', content)
        file_ids[rel].update(ids)

    broken = []
    for rel in html_files:
        content = read_file(rel)
        if content is None:
            continue
        # Find all hrefs
        hrefs = re.findall(r'href="([^"]+)"', content)
        base_dir = os.path.dirname(rel)  # "" for top-level, "css/" etc.
        for href in hrefs:
            if href.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
                continue  # external links — skip
            if href.startswith("#"):
                # Same-file anchor
                anchor = href[1:]
                if anchor and anchor not in file_ids.get(rel, set()):
                    broken.append(f"{rel}: href=\"{href}\" — id '{anchor}' not found in {rel}")
            elif "#" in href:
                # file#anchor
                parts = href.split("#", 1)
                target_file = parts[0]
                anchor = parts[1] if len(parts) > 1 else ""
                # Resolve relative to base_dir
                target_path = os.path.normpath(os.path.join(base_dir, target_file))
                if not os.path.isfile(os.path.join(SITE_DIR, target_path)):
                    broken.append(f"{rel}: href=\"{href}\" — file '{target_path}' not found")
                elif anchor and target_path.replace("\\", "/") in file_ids:
                    if anchor not in file_ids[target_path.replace("\\", "/")]:
                        broken.append(f"{rel}: href=\"{href}\" — id '{anchor}' not found in {target_path}")
            elif href == "/":
                # Root reference → index.html
                if not os.path.isfile(os.path.join(SITE_DIR, "index.html")):
                    broken.append(f"{rel}: href=\"/\" → index.html not found")
            elif href.endswith(".html") or "." not in href.split("/")[-1]:
                # Resolve relative path
                target_path = os.path.normpath(os.path.join(base_dir, href))
                if not os.path.isfile(os.path.join(SITE_DIR, target_path)):
                    broken.append(f"{rel}: href=\"{href}\" — file '{target_path}' not found")
    if broken:
        return False, "; ".join(broken[:5])
    return True, "All internal links resolve"


# ---------------------------------------------------------------------------
# TEST 4 — CSS brace balance
# ---------------------------------------------------------------------------
def test_css_braces():
    css_files = ["css/tokens.css", "css/layout.css", "css/components.css", "css/examples.css"]
    errors = []
    for rel in css_files:
        content = read_file(rel)
        if content is None:
            errors.append(f"{rel}: cannot read")
            continue
        # Remove comments
        no_comments = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        opens = no_comments.count('{')
        closes = no_comments.count('}')
        if opens != closes:
            errors.append(f"{rel}: {opens} '{{' vs {closes} '}}'")
    if errors:
        return False, "; ".join(errors)
    return True, "All CSS files have balanced braces"


# ---------------------------------------------------------------------------
# TEST 5 — CSS variables used are defined in :root (tokens.css)
# ---------------------------------------------------------------------------
def test_css_variables_defined():
    """Ensure every var(--xxx) used in any CSS is defined in tokens.css :root."""
    tokens_content = read_file("css/tokens.css")
    if tokens_content is None:
        return False, "css/tokens.css cannot be read"
    # Extract :root block
    root_match = re.search(r':root\s*\{([^}]*)\}', tokens_content, re.DOTALL)
    if not root_match:
        return False, "No :root block in tokens.css"
    root_block = root_match.group(1)
    defined = set(re.findall(r'(--[\w-]+)\s*:', root_block))
    # Always-allowed vars
    defined.update({"--mx", "--my", "--h"})  # custom properties set via JS/style

    css_files = ["css/layout.css", "css/components.css", "css/examples.css"]
    undefined = []
    for rel in css_files:
        content = read_file(rel)
        if content is None:
            continue
        used = set(re.findall(r'var\((--[\w-]+)[\s,)]', content))
        for var in used:
            if var not in defined:
                undefined.append(f"{rel}: var({var}) not defined in :root")
    if undefined:
        return False, "; ".join(undefined[:5])
    return True, "All CSS variables defined in :root"


# ---------------------------------------------------------------------------
# TEST 6 — JS brace/paren balance
# ---------------------------------------------------------------------------
def test_js_balance():
    js_files = ["js/nav.js", "js/scroll.js", "js/theme.js", "js/examples.js"]
    errors = []
    for rel in js_files:
        content = read_file(rel)
        if content is None:
            errors.append(f"{rel}: cannot read")
            continue
        # Remove comments (// and /* */)
        no_comments = re.sub(r'//[^\n]*', '', content)
        no_comments = re.sub(r'/\*.*?\*/', '', no_comments, flags=re.DOTALL)
        # Remove strings (rough)
        no_strings = re.sub(r'"(?:[^"\\]|\\.)*"', '""', no_comments)
        no_strings = re.sub(r"'(?:[^'\\]|\\.)*'", "''", no_strings)
        no_strings = re.sub(r'`(?:[^`\\]|\\.)*`', '``', no_strings)

        counts = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0}
        for ch in no_strings:
            if ch in counts:
                counts[ch] += 1
        if counts['('] != counts[')']:
            errors.append(f"{rel}: parens {counts['(']} open vs {counts[')']} close")
        if counts['{'] != counts['}']:
            errors.append(f"{rel}: braces {counts['{']} open vs {counts['}']} close")
        if counts['['] != counts[']']:
            errors.append(f"{rel}: brackets {counts['[']} open vs {counts[']']} close")
    if errors:
        return False, "; ".join(errors)
    return True, "All JS files have balanced delimiters"


# ---------------------------------------------------------------------------
# TEST 7 — Formspree action URL present in form
# ---------------------------------------------------------------------------
def test_formspree_action():
    html_files = ["index.html", "exemplos.html"]
    found = False
    for rel in html_files:
        content = read_file(rel)
        if content is None:
            continue
        if re.search(r'<form[^>]*action="https://formspree\.io/', content):
            found = True
            break
    if not found:
        return False, "No form with Formspree action found"
    return True, "Formspree action URL present"


# ---------------------------------------------------------------------------
# TEST 8 — WhatsApp number consistency
# ---------------------------------------------------------------------------
def test_whatsapp_consistency():
    """All wa.me links in the site must use the same phone number."""
    html_files = ["index.html", "exemplos.html", "politica-privacidade.html"]
    numbers = {}
    for rel in html_files:
        content = read_file(rel)
        if content is None:
            continue
        matches = re.findall(r'wa\.me/(\d+)', content)
        for num in matches:
            numbers.setdefault(num, []).append(rel)
    if len(numbers) > 1:
        details = ", ".join(f"{n} (in {', '.join(set(files))})" for n, files in numbers.items())
        return False, f"Inconsistent WhatsApp numbers: {details}"
    if not numbers:
        return True, "No WhatsApp links found (OK — no number to be inconsistent)"
    return True, f"All WhatsApp links use number {list(numbers.keys())[0]}"


# ---------------------------------------------------------------------------
# Run all tests
# ---------------------------------------------------------------------------
def main():
    tests = [
        ("1. File existence", test_file_existence),
        ("2. HTML well-formedness", test_html_well_formedness),
        ("3. Internal links", test_internal_links),
        ("4. CSS brace balance", test_css_braces),
        ("5. CSS variables defined", test_css_variables_defined),
        ("6. JS balance", test_js_balance),
        ("7. Formspree action", test_formspree_action),
        ("8. WhatsApp consistency", test_whatsapp_consistency),
    ]

    print(f"CodeHouse Site Smoke Test")
    print(f"Site dir: {SITE_DIR}")
    print(f"{'='*60}")

    failures = 0
    for name, fn in tests:
        try:
            ok, msg = fn()
        except Exception as e:
            ok, msg = False, f"EXCEPTION: {e}"
        status = "OK  " if ok else "FAIL"
        print(f"  [{status}] {name}: {msg}")
        if not ok:
            failures += 1

    print(f"{'='*60}")
    if failures == 0:
        print(f"ALL {len(tests)} TESTS PASSED")
        sys.exit(0)
    else:
        print(f"{failures}/{len(tests)} TESTS FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()