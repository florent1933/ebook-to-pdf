from scrapy.http import Request
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

def normalizeUrl(url, response):
    base_url = get_base_url(response)
    if not url.startswith('http'):
        url = urljoin_rfc(base_url, url)
        url = unicode(url, 'utf-8')
    return url

def add_content(item, content):
    """
    Add the content to the item['content']
    """
    if item['content']:
        item['content'][0] = item['content'][0] + content # Make them unique
    else:
        item['content'] = content