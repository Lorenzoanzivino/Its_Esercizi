--(Riguardare le slide se necessario!)

--1. Quali sono i nomi degli impiegati nati a partire dall'anno 
--2. Quali sono i nomi di tutti i progetti?
--3. Quali sono gli stipendi dei direttori?
--4. Quanti sono i progettisti?
--5. Quanti sono i responsabili?
--6. Quanti sono i progettisti che non sono responsabili? Non la sapete fare!
--7. Qual è lo stipendio medio dei segretari?
--8. Qual è l'età della/o studente meno giovane?
    usare select(date_part('year',age(current_date, <DATA DI NASCITA>))) as eta FROM [...];
--9. Quanti sono i direttori che hanno assolto agli obblighi militari?
--10. Quanti sono i progetti di cui è responsabile un'impiegata con almeno due figli?

-- Consegnare un unico file queries.sql contenente il codice SQL.


-- 1
select nome from persona, impiegato
where persona.cf = impiegato.persona
order by data_nascita asc;

-- 2
select nome from progetto;

-- 3
select stipendio from impiegato
where ruolo = 'Direttore';

-- 4
select count (*) from impiegato
where ruolo = 'Progettista';

-- 5
select count (*) from impiegato, progetto
where ruolo = 'Progettista';

-- 7
select AVG(stipendio) from impiegato
where ruolo = 'Segretario';

-- 8
select max(date_part('year', age(current_date, data_nascita))) as eta
FROM persona, studente
where persona.cf = studente.persona;

-- 9
select count(cf) from persona, impiegato
where ruolo = 'Direttore' 
    and persona.cf = impiegato.persona 
    and persona.pos_uomo is not null;

-- 10
select count(id) from persona, progetto
where persona.cf = progetto.resp_prog
	and persona.maternita >=2;