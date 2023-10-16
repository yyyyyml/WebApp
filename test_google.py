from google import google_scholar_search

# 示例用法
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