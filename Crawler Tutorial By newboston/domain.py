from urllib.parse import urlparse

# 도메인 가져오기
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results [-1]
    except:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

print(get_domain_name('https://gomyo.tistory.com/5'))