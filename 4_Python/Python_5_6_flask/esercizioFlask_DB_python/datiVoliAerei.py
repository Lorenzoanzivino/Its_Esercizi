DB = {
  "Nazione": {
    1: {
      "id": 1,
      "nome": "Italia"
    },
    2: {
      "id": 2,
      "nome": "Spagna"
    }
  },
  "Citta": {
    1: {
      "id": 1,
      "n_abitanti": 60000,
      "nome": "Pomezia",
      "nazione": 1
    },
    2: {
      "id": 2,
      "n_abitanti": 2500000,
      "nome": "Roma",
      "nazione": 1
    },
    3: {
      "id": 3,
      "n_abitanti": 3200000,
      "nome": "Madrid",
      "nazione": 2
    }
  },
  "Aereoporto": {
    1: {
      "id": 1,
      "nome": "Aeroporto di Roma-Fiumicino",
      "codice": "FCO",
      "citta": 2
    },
    2: {
      "id": 2,
      "nome": "Aeroporto di Madrid-Barajas",
      "codice": "MAD",
      "citta": 3
    },
    3: {
      "id": 3,
      "nome": "Aeroporto di Roma-Ciampino",
      "codice": "CIA",
      "citta": 2
    }
  },
  "CompagniaAerea": {
    1: {
      "id": 1,
      "fondazione": 2021,
      "nome": "ITA Airways",
      "citta": 2
    },
    2: {
      "id": 2,
      "fondazione": 1927,
      "nome": "Iberia",
      "citta": 3
    }
  },
  "Volo": {
    1: {
      "id": 1,
      "durata_in_minuti": 150,
      "codice": "AZ060",
      "compagniaAerea": 1,
      "aeroporto_partenza": 1,
      "aeroporto_arrivo": 2
    },
    2: {
      "id": 2,
      "durata_in_minuti": 145,
      "codice": "IB3231",
      "compagniaAerea": 2,
      "aeroporto_partenza": 2,
      "aeroporto_arrivo": 1
    },
    3: {
      "id": 3,
      "durata_in_minuti": 60,
      "codice": "AZ1010",
      "compagniaAerea": 1,
      "aeroporto_partenza": 1,
      "aeroporto_arrivo": 3
    }
  }
}