import pytest
from database_manager import DatabaseManager,DB_SCHEMA_FILE,V1_QUERY_FILE,V2_QUERY_FILE

@pytest.fixture(scope='session')
def db_manager():
    manager = DatabaseManager()
    manager.execute_sql_file(DB_SCHEMA_FILE)
    yield manager
    manager.close()

# test_query_v2.pyの改修の影響に関する検証
def test_query_v2_reflects_sql_change(db_manager:DatabaseManager):
    actual_result = db_manager.execute_query_from_file(V2_QUERY_FILE)

    expected_results = [('ヒアルロン酸', 9), ('セラミド', 7), ('グリセリン', 5)] 
    
    # 順序を無視して比較
    assert sorted(actual_result) == sorted(expected_results)

def test_query_1_reflects_sql_change(db_manager:DatabaseManager):
    actual_results = db_manager.execute_query_from_file(V1_QUERY_FILE)
    expected_results = [
        ('ヒアルロン酸','Moisturizer'),
        ('レチノール','Antioxidant')
    ]
    assert sorted(actual_results) == sorted(expected_results)

@pytest.mark.parametrize(
    'name,expected_cost',
    [
        ('ヒアルロン酸',0.5),
        ('レチノール',1.2),
        ('グリセリン',0.1)
    ]
)

def test_ingredient_cost_check_parameterized(
    db_manager:DatabaseManager,
    name:str,
    expected_cost:float
):

    query = f"SELECT cost_per_gram FROM ingredients WHERE name ='{name}';"
    
    cursor = db_manager.conn.execute(query)
    actual_cost = cursor.fetchone()[0]

    assert actual_cost == expected_cost