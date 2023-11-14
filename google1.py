from pprint import pprint
import requests
from bs4 import BeautifulSoup


def google_scholar_search(query, pn=1):
    # 设置搜索URL
    base_url = "https://scholar.google.com/scholar"
    params = {
        "as_vis": 1,
        "as_sdt": "0,5",
        "start": (pn - 1) * 10,  # 10表示第二页，每页通常有10个结果
        "q": query,
    }

    # 发送HTTP GET请求
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # 解析搜索结果页面
        soup = BeautifulSoup(response.text, "html.parser")

        # 查找结果条目
        results = soup.find_all("div", class_="gs_ri")
        results_pdf = soup.find_all("div", class_="gs_or_ggsm")
        # print(results_pdf)

        # 存储结果信息的列表
        search_results = []
        index = 0

        for result in results:
            title = result.find("h3", class_="gs_rt").get_text()
            link = result.find("h3", class_="gs_rt").find("a")["href"]
            snippet = result.find("div", class_="gs_rs").get_text()

            # 从同一个结果页面中提取更多信息
            authors = result.find("div", class_="gs_a").get_text()
            citations = result.find("div", class_="gs_flb").find("a", class_=False).get_text()
            pdf_link = None

            if index < len(results_pdf):
                result_pdf = results_pdf[index]
                pdf_id = result_pdf.find("a")["data-clk-atid"]

            result_id = result.find("h3", class_="gs_rt").find("a")["data-clk-atid"]
            # print(result_id)
            # print(pdf_id)
            if pdf_id == result_id:
                pdf_link = result_pdf.find("a")["href"]
                index += 1

            result_info = {
                "title": title,
                "link": link,
                "snippet": snippet,
                "authors": authors,
                "citations": citations,
                "pdf_link": pdf_link
            }
            # pprint(result_info)
            # print(index)

            search_results.append(result_info)

        return search_results
    else:
        print("Error fetching search results.")
        return []
    
if __name__ == "__main__":
    query = "Deep Learning"
    page = 1
    results = google_scholar_search(query, page)

    for i, result in enumerate(results):
        print(f"Result {i+1}:")
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Snippet: {result['snippet']}")
        print(f"Authors: {result['authors']}")
        print(f"Citations: {result['citations']}")
        print(f"PDF Link: {result['pdf_link']}")
        print("\n")
