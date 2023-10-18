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

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
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


class WebItemDatabase:
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


class LiteratureItemDatabase:
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


class MessageDatabase:
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


class WebFavoriteDatabase:
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

