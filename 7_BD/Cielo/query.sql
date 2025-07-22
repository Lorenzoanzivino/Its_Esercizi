-- 1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
select codice, comp 
from volo
where durataMinuti > 180;

-- 2. Quali sono le compagnie che hanno voli che superano le 3 ore?
select distinct compagnia.nome
from compagnia, volo
where compagnia.nome = volo.comp
	and volo.durataMinuti > 180;

-- 3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice ‘CIA’ ?
select distinct volo.codice, volo.comp
from volo, arrpart
where arrpart.comp = volo.comp
	and volo.codice = arrpart.codice
	and arrpart.partenza = 'CIA';


-- 4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice ‘FCO’ ?

select distinct compagnia.nome
from compagnia, volo, arrpart
where arrpart.arrivo = 'FCO'
	and compagnia.nome = volo.comp
	and arrpart.comp = volo.comp
	and volo.codice = arrpart.codice; 

-- 5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’ ?

select distinct volo.codice, volo.comp
from volo, compagnia, ArrPart
where compagnia.nome = volo.comp
	and arrpart.comp = volo.comp
	and volo.codice = arrpart.codice
	and arrpart.partenza = 'FCO'
	and arrpart.arrivo = 'JFK';
	
-- 6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?

select distinct compagnia.nome
from compagnia, volo, arrpart
where arrpart.arrivo = 'JFK'
	and arrpart.partenza = 'FCO'
	and compagnia.nome = volo.comp
	and arrpart.comp = volo.comp
	and volo.codice = arrpart.codice; 
	
-- 7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?

select distinct arrpart.comp
from arrpart, luogoaeroporto la1, luogoaeroporto la2
where la1.citta = 'Roma'
	and la2.citta = 'New York'
	and la1.aeroporto = arrpart.partenza
	and la2.aeroporto = arrpart.arrivo

-- 8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli della compagnia di nome ‘MagicFly’?

select distinct ae.codice, ae.nome, la.citta
from arrpart, aeroporto ae, luogoaeroporto la
where arrpart.comp = 'MagicFly'
	and arrpart.partenza = ae.codice
	and la.aeroporto = ae.codice

-- 9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ 
-- e atterrano ad un qualunque aeroporto della città di ‘New York’ ? 
-- Restituire: codice del volo, nome della compagnia, e aeroporti di partenza e arrivo.

select distinct ap.codice as codice_volo, ap.comp as compagnia, ap.partenza, ap.arrivo
from arrpart ap, luogoaeroporto la1, luogoaeroporto la2
where ap.arrivo = la1.aeroporto
	and ap.partenza = la2.aeroporto
	and la1.citta = 'New York'
	and la2.citta = 'Roma'


-- 10. Quali sono i possibili piani di volo con esattamente un cambio 
-- (utilizzando solo voli della stessa compagnia) 
-- da un qualunque aeroporto della città di ‘Roma’ ad un qualunque aeroporto della città di ‘New York’ ? 
-- Restituire: nome della compagnia, codici dei voli, e aeroporti di partenza, scalo e arrivo.


select ar1.comp as compagnia, ar1.codice as codice_volo_1, ar1.partenza as partenza, ar1.arrivo as scalo, 
	ar2.codice as codice_volo_2, ar2.arrivo as arrivo
from arrpart ar1, arrpart ar2, luogoaeroporto la1, luogoaeroporto la2
where ar1.arrivo = ar2.partenza
	and ar1.comp = ar2.comp
	and la1.citta = 'Roma'
	and la2.citta = 'New York'
	and ar1.partenza = la1.aeroporto
	and ar2.arrivo = la2.aeroporto



-- 11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’,
-- atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione

select distinct c.nome
from arrpart ar, compagnia c
where c.nome = ar.comp
	and ar.partenza = 'FCO'
	and ar.arrivo = 'JFK'
	and c.annoFondaz is not Null