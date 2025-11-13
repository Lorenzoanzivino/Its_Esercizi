-- DOMINI
CREATE DOMAIN stringa AS varchar;
CREATE DOMAIN reale AS real CHECK (VALUE >= 0);
CREATE DOMAIN realeI01 AS real CHECK (VALUE > 0 AND VALUE < 1);
CREATE DOMAIN intero AS integer CHECK (VALUE >= 0);
CREATE DOMAIN codicefiscale AS char(16) CHECK (VALUE ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');
CREATE DOMAIN telefono AS varchar(20) CHECK (VALUE ~ '^\+?[0-9]{1,3}[\s\-]?[0-9]{6,14}$');
CREATE DOMAIN partitaiva AS char(11) CHECK (VALUE ~ '^[A-Z]{2}?[0-9A-Z]{8,13}$');
CREATE DOMAIN email AS varchar CHECK (VALUE ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');
CREATE DOMAIN data_nascita AS date;