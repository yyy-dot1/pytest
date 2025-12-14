import sqlite3
from typing import List,Tuple,Any

class DatabaseManager:
    def __init__(self,db_path=":memory:"):
        # セッション情報
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    # SQLファイル実行メソッド
    # データベースの構造を構築したり、データをセットアップ/更新する
    def execute_sql_file(self,sql_file_path:str):
        # sqlファイルを読みこむ
        with open(sql_file_path,'r',encoding='UTF-8') as f:
            sql_script = f.read()
        # 実行する
        self.conn.executescript(sql_script)
        # 登録する
        self.conn.commit()
    # クエリファイル実行メソッド
    # データベースから特定のデータを取得する
    def execute_query_from_file(self,sql_file_path:str) -> List[Tuple[Any]]:
        with open(sql_file_path,'r',encoding='utf-8') as f:
            query = f.read()
        cursor = self.conn.execute(query)
        #　タプル型で結果を返す
        return [tuple(row) for row in cursor.fetchall()]

    def close(self):
        self.conn.close()

#テストファイルのインポート用定数を定義
DB_SCHEMA_FILE = 'beauty_db.sql'
V1_QUERY_FILE = 'target_query_v1.sql'
V2_QUERY_FILE = 'target_query_v2.sql'