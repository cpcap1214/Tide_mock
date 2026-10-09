// Browser layout QA only. This does not compile or render SwiftUI.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async()=>{
 const root=path.resolve(__dirname,'..');
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const page=await browser.newPage({viewport:{width:707,height:1536},deviceScaleFactor:1});
 const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 const out=path.join(root,'Preview','renders');fs.mkdirSync(out,{recursive:true});
 for(const [i,offset] of [0,915,1999,2850].entries()){
  await page.goto('file://'+path.join(root,'Preview','index.html')+'?offset='+offset);
  await page.evaluate(()=>Promise.all([...document.images].map(i=>i.decode())));
  await page.waitForTimeout(250);
  await page.screenshot({path:path.join(out,`0${i+1}-browser-layout.png`)});
  const facts=await page.evaluate(()=>({scrollTop:document.querySelector('.scroll').scrollTop,width:document.querySelector('#screen').offsetWidth,contentHeight:document.querySelector('.canvas').offsetHeight,images:[...document.images].every(i=>i.complete&&i.naturalWidth>0),statusBar:document.querySelector('.time').textContent}));
  console.log(JSON.stringify({offset,...facts}));
 }
 if(errors.length) throw new Error(errors.join('\n'));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
