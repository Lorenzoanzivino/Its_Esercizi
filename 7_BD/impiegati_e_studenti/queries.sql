--(Riguardare le slide se necessario!)

-- Consegnare un unico file queries.sql contenente il codice SQL.

-- 1. Quali sono i nomi degli impiegati nati a partire dall'anno 1965
select nome 
from persona p, impiegato i
where p.cf = i.persona
    and data_nascita >= '1965-01-01'
order by data_nascita asc;

-- 2. Quali sono i nomi di tutti i progetti?
select nome from progetto;

-- 3. Quali sono gli stipendi dei direttori?
select stipendio from impiegato
where ruolo = 'Direttore';

-- 4. Quanti sono i progettisti?
select count (*) from impiegato
where ruolo = 'Progettista';

-- 5. Quanti sono i responsabili?
select count (distinct resp_prog) from impiegato, progetto
where ruolo = 'Progettista';


-- 6. Quanti sono i progettisti che non sono responsabili? Non la sapete fare!
select * from impiegato
where impiegato.ruolo = 'Progettista'
    and persona not in (
        select distinct resp_prog 
        from progetto
        );    -- una query in una query
        

-- 7. Qual è lo stipendio medio dei segretari?
select AVG(stipendio) from impiegato
where ruolo = 'Segretario';

-- 8. Qual è l'età della/o studente meno giovane?
select MAX(date_part('year', age(current_date, data_nascita))) as eta
FROM persona, studente
where persona.cf = studente.persona;

-- 9. Quanti sono i direttori che hanno assolto agli obblighi militari?
select count(cf) from persona, impiegato
where ruolo = 'Direttore' 
    and persona.cf = impiegato.persona 
    and persona.pos_uomo = 'Assolto';

-- 10. Quanti sono i progetti di cui è responsabile un'impiegata con almeno due figli?
select count(*) from persona, progetto
where persona.cf = progetto.resp_prog
	and persona.maternita >=2;