SELECT
    name,
    category
FROM
    ingredients
WHERE 
    -- フィルタリング
    effectiveness_score >= 8
ORDER BY name;