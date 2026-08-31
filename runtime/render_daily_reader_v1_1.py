#!/usr/bin/env python3
from __future__ import annotations
import argparse,html,json,re,subprocess
from pathlib import Path

SCHEMA='READER_DOM_V1'
DS='ENERGY_INTEL_READER_DS_V1'
CSS='energy-intel-reader-ds-v1.css'

def read_frontmatter(txt):
    if not txt.startswith('---\n'): return {},txt
    end=txt.find('\n---\n',4)
    if end<0: return {},txt
    meta={}
    for line in txt[4:end].splitlines():
        if ':' in line:
            k,v=line.split(':',1); meta[k.strip()]=v.strip().strip('"\'')
    return meta,txt[end+5:]

def load_source_map(path):
    if not path: return {}
    obj=json.loads(Path(path).read_text('utf-8'))
    rows=obj.get('source_map') or obj.get('sources') or []
    out={}
    for r in rows:
        sid=str(r.get('source_id') or r.get('id') or '').strip().upper()
        url=r.get('url')
        if sid and url: out[sid]=url
    return out

def inject_source_links(body, source_map):
    for sid,url in source_map.items():
        body=re.sub(
            rf'\[Source:\s*{re.escape(sid)}\](?!\()',
            f'[Source: {sid}]({url})',
            body,
            flags=re.I
        )
    return body

def pandoc_fragment(md_path):
    cp=subprocess.run(['pandoc',str(md_path),'-f','gfm','-t','html5'],text=True,encoding='utf-8',errors='replace',capture_output=True)
    if cp.returncode: raise RuntimeError((cp.stderr or cp.stdout)[-1800:])
    frag=cp.stdout
    frag=re.sub(r'<table>', '<div class="ei-table-wrap"><table>',frag)
    frag=frag.replace('</table>','</table></div>')
    frag=re.sub(r'<a\s+href="(https?://[^"]+)"',r'<a href="\1" target="_blank" rel="noopener noreferrer"',frag)
    return frag

def toc(fragment):
    hs=re.findall(r'<h2 id="([^"]+)">(.*?)</h2>',fragment,re.S)
    return '\n'.join(f'<a href="#{html.escape(i,quote=True)}">{re.sub("<.*?>","",t)}</a>' for i,t in hs[:30])

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',required=True)
    ap.add_argument('--output',required=True)
    ap.add_argument('--surface',choices=['private','public'],required=True)
    ap.add_argument('--css-href',default='../../assets/'+CSS)
    ap.add_argument('--period',default='')
    ap.add_argument('--source-map',default='')
    a=ap.parse_args()

    src=Path(a.input); raw=src.read_text('utf-8-sig',errors='replace')
    meta,body=read_frontmatter(raw)
    if meta.get('reader_schema') not in {None,'',SCHEMA}: raise SystemExit('reader_schema mismatch')
    if meta.get('design_system') not in {None,'',DS}: raise SystemExit('design_system mismatch')

    source_map=load_source_map(a.source_map)
    body=inject_source_links(body,source_map)

    unresolved=sorted(set(re.findall(r'\[Source:\s*(S\d+)\](?!\()',body,re.I)))
    if source_map and unresolved:
        raise SystemExit('unresolved source markers: '+','.join(unresolved))

    tmp=src.with_suffix(src.suffix+'.reader_tmp.md')
    tmp.write_text(body,encoding='utf-8')
    try: frag=pandoc_fragment(tmp)
    finally: tmp.unlink(missing_ok=True)

    h1=re.search(r'<h1[^>]*>(.*?)</h1>',frag,re.S)
    title=re.sub('<.*?>','',h1.group(1)) if h1 else f'Energy Intel Daily {a.period}'
    if h1: frag=frag[:h1.start()]+frag[h1.end():]
    edition='Private' if a.surface=='private' else 'Public'

    doc=f'''<!doctype html>
<html lang="zh-CN" data-reader-schema="{SCHEMA}" data-reader-citation-mode="INLINE_EXTERNAL_V1">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><link rel="stylesheet" href="{html.escape(a.css_href,quote=True)}"></head>
<body class="energy-intel-reader cycle-daily">
<header class="ei-header"><div class="ei-kicker">ENERGY INTEL · DAILY · {edition.upper()}</div><h1>{html.escape(title)}</h1><div class="ei-meta">Period: {html.escape(a.period)} · Editorial: DAILY_V4 · Reader: {SCHEMA} · Design: {DS}</div></header>
<div class="ei-shell"><nav class="ei-toc">{toc(frag)}</nav><article class="ei-article">{frag}</article></div>
<footer class="ei-footer">Energy Intel · {edition} surface · {html.escape(a.period)}</footer>
</body></html>
'''
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(doc,encoding='utf-8')
    print(out)

if __name__=='__main__': raise SystemExit(main())
