
# Algoritmo di dijsktra

## come si fa

1. si mette al infinito come valore predefinito ad ogni nodo
2. si va dal lato a costo minore 
3. si assegna il costo al nodo(il costo partendo da h)
4. si segna da chi ho visitato
5. si fa la somma tra i costi da h 

## esempio
**Grafo orientato con pesi non negativi:**

- **Nodi:** A, B, C, D, E  
- **Archi e pesi:**  
  - A → B (peso 6)  
  - A → D (peso 1)  
  - D → B (peso 2)  
  - B → E (peso 3)  
  - D → E (peso 4)  
  - A → C (peso 5)  
  - C → E (peso 2)  

**Rappresentazione visiva:**  
```
    (A)
   / | \
  6↓ 1↓ ↓5
  (B)←(D) (C)
   |  ↗ |  ↘
  3↓ /2 |4  ↘2
  (E)   |    (E)
```

### Esercizio:
1. **Trova il cammino minimo da A a tutti gli altri nodi** usando l'algoritmo di Dijkstra.  
2. **Costruisci la tabella delle distanze** passo dopo passo.  
3. **Verifica il risultato finale** (soluzione sotto).

---

### Soluzione:
**Distanze finali dal nodo A:**  
- A → A: 0  
- A → B: 3 (percorso: A → D → B)  
- A → C: 5 (percorso diretto: A → C)  
- A → D: 1 (percorso diretto: A → D)  
- A → E: 5 (percorso: A → D → E)  

**Tabella passo-passo (sintesi):**

| Nodo visitato | Distanze | A   | B   | C   | D   | E   |
| ------------- | -------- | --- | --- | --- | --- | --- |
| Inziale       |          | 0   | ∞   | ∞   | ∞   | ∞   |
| Visto A       |          | 0   | 6   | 5   | 1   | ∞   |
| Visto D       |          | 0   | 3   | 5   | -   | 5   |
| Visto B       |          | 0   | -   | 5   | -   | 5   |
| Visto C       |          | 0   | -   | -   | -   | 5   |
| Visto E       |          | -   | -   | -   | -   | -   |

