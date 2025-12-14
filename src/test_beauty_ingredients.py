# import pytest
# from database_manager import DatabaseManager,DB_SCHEMA_FILE ,V1_QUERY_FILE,V2_QUERY_FILE

# @pytest.fixture
# def db_manager():
#     manager = DatabaseManager()
#     manager.execute_sql_file(DB_SCHEMA_FILE)
#     yield manager

#     manager.close()

# # 期待値と実際の値の比較(V2_QUERY_FILE)
# def test_query_v2_reflects_sql_change(db_manager:DatabaseManager):
#     actual_results = db_manager.execute_query_from_file(V2_QUERY_FILE)
#     expected_results = [
#         ('ヒアルロン酸',9)
#         ('セラミド',7)
#     ]

#     assert actual_results == expected_results

# # 期待値と実際の値の比較(V1_QUERY_FILE)
# def test_query_v1_for_regression(db_manager:DatabaseManager):
#     actual_results = db_manager.execute_query_from_file(V1_QUERY_FILE)
#     expected_results = [
#         ('ヒアルロン酸','Moisturizer')
#         ('セラミド','Antioxidant')
#     ]

#     assert sorted(actual_results) == sorted(expected_results)

# @pytest.mark.parametrize(
#     'ingredient_name','expected_cost',
#     [
#         ('ヒアルロン酸',0.5),
#         ('レチノール',1.2),
#         ('グリセリン',0.1)
#     ]
# )

# # 改修後のSQLクエリ (target_query.sql) の実行結果が期待される結果と一致するかどうかを検証する
# def test_ingredient_cost_check_parameterized(
#     db_manager_setup: DatabaseManager,
#     ingredient_name:str,
#     expected_cost:float #パラメータライズ
# ):
    
#     query = f"SELECT cost_per_gram FROM ingredients WHERE name ='{ingredient_name}';"
#     cursor = db_manager_setup.conn.execute(query)
#     # index[0]の値
#     actual_cost = cursor.fetchone()[0]

#     assert actual_cost == expected_cost

# # Pythonのロジックによってデータが変わったとき、その後の SQLクエリの結果が仕様通りか検証する。
#     # UPDATEクエリがDBの状態を正しく変更したか
#     # インメモリデータベースのデータが期待通りに更新されているか
#     # 変更されたデータに対しても正しくフィルタリングと抽出できてるか
#     # よきせぬバグが起こってないか
#     # SQLファイルに書かれたロジックの回収もPythonでデータを変更する回収も、システム全体の動作が期待通りであるか
# # Pythonで定義した期待値（仕様）と、実際に読み込んだSQLファイルが返す結果が一致するか検証する
# def test_python_logic_modifies_data(db_manager:DatabaseManager):
#     # V2_QUERY_FILEのデータを変更したものを作成
#     update_query = "UPDATE ingredients SET effectiveness_score = 8 WHERE name = 'グリセリン';"
#     db_manager.conn.execute(update_query)
#     db_manager.conn.commit()
#     # V2_QUERY_FILEを読み込む
#     updated_result = db_manager.execute_query_from_file(V2_QUERY_FILE)

#     expected_updated_results = [
#         ('ヒアルロン酸', 9),
#         ('グリセリン', 8),
#         ('セラミド', 7)
#     ]
    
#     assert len(updated_result) == 3,"FALSE"
#     assert sorted(updated_result) == sorted(expected_updated_results),"FALSE"
