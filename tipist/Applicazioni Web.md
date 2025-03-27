# Applicazioni Web

## **Premessa**

Le **applicazioni web** sono software accessibili tramite un browser e utilizzano **Internet** o reti aziendali per fornire servizi agli utenti. Si basano su **architetture client-server** e spesso adottano un'architettura **multi-tier** per scalabilità, sicurezza e manutenibilità.

---

## **Socket: Cosa sono e a cosa servono**

Un **socket** è un'interfaccia di comunicazione tra due processi su una rete. È identificato da:

- **Indirizzo IP** (identifica il dispositivo sulla rete)
- **Porta logica** (identifica il processo specifico sul dispositivo)

I socket operano a **livello di trasporto** del modello OSI e utilizzano protocolli come:

- **TCP (Transmission Control Protocol)**: Connessione affidabile con controllo degli errori.
- **UDP (User Datagram Protocol)**: Connessione veloce, ma senza garanzia di consegna.

### **Caratteristiche principali**

- Due protocolli diversi possono usare la stessa **porta logica**, purché abbiano protocolli di trasporto differenti.
- Una comunicazione è univocamente identificata da:
  **(Protocollo, IP1, Porta1, IP2, Porta2)**
- Due componenti fondamentali:
  - **Socket lato client** → (IPc, Porta\_c) → gestisce la risposta dal server.
  - **Socket lato server** → (IPs, Porta\_s) → gestisce le richieste dei client.

---

## **Architettura TCP/IP**

L'architettura **TCP/IP** è il modello su cui si basa Internet ed è suddivisa in quattro livelli:

1. **Livello di accesso alla rete**: Gestisce la trasmissione fisica dei dati.
2. **Livello Internet**: Instrada i pacchetti tramite protocolli come **IP**.
3. **Livello di trasporto**: Garantisce la comunicazione end-to-end con **TCP** o **UDP**.
4. **Livello applicativo**: Comprende i protocolli come **HTTP, FTP, SMTP**.

---

## **Elementi di un’Applicazione Web**

1. **Architettura**: Può essere **client-server**, **peer-to-peer (P2P)** o **ibrida**.
2. **Accesso concorrente**: Più utenti possono interagire contemporaneamente.
3. **Gestione di grandi database**: Dati distribuiti e ottimizzati.
4. **Sicurezza**: Autenticazione, crittografia, protezione dagli attacchi.
5. **Gestione delle transazioni**: Esecuzione atomica delle operazioni per mantenere la coerenza dei dati.

---

## **Architettura Multi-Tier**

Le applicazioni moderne utilizzano architetture **multi-tier** (a più livelli) per una maggiore efficienza e modularità.

### **Principali livelli (tier)**

1. **Presentation Tier (Front-end)**: Interfaccia utente, realizzata con HTML, CSS, JavaScript.
2. **Application Tier (Middleware)**: Logica applicativa, gestita da API e framework backend.
3. **Data Tier (Back-end)**: Gestione database e archiviazione.

L'uso di **più livelli** migliora la scalabilità e la manutenibilità dell'applicazione.

---

## **Comunicazione Client-Server**

### **Tipologie di comunicazione**

- **Unicast** → Il server gestisce un solo client alla volta.
- **Multicast** → Il server gestisce più client contemporaneamente.

**Multicast dettagli:**

- Il server accetta una connessione e la sposta su una **porta secondaria** per gestire nuove richieste simultanee.

---

## **Evoluzione delle Architetture Web**

1. **Applicazioni Monolitiche (uni-tier)** → Tutti i componenti sono in un unico sistema.
2. **Applicazioni Two-Tier:**
   - **Thin client** → Il server elabora quasi tutto, il client si occupa della presentazione.
   - **Thick client** → Parte dell'elaborazione viene gestita dal client.
3. **Applicazioni Multi-Tier (n-tier)** → Separazione tra front-end, middleware e back-end per scalabilità.

---

## **Architetture di Rete**

1. **Client-Server** → Un server centrale gestisce le richieste.
2. **Peer-to-Peer (P2P):**
   - **Centralizzato** → Un server coordina i peer.
   - **Decentralizzato** → Nessun server centrale, peer autonomi.
   - **Misto** → Peer con ruoli specializzati.

---

## **Domande e Risposte**

1. **Una macchina server non può essere anche client?** → **(Falso)**, può eseguire entrambi i ruoli.
2. **Non sono gli host a essere client o server, ma i processi?** → **(Vero)**, dipende dal software in esecuzione.
3. **Un host può essere contemporaneamente sia client che server?** → **(Vero)**, es. un PC può ospitare un sito web e navigare.
4. **Un processo server può a sua volta diventare client?** → **(Vero)**, es. un database server può richiedere dati ad altri server.
5. **Un servizio può essere fornito da più server?** → **(Vero)**, per migliorare affidabilità e scalabilità.

