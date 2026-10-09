#!/usr/bin/env python3
"""Offline SVG geometry study; not a native SwiftUI or browser screenshot."""
from pathlib import Path
import base64, html, subprocess
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'Preview'/'renders'; OUT.mkdir(parents=True,exist_ok=True)
P=[]
def add(s): P.append(s)
def paint(color, attr='fill'):
 if color.startswith('#') and len(color)==9:return f'{attr}="{color[:7]}" {attr}-opacity="{int(color[7:9],16)/255:.4f}"'
 return f'{attr}="{color}"'
def rect(x,y,w,h,fill,r=0,stroke='none',sw=1): add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" {paint(fill)} {paint(stroke,"stroke")} stroke-width="{sw}"/>')
def text(x,y,s,size=24,fill='#fafaf9',weight='400',anchor='start',family='Arial',italic=False):
 add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" {paint(fill)}'+(' font-style="italic"' if italic else '')+'>'+html.escape(s)+'</text>')
def art(name,x,y,w,h):
 p=ROOT/'TIDEHome'/'Assets.xcassets'/(name+'.imageset')/(name+'.png')
 b=base64.b64encode(p.read_bytes()).decode()
 add(f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="none" href="data:image/png;base64,{b}"/>')
paths={
'breath':'<path d="M5 28C2 12 13 3 28 4C30 22 19 30 5 28M5 28L17 15" fill="none" stroke="currentColor" stroke-width="2.9" stroke-linejoin="round"/>',
'focus':'<circle cx="16" cy="16" r="13.3" fill="none" stroke="currentColor" stroke-width="2.7"/><circle cx="16" cy="16" r="3.5"/>',
'sleep':'<path d="M16 2.5C24 3 29 8 29 15C29 23 23 28 16 28C8 28 4 23 3 17C15 19 21 10 16 2.5Z" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="5.3" cy="5.3" r="2.2"/>',
'home':'<rect x="3" y=".5" width="26" height="31" rx="4"/><path d="M12.6 21.3C15.5 18.2 14.7 10.1 20.2 10.1" fill="none" stroke="#393530" stroke-width="2.5" stroke-linecap="round"/>',
'moon':'<path d="M22 2C11 1 13 26 28.5 23C25 29 20 31 14 30C6 29 1 23 2 16C1 5 12-1 22 2Z"/>',
'meditation':'<path d="M16 3C20 3 25 15 28 23C31 29 29 30 24 30H7C1 30 1 28 4 23C7 15 12 3 16 3Z"/>',
'sound':'<circle cx="16" cy="16" r="15"/>',
'chevron':'<path d="M11 5l10 11-10 11" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>',
'sparkle':'<path d="M11 7Q13 17 21 19Q13 21 11 31Q9 21 1 19Q9 17 11 7ZM24 0Q25 6 31 8Q25 10 24 16Q23 10 17 8Q23 6 24 0Z"/>',
'location':'<path d="M3 13L29 3L20 29L15 18Z"/>'}
def icon(name,x,y,w=32,fill='#fafaf9'):
 add(f'<g transform="translate({x} {y}) scale({w/32})" color="{fill}" fill="{fill}">{paths[name]}</g>')
def glass(x,y,w,h,r,fill='#706b68',opacity=0.6):
 add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" fill-opacity="{opacity}" stroke="url(#glass-edge)" stroke-width="1.4"/>')
for idx,offset in enumerate([0,915,1999,2850],1):
 P=[]
 add('<svg xmlns="http://www.w3.org/2000/svg" width="707" height="1536" viewBox="0 0 707 1536">')
 add('''<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#535454"/><stop offset=".52" stop-color="#849198"/><stop offset="1" stop-color="#898d90"/></linearGradient>
 <linearGradient id="glass-edge" x1="0" y1="0" x2="1" y2="1"><stop stop-color="white" stop-opacity=".6"/><stop offset=".5" stop-color="white" stop-opacity=".16"/><stop offset="1" stop-color="white" stop-opacity=".43"/></linearGradient>
 <linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#353532"/><stop offset=".72" stop-color="#353532"/><stop offset=".84" stop-color="#353532" stop-opacity=".92"/><stop offset="1" stop-color="#353532" stop-opacity="0"/></linearGradient>
 <linearGradient id="orb"><stop stop-color="#26757d"/><stop offset=".62" stop-color="#329da5"/><stop offset="1" stop-color="#42aeb1"/></linearGradient>
 <linearGradient id="avatar" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#ac00c7"/><stop offset="1" stop-color="#68218f"/></linearGradient>
 <linearGradient id="membership" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#b7bbc9"/><stop offset=".44" stop-color="#c7bec6"/><stop offset="1" stop-color="#d8c2a9"/></linearGradient>
 <linearGradient id="bottom" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#796c65" stop-opacity="0"/><stop offset="1" stop-color="#796c65" stop-opacity=".74"/></linearGradient>
 <linearGradient id="water-fade" x1="0" y1="0" x2="0" y2="1"><stop stop-color="white" stop-opacity="0"/><stop offset=".13" stop-color="white"/><stop offset="1" stop-color="white"/></linearGradient><mask id="water-mask"><rect x="0" y="1095" width="707" height="405" fill="url(#water-fade)"/></mask><clipPath id="viewport"><rect width="707" height="1536"/></clipPath>
 </defs><g clip-path="url(#viewport)">''')
 rect(0,0,707,1536,'#393530')
 if offset==0:
  rect(0,0,707,252,'url(#sky)');art('hero-scene',0,250,707,882);add('<g mask="url(#water-mask)">');art('hero-water',0,1095,707,405);add('</g>');rect(0,1086,707,450,'url(#bottom)');glass(39,1370,629,190,33,'#aaa2a0',.14)
 add(f'<g transform="translate(0 {-offset})">')
 if offset==0:icon('sparkle',39,1142,23,'#cfcdcb');text(68,1162,'Now for you',24,'#cfcdcb','500')
 for i,(label,glyph) in enumerate([('Breathwork','breath'),('Focus Timer','focus'),('Sleep Tracker','sleep')]):
  x=39+i*271;glass(x,1200,251,138,32,'#d0c8c7' if offset==0 else '#797574',.3 if offset==0 else .48);icon(glyph,x+30,1231,31);text(x+28,1309,label,24,'#d0cdcb')
 if offset!=0:
  text(39,1426,'Oct 9th',22,'#817c77');text(39,1466,'Be yourself; everyone else is',28);text(39,1506,'already taken.',28);text(39,1547,'Author, Oscar Wilde',22,'#817c77')
  add('<circle cx="623" cy="1477" r="45" fill="url(#orb)"/>')
 for row,items in enumerate([[(245,'✨ Daily Meditation'),(140,'◻ Sleep'),(230,'📖 Improve Focus')],[(197,'💨 Breathwork'),(277,'🌿 Emotion Regulation'),(218,'🐤 Reduce Stress')]]):
  x=39
  for w,label in items:
   y=1618+row*80;rect(x,y,w,60,'#494542',30);text(x+w/2,y+39,label,22,weight='500',anchor='middle');x+=w+19
 for y,title,cards in [
 (1825,'Quiet the Mind',[('annoyance','Annoyance','5-15 min · Meditation'),('exhaustion','Exhaustion','5-20 min · Meditation'),('sadness-peek','Sadness','5-15 min · Meditation')]),
 (2314,'Daytime Stress Relief',[('mind-detox','Mind Detox','10 min · Meditation'),('let-go','Let Go of Thoughts','10 min · Meditation'),('panic-peek','Panic','10 min · Meditation')]),
 (2803,'Better Focus, Higher Efficiency',[('before-study','Before Study','5-10 min · Meditation'),('eye-strain','Eye Strain','5-10 min · Meditation'),('steps-peek','Step by Step','10-20 min · Meditation')])]:
  text(39,y+34,title,34,weight='500');icon('chevron',649,y+7,25)
  for i,(a,t,d) in enumerate(cards):
   x=39+310*i;art(a,x,y+68,284 if i<2 else 48,284)
   if a=='exhaustion':rect(x+220,y+84,48,28,'#929d99',6);text(x+244,y+104,'Free',15,'#fff',anchor='middle')
   text(x+3,y+389,t,24);text(x+3,y+418,d,18,'#918c86')
 text(39,3326,'Join TIDE Plus',35,weight='500')
 rect(39,3346,629,429,'url(#membership)',33,'#fff',1.5)
 text(263,3472,'TIDE',42,weight='500');add('<g transform="translate(367 3426) scale(1.039 1)" fill="none" stroke="white" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 53L12 23M3 31C-4 23 9 14 19 16C39 17 20 38 3 41M22 39C38 26 50-3 40 3C31 7 24 39 33 40C38 43 43 30 45 24C42 31 36 46 45 40C50 36 53 30 55 24C52 33 48 47 56 39C59 36 59 33 61 29M74 23C66 15 59 23 65 29C72 33 74 38 68 40C61 45 55 37 60 33"/></g>')
 for n,t in enumerate(['Enjoy exclusive premium content and','advanced features across all','platforms.']):text(353.5,3526+31*n,t,25,weight='500',anchor='middle')
 rect(194,3637,318,79,'#ffffffbd',40,'#ffffffb3',1.4);text(353,3685,'Learn More',26,'#a68f7f','500','middle')
 text(39,3872,'Library',34,weight='500')
 for x,label,a in [(39,'Meditation','library-meditation'),(364,'Soundscape','library-soundscape')]:
  rect(x,3909,304,197,'#4e4a46',27);art(a,x+168,3918,121,102);text(x+19,4083,label,24,weight='500')
 text(353.5,4233,'A mindful space for you.',21,'#867d74','400','middle',family='Times New Roman',italic=True)
 add('</g>')
 if offset:rect(0,0,707,289,'url(#shade)')
 text(77,63,'18:25',32,weight='600');icon('moon' if offset else 'location',165,39,26)
 for n in range(4):rect(498+n*9,65-(10+n*5),5,10+n*5,'#fff',2.5)
 text(547,63,'5G',26,weight='500');rect(592,40,47,25,'#ffffff52',7);rect(592,40,42,25,'#fff',6);text(615.5,62,'88',23,'#383735','700','middle');rect(642,47,3,10,'#ffffff66',2)
 text(32,179,'Good day',50,weight='600')
 glass(436,130,149,64,34,'#ffffff',.15)
 add('<g transform="translate(465 147)" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11h6l9-8v26l-9-8H4V11m21-3v10M3 3l26 26"/></g>')
 for x in [528,543]:
  for y in [149,164]:rect(x,y,9,9,'none',2.6,'#fff',2.8)
 add('<circle cx="641.5" cy="162.5" r="32.5" fill="url(#avatar)" stroke="#ffffff2e" stroke-width="1.2"/>');text(641.5,173,'心哲',27,anchor='middle',family='Noto Sans CJK TC');add('<circle cx="666" cy="139" r="7" fill="#fe555d"/>')
 for i,s in enumerate('SMTWTFS'):text(45+34*i,233,s,20,'#fafaf9' if i==5 else '#ffffff61','600','middle')
 glass(33,1403,641,100,54,'#b6adb0',.38);rect(40,1409,168,87,'#3027208c',44)
 for i,(label,glyph) in enumerate([('Home','home'),('Sleep','moon'),('Meditation','meditation'),('Sound','sound')]):
  cx=123.6+153.25*i;icon(glyph,cx-15.5,1426,31,'#fafaf9' if i==0 else '#b8b3b4');text(cx,1481,label,17,'#fff','600','middle')
 add('</g></svg>')
 svg=OUT/f'0{idx}-offline-layout.svg';svg.write_text('\n'.join(P))
 png=OUT/f'0{idx}-offline-layout.png'
 result=subprocess.run(['inkscape',str(svg),'--export-type=png','--export-filename='+str(png)],capture_output=True,text=True)
 if result.returncode:raise RuntimeError(result.stderr)
 print(png)
