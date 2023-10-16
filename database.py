import sqlite3

class UserDatabase:
    def __init__(self, db_file):
        # 连接到数据库文件
        self.conn = sqlite3.connect(db_file)
        # 创建游标
        self.cursor = self.conn.cursor()
        # 创建用户表，如果不存在的话
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            permission TEXT,
            history TEXT,
            favorites TEXT
        )''')
        # 提交更改
        self.conn.commit()

    def add_user(self, username, password, permission, history, favorites):
        # 插入新用户记录
        self.cursor.execute("INSERT INTO users (username, password, permission, history, favorites) VALUES (?, ?, ?, ?, ?)",
                            (username, password, permission, history, favorites))
        # 提交更改
        self.conn.commit()
    
    def update_user(self, username, password, permission, history, favorites):
        # 更新用户信息
        self.cursor.execute("UPDATE users SET password=?, permission=?, history=?, favorites=? WHERE username=?", (password, permission, history, favorites, username))
        # 提交更改
        self.conn.commit()

    def delete_user(self, username):
        # 删除用户记录
        self.cursor.execute("DELETE FROM users WHERE username=?", (username,))
        # 提交更改
        self.conn.commit()
    
    def get_user(self, username):
        # 获取用户信息
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        # 返回一条记录
        return self.cursor.fetchone()

class SearchResultsDatabase:
    def __init__(self, db_file):
        # 连接到数据库文件
        self.conn = sqlite3.connect(db_file)
        # 创建游标
        self.cursor = self.conn.cursor()
        # 创建搜索结果表，如果不存在的话
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS search_results (
            url TEXT PRIMARY KEY,
            likes INTEGER
        )''')
        # 提交更改
        self.conn.commit()

    def add_result(self, url, likes):
        # 插入新搜索结果
        self.cursor.execute("INSERT INTO search_results (url, likes) VALUES (?, ?)", (url, likes))
        # 提交更改
        self.conn.commit()

    def update_result(self, url, likes):
        # 更新搜索结果的点赞数
        self.cursor.execute("UPDATE search_results SET likes=? WHERE url=?", (likes, url))
        # 提交更改
        self.conn.commit()

    def delete_result(self, url):
        # 删除搜索结果记录
        self.cursor.execute("DELETE FROM search_results WHERE url=?", (url,))
        # 提交更改
        self.conn.commit()
        
    def get_result(self, url):
        # 获取搜索结果信息
        self.cursor.execute("SELECT * FROM search_results WHERE url=?", (url,))
        # 返回一条记录
        return self.cursor.fetchone()

class LiteratureDatabase:
    def __init__(self, db_file):
        # 连接到数据库文件
        self.conn = sqlite3.connect(db_file)
        # 创建游标
        self.cursor = self.conn.cursor()
        # 创建文献表，如果不存在的话
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS literature (
            url TEXT PRIMARY KEY,
            path TEXT
        )''')
        # 提交更改
        self.conn.commit()

    def add_literature(self, url, path):
        # 插入新文献记录
        self.cursor.execute("INSERT INTO literature (url, path) VALUES (?, ?)", (url, path))
        # 提交更改
        self.conn.commit()

    def update_literature(self, url, path):
        # 更新文献的文件路径
        self.cursor.execute("UPDATE literature SET path=? WHERE url=?", (path, url))
        # 提交更改
        self.conn.commit()

    def delete_literature(self, url):
        # 删除文献记录
        self.cursor.execute("DELETE FROM literature WHERE url=?", (url,))
        # 提交更改
        self.conn.commit()
        
    def get_literature(self, url):
        # 获取文献信息
        self.cursor.execute("SELECT * FROM literature WHERE url=?", (url,))
        # 返回一条记录
        return self.cursor.fetchone()
