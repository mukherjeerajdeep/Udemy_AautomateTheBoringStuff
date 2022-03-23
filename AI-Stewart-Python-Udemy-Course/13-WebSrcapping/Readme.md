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
![Soup Syntax ](C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\13-WebSrcapping\Soup_Syntax.PNG)

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
<span class="toctext">1975–1990</span>
<span class="toctext">1990–2000</span>
<span class="toctext">2000–2018</span>
<span class="toctext">Personal life</span>
<span class="toctext">Marriages</span>
<span class="toctext">Disability</span>
<span class="toctext">Disability outreach</span>
<span class="toctext">Plans for a trip to space</span>
<span class="toctext">Death</span>
<span class="toctext">Personal views</span>
<span class="toctext">Future of humanity</span>
<span class="toctext">Religion and atheism</span>
<span class="toctext">Politics</span>
<span class="toctext">Appearances in popular media</span>
<span class="toctext">Awards and honours</span>
<span class="toctext">Medal for Science Communication</span>
<span class="toctext">Publications</span>
<span class="toctext">Popular books</span>
<span class="toctext">Co-authored</span>
<span class="toctext">Forewords</span>
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
Career
1966–1975
1975–1990
1990–2000
2000–2018
Personal life
Marriages
Disability
Disability outreach
Plans for a trip to space
Death
Personal views
Future of humanity
Religion and atheism
Politics
Appearances in popular media
Awards and honours
Medal for Science Communication
Publications
Popular books
Co-authored
Forewords
Children's fiction
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
<meta content="origin" name="referrer"/>
<meta content="origin-when-crossorigin" name="referrer"/>
<meta content="origin-when-cross-origin" name="referrer"/>
<meta content="noindex,nofollow" name="robots"/>
<meta content="telephone=no" name="format-detection"/>
<meta content="Deep Blue (chess computer - Wikipedia" property="og:title"/>
<meta content="website" property="og:type"/>
<link href="//upload.wikimedia.org" rel="preconnect"/>
<link href="//en.m.wikipedia.org/wiki/Deep_Blue_(chess_computer" media="only screen and (max-width: 720px)" rel="alternate"/>
<link href="/static/apple-touch/wikipedia.png" rel="apple-touch-icon"/>
<link href="/static/favicon/wikipedia.ico" rel="shortcut icon"/>
<link href="/w/opensearch_desc.php" rel="search" title="Wikipedia (en)" type="application/opensearchdescription+xml"/>
<link href="//en.wikipedia.org/w/api.php?action=rsd" rel="EditURI" type="application/rsd+xml"/>
<link href="https://creativecommons.org/licenses/by-sa/3.0/" rel="license"/>
<link href="https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer" rel="canonical"/>
<link href="//meta.wikimedia.org" rel="dns-prefetch"/>
<link href="//login.wikimedia.org" rel="dns-prefetch"/>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-Deep_Blue_chess_computer rootpage-Deep_Blue_chess_computer skin-vector action-view skin-vector-legacy"><div class="noprint" id="mw-page-base"></div>
<div class="noprint" id="mw-head-base"></div>
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<div id="siteNotice"><!-- CentralNotice --></div>
<div class="mw-indicators">
</div>
<h1 class="firstHeading mw-first-heading" id="firstHeading">Deep Blue (chess computer</h1>
<div class="vector-body" id="bodyContent">
<div class="noprint" id="siteSub">From Wikipedia, the free encyclopedia</div>
<div id="contentSub"></div>
<div id="contentSub2"></div>
<div id="jump-to-nav"></div>
<a class="mw-jump-link" href="#mw-head">Jump to navigation</a>
<a class="mw-jump-link" href="#searchInput">Jump to search</a>
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="noarticletext mw-content-ltr" dir="ltr" lang="en">
<div class="pagetitlecorrection"><table class="plainlinks fmbox fmbox-editnotice" id="newarticletext" role="presentation"><tbody><tr><td class="mbox-image"><img alt="" data-file-height="48" data-file-width="48" decoding="async" height="40" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/40px-Dialog-information_on.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/60px-Dialog-information_on.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Dialog-information_on.svg/80px-Dialog-information_on.svg.png 2x" width="40"/></td><td class="mbox-text" style="font-weight:bold">Did you mean: <a href="/wiki/Deep_Blue_(chess_computer)" title="Deep Blue (chess computer)">Deep Blue (chess computer)</a>?</td></tr></tbody></table></div> <table class="plainlinks fmbox fmbox-system" id="noarticletext" role="presentation"><tbody><tr><td class="mbox-text" style="padding: 0.6em 0.9em;"><div class="infobox" id="sisterproject" style="width: 20em; font-size: 90%; float: right; padding: 0.5em;">Look for <b>Deep Blue (chess computer</b> on one of Wikipedia's <a href="/wiki/Special:SiteMatrix" title="Special:SiteMatrix">sister projects</a>:
<table cellpadding="1" cellspacing="0" style="background: none; margin: auto;">
<tbody><tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wiktionary-logo-v2.svg"><img alt="Wiktionary-logo-v2.svg" data-file-height="391" data-file-width="391" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/30px-Wiktionary-logo-v2.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/45px-Wiktionary-logo-v2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/0/06/Wiktionary-logo-v2.svg/60px-Wiktionary-logo-v2.svg.png 2x" width="30"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://en.wiktionary.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wiktionary:Special:Search/Deep Blue (chess computer">Wiktionary</a> (dictionary)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wikibooks-logo.svg"><img alt="Wikibooks-logo.svg" data-file-height="300" data-file-width="300" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/30px-Wikibooks-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/45px-Wikibooks-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/60px-Wikibooks-logo.svg.png 2x" width="30"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://en.wikibooks.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wikibooks:Special:Search/Deep Blue (chess computer">Wikibooks</a> (textbooks)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wikiquote-logo.svg"><img alt="Wikiquote-logo.svg" data-file-height="355" data-file-width="300" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/25px-Wikiquote-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/38px-Wikiquote-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/51px-Wikiquote-logo.svg.png 2x" width="25"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://en.wikiquote.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wikiquote:Special:Search/Deep Blue (chess computer">Wikiquote</a> (quotations)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wikisource-logo.svg"><img alt="Wikisource-logo.svg" data-file-height="430" data-file-width="410" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/29px-Wikisource-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/43px-Wikisource-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/57px-Wikisource-logo.svg.png 2x" width="29"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://en.wikisource.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wikisource:Special:Search/Deep Blue (chess computer">Wikisource</a> (library)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wikiversity_logo_2017.svg"><img alt="Wikiversity logo 2017.svg" data-file-height="512" data-file-width="626" decoding="async" height="25" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/30px-Wikiversity_logo_2017.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/45px-Wikiversity_logo_2017.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/60px-Wikiversity_logo_2017.svg.png 2x" width="30"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://en.wikiversity.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wikiversity:Special:Search/Deep Blue (chess computer">Wikiversity</a> (learning resources)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Commons-logo.svg"><img alt="Commons-logo.svg" data-file-height="1376" data-file-width="1024" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/22px-Commons-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/33px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/45px-Commons-logo.svg.png 2x" width="22"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://commons.wikimedia.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="commons:Special:Search/Deep Blue (chess computer">Commons</a> (media)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wikivoyage-Logo-v3-icon.svg"><img alt="Wikivoyage-Logo-v3-icon.svg" data-file-height="193" data-file-width="193" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Wikivoyage-Logo-v3-icon.svg/30px-Wikivoyage-Logo-v3-icon.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Wikivoyage-Logo-v3-icon.svg/45px-Wikivoyage-Logo-v3-icon.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Wikivoyage-Logo-v3-icon.svg/60px-Wikivoyage-Logo-v3-icon.svg.png 2x" width="30"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://en.wikivoyage.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wikivoyage:Special:Search/Deep Blue (chess computer">Wikivoyage</a> (travel guide)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wikinews-logo.svg"><img alt="Wikinews-logo.svg" data-file-height="415" data-file-width="759" decoding="async" height="16" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/30px-Wikinews-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/45px-Wikinews-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/60px-Wikinews-logo.svg.png 2x" width="30"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://en.wikinews.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wikinews:Special:Search/Deep Blue (chess computer">Wikinews</a> (news source)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wikidata-logo.svg"><img alt="Wikidata-logo.svg" data-file-height="590" data-file-width="1050" decoding="async" height="17" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/30px-Wikidata-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/45px-Wikidata-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/60px-Wikidata-logo.svg.png 2x" width="30"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://www.wikidata.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wikidata:Special:Search/Deep Blue (chess computer">Wikidata</a> (linked database)</td>
</tr>
<tr style="height: 30px;">
<td style="text-align: center; vertical-align: middle;"><a class="image" href="/wiki/File:Wikispecies-logo.svg"><img alt="Wikispecies-logo.svg" data-file-height="1103" data-file-width="941" decoding="async" height="30" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/26px-Wikispecies-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/38px-Wikispecies-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/51px-Wikispecies-logo.svg.png 2x" width="26"/></a></td>
<td style="vertical-align: middle;"><a class="extiw" href="https://species.wikimedia.org/wiki/Special:Search/Deep_Blue_(chess_computer" title="wikispecies:Special:Search/Deep Blue (chess computer">Wikispecies</a> (species directory)</td>
</tr>
</tbody></table></div><b>Wikipedia does not have an article with this exact name.</b> Please <span class="plainlinks"><a class="external text" href="https://en.wikipedia.org/w/index.php?search=Deep+Blue+%28chess+computer&amp;title=Special%3ASearch&amp;fulltext=1">search for <i>Deep Blue (chess computer</i> in Wikipedia</a></span> to check for alternative titles or spellings.
<ul><li>You need to <a class="external text" href="https://en.wikipedia.org/w/index.php?title=Special:UserLogin&amp;returnto=Deep+Blue+%28chess+computer">log in or create an account</a> to create this page.</li>
<li><span class="plainlinks"><a class="external text" href="https://en.wikipedia.org/w/index.php?search=Deep+Blue+%28chess+computer&amp;title=Special%3ASearch&amp;fulltext=1&amp;ns0=1">Search for "<i>Deep Blue (chess computer</i>"</a></span> in existing articles.</li>
<li><a href="/wiki/Special:WhatLinksHere/Deep_Blue_(chess_computer" title="Special:WhatLinksHere/Deep Blue (chess computer">Look for pages within Wikipedia that link to this title</a>.</li></ul>
<div id="noarticletext_technical">
<hr/>
<p><b>Other reasons this message may be displayed:</b>
</p>
<ul><li>If a page was recently created here, it may not be visible yet because of a delay in updating the database; wait a few minutes or <a href="/wiki/Special:Purge/Deep_Blue_(chess_computer" title="Special:Purge/Deep Blue (chess computer">try the purge function</a>.</li>
<li>Titles on Wikipedia are <b><a href="/wiki/Case_sensitivity" title="Case sensitivity">case sensitive</a></b> except for the first character; please <span class="plainlinks"><a class="external text" href="https://en.wikipedia.org/w/index.php?search=Deep+Blue+%28chess+computer&amp;title=Special%3ASearch&amp;fulltext=1">check alternative capitalizations</a></span> and consider adding a <a href="/wiki/Wikipedia:Redirect" title="Wikipedia:Redirect">redirect</a> here to the correct title.</li>
<li>If the page has been deleted, <a class="external text" href="https://en.wikipedia.org/w/index.php?title=Special:Log/delete&amp;page=Deep_Blue_(chess_computer">check the <b>deletion log</b></a>, and see <a href="/wiki/Wikipedia:Why_was_the_page_I_created_deleted%3F" title="Wikipedia:Why was the page I created deleted?">Why was the page I created deleted?</a>.</li></ul>
</div></td></tr></tbody></table>
</div><noscript><img alt="" height="1" src="//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" style="border: none; position: absolute;" title="" width="1"/></noscript>
<div class="printfooter">Retrieved from "<a dir="ltr" href="https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer">https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer</a>"</div></div>
<div class="catlinks catlinks-allhidden" data-mw="interface" id="catlinks"></div>
</div>
</div>
<div id="mw-data-after-content">
<div class="read-more-container"></div>
</div>
<div id="mw-navigation">
<h2>Navigation menu</h2>
<div id="mw-head">
<nav aria-labelledby="p-personal-label" class="mw-portlet mw-portlet-personal vector-user-menu-legacy vector-menu" id="p-personal" role="navigation">
<label aria-label="" class="vector-menu-heading" id="p-personal-label">
<span class="vector-menu-heading-label">Personal tools</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"><li class="mw-list-item" id="pt-anonuserpage"><span>Not logged in</span></li><li class="mw-list-item" id="pt-anontalk"><a accesskey="n" href="/wiki/Special:MyTalk" title="Discussion about edits from this IP address [n]"><span>Talk</span></a></li><li class="mw-list-item" id="pt-anoncontribs"><a accesskey="y" href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]"><span>Contributions</span></a></li><li class="mw-list-item" id="pt-createaccount"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=Deep+Blue+%28chess+computer" title="You are encouraged to create an account and log in; however, it is not mandatory"><span>Create account</span></a></li><li class="mw-list-item" id="pt-login"><a accesskey="o" href="/w/index.php?title=Special:UserLogin&amp;returnto=Deep+Blue+%28chess+computer" title="You're encouraged to log in; however, it's not mandatory. [o]"><span>Log in</span></a></li></ul>
</div>
</nav>
<div id="left-navigation">
<nav aria-labelledby="p-namespaces-label" class="mw-portlet mw-portlet-namespaces vector-menu vector-menu-tabs" id="p-namespaces" role="navigation">
<label aria-label="" class="vector-menu-heading" id="p-namespaces-label">
<span class="vector-menu-heading-label">Namespaces</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"><li class="selected mw-list-item" id="ca-nstab-main"><a accesskey="c" href="/w/index.php?title=Deep_Blue_(chess_computer&amp;action=edit&amp;redlink=1" title="View the content page (page does not exist) [c]"><span>Article</span></a></li><li class="new mw-list-item" id="ca-talk"><a accesskey="t" href="/w/index.php?title=Talk:Deep_Blue_(chess_computer&amp;action=edit&amp;redlink=1" rel="discussion" title="Discuss improvements to the content page (page does not exist) [t]"><span>Talk</span></a></li></ul>
</div>
</nav>
<nav aria-labelledby="p-variants-label" class="mw-portlet mw-portlet-variants emptyPortlet vector-menu-dropdown-noicon vector-menu vector-menu-dropdown" id="p-variants" role="navigation">
<input aria-haspopup="true" aria-labelledby="p-variants-label" class="vector-menu-checkbox" data-event-name="ui.dropdown-p-variants" id="p-variants-checkbox" role="button" type="checkbox"/>
<label aria-label="Change language variant" class="vector-menu-heading" id="p-variants-label">
<span class="vector-menu-heading-label">English</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"></ul>
</div>
</nav>
</div>
<div id="right-navigation">
<nav aria-labelledby="p-views-label" class="mw-portlet mw-portlet-views emptyPortlet vector-menu vector-menu-tabs" id="p-views" role="navigation">
<label aria-label="" class="vector-menu-heading" id="p-views-label">
<span class="vector-menu-heading-label">Views</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"></ul>
</div>
</nav>
<nav aria-labelledby="p-cactions-label" class="mw-portlet mw-portlet-cactions emptyPortlet vector-menu-dropdown-noicon vector-menu vector-menu-dropdown" id="p-cactions" role="navigation" title="More options">
<input aria-haspopup="true" aria-labelledby="p-cactions-label" class="vector-menu-checkbox" data-event-name="ui.dropdown-p-cactions" id="p-cactions-checkbox" role="button" type="checkbox"/>
<label aria-label="" class="vector-menu-heading" id="p-cactions-label">
<span class="vector-menu-heading-label">More</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"></ul>
</div>
</nav>
<div class="vector-search-box-vue vector-search-box-show-thumbnail vector-search-box-auto-expand-width vector-search-box" id="p-search" role="search">
<div>
<h3>
<label for="searchInput">Search</label>
</h3>
<form action="/w/index.php" class="vector-search-box-form" id="searchform">
<div class="vector-search-box-inner" data-search-loc="header-navigation" id="simpleSearch">
<input accesskey="f" aria-label="Search Wikipedia" autocapitalize="sentences" class="vector-search-box-input" id="searchInput" name="search" placeholder="Search Wikipedia" title="Search Wikipedia [f]" type="search"/>
<input name="title" type="hidden" value="Special:Search"/>
<input class="searchButton mw-fallbackSearchButton" id="mw-searchButton" name="fulltext" title="Search Wikipedia for this text" type="submit" value="Search"/>
<input class="searchButton" id="searchButton" name="go" title="Go to a page with this exact name if it exists" type="submit" value="Go"/>
</div>
</form>
</div>
</div>
</div>
</div>
<div id="mw-panel">
<div id="p-logo" role="banner">
<a class="mw-wiki-logo" href="/wiki/Main_Page" title="Visit the main page"></a>
</div>
<nav aria-labelledby="p-navigation-label" class="mw-portlet mw-portlet-navigation vector-menu vector-menu-portal portal" id="p-navigation" role="navigation">
<label aria-label="" class="vector-menu-heading" id="p-navigation-label">
<span class="vector-menu-heading-label">Navigation</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"><li class="mw-list-item" id="n-mainpage-description"><a accesskey="z" href="/wiki/Main_Page" icon="home" title="Visit the main page [z]"><span>Main page</span></a></li><li class="mw-list-item" id="n-contents"><a href="/wiki/Wikipedia:Contents" title="Guides to browsing Wikipedia"><span>Contents</span></a></li><li class="mw-list-item" id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Articles related to current events"><span>Current events</span></a></li><li class="mw-list-item" id="n-randompage"><a accesskey="x" href="/wiki/Special:Random" icon="die" title="Visit a randomly selected article [x]"><span>Random article</span></a></li><li class="mw-list-item" id="n-aboutsite"><a href="/wiki/Wikipedia:About" title="Learn about Wikipedia and how it works"><span>About Wikipedia</span></a></li><li class="mw-list-item" id="n-contactpage"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us" title="How to contact Wikipedia"><span>Contact us</span></a></li><li class="mw-list-item" id="n-sitesupport"><a href="https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;uselang=en" title="Support us by donating to the Wikimedia Foundation"><span>Donate</span></a></li></ul>
</div>
</nav>
<nav aria-labelledby="p-interaction-label" class="mw-portlet mw-portlet-interaction vector-menu vector-menu-portal portal" id="p-interaction" role="navigation">
<label aria-label="" class="vector-menu-heading" id="p-interaction-label">
<span class="vector-menu-heading-label">Contribute</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"><li class="mw-list-item" id="n-help"><a href="/wiki/Help:Contents" icon="help" title="Guidance on how to use and edit Wikipedia"><span>Help</span></a></li><li class="mw-list-item" id="n-introduction"><a href="/wiki/Help:Introduction" title="Learn how to edit Wikipedia"><span>Learn to edit</span></a></li><li class="mw-list-item" id="n-portal"><a href="/wiki/Wikipedia:Community_portal" title="The hub for editors"><span>Community portal</span></a></li><li class="mw-list-item" id="n-recentchanges"><a accesskey="r" href="/wiki/Special:RecentChanges" icon="recentChanges" title="A list of recent changes to Wikipedia [r]"><span>Recent changes</span></a></li><li class="mw-list-item" id="n-upload"><a href="/wiki/Wikipedia:File_Upload_Wizard" title="Add images or other media for use on Wikipedia"><span>Upload file</span></a></li></ul>
</div>
</nav>
<nav aria-labelledby="p-tb-label" class="mw-portlet mw-portlet-tb vector-menu vector-menu-portal portal" id="p-tb" role="navigation">
<label aria-label="" class="vector-menu-heading" id="p-tb-label">
<span class="vector-menu-heading-label">Tools</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"><li class="mw-list-item" id="t-whatlinkshere"><a accesskey="j" href="/wiki/Special:WhatLinksHere/Deep_Blue_(chess_computer" title="List of all English Wikipedia pages containing links to this page [j]"><span>What links here</span></a></li><li class="mw-list-item" id="t-upload"><a accesskey="u" href="/wiki/Wikipedia:File_Upload_Wizard" title="Upload files [u]"><span>Upload file</span></a></li><li class="mw-list-item" id="t-specialpages"><a accesskey="q" href="/wiki/Special:SpecialPages" title="A list of all special pages [q]"><span>Special pages</span></a></li><li class="mw-list-item" id="t-print"><a accesskey="p" href="javascript:print();" rel="alternate" title="Printable version of this page [p]"><span>Printable version</span></a></li><li class="mw-list-item" id="t-info"><a href="/w/index.php?title=Deep_Blue_(chess_computer&amp;action=info" title="More information about this page"><span>Page information</span></a></li></ul>
</div>
</nav>
<nav aria-labelledby="p-lang-label" class="mw-portlet mw-portlet-lang vector-menu vector-menu-portal portal" id="p-lang" role="navigation">
<label aria-label="" class="vector-menu-heading" id="p-lang-label">
<span class="vector-menu-heading-label">Languages</span>
</label>
<div class="vector-menu-content">
<ul class="vector-menu-content-list"></ul>
<div class="after-portlet after-portlet-lang"><span class="uls-after-portlet-link"></span></div>
</div>
</nav>
</div>
</div>
<footer class="mw-footer" id="footer" role="contentinfo">
<ul id="footer-info">
</ul>
<ul id="footer-places">
<li id="footer-places-privacy"><a class="extiw" href="https://foundation.wikimedia.org/wiki/Privacy_policy" title="wmf:Privacy policy">Privacy policy</a></li>
<li id="footer-places-about"><a href="/wiki/Wikipedia:About" title="Wikipedia:About">About Wikipedia</a></li>
<li id="footer-places-disclaimer"><a href="/wiki/Wikipedia:General_disclaimer" title="Wikipedia:General disclaimer">Disclaimers</a></li>
<li id="footer-places-contact"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us">Contact Wikipedia</a></li>
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