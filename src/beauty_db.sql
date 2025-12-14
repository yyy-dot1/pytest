-- テーブルが存在すれば削除し、新しく作成
DROP TABLE IF EXISTS ingredients;

CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    effectiveness_score INTEGER, -- 効果スコア (1-10)
    cost_per_gram REAL          -- グラムあたりの単価
);

-- 初期データの挿入(全てtapule型)

INSERT INTO ingredients (id, name, category, effectiveness_score, cost_per_gram) VALUES
(1, 'ヒアルロン酸', 'Moisturizer', 9, 0.5);

INSERT INTO ingredients (id, name, category, effectiveness_score, cost_per_gram) VALUES
(2, 'レチノール', 'Antioxidant', 8, 1.2);

INSERT INTO ingredients (id, name, category, effectiveness_score, cost_per_gram) VALUES
(3, 'セラミド', 'Moisturizer', 7, 0.8);

INSERT INTO ingredients (id, name, category, effectiveness_score, cost_per_gram) VALUES
(4, 'ビタミンC誘導体', 'Antioxidant', 6, 0.6);

INSERT INTO ingredients (id, name, category, effectiveness_score, cost_per_gram) VALUES
(5, 'グリセリン', 'Moisturizer', 5, 0.1);