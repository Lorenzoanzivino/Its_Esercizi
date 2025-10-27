-- Spiegazione del JOIN

select *
from volo v, compagnia c
where v.comp = c.nome;

-- JOIN - Contapposizione tra 2 tabelle
-- (Metto insieme una ennupla della prima tabella con la ennupla della seconda quando la condizione è vera)

select *
from volo v 
    JOIN compagnia c 
        ON v.comp = c.nome
    JOIN arrpart ap
        ON v.codice = ap.codice
            and
            v.comp = ap.comp;


-- JOIN ESTERNI - prendo tutte le ennuple di una tabella mentre dell'altra tabella solo quelle ennuple che si accoppiano.

select *
from compagnia c LEFT OUTER JOIN volo vecchia
    ON c.nome = v.comp;