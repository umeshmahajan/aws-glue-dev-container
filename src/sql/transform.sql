SELECT 
    name,
    id,
    UPPER(name) AS name_upper
FROM source_table
WHERE id IS NOT NULL
