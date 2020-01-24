import requests
from lxml import html
import re

link_nkrya = 'http://search1.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&' + \
             'mydocsize=&dpp=&spp=&spd=&text=lexform&mode=main&sort=gr_tagging&lang=ru&nodia=1&req='

leeds_settings = '&c=RUWAC-PARSED&searchtype=conc&contextsize=60c&sort1=word&sort2=right&' \
                 'terminate=100&llstat=on&cleft=0&cright=1&cfilter=&da=word'

leeds_base_url = 'http://corpus.leeds.ac.uk/cgi-bin/cqp.pl?q='


def get_nkrya(word: str):
    url = link_nkrya + str(word)
    raw_page = html.document_fromstring((requests.get(url, allow_redirects=False)).content)
    try:
        context = str(raw_page.cssselect("ul li")[1].text_content())
    except IndexError:
        return ''
    return context


def get_leeds(word: str):
    pattern = re.compile('([^\s^,^.\w]|_)+')
    if '/' in word:
        word = word[0:word.index('/')]
    link_leeds = leeds_base_url + word.lower() + leeds_settings
    raw_page = html.document_fromstring((requests.get(link_leeds, allow_redirects=False)).content)
    try:
        context = raw_page.cssselect('tbody tr')[1].text_content()
    except IndexError:
        return ''
    context = context.replace('\n', '')
    context_out = pattern.sub('', context)
    context_out = str(' '.join(context_out.split()))
    return context_out








