// Install playwright locally, or point PLAYWRIGHT_MODULE at an existing installation.
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root = path.resolve(__dirname, '../..');
const out = path.resolve(__dirname, '../images');
const uri = p => 'data:image/svg+xml;base64,' + fs.readFileSync(path.join(root, p)).toString('base64');
const logo = uri('assets/brand/logo.svg');
const diagram = uri('assets/diagrams/strategy.svg');
const slides = [
  ['01 / START WITH A PROBLEM', 'Learn the change.\nThen the pattern.', '23 Design Patterns', 'Runnable C++20 • Diagrams • Four languages'],
  ['02 / THE PROBLEM', 'A diagram alone\nis not a decision.', 'What changes? Who owns it?', 'Read the motivation, naive solution, and trade-offs.'],
  ['03 / THE METHOD', 'Give shipping\nits own rule.', 'Strategy: Checkout + ShippingRule', 'One checkout receives a standard or express policy.'],
  ['04 / THE EXAMPLE', 'Same checkout.\nDifferent totals.', 'Standard: 45\nExpress: 55\nExpress large: 120', 'Expected output from the Strategy C++20 example.'],
  ['05 / THE RESULT', 'Read it. Run it.\nChange the rule.', '23 examples with expected output', 'Compare behavior, then judge the abstraction.'],
  ['06 / YOUR NEXT STEP', 'Start with\nStrategy.', 'Explore 23 Design Patterns', 'Choose one pattern. Run its example. Try its challenge.'],
];
function document(w,h,slide) {
  const tall=h>=w;
  const [kicker,headline,sub,foot]=slide || ['PROBLEM → PATTERN → PRACTICE','23 Design Patterns','Learn GoF patterns with runnable C++20.','23 patterns • 4 documentation languages'];
  return `<!doctype html><html><meta charset="utf-8"><style>
  *{box-sizing:border-box}body{margin:0;background:#e7c99f;color:#25170e;font-family:Arial,sans-serif}
  main{width:${w}px;height:${h}px;padding:${tall?'65px':'30px 64px'};display:flex;flex-direction:column;position:relative;border:1px solid #c99e64}
  header{display:flex;align-items:center;gap:18px;font-size:23px;color:#76583f;border-bottom:1px solid #c99e64;padding-bottom:24px}header img{width:70px;height:47.5px}header span:last-child{margin-left:auto;font:18px Consolas,monospace}
  .kicker{color:#aa4117;font:22px Consolas,monospace;letter-spacing:2px;margin:${tall?'68px':'27px'} 0 18px}
  h1{font-size:${tall?'78':'76'}px;line-height:1.06;letter-spacing:-3px;margin:0;white-space:pre-line;font-weight:800}
  .sub{font-size:${tall?'36':'28'}px;line-height:1.45;white-space:pre-line;margin:24px 0;color:#76583f}
  .evidence{margin-top:auto;background:#101923;border-radius:16px;padding:${tall?'35px 25px':'16px'};color:#eaf2f5}.evidence p{margin:0 0 12px;color:#73e5b0;font:19px Consolas,monospace;letter-spacing:1px}.evidence img{width:100%;display:block}
  footer{margin-top:${tall?'42':'22'}px;font-size:${tall?'25':'21'}px;line-height:1.45}footer small{display:block;font:17px Consolas,monospace;color:#76583f;margin-top:12px}
  ${!tall ? "header{padding-bottom:14px}header img{width:56px;height:38px}.kicker{margin:20px 0 12px}.sub{margin:14px 0}.evidence img{height:112px;object-fit:contain}footer{margin-top:16px}footer small{margin-top:8px}" : ""}</style><main><header><img src="${logo}" alt="Sanfor logo"><span>Sanfor2004</span><span>C++20 / GoF</span></header><div class="kicker">${kicker}</div><h1>${headline}</h1><div class="sub">${sub}</div><div class="evidence"><p>STRATEGY / INTERCHANGEABLE SHIPPING POLICY</p><img src="${diagram}" alt="Checkout calls ShippingRule, supplied by standard or express lambdas"></div><footer>${foot}<small>${tall?'23 Design Patterns · ':''}English / Egyptian Arabic / 简体中文 / Italiano</small></footer></main></html>`;
}
(async()=>{
  fs.mkdirSync(out,{recursive:true});
  const browser=await chromium.launch({headless:true});
  const page=await browser.newPage({deviceScaleFactor:1});
  try {
    if (process.argv.includes('--inspect-sources')) {
      await page.setViewportSize({width:960,height:310});
      await page.setContent(`<body style="background:#e7c99f;padding:20px"><img src="${logo}" width="112" height="76"><img src="${diagram}" width="900"></body>`);
      await page.screenshot({path:path.join(__dirname,'source-assets.png')});
      return;
    }
    const formats=[['github-social-preview',1280,640],['social-preview-landscape',1200,630],['social-preview-square',1080,1080],['social-preview-portrait',1080,1350],...slides.map((s,i)=>[`carousel-0${i+1}`,1080,1350,s])];
    const manifest=[];
    for (const [name,w,h,slide] of formats) {
      const html=path.join(__dirname,name+'.html');
      fs.writeFileSync(html,document(w,h,slide));
      await page.setViewportSize({width:w,height:h});
      await page.goto(pathToFileURL(html).href);
      await page.evaluate(()=>document.fonts.ready);
      const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth||document.documentElement.scrollHeight>innerHeight);
      if(overflow) throw new Error('Overflow: '+name);
      const file=path.join(out,name+'.png');
      await page.screenshot({path:file});
      const bytes=fs.statSync(file).size;
      if(name==='github-social-preview'&&bytes>=1000000) throw new Error('GitHub preview exceeds 1 MB');
      manifest.push({file:name+'.png',width:w,height:h,bytes});
    }
    // Render the repository's existing editable preview with its updated name.
    await page.setViewportSize({width:1280,height:640});
    await page.goto(pathToFileURL(path.join(root,'assets/social-preview.svg')).href);
    await page.screenshot({path:path.join(root,'assets/social-preview.png')});
    fs.writeFileSync(path.join(__dirname,'image-validation.json'),JSON.stringify(manifest,null,2)+'\n');
    console.log(JSON.stringify(manifest,null,2));
  } finally { await browser.close(); }
})().catch(e=>{console.error(e);process.exitCode=1});
