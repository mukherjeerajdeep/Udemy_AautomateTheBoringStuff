WebScrapping

The `requests` module is a third-party module for downloading web pages and files.
requests.get() returns a Response object.
The raise_for_status() Response method will raise an exception if the download failed.
You can save a downloaded file to your hard drive with calls to the iter_content() method.

```python
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.status_code
200

res.text[:500]
'The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare\r\n\r\nThis eBook is for the use of anyone anywhere at no cost and with\r\nalmost no restrictions whatsoever.  You may copy it, give it away or\r\nre-use it under the terms of the Project Gutenberg License included\r\nwith this eBook or online at www.gutenberg.org/license\r\n\r\n\r\nTitle: Romeo and Juliet\r\n\r\nAuthor: William Shakespeare\r\n\r\nPosting Date: May 25, 2012 [EBook #1112]\r\nRelease Date: November, 1997  [Etext #1112]\r\n\r\nLanguage: Eng'

res = requests.get('https://automatetheboringstuff.com/files/rj.txt/dhahdah')

# Check for any error occured or nor
res.raise_for_status()

playFile = open('RomeoJuliet.txt', 'wb')  # In binary form

for chunk in res.iter_content(10000):  # iter_contents returns bytes
    playFile.write(chunk)

315
playFile.close()

import os

os.getcwd()
'C:\\Python'

os.chdir('/AI-Stewart-Python-Udemy-Course/13-WebSrcapping')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
playFile = open('RomeoJuliet.txt', 'wb')

for chunk in res.iter_content(10000):
    playFile.write(chunk)

10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
8978

playFile.close()
```

**Use of `requests` and `bs4` with `lxml` module** 

```python
import bs4
import lxml

result = requests.get("http://www.example.com/")
result
<Response [200]>

print(result)
<Response [200]>
print(result.text)
```
```html
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```

With the use of Beautiful Soup

```python
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
```

```html
<!DOCTYPE html>
<html>
<head>
<title>Example Domain</title>
<meta charset="utf-8"/>
<meta content="text/html; charset=utf-8" http-equiv="Content-type"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```

Selecting a special element, passing a specific tag to `soup.select()` will help to grab the content of the part of the 
HTML file. 

