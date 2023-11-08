from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 创建一个UserAgent对象，用于生成随机User-Agent头部
ua = UserAgent()

def baidu_search(query, pn):
    # print(query)
    # print(pn)
    search_results = []

    base_url = "https://www.baidu.com/s"

    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate, compress',
        # 'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive',
        # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        'User-Agent': ua.random,  # 随机User-Agent头部
    }
    
    params = {
        "wd": query,          # 搜索关键词
        "pn": (pn - 1) * 10  # 10表示第二页，每页通常有10个结果
    }

    # 发送HTTP GET请求  
    response = requests.get(base_url, params=params, headers=headers)

    # 使用BeautifulSoup解析页面
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

    # 提取相关搜索词
    related_results = soup.find_all('a', class_='rs-link_2DE3Q')
    related_words = [related.get('title') for related in related_results]

    first_dict = {'results': related_words, 'type': 'related'}
    search_results.append(first_dict)

    result_divs = soup.find_all('div', class_='c-container')
    visited_urls = set()  # 用于存储已经访问过的URL

    for result in result_divs:
        result_dict = {}
        if result.h3:
            title_elem = result.h3.a
            if title_elem:
                title = title_elem.get_text()  # 提取标题
                url = title_elem['href']  # 提取URL
                if url in visited_urls:
                    continue  # 如果URL已经存在于集合中，跳过该结果
                
                visited_urls.add(url)  # 将URL添加到已访问集合
                result_dict['title'] = title
                result_dict['url'] = url
            else:
                continue
        else:
            continue
            
        description_elem = result.find('span', class_='content-right_8Zs40')
        if description_elem:
            description = description_elem.get_text()  # 提取描述
            result_dict['des'] = description
        else:
            continue
            
        source_elem = result.find('span', class_='c-color-gray')
        if source_elem:
            source = source_elem.get_text()  # 提取来源
            result_dict['origin'] = source
        else:
            result_dict['origin'] = None
            
        time_elem = result.find('span', class_='c-color-gray2')
        if time_elem:
            time = time_elem.get_text()  # 提取时间
            result_dict['time'] = time
        else:
            result_dict['time'] = None
            
        result_dict['type'] = 'result'  # 可根据需要设置不同的类型
        search_results.append(result_dict)

    # pprint(search_results)
    return search_results


if __name__ == '__main__':
    search_results = baidu_search("算法", 2)
    pprint(search_results)