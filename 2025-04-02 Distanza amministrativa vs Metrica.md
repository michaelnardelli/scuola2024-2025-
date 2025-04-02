 # Distanza Amministrativa vs Metrica

## Definizione

- **Distanza Amministrativa**: Misura basata su criteri organizzativi, gerarchici o burocratici.
- **Metrica**: Misura quantitativa basata su dati oggettivi e calcoli matematici.

## Differenze Principali

1. **Base di calcolo**:
    - Distanza amministrativa: soggettiva, dipende da regole o politiche.
    - Metrica: oggettiva, basata su numeri e formule.
2. **Applicazione**:
    - Distanza amministrativa: utile per decisioni organizzative.
    - Metrica: utilizzata per analisi tecniche o scientifiche.

## Esempi

1. **Distanza Amministrativa**:
    - Numero di livelli gerarchici tra due dipartimenti (es. 3 livelli tra il dipartimento A e il dipartimento B).
    - Numero di approvazioni necessarie per completare un processo (es. 5 approvazioni per un progetto).
2. **Metrica**:
    - Distanza fisica in chilometri tra due uffici (es. 12 km tra l'ufficio X e l'ufficio Y).
    - Tempo medio di risposta in secondi per un sistema (es. 2,5 secondi).

## Considerazioni

- Entrambe le misure sono utili, ma devono essere applicate nel contesto appropriato.
- La combinazione di entrambe può fornire una visione più completa.
- Ad esempio, valutare sia il numero di livelli gerarchici sia la distanza fisica può migliorare la pianificazione logistica.

## Costi di OSPF, RIP e Statico

| Protocollo         | Costo Predefinito         |
|--------------------|---------------------------|
| **OSPF**           | Basato sulla larghezza di banda (es. 1 per un link da 100 Mbps) |
| **RIP**            | Numero di salti (es. 1 salto = costo 1) |
| **Statico**        | Definito manualmente dall'amministratore (es. 1, 5, 10, ecc.) |

- **OSPF**: Utilizza una metrica basata sulla larghezza di banda, dove i link più veloci hanno un costo inferiore.
- **RIP**: La metrica è il numero di salti, con un massimo di 15 salti per evitare loop.
- **Statico**: Il costo è configurato manualmente, offrendo flessibilità ma richiedendo maggiore gestione.