```python
soup.select('title')
[<title>Example Domain</title>]

# it returns a list
soup.select('p')
[<p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>, <p><a href="https://www.iana.org/domains/example">More information...</a></p>]

# only the actual text to get
soup.select('title')[0].getText
<bound method PageElement.get_text of <title>Example Domain</title>>


soup.select('title')[0].getText()
'Example Domain'
```
Soup Syntax 
![Soup_Syntax](https://user-images.githubusercontent.com/43293317/159789501-228e3f41-dea9-442e-a679-045cf01eb397.PNG)

Soup Man-Page
[BS4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class)

Some Web Scrapping site :
[1](http://www.example.com/)
[2](https://toscrape.com/)
[3](https://toscrape.com/)
[4](https://quotes.toscrape.com)

```python
res = requests.get('https://en.wikipedia.org/wiki/Stephen_Hawking')

res.status_code
200

soup = bs4.BeautifulSoup(res.text, 'lxml')

first_item = soup.select('.toctext')[0] # get the first item from the list which contains the value from the class "toctext". It is written in the way of .toctext.

# print the item
first_item.text
'Early life'

# for all the item in the list
for item in soup.select('.toctext'):
    print(item)

    
<span class="toctext">Early life</span>
<span class="toctext">Family</span>
<span class="toctext">Primary and secondary school years</span>
<span class="toctext">Undergraduate years</span>
<span class="toctext">Postgraduate years</span>
<span class="toctext">Career</span>
<span class="toctext">1966–1975</span>
.....
<span class="toctext">Children's fiction</span>
<span class="toctext">Films and series</span>
<span class="toctext">Selected academic works</span>
<span class="toctext">References</span>
<span class="toctext">Notes</span>
<span class="toctext">Citations</span>
<span class="toctext">Sources</span>
<span class="toctext">External links</span>

# or more precisely
for item in soup.select('.toctext'):
    print(item.text)

    
Early life
Family
Primary and secondary school years
Undergraduate years
Postgraduate years
....
Films and series
Selected academic works
References
Notes
Citations
Sources
External links
```

Capturing the images

```python
res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer')
soup = bs4.BeautifulSoup(res.text, 'lxml')

soup
```
```html
<!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<meta charset="utf-8"/>
<title>Deep Blue (chess computer - Wikipedia</title>
<script>document.documentElement.className="client-js";RLCONF={"wgBreakFrames":false,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"3cf6fbfa-23b7-4a4e-92b9-07134ccd5e65","wgCSPNonce":false,"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Deep_Blue_(chess_computer","wgTitle":"Deep Blue (chess computer","wgCurRevisionId":0,"wgRevisionId":0,"wgArticleId":0,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":[],"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"Deep_Blue_(chess_computer","wgRelevantArticleId":0,"wgIsProbablyEditable":false,"wgRelevantPageIsProbablyEditable":false,"wgRestrictionCreate":[],"wgFlaggedRevsParams":{"tags":{"status":{"levels":-1}}},
"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgMFDisplayWikibaseDescriptions":{"search":true,"nearby":true,"watchlist":true,"tagline":false},"wgWMESchemaEditAttemptStepOversample":false,"wgWMEPageLength":0,"wgNoticeProject":"wikipedia","wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsFlags":10,"wgULSCurrentAutonym":"English","wgEditSubmitButtonLabelPublish":true,"wgCentralAuthMobileDomain":false,"wgULSPosition":"interlanguage","wgULSisCompactLinksEnabled":true,"wgGENewcomerTasksGuidanceEnabled":true,"wgGEAskQuestionEnabled":false,"wgGELinkRecommendationsFrontendEnabled":false};RLSTATE={"ext.globalCssJs.user.styles":"ready","site.styles":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading","skins.vector.styles.legacy":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.wikimediaBadges":"ready","ext.uls.interlanguage":"ready"};RLPAGEMODULES=["site"
,"mediawiki.page.ready","skins.vector.legacy.js","ext.gadget.ReferenceTooltips","ext.gadget.charinsert","ext.gadget.extra-toolbar-buttons","ext.gadget.refToolbar","ext.gadget.switcher","mmv.head","mmv.bootstrap.autostart","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.cx.eventlogging.campaigns","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.centralauth.centralautologin","ext.popups","ext.uls.compactlinks","ext.uls.interface","ext.growthExperiments.SuggestedEditSession"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.implement("user.options@1i9g4",function($,jQuery,require,module){mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});});});</script>
<link href="/w/load.php?lang=en&amp;modules=ext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cskins.vector.styles.legacy&amp;only=styles&amp;skin=vector" rel="stylesheet"/>
<script async="" src="/w/load.php?lang=en&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector"></script>
<meta content="" name="ResourceLoaderDynamicStyles"/>
<link href="/w/load.php?lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector" rel="stylesheet"/>
<meta content="MediaWiki 1.39.0-wmf.3" name="generator"/>
......
    <li id="footer-places-mobileview"><a class="noprint stopMobileRedirectToggle" href="//en.m.wikipedia.org/w/index.php?title=Deep_Blue_(chess_computer&amp;mobileaction=toggle_view_mobile">Mobile view</a></li>
<li id="footer-places-developers"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute">Developers</a></li>
<li id="footer-places-statslink"><a href="https://stats.wikimedia.org/#/en.wikipedia.org">Statistics</a></li>
<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Cookie_statement">Cookie statement</a></li>
</ul>
<ul class="noprint" id="footer-icons">
<li id="footer-copyrightico"><a href="https://wikimediafoundation.org/"><img alt="Wikimedia Foundation" height="31" loading="lazy" src="/static/images/footer/wikimedia-button.png" srcset="/static/images/footer/wikimedia-button-1.5x.png 1.5x, /static/images/footer/wikimedia-button-2x.png 2x" width="88"/></a></li>
<li id="footer-poweredbyico"><a href="https://www.mediawiki.org/"><img alt="Powered by MediaWiki" height="31" loading="lazy" src="/static/images/footer/poweredby_mediawiki_88x31.png" srcset="/static/images/footer/poweredby_mediawiki_132x47.png 1.5x, /static/images/footer/poweredby_mediawiki_176x62.png 2x" width="88"/></a></li>
</ul>
</footer>
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.191","walltime":"0.225","ppvisitednodes":{"value":398,"limit":1000000},"postexpandincludesize":{"value":26262,"limit":2097152},"templateargumentsize":{"value":588,"limit":2097152},"expansiondepth":{"value":14,"limit":100},"expensivefunctioncount":{"value":6,"limit":500},"unstrip-depth":{"value":0,"limit":20},"unstrip-size":{"value":0,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  180.422      1 -total","100.00%  180.422      1 Template:No_article_text"," 73.14%  131.965      2 Template:Fmbox"," 33.14%   59.786      1 Template:New_page_DYM"," 14.71%   26.542      1 Template:Did_you_mean/box"," 10.54%   19.019      1 Template:No_article_text/sister_projects","  4.31%    7.776      3 Template:Plain_link"]},"scribunto":{"limitreport-timeusage":{"value":"0.106","limit":"10.000"},"limitreport-memusage":{"value":1721516,"limit":52428800}},"cachereport":{"origin":"mw1319","timestamp":"20220323070904","ttl":1814400,"transientcontent":false}}});mw.config.set({"wgBackendResponseTime":341,"wgHostname":"mw1319"});});</script>
</body>
</html>
```

```python
soup.select('img')                                                                                                    
[<img alt="" data-file-height="48" data-file-width="48" decoding="async" height="40" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/40px-Dialog-information_on.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/60px-Dialog-information_on.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/80px-Dialog-information_on.svg.png 2x" width="40"/>, <img alt="Wiktionary-logo-v2.svg" data-file-height="391" data-file-width="391" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/30px-Wiktionary-logo-v2.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/45px-Wiktionary-logo-v2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/60px-Wiktionary-logo-v2.svg.png 2x" width="30"/>, <img alt="Wikibooks-logo.svg" data-file-height="300" data-file-width="300" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/30px-Wikibooks-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/45px-Wikibooks-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/60px-Wikibooks-logo.svg.png 2x" width="30"/>, <img alt="Wikiquote-logo.svg" data-file-height="355" data-file-width="300" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/25px-Wikiquote-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/38px-Wikiquote-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/51px-Wikiquote-logo.svg.png 2x" width="25"/>, <img alt="Wikisource-logo.svg" data-file-height="430" data-file-width="410" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/29px-Wikisource-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/43px-Wikisource-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/57px-Wikisource-logo.svg.png 2x" width="29"/>, <img alt="Wikiversity logo 2017.svg" data-file-height="512" data-file-width="626" decoding="async" height="25" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/30px-Wikiversity_logo_2017.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/45px-Wikiversity_logo_2017.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/60px-Wikiversity_logo_2017.svg.png 2x" width="30"/>, <img alt="Commons-logo.svg" data-file-height="1376" data-file-width="1024" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/22px-Commons-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/33px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/45px-Commons-logo.svg.png 2x" width="22"/>, <img alt="Wikivoyage-Logo-v3-icon.svg" data-file-height="193" data-file-width="193" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Wikivoyage-Logo-v3-icon.svg/30px-Wikivoyage-Logo-v3-icon.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Wikivoyage-Logo-v3-icon.svg/45px-Wikivoyage-Logo-v3-icon.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Wikivoyage-Logo-v3-icon.svg/60px-Wikivoyage-Logo-v3-icon.svg.png 2x" width="30"/>, <img alt="Wikinews-logo.svg" data-file-height="415" data-file-width="759" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/30px-Wikinews-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/45px-Wikinews-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/60px-Wikinews-logo.svg.png 2x" width="30"/>, <img alt="Wikidata-logo.svg" data-file-height="590" data-file-width="1050" decoding="async" height="17" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/30px-Wikidata-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/45px-Wikidata-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/60px-Wikidata-logo.svg.png 2x" width="30"/>, <img alt="Wikispecies-logo.svg" data-file-height="1103" data-file-width="941" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/26px-Wikispecies-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/38px-Wikispecies-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/51px-Wikispecies-logo.svg.png 2x" width="26"/>, <img alt="" height="1" src="//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" style="border: none; position: absolute;" title="" width="1"/>, <img alt="Wikimedia Foundation" height="31" loading="lazy" src="/static/images/footer/wikimedia-button.png" srcset="/static/images/footer/wikimedia-button-1.5x.png 1.5x, /static/images/footer/wikimedia-button-2x.png 2x" width="88"/>, <img alt="Powered by MediaWiki" height="31" loading="lazy" src="/static/images/footer/poweredby_mediawiki_88x31.png" srcset="/static/images/footer/poweredby_mediawiki_132x47.png 1.5x, /static/images/footer/poweredby_mediawiki_176x62.png 2x" width="88"/>]

soup.select('img')[0]                                                                                                     
<img alt="" data-file-height="48" data-file-width="48" decoding="async" height="40" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/40px-Dialog-information_on.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/60px-Dialog-information_on.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/80px-Dialog-information_on.svg.png 2x" width="40"/>
```

Let's try to find out a class
```python
soup.select('.image')[0]                                                                                                    
<a class="image" href="/wiki/File:Wiktionary-logo-v2.svg"><img alt="Wiktionary-logo-v2.svg" data-file-height="391" data-file-width="391" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/30px-Wiktionary-logo-v2.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/45px-Wiktionary-logo-v2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/60px-Wiktionary-logo-v2.svg.png 2x" width="30"/></a>
```                                                                                                     

Using the real site with Book Scrapping

```python
# using the https://books.toscrape.com/ and https://toscrape.com/
import requests
import bs4

# scrap per page https://books.toscrape.com/catalogue/page-2.html
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

base_url.format('20')
'https://books.toscrape.com/catalogue/page-20.html'

page_num = 12
base_url.format(page_num)
'https://books.toscrape.com/catalogue/page-12.html'

# grab the product_pod
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')

soup.select('.product_pod')

len(soup.select('.product_pod'))
20

products = soup.select('.product_pod')
example = products[0]

example
<article class="product_pod">
<div class="image_container">
<a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>
</div>
<p class="star-rating Three">
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
</p>
<h3><a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
<div class="product_price">
<p class="price_color">Â£51.77</p>
<p class="instock availability">
<i class="icon-ok"></i>
    
        In stock
    
</p>
<form>
<button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
</form>
</div>
</article>

# quick and dirty way
str(example)
'<article class="product_pod">\n<div class="image_container">\n<a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>\n</div>\n<p class="star-rating Three">\n<i class="icon-star"></i>\n<i class="icon-star"></i>\n<i class="icon-star"></i>\n<i class="icon-star"></i>\n<i class="icon-star"></i>\n</p>\n<h3><a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>\n<div class="product_price">\n<p class="price_color">Â£51.77</p>\n<p class="instock availability">\n<i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n<form>\n<button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>\n</form>\n</div>\n</article>'

'star-rating Two' in str(example)
False

'star-rating Three' in str(example)
True

example.select('.star-rating Three')
[]

example.select('.star-rating.Three')
[<p class="star-rating Three">
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
</p>]

example.select('.star-rating Three') is []
False

example.select('.star-rating Two') is []
False

example.select('.star-rating Three').count()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    example.select('.star-rating Three').count()
TypeError: ResultSet.count() takes exactly one argument (0 given)


example
<article class="product_pod">
<div class="image_container">
<a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>
</div>
<p class="star-rating Three">
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
<i class="icon-star"></i>
</p>
<h3><a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
<div class="product_price">
<p class="price_color">Â£51.77</p>
<p class="instock availability">
<i class="icon-ok"></i>
    
        In stock
    
</p>
<form>
<button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
</form>
</div>
</article>

example.select('a')
[<a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>, <a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>]

# take the index 1
example.select('a')[1]
<a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>

type(example.select('a')[1])
<class 'bs4.element.Tag'>

# same bs4 object so we can use the dictionary
example.select('a')[1]['title']
'A Light in the Attic'

two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

import pprint

OUTPUT
pprint.pprint(two_star_titles)
['Starving Hearts (Triangular Trade Trilogy, #1)',
 'Libertarianism for Beginners',
 "It's Only the Himalayas",
 'How Music Works',
 'Maude (1883-1993):She Grew Up with']
```

Exercise Solution for the Jose Portila
[Exercise ToScrape](https://quotes.toscrape.com/tag/love/)

```python
import requests
import bs4

base_url = 'https://quotes.toscrape.com/page/{}/'

base_url.format('1')
'https://quotes.toscrape.com/page/1/'

for _ in range(0,3):
    print(base_url.format(_))

    
https://quotes.toscrape.com/page/0/
https://quotes.toscrape.com/page/1/
https://quotes.toscrape.com/page/2/

res_home = requests.get(base_url.format('1'))

res_home
<Response [200]>

res_home.text



pprint.pprint(res_home.text)
OUTPUT
```
```html
('<!DOCTYPE html>\n'
 '<html lang="en">\n'
 '<head>\n'
 '\t<meta charset="UTF-8">\n'
 '\t<title>Quotes to Scrape</title>\n'
 '    <link rel="stylesheet" href="/static/bootstrap.min.css">\n'
 '    <link rel="stylesheet" href="/static/main.css">\n'
 '</head>\n'

```
Selecting the authors only in a set not list

```python
soup = bs4.BeautifulSoup(res_home.text, 'lxml')

soup.select('small')
[<small class="author" itemprop="author">Albert Einstein</small>, <small class="author" itemprop="author">J.K. Rowling</small>, <small class="author" itemprop="author">Albert Einstein</small>, <small class="author" itemprop="author">Jane Austen</small>, <small class="author" itemprop="author">Marilyn Monroe</small>, <small class="author" itemprop="author">Albert Einstein</small>, <small class="author" itemprop="author">André Gide</small>, <small class="author" itemprop="author">Thomas A. Edison</small>, <small class="author" itemprop="author">Eleanor Roosevelt</small>, <small class="author" itemprop="author">Steve Martin</small>]


soup.select('small')[0]
<small class="author" itemprop="author">Albert Einstein</small>

OPTION 1
authors = soup.find_all('small', class_ = 'author' )

authors[0].text
'Albert Einstein'

type(authors)
<class 'bs4.element.ResultSet'>

OPTION 2
soup.select('small')[0].text
'Albert Einstein'

for authors in soup.select('small'):
    print(authors.text)

    
Albert Einstein
J.K. Rowling
Albert Einstein
Jane Austen
Marilyn Monroe
Albert Einstein
André Gide
Thomas A. Edison
Eleanor Roosevelt
Steve Martin

FULL PROGRAM

auth_list = []
for authors in soup.select('small'):
    auth_list.append(authors.text)
    print(auth_list)

auth_list
['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin', 'Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']


set(auth_list)
{'Albert Einstein', 'Thomas A. Edison', 'Jane Austen', 'Marilyn Monroe', 'André Gide', 'J.K. Rowling', 'Steve Martin', 'Eleanor Roosevelt'}
 
```
Selecting the Text Only, which is a class and hence it is inside the method call `soup.select()` as "`.text`", check the syntax above.

```python
for quote in soup.select('.text'):
    print(quote.text)

    
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“It is our choices, Harry, that show what we truly are, far more than our abilities.”
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as thou
```
Top ten list for the favourite quotes 

```python
for topten in soup.select('.tag-item'):
    print(topten.text.strip())

    
love
inspirational
life
humor
books
reading
friendship
friends
truth
simile
```


**Selenium Module usage**

To import `selenium`, you need to run: "**from selenium import webdriver**" (and not "import selenium").
To open the browser, run: `browser = webdriver.Firefox()`
To send the browser to a URL, run: `browser.get(‘https://inventwithpython.com')`
The `browser.find_elements_by_css_selector()` method will return a list of WebElement objects: elems = browser.find_elements_by_css_selector(‘img')

WebElement objects have a "`text`" variable that contains the element's HTML.html in a string: elems[0].text
The `click()` method will click on an element in the browser.
The `send_keys()` method will type into a specific element in the browser.
The` submit()` method will simulate clicking on the Submit button for a form.
The browser can also be controlled with these methods: `back()`, `forward()`, `refresh()`, `quit()`.
