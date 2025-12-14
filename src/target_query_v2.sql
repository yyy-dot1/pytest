SELECT 
    name,
    effectiveness_score
FROM
    ingredients
WHERE   
    category = 'Moisturizer' AND 'effectiveness_score' >= 7
ORDER BY effectiveness_score DESC;