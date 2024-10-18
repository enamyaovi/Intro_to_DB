-- SHOW COLUMNS FROM Books FROM alx_book_store;
USE alx_book_store;

SELECT 
    TABLE_NAME, 
    COLUMN_NAME, 
    COLUMN_TYPE
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'Books';