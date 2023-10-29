import sqlite3
import os

# 数据库文件路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_DB = os.path.join(BASE_DIR, 'databases/users.sqlite')
WEB_ITEMS_DB = os.path.join(BASE_DIR, 'databases/web_items.sqlite')
LITERATURE_ITEMS_DB = os.path.join(BASE_DIR, 'databases/literature_items.sqlite')
MESSAGES_DB = os.path.join(BASE_DIR, 'databases/messages.sqlite')
WEB_FAVORITES_DB = os.path.join(BASE_DIR, 'databases/web_favorites.sqlite')
WEB_BROWSES_DB = os.path.join(BASE_DIR, 'databases/web_browses.sqlite')
LITERATURE_FAVORITES_DB = os.path.join(BASE_DIR, 'databases/literature_favorites.sqlite')
LITERATURE_BROWSES_DB = os.path.join(BASE_DIR, 'databases/literature_browses.sqlite')

def get_user_database():
    return UserDatabase(USERS_DB)

def get_web_item_database():
    return WebItemDatabase(WEB_ITEMS_DB)

def get_literature_item_database():
    return LiteratureItemDatabase(LITERATURE_ITEMS_DB)

def get_message_database():
    return MessageDatabase(MESSAGES_DB)

def get_web_favorite_database():
    return WebFavoriteDatabase(WEB_FAVORITES_DB)

def get_web_browse_database():
    return WebBrowseDatabase(WEB_BROWSES_DB)

def get_literature_favorite_database():
    return LiteratureFavoriteDatabase(LITERATURE_FAVORITES_DB)

def get_literature_browse_database():
    return LiteratureBrowseDatabase(LITERATURE_BROWSES_DB)

class UserDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            permission TEXT
        )''')
        self.conn.commit()

    def add_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password, permission) VALUES (?, ?, ?)",
                            (username, password, 'user'))
        self.conn.commit()
    
    def update_user(self, user_id, username, password, permission):
        self.cursor.execute("UPDATE users SET username=?, password=?, permission=? WHERE id=?", 
                            (username, password, permission, user_id))
        self.conn.commit()

    def delete_user(self, username):
        self.cursor.execute("DELETE FROM users WHERE username=?", (username,))
        self.conn.commit()
    
    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = self.cursor.fetchone()
        if user:
            return {
                'id': user[0],
                'username': user[1],
                'password': user[2],
                'permission': user[3]
            }
        else:
            return None
    
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        user_list = []
        for user in users:
            user_info = {
                'id': user[0],
                'username': user[1],
                'password': user[2],
                'permission': user[3]
            }
            user_list.append(user_info)
        return user_list
    
    def update_permission(self, username, new_permission):
        # 更新用户权限
        self.cursor.execute("UPDATE users SET permission=? WHERE username=?", (new_permission, username))
        self.conn.commit()


class WebItemDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS web_items (
            id INTEGER PRIMARY KEY,
            link TEXT UNIQUE,
            title TEXT,
            origin TEXT,
            snippet TEXT,
            time_origin TEXT,
            likes INTEGER,
            favorites INTEGER,
            browses INTEGER
        )''')
        self.conn.commit()
        
    def add_web_item(self, link, title, origin, snippet, time_origin, likes, favorites, browses):
        self.cursor.execute("INSERT INTO web_items (link, title, origin, snippet, time_origin, likes, favorites, browses) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (link, title, origin, snippet, time_origin, likes, favorites, browses))
        self.conn.commit()

    def update_web_item(self, web_item_id, link, title, origin, snippet, time_origin, likes, favorites, browses):
        self.cursor.execute("UPDATE web_items SET link=?, title=?, origin=?, snippet=?, time_origin=?, likes=?, favorites=?, browses=? WHERE id=?", 
                            (link, title, origin, snippet, time_origin, likes, favorites, browses, web_item_id))
        self.conn.commit()

    def delete_web_item(self, web_item_id):
        self.cursor.execute("DELETE FROM web_items WHERE id=?", (web_item_id,))
        self.conn.commit()
        
    def get_web_item(self, web_item_id):
        self.cursor.execute("SELECT * FROM web_items WHERE id=?", (web_item_id,))
        return self.cursor.fetchone()

    def get_web(self, title):
        self.cursor.execute("SELECT * FROM web_items WHERE title=?", (title,))
        webr = self.cursor.fetchone()
        if webr:
            return {
                'id': webr[0],
                'link': webr[1],
                'title': webr[2],
                'origin': webr[3],
                'snippet': webr[4],
                'time_origin': webr[5],
                'likes': webr[6],
                'favorites': webr[7],
                'browses': webr[8]
            }
        else:
            return None


class LiteratureItemDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS literature_items (
            id INTEGER PRIMARY KEY,
            link TEXT UNIQUE,
            title TEXT,
            link_pdf TEXT,
            snippet TEXT,
            author TEXT,
            summary_path TEXT,
            cites INTEGER,
            likes INTEGER,
            favorites INTEGER,
            browses INTEGER
        )''')
        self.conn.commit()
        
    def add_literature_item(self, link, title, link_pdf, snippet, author, summary_path, cites, likes, favorites, browses):
        self.cursor.execute("INSERT INTO literature_items (link, title, link_pdf, snippet, author, summary_path, cites, likes, favorites, browses) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (link, title, link_pdf, snippet, author, summary_path, cites, likes, favorites, browses))
        self.conn.commit()

    def update_literature_item(self, literature_item_id, link, title, link_pdf, snippet, author, summary_path, cites, likes, favorites, browses):
        self.cursor.execute("UPDATE literature_items SET link=?, title=?, link_pdf=?, snippet=?, author=?, summary_path=?, cites=?, likes=?, favorites=?, browses=? WHERE id=?", 
                            (link, title, link_pdf, snippet, author, summary_path, cites, likes, favorites, browses, literature_item_id))
        self.conn.commit()

    def delete_literature_item(self, literature_item_id):
        self.cursor.execute("DELETE FROM literature_items WHERE id=?", (literature_item_id,))
        self.conn.commit()

    def get_literature_item(self, literature_item_id):
        self.cursor.execute("SELECT * FROM literature_items WHERE id=?", (literature_item_id,))
        return self.cursor.fetchone()

    def get_lit(self, title):
        self.cursor.execute("SELECT * FROM literature_items WHERE title=?", (title,))
        litr = self.cursor.fetchone()
        if litr:
            return {
                'id': litr[0],
                'link': litr[1],
                'title': litr[2],
                'link_pdf': litr[3],
                'snippet': litr[4],
                'author': litr[5],
                'summary_path':litr[6],
                'cites':litr[7],
                'likes': litr[8],
                'favorites': litr[9],
                'browses': litr[10]
            }
        else:
            return None
        
    def add_or_update_summary_path(self, link_pdf, summary_path):
        # 检查数据库中是否已存在给定 link_pdf
        self.cursor.execute("SELECT id FROM literature_items WHERE link_pdf=?", (link_pdf,))
        existing_id = self.cursor.fetchone()

        if existing_id:
            # 如果 link_pdf 已存在，更新其 summary_path
            self.cursor.execute("UPDATE literature_items SET summary_path=? WHERE id=?", (summary_path, existing_id[0]))
            self.conn.commit()
        else:
            # 如果 link_pdf 不存在，添加新记录
            self.cursor.execute("INSERT INTO literature_items (link_pdf, summary_path) VALUES (?, ?)", (link_pdf, summary_path))
            self.conn.commit()
            
    def get_summary_path(self, link_pdf):
        self.cursor.execute("SELECT summary_path FROM literature_items WHERE link_pdf=?", (link_pdf,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None




class MessageDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            sender TEXT,
            time TEXT,
            content TEXT
        )''')
        self.conn.commit()
        
    def add_message(self, sender, time, content):
        self.cursor.execute("INSERT INTO messages (sender, time, content) VALUES (?, ?, ?)",
                            (sender, time, content))
        self.conn.commit()

    def update_message(self, message_id, sender, time, content):
        self.cursor.execute("UPDATE messages SET sender=?, time=?, content=? WHERE id=?", 
                            (sender, time, content, message_id))
        self.conn.commit()

    def delete_message(self, message_id):
        self.cursor.execute("DELETE FROM messages WHERE id=?", (message_id,))
        self.conn.commit()
    
    def get_message(self, message_id):
        self.cursor.execute("SELECT * FROM messages WHERE id=?", (message_id,))
        return self.cursor.fetchone()
    
    def get_all_messages(self):
        self.cursor.execute("SELECT * FROM messages")
        messages = self.cursor.fetchall()
        message_list = []
        for message in messages:
            message_info = {
                'id': message[0],
                'sender': message[1],
                'time': message[2],
                'content': message[3]
            }
            message_list.append(message_info)
        return message_list



class WebFavoriteDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS web_favorites (
            id INTEGER PRIMARY KEY,
            user TEXT,
            link TEXT,
            time_favorite INTEGER
        )''')
        self.conn.commit()
        
    def add_web_favorite(self, user, link, time_favorite):
        self.cursor.execute("INSERT INTO web_favorites (user, link, time_favorite) VALUES (?, ?, ?)",
                            (user, link, time_favorite))
        self.conn.commit()

    def delete_web_favorite(self, web_favorite_id):
        self.cursor.execute("DELETE FROM web_favorites WHERE id=?", (web_favorite_id,))
        self.conn.commit()
    
    def get_web_favorite(self, web_favorite_id):
        self.cursor.execute("SELECT * FROM web_favorites WHERE id=?", (web_favorite_id,))
        return self.cursor.fetchone()


class WebBrowseDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS web_browses (
            id INTEGER PRIMARY KEY,
            user TEXT,
            link TEXT,
            time_browse INTEGER
        )''')
        self.conn.commit()
        
    def add_web_browse(self, user, link, time_browse):
        self.cursor.execute("INSERT INTO web_browses (user, link, time_browse) VALUES (?, ?, ?)",
                            (user, link, time_browse))
        self.conn.commit()

    def delete_web_browse(self, web_browse_id):
        self.cursor.execute("DELETE FROM web_browses WHERE id=?", (web_browse_id,))
        self.conn.commit()

    def get_web_browse(self, web_browse_id):
        self.cursor.execute("SELECT * FROM web_browses WHERE id=?", (web_browse_id,))
        return self.cursor.fetchone()


class LiteratureFavoriteDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS literature_favorites (
            id INTEGER PRIMARY KEY,
            user TEXT,
            link TEXT,
            time_favorite INTEGER
        )''')
        self.conn.commit()
        
    def add_literature_favorite(self, user, link, time_favorite):
        self.cursor.execute("INSERT INTO literature_favorites (user, link, time_favorite) VALUES (?, ?, ?)",
                            (user, link, time_favorite))
        self.conn.commit()
        
    def delete_literature_favorite(self, literature_favorite_id):
        self.cursor.execute("DELETE FROM literature_favorites WHERE id=?", (literature_favorite_id,))
        self.conn.commit()
    
    def get_literature_favorite(self, literature_favorite_id):
        self.cursor.execute("SELECT * FROM literature_favorites WHERE id=?", (literature_favorite_id,))
        return self.cursor.fetchone()

class LiteratureBrowseDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS literature_browses (
            id INTEGER PRIMARY KEY,
            user TEXT,
            link TEXT,
            time_browse INTEGER
        )''')
        self.conn.commit()
        
    def add_literature_browse(self, user, link, time_browse):
        self.cursor.execute("INSERT INTO literature_browses (user, link, time_browse) VALUES (?, ?, ?)",
                            (user, link, time_browse))
        self.conn.commit()

    def delete_literature_browse(self, literature_browse_id):
        self.cursor.execute("DELETE FROM literature_browses WHERE id=?", (literature_browse_id,))
        self.conn.commit()
    
    def get_literature_browse(self, literature_browse_id):
        self.cursor.execute("SELECT * FROM literature_browses WHERE id=?", (literature_browse_id,))
        return self.cursor.fetchone()

