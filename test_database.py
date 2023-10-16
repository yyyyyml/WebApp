from database import UserDatabase, SearchResultsDatabase, LiteratureDatabase

# 创建数据库对象
# 会在当前路径生成三个.sqlite文件
user_db = UserDatabase('sqlite/users.sqlite')
search_db = SearchResultsDatabase('sqlite/search_results.sqlite')
literature_db = LiteratureDatabase('sqlite/literature.sqlite')

# 添加用户
user_db.add_user('john_doe', 'password123', 'user', '[]', '[]')

# 获取用户
user = user_db.get_user('john_doe')
print(user)  # 输出：('john_doe', 'password123', 'user', '[]', '[]')

# 更新用户信息
user_db.update_user('john_doe', 'new_password', 'admin', '["search1", "search2"]', '["url1", "url2"]')

# 获取更新后的用户信息
updated_user = user_db.get_user('john_doe')
print(updated_user)  # 输出：('john_doe', 'new_password', 'admin', '["search1", "search2"]', '["url1", "url2"]')

# 删除用户
user_db.delete_user('john_doe')

# 尝试获取已删除的用户
deleted_user = user_db.get_user('john_doe')
print(deleted_user)  # 输出：None，因为用户已被删除

# 添加搜索结果
search_db.add_result('https://example.com/result1', 10)

# 获取搜索结果
result = search_db.get_result('https://example.com/result1')
print(result)  # 输出：('https://example.com/result1', 10)

# 更新搜索结果的点赞数
search_db.update_result('https://example.com/result1', 15)

# 获取更新后的搜索结果
updated_result = search_db.get_result('https://example.com/result1')
print(updated_result)  # 输出：('https://example.com/result1', 15)

# 删除搜索结果
search_db.delete_result('https://example.com/result1')

# 尝试获取已删除的搜索结果
deleted_result = search_db.get_result('https://example.com/result1')
print(deleted_result)  # 输出：None，因为搜索结果已被删除

# 添加文献
literature_db.add_literature('https://example.com/paper1', '/path/to/paper1.pdf')

# 获取文献
paper = literature_db.get_literature('https://example.com/paper1')
print(paper)  # 输出：('https://example.com/paper1', '/path/to/paper1.pdf')

# 更新文献的文件路径
literature_db.update_literature('https://example.com/paper1', '/new_path/to/paper1.pdf')

# 获取更新后的文献信息
updated_paper = literature_db.get_literature('https://example.com/paper1')
print(updated_paper)  # 输出：('https://example.com/paper1', '/new_path/to/paper1.pdf')

# 删除文献
literature_db.delete_literature('https://example.com/paper1')

# 尝试获取已删除的文献
deleted_paper = literature_db.get_literature('https://example.com/paper1')
print(deleted_paper)  # 输出：None，因为文献已被删除
