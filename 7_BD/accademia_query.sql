-- 1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome ‘Pegasus’ ?

select wp.nome, wp.inizio, wp.fine 
from wp, progetto 
where progetto.nome = 'Pegasus' and wp.progetto = progetto.id;

-- 2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
-- una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?

SELECT distinct Persona.nome, Persona.cognome, Persona.posizione
FROM Persona, AttivitaProgetto, Progetto
WHERE Persona.id = AttivitaProgetto.persona
  AND AttivitaProgetto.progetto = Progetto.id
  AND Progetto.nome = 'Pegasus'
order by Persona.cognome desc;


-- 3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
-- una attività nel progetto ‘Pegasus’ ?

select distinct p.nome, p.cognome, p.posizione
from persona p, attivitaprogetto ap, attivitaprogetto ap2,progetto pr
where p.id = ap.persona 
	and ap.progetto = pr.id 
	and ap2.id <> ap.id
	and ap2.persona = ap.persona
	and ap2.progetto = ap.progetto
	and pr.nome ='Pegasus'
order by p.cognome desc;


-- 4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto almeno una assenza per malattia?

select distinct p.nome, p.cognome, p.posizione
from persona p, assenza a
where a.persona = p.id
	and p.posizione = 'Professore Ordinario'
	and a.tipo = 'Malattia';


-- 5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
-- fatto più di una assenza per malattia?

select distinct p.nome, p.cognome, p.posizione
from persona p, assenza a1, assenza a2
where a1.persona = p.id
	and a1.id <> a2.id
	and a1.persona = a2.persona
	and p.posizione = 'Professore Ordinario'
	and a1.tipo = 'Malattia'; 


-- 6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
-- un impegno per didattica?

select distinct p.nome, p.cognome, p.posizione
from persona p, AttivitaNonProgettuale a
where a.persona = p.id
	and p.posizione = 'Ricercatore'
	and a.tipo = 'Didattica';


-- 7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
-- impegno per didattica?

select distinct p.nome, p.cognome, p.posizione
from persona p, AttivitaNonProgettuale a1, AttivitaNonProgettuale a2
where a1.persona = p.id
	and a1.id <> a2.id
	and a1.persona = a2.persona
	and p.posizione = 'Ricercatore'
	and a1.tipo = 'Didattica';


-- 8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali?

select p.nome, p.cognome
from persona p, AttivitaProgetto ap, AttivitaNonProgettuale anp
where ap.persona = p.id
	and anp.persona = p.id
	and ap.giorno = anp.giorno;


-- 9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
-- attività progettuali che attività non progettuali? Si richiede anche di proiettare il
-- giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
-- entrambe le attività.

select p.nome , p.cognome, pr.nome as prj, ap.oreDurata as h_prj, anp.tipo as att_noprj , anp.oreDurata as h_noprj 
from persona p, AttivitaProgetto ap, AttivitaNonProgettuale anp, progetto pr
where ap.persona = p.id
	and anp.persona = p.id
	and ap.giorno = anp.giorno
	and ap.progetto = pr.id;


-- 10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali?

select p.nome, p.cognome
from persona p, assenza a, AttivitaProgetto ap
where p.id = a.persona
	and p.id = ap.persona
	and a.giorno = ap.giorno;


-- 11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
-- assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
-- nome del progetto, la causa di assenza e la durata in ore della attività progettuale.

select p.nome, p.cognome, a.giorno as giorno, a.tipo as causa_ass, pr.nome, ap.oreDurata as ore_att_prj
from persona p, assenza a, AttivitaProgetto ap, progetto pr
where p.id = a.persona
	and p.id = ap.persona
	and a.giorno = ap.giorno
	and ap.progetto = pr.id;


-- 12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?

select distinct wp1.nome
from wp wp1, wp wp2, progetto p
where wp1.nome = wp2.nome
	and wp1.progetto = p.id
	and wp1.progetto <> wp2.progetto;