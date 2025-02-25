# Applicazioni Web

## **Premessa**

### **Socket: Cosa sono e a cosa servono**

Un **socket** è una struttura dati che rappresenta un canale di comunicazione tra due processi su una rete. È identificato da:

- **Indirizzo IP** (che identifica il dispositivo sulla rete)
    
- **Porta logica** (che identifica un processo specifico sul dispositivo)
    

Si colloca a **livello di trasporto** nel modello OSI e utilizza protocolli come **TCP** (connessione affidabile) o **UDP** (connessione veloce ma senza garanzie di consegna).

**Scopo dei socket:** Permettono di stabilire e gestire una connessione **client-server** per lo scambio di dati e servizi in rete.

### **Caratteristiche principali**

- Due protocolli differenti possono utilizzare la **stessa porta logica**, purché abbiano protocolli di trasporto diversi.
    
- Per identificare univocamente una comunicazione si utilizza il concetto di **associazione**: **(Protocollo, IP1, Porta1, IP2, Porta2)**
    

Un socket ha due componenti fondamentali:

- **Socket lato client** → (IPc, Porta_c) → gestisce la risposta ricevuta dal server.
    
- **Socket lato server** → (IPs, Porta_s) → gestisce la richiesta proveniente dal client.
    

---

## **Elementi di un’applicazione web**

1. **Architettura**: Può essere **client-server**, **peer-to-peer (P2P)** o **ibrida**.
    
2. **Accesso concorrente** ai servizi: più utenti possono interagire simultaneamente.
    
3. **Applicazioni complesse**: gestione avanzata delle risorse e interfacce sofisticate.
    
4. **Gestione di grandi archivi**: spesso i dati sono distribuiti e richiedono sistemi scalabili.
    
5. **Requisiti di sicurezza**: autenticazione, autorizzazione, crittografia, protezione da attacchi.
    
6. **Gestione delle transazioni**: insieme di operazioni eseguite in modo atomico per garantire la consistenza dei dati.
    

---

## **Comunicazione Client-Server**

### **Tipologie di comunicazione**

- **Unicast** → Il server gestisce un solo client alla volta.
    
- **Multicast** → Il server può gestire più client simultaneamente.
    

**Dettagli sulla comunicazione multicast:**

- Il server, dopo aver accettato una connessione iniziale, la sposta su **una porta secondaria** per mantenere libera la porta principale per nuove connessioni.
    

---

## **Architettura delle Applicazioni Web**

Le applicazioni web si basano su due concetti fondamentali:

- **Livelli (tier)** → Insieme di nodi fisici che elaborano i dati dell’applicazione.
    
- **Strati (layer)** → Componenti software che implementano le diverse funzionalità dell’applicazione.
    

### **Struttura logica di un’applicazione web**

1. **Front-end** → Interfaccia utente (browser, app mobile, ecc.).
    
2. **Middleware** → Logica applicativa (gestione dati, API, sicurezza, ecc.).
    
3. **Back-end** → Gestione delle risorse (database, file system, ecc.).
    

---

## **Evoluzione delle Architetture Web**

1. **Applicazioni Monolitiche (uni-tier)** → Tutti i componenti dell’applicazione sono eseguiti in un unico sistema.
    
2. **Applicazioni Two-Tier:**
    
    - **Thin client** → Il server elabora la maggior parte dei dati, il client gestisce solo la presentazione.
        
    - **Thick client** → Il client gestisce una parte dell’elaborazione, riducendo il carico sul server.
        
3. **Applicazioni Three-Tier e Multi-Tier (n-tier)** → Separazione tra front-end, middleware e back-end per scalabilità e manutenibilità.
    

---

## **Compiti per casa**

- **Architettura IP/TCP** → Approfondire a pagina 45 del libro di testo.
    
- **Porte logiche (significato e classificazione)** → Vedere pagine 108-109 del testo oppure chiedere a ChatGPT :-)
    

---

## **Architetture fisiche delle Applicazioni di Rete**

1. **Client-Server** → Un server centrale gestisce le richieste provenienti dai client.
    
2. **Peer-to-Peer (P2P):**
    
    - **Centralizzato** → Un server coordina i peer (gestione risorse, registrazione, ecc.).
        
    - **Decentralizzato** → Nessun server centrale, i peer operano autonomamente.
        
    - **Misto** → Peer con ruoli specializzati per migliorare le prestazioni.
        

---

## **Connessione tramite Socket**

### **Domande e Risposte**

1. **Una macchina server non può essere anche client** → **(Falso)**, un dispositivo può eseguire sia processi client che server.
    
2. **Non sono gli host a essere client o server, ma i processi** → **(Vero)**, dipende dal software in esecuzione.
    
3. **Un host può essere contemporaneamente sia client che server** → **(Vero)**, es. un computer può ospitare un sito web e navigare su Internet.
    
4. **Ogni processo server può a sua volta diventare client** → **(Vero, rispetto a un altro processo)**, es. un database server che invia richieste a un altro server.
    
5. **Un servizio è un’entità astratta che viene fornita da uno o più server** → **(Vero, un servizio complesso può essere distribuito su più server per migliorare affidabilità e scalabilità).**