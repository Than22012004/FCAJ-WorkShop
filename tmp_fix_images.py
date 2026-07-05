from pathlib import Path
import re

root = Path('c:/Users/ASUS/Báo cáo thực tập/FCAJ---Work-shop').resolve()
content_dir = root / 'content'
static_images_dir = root / 'static' / 'images'

files = [p for p in static_images_dir.rglob('*') if p.is_file()]
by_lower = {p.relative_to(static_images_dir).as_posix().lower(): p.relative_to(static_images_dir).as_posix() for p in files}

md_pattern = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
html_pattern = re.compile(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', re.I)

changed = []
missing = []

for md_path in sorted(content_dir.rglob('*.md')):
    text = md_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    new_lines = []
    in_code = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_code = not in_code
            new_lines.append(line)
            continue
        if in_code:
            new_lines.append(line)
            continue

        def repl_markdown(match):
            nonlocal changed, missing
            raw = match.group(1).strip()
            if raw.startswith('<') and raw.endswith('>'):
                raw = raw[1:-1]
            candidate = raw.split()[0]
            candidate = candidate.split('#', 1)[0].split('?', 1)[0]
            if candidate.startswith(('http://', 'https://', 'data:', 'mailto:', '#')):
                return match.group(0)
            rel = None
            if candidate.startswith('/'):
                cand = candidate.lstrip('/')
                for prefix in ['images/', 'static/images/']:
                    if cand.startswith(prefix):
                        cand = cand[len(prefix):]
                        rel = cand
                        break
                if rel is None:
                    rel = cand
            else:
                for prefix in ['images/', './images/', '../images/', 'static/images/', 'content/images/']:
                    if candidate.startswith(prefix):
                        rel = candidate[len(prefix):]
                        break
                if rel is None:
                    if re.match(r'^[A-Za-z]:\\', candidate):
                        rel = None
                    else:
                        rel = Path(candidate).name
            if rel is None:
                return match.group(0)
            rel_norm = rel.replace('\\', '/').lstrip('/')
            rel_key = rel_norm.lower()
            actual = None
            if rel_key in by_lower:
                actual = by_lower[rel_key]
            else:
                basename = Path(rel_norm).name.lower()
                matches = [rel_path for rel_path in by_lower if rel_path.endswith('/' + basename) or rel_path == basename]
                if len(matches) == 1:
                    actual = by_lower[matches[0]]
            if actual:
                new_path = '/images/' + actual.replace('\\', '/')
                if new_path != '/' + candidate.lstrip('/'):
                    changed.append((str(md_path.relative_to(root)), candidate, new_path))
                return match.group(0).replace(candidate, new_path)
            missing.append((str(md_path.relative_to(root)), candidate))
            return match.group(0)

        def repl_html(match):
            nonlocal changed, missing
            raw = match.group(1)
            candidate = raw.split('#', 1)[0].split('?', 1)[0]
            if candidate.startswith(('http://', 'https://', 'data:', 'mailto:', '#')):
                return match.group(0)
            rel = None
            if candidate.startswith('/'):
                cand = candidate.lstrip('/')
                for prefix in ['images/', 'static/images/']:
                    if cand.startswith(prefix):
                        cand = cand[len(prefix):]
                        rel = cand
                        break
                if rel is None:
                    rel = cand
            else:
                for prefix in ['images/', './images/', '../images/', 'static/images/', 'content/images/']:
                    if candidate.startswith(prefix):
                        rel = candidate[len(prefix):]
                        break
                if rel is None:
                    if re.match(r'^[A-Za-z]:\\', candidate):
                        rel = None
                    else:
                        rel = Path(candidate).name
            if rel is None:
                return match.group(0)
            rel_norm = rel.replace('\\', '/').lstrip('/')
            rel_key = rel_norm.lower()
            actual = None
            if rel_key in by_lower:
                actual = by_lower[rel_key]
            else:
                basename = Path(rel_norm).name.lower()
                matches = [rel_path for rel_path in by_lower if rel_path.endswith('/' + basename) or rel_path == basename]
                if len(matches) == 1:
                    actual = by_lower[matches[0]]
            if actual:
                new_path = '/images/' + actual.replace('\\', '/')
                if new_path != '/' + candidate.lstrip('/'):
                    changed.append((str(md_path.relative_to(root)), candidate, new_path))
                return match.group(0).replace(raw, new_path)
            missing.append((str(md_path.relative_to(root)), candidate))
            return match.group(0)

        new_line = md_pattern.sub(repl_markdown, line)
        new_line = html_pattern.sub(repl_html, new_line)
        new_lines.append(new_line)

    if '\n'.join(new_lines) != text:
        md_path.write_text('\n'.join(new_lines) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')

print('CHANGED_COUNT', len(changed))
for item in changed:
    print('CHANGE', item[0], '=>', item[1], '->', item[2])
print('MISSING_COUNT', len(missing))
for item in missing:
    print('MISSING', item[0], '=>', item[1])
