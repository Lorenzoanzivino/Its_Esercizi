-- 1. Quanti sono gli strutturati di ogni fascia?
select posizione, count(posizione) from Persona
group by posizione;


-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?
select count(*) from Persona
where stipendio >= 40000;


-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?
select count(*) from progetto
where budget > 50000 and fine < current_date;


-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’ ?
select avg(oredurata) as media, min(oredurata) as minimo, max(oredurata) as massimo 
from attivitaProgetto, progetto
where nome = 'Pegasus'
	and progetto.id = attivitaprogetto.progetto;



-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?
select pr.id as id_persona, avg(oredurata), min(oredurata), max(oredurata) 
from AttivitaProgetto ap, Progetto p, Persona pr
where p.nome ='Pegasus' 
	and p.id = ap.progetto
	and ap.persona = pr.id
group by pr.id;


-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?
select p.id as id_persona, nome, cognome, sum(oredurata) as ore_didattica
from persona p, AttivitaNonProgettuale anp
where p.id = anp.persona
	and tipo ='Didattica'
group by p.id;


-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?
select avg(stipendio), min(stipendio), max(stipendio)
from persona
where posizione = 'Ricercatore';


-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?
select posizione, avg(stipendio), min(stipendio), max(stipendio)
from persona
group by posizione;



-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?
select pr.id as id_progetto, pr.nome as progetto, sum(oredurata) as totale_ore
from persona p, attivitaProgetto ap, progetto pr
where p.id = ap.persona
	and ap.progetto = pr.id
	and p.nome = 'Ginevra'
	and p.cognome = 'Riva'
group by pr.id;


-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?
select pr.id as id_progetto, pr.nome as progetto from progetto pr, persona p, attivitaProgetto ap
where p.id = ap.persona
	and ap.progetto = pr.id
group by pr.id, pr.nome
having count(distinct p.id) > 2;


-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?
select p.id as id_persona, p.nome, p.cognome
from Persona p, AttivitaProgetto ap
where p.id = ap.persona
  and p.posizione = 'Professore Associato'
group by p.id, p.nome, p.cognome
having count(distinct ap.progetto) > 1;