#!/usr/bin/env python3
"""Structural validation only; does not claim Swift compilation or iOS rendering."""
import json,re,xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parents[1]
s=(R/'TIDEHome.xcodeproj/project.pbxproj').read_text()
s=re.sub(r'//[^\n]*|/\*.*?\*/','',s,flags=re.S)
tokens=re.findall(r'"(?:\\.|[^"\\])*"|[{}()=;,]|[^\s{}()=;,]+',s)
i=0
def value():
 global i
 t=tokens[i];i+=1
 if t=='{':
  d={}
  while tokens[i]!='}':
   k=value();assert tokens[i]=='=';i+=1;d[k]=value();assert tokens[i]==';';i+=1
  i+=1;return d
 if t=='(':
  a=[]
  while tokens[i]!=')':
   a.append(value())
   if tokens[i]==',':i+=1
  i+=1;return a
 return bytes(t[1:-1],'utf-8').decode('unicode_escape') if t.startswith('"') else t
project=value();assert i==len(tokens)
objects=project['objects'];assert project['rootObject'] in objects
for key,obj in objects.items():
 for field in ['fileRef','buildConfigurationList','mainGroup','productRefGroup','productReference']:
  if field in obj:assert obj[field] in objects,(key,field,obj[field])
 for field in ['children','files','buildPhases','buildConfigurations','targets']:
  for ref in obj.get(field,[]):assert ref in objects,(key,field,ref)
sources=list((R/'TIDEHome').glob('*.swift'))
source_refs=[v['path'] for v in objects.values() if v.get('lastKnownFileType')=='sourcecode.swift']
assert sorted(source_refs)==sorted(p.name for p in sources)
phase=next(v for v in objects.values() if v.get('isa')=='PBXSourcesBuildPhase')
assert len(phase['files'])==len(sources)
asset_root=R/'TIDEHome/Assets.xcassets';assets=[]
for p in asset_root.rglob('Contents.json'):
 j=json.loads(p.read_text())
 for image in j.get('images',[]):
  if 'filename' in image:
   a=p.parent/image['filename'];im=Image.open(a);im.verify();assets.append(p.parent.stem)
assert len(assets)==16
all_swift='\n'.join(p.read_text() for p in sources)
for n in re.findall(r'artwork:\s*"([a-z][a-z-]+)"|Image\("([a-z][a-z-]+)"\)',all_swift):
 name=next(x for x in n if x)
 assert name in assets,name
for p in (R/'TIDEHome.xcodeproj').rglob('*.xcscheme'):ET.parse(p)
ET.parse(R/'TIDEHome.xcodeproj/project.xcworkspace/contents.xcworkspacedata')
assert 'URLSession' not in all_swift and 'WKWebView' not in all_swift
assert len(list((R/'Preview/renders').glob('*-offline-layout.png')))==4
for p in (R/'Preview/renders').glob('*-offline-layout.png'):
 assert Image.open(p).size==(707,1536)
report={'project_structure':'passed','swift_target_membership':f'{len(sources)} files passed','artwork_assets':f'{len(assets)} images decoded','shared_scheme_and_workspace_xml':'passed','scope':'structural checks only; see Design/Verified and README for native runtime verification'}
print(json.dumps(report,indent=2))
