-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?
select a.codice, a.nome, count(distinct comp)
from aeroporto a, ArrPart ap
where ap.partenza = a.codice or ap.arrivo = a.codice
group by a.codice, a.nome;


-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno 100 minuti?
select count(*) as num_Voli
from volo v, arrpart ap
where v.codice = ap.codice
	and v.comp = ap.comp
	and ap.partenza = 'HTR'
	and v.durataminuti >= 100;


-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione nella quale opera?
select la.nazione, count(distinct la.aeroporto) as num_aerop
from arrpart ap, volo v, compagnia c, aeroporto a, luogoaeroporto la
where c.nome = 'Apitalia'
  and v.comp = c.nome
  and ap.codice = v.codice
  and ap.comp = v.comp
  and (ap.partenza = a.codice or ap.arrivo = a.codice)
  and la.aeroporto = a.codice
group by la.nazione;


-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla compagnia ‘MagicFly’ ?
select avg(durataminuti) as media, 
	min(durataminuti),
	max(durataminuti)
from volo v
where comp = 'MagicFly';


-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli aeroporti?
select a.codice, a.nome, min(c.annofondaz) as anno
from aeroporto a, arrPart ap, volo v, compagnia c
where v.codice = ap.codice
	and v.comp = ap.comp
	and (a.codice = ap.partenza or a.codice = ap.arrivo)
	and v.comp = c.nome
group by a.codice, a.nome;


-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più voli?
select la_partenza.nazione as nazione_partenza,   -- nazione da cui parte il volo
    count(distinct la_arrivo.nazione) as num_nazioni_raggiungibili
from arrPart ap, aeroporto a_partenza, aeroporto a_arrivo, 
     luogoAeroporto la_partenza, luogoAeroporto la_arrivo
where ap.partenza = a_partenza.codice              -- collega partenza a aeroporto
  and ap.arrivo = a_arrivo.codice                  -- collega arrivo a aeroporto
  and a_partenza.codice = la_partenza.aeroporto   -- collega aeroporto alla nazione di partenza
  and a_arrivo.codice = la_arrivo.aeroporto       -- collega aeroporto alla nazione di arrivo
group by la_partenza.nazione;


-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?
select a.codice, a.nome, avg(durataminuti) as media_durata
from aeroporto a, arrPart ap, volo v
where a.codice = ap.partenza
	and v.codice = ap.codice
	and v.comp = ap.comp
group by a.codice, a.nome;


-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate a partire dal 1950?
select nome, sum(durataminuti) as durata_tot
from compagnia c, volo v
where c.annofondaz >= 1950
	and v.comp = c.nome
group by nome;


-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?
select a.codice, a.nome
from aeroporto a, arrPart ap, volo v
where (ap.partenza = a.codice or ap.arrivo = a.codice)
	and ap.comp = v.comp
	and ap.codice = v.codice
group by a.codice, a.nome
having count(distinct v.comp) = 2;


-- 10. Quali sono le città con almeno due aeroporti?
select citta
from luogoAeroporto
group by citta
having count(*) >= 2;


-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6 ore?
select v.comp as compagnia
from volo v
group by v.comp
having avg(durataminuti) > 6 * 60;


-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?
select v.comp as compagnia
from volo v
group by v.comp
having min(durataminuti) > 100;


-- 13
with D as (select max(durataminuti) as max_durata from volo)
select comp
from volo, D
group by comp, D.max_durata
having max(durataminuti) = D.max_durata;

-- 14 Qual'e il nome delle compagnie che non hanno alcun volo

with D as 
	(select distinct ap.comp
	from volo as v, arrpart as ap
	where ap.codice = v.codice
	and ap.comp = v.comp)

select c.nome
from compagnia as c
group by c.nome
having c.nome not in (select * from D)