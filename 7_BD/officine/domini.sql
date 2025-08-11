CREATE DOMAIN stringa AS varchar(255);

CREATE DOMAIN intero AS integer CHECK 
    (VALUE >= 0);
CREATE DOMAIN codicefiscale AS char(16) 
    CHECK (VALUE ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

CREATE DOMAIN telefono AS varchar(20) 
    CHECK (VALUE ~ '^\+?[0-9]{1,3}[\s\-]?[0-9]{6,14}$');

CREATE DOMAIN partitaiva AS char(11) 
    CHECK (VALUE ~ '^[0-9]{11}$');

CREATE DOMAIN data_nascita AS date;

CREATE DOMAIN orario AS time;

