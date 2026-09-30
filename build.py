# Generates the static Loopr legal pages. No framework, no build step at serve time.
import html, re
UPDATED = "30 September 2026"
EMAIL = "pascallindenau@googlemail.com"
NAV = [("index.html","Legal"),("privacy.html","Privacy"),("terms.html","Terms"),("notice.html","Notice"),("imprint.html","Imprint")]

def page(fname, title, body, desc):
    nav = "\n".join(f'      <a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Loopr</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">
  <header class="site">
    <a class="brand" href="index.html">Loopr</a>
    <nav class="pages">
{nav}
    </nav>
  </header>
  <main>
{body}
  </main>
  <footer class="site">Loopr is an independent project and is not affiliated with WHOOP, Inc.</footer>
</div>
</body>
</html>
'''

def md(text):
    """Tiny markdown subset: #, ##, paragraphs, - lists, **bold**, [t](u)."""
    out=[]; lst=False
    def inline(s):
        s=html.escape(s, quote=False)
        s=re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s=re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
        return s
    blocks=[]
    for block in text.strip().split("\n\n"):
        lines=block.strip().split("\n")
        if lines[0].startswith("## ") and len(lines)>1:
            blocks += [lines[:1], lines[1:]]
        else:
            blocks.append(lines)
    for lines in blocks:
        if lines[0].startswith("- "):
            out.append("<ul>"+"".join(f"<li>{inline(l[2:])}</li>" for l in lines)+"</ul>")
        elif lines[0].startswith("## "):
            out.append(f"<h2>{inline(lines[0][3:])}</h2>")
        elif lines[0].startswith("# "):
            out.append(f"<h1>{inline(lines[0][2:])}</h1>")
            if len(lines)>1: out.append(f'<p class="meta">{inline(" ".join(lines[1:]))}</p>')
        elif lines[0].startswith("> "):
            out.append(f'<div class="banner">{inline(" ".join(l[2:] for l in lines))}</div>')
        elif len(lines)>1 and not any(l.rstrip().endswith(('.',':',';',',')) for l in lines):
            out.append("<p>"+"<br>".join(inline(l) for l in lines)+"</p>")
        else:
            out.append(f"<p>{inline(' '.join(lines))}</p>")
    return "\n".join("    "+o for o in out)

import pages
for fname,title,desc,text in pages.PAGES:
    open(fname,"w").write(page(fname,title,md(text.replace("{UPDATED}",UPDATED).replace("{EMAIL}",EMAIL)),desc))
print("built", len(pages.PAGES), "pages")
