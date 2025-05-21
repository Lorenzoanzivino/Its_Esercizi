'''Esercizio 4: Sistema di gestione dell'università

Creare un sistema per gestire un'università con dipartimenti, corsi, professori e studenti.

1. Creare una classe astratta Persona:
Gli attributi:

    Il nome
    L'età

I metodi di ricerca:

    get-role, un metodo astratto da implementare dalle sottoclassi.
    ?st?, metodo per restituire una rappresentazione delle stringhe della persona.

2. Creare sottoclassi Studente e professore che ereditano dalla persona e implementare il metodo astratto.

Studente di classe :
Altri attributi:

        - studente-id,
        Corsi (elenco delle istanze del corso).

Metodo aggiuntivo:

        Iscriviti, per iscrivere lo studente in un corso.

Professore di classe :
Altri attributi:

        - Professorid,
        dipartimento (un'istanza del dipartimento),
        Corsi (elenco delle istanze del corso)

Metodo aggiuntivo:

        assegna-tocourse, assegnare il professore ad un corso.


- 3. Crea un corso di classe:
Gli attributi:

    Il nome del corso
    Il codice di corso
    Studenti (elenco delle istanze degli studenti)
    Professore (istanza di professori)

I metodi di ricerca:

    Add-student, per aggiungere uno studente al corso.
    Set-professor, per impostare il professore per il corso.
    ?st?, metodo per restituire una rappresentazione delle stringhe del corso.

- 4. Creare un dipartimento di classe:

Gli attributi:

    Il nome del dipartimento
    Corsi (elenco delle istanze del corso)
    Professori (liste delle istanze del Professore)

I metodi di ricerca:

    Add-course, per aggiungere un corso al dipartimento.
    add-professor, per aggiungere un professore al dipartimento.
    ?st?, metodo per restituire una rappresentazione di stringa del dipartimento.

5. - Si'. Creare una classe di università :

Gli attributi:

    Il nome
    dipartimenti (elenco delle istanze del Dipartimento)
    Studenti (elenco delle istanze degli studenti)

I metodi di ricerca:

    Add-department, per aggiungere un dipartimento all'università.
    Add-student, per aggiungere uno studente all'università.
    ?strà, metodo per restituire una rappresentazione di stringa dell'università.

Infine, scrivi un semplice programma di driver. Dopo aver creato un'università, dovresti iniziare creando istanze dei componenti principali che compongono un'università:

    Dipartimenti (ad es. Scienze informatiche, Letteratura)

    Corsi (ad es. Strutture dati, Letteratura medievale)

    Professori (ad esempio, membri della facoltà che insegneranno i corsi)

    Studenti (ad es. individui che si iscrivono ai corsi)

Una volta create queste istanze, segui questi passaggi:

    Aggiungere tutte le entità all'università: Assicurarsi che la classe universitaria possa registrare dipartimenti e studenti.

    Iscrivetevi studenti in corsi : Simula la registrazione degli studenti assegnando gli studenti a uno o più corsi.

    Assegnare professori ai corsi: ogni corso dovrebbe avere un professore responsabile dell'insegnamento.

    Visualizza lo stato dell'università: ad ogni passo significativo, stampa un riepilogo dello stato attuale dell'università. Questo potrebbe includere:
        Un elenco di corsi con docenti assegnati.
        Quali studenti sono iscritti a quali corsi.
        Una ripartizione dei dipartimenti e i corsi che offrono.
'''