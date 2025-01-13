# Certificato Digitale (TPIST - 13/11/2024)

- **Rilasciato da CA**
  - Appartiene a una struttura di certificazione di tipo gerarchico.

- **Funzione**
  - Certificato di appartenenza di una chiave pubblica a un soggetto.

- **Formato**
  - Contiene i dati del soggetto e della CA che ha rilasciato il certificato.
  - Firmato elettronicamente dalla CA per garantire autenticità e integrità.

---

# Firma Digitale

- **Descrizione**
  - Sistema di HASH crittografato.
  
- **HASH**
  - Definizione: Digest o impronta del messaggio.
  - Viene generato e crittografato con la chiave privata di chi appone la firma.

- **Controllo di Affidabilità** (K<sup>+</sup>)
  - **Integrità** garantita dalle caratteristiche dell'HASH.

---

### Procedura per l’Integrità

| Passo | Descrizione                                                                                                                                                                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **a** | Generazione della firma:  <br> \( e(H, K_a^-) = H' \) = firma (dove H è l'HASH, crittografato con la chiave privata \( K_a^- \))                                                       |
| **b** | Verifica della firma:  <br> \( D(H', K_a^+) = H \) - controllo integrità (dove \( H' \) viene decifrato con la chiave pubblica \( K_a^+ \), risultando in H se il messaggio è integro) |

## controllo integirtà  

1) hash(d)=H
2) e(h,Ka^-)=H1
1)

---

## Propieta  HASH

1) quasi iniiettiva

- doc1=-doc2 allora HAsh1=-HASH2

2) effetto valanga

- sensiblita alle midfiche

3) one-way

- funzioni "botola"
- uni direzzionale
   H-->doc
