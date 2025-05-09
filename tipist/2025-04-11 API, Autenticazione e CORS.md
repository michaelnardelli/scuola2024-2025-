# API, Autenticazione e CORS: Riassunto degli Schemi Architetturali
*(Gestione delle Richieste Cross-Origin tra Frontend e API Esterne)*  

---

### **Problema Centrale: Politica della Stessa Origine (SOP)**  
- **Definizione**: Meccanismo di sicurezza del browser che blocca le richieste cross-origin (es. `domain-a.com` → `domain-b.com`).  
- **Soluzioni**: Due schemi architetturali per aggirare le restrizioni SOP:  

---

### **Schema 1: Proxy Lato Server**  
**Architettura**:  
```
Browser (domain-a.com) → Proxy Server (domain-a.com/api/proxy) → API Esterna (domain-b.com)
```  
**Caratteristiche Principali**:  
- **Sicurezza**: Chiavi segrete (API key, token) gestite lato server, evitando esposizione client-side.  
- **Bypass CORS**: Nessuna dipendenza dalla configurazione CORS dell'API esterna.  
- **Controllo**: Abilita caching, rate limiting, logging e trasformazione dei dati.  

**Vantaggi**:  
✅ Sicurezza migliorata (nessun segreto lato client).  
✅ Compatibile con API prive di supporto CORS.  
✅ Controllo centralizzato su richieste/risposte.  
✅ Whitelisting degli IP (solo l'IP del proxy).  

**Svantaggi**:  
⚠️ Latenza aumentata (passaggio aggiuntivo in rete).  
⚠️ Sovraccarico infrastrutturale (configurazione/manutenzione del proxy).  
⚠️ Rischio di colli di bottiglia sul server.  

**Casi d’Uso**:  
- API che richiedono credenziali segrete.  
- API legacy o di terze parti senza CORS.  
- Necessità di aggregazione, caching o trasformazione dei dati.  

---

### **Schema 2: Richieste Dirette Lato Client (CORS)**  
**Architettura**:  
```
Browser (domain-a.com) → API Esterna (domain-b.com)
```  
**Caratteristiche Principali**:  
- **Header CORS**: L'API esterna deve includere header come `Access-Control-Allow-Origin`.  
- **Richieste Preflight**: Necessarie per richieste "non semplici" (es. PUT, header personalizzati).  

**Vantaggi**:  
✅ Latenza ridotta (comunicazione diretta).  
✅ Infrastruttura semplificata (nessun proxy).  
✅ Conformità agli standard (utilizza CORS).  

**Svantaggi**:  
⚠️ Rischi di sicurezza (gestione token lato client).  
⚠️ Dipendenza dalla configurazione CORS dell'API esterna.  
⚠️ Nessun controllo su richieste/risposte (mancanza di caching/aggregazione).  

**Casi d’Uso**:  
- API pubbliche progettate per browser.  
- API sotto lo stesso controllo organizzativo.  
- Requisiti di bassa latenza (es. app in tempo reale).  

---

### **Spiegazione del Preflight CORS**  
**Attivazione**: Per richieste "non semplici" (es. `PUT`, `DELETE`, header personalizzati, credenziali).  
**Flusso**:  
1. **Preflight (OPTIONS)**: Il browser verifica se l'API consente:  
   - `Origin`, `Access-Control-Request-Method`, `Access-Control-Request-Headers`.  
2. **Risposta API**: Deve includere:  
   - `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`.  
3. **Esito**:  
   - **Consentito**: Procede con la richiesta effettiva.  
   - **Bloccato**: Errore CORS in caso di header non corretti.  

---

### **Tabella di Confronto**  
| Caratteristica          | Proxy Lato Server              | CORS Diretto                   |  
|-------------------------|---------------------------------|--------------------------------|  
| **Sicurezza**           | Alta (segreti lato server)     | Inferiore (token lato client) |  
| **Latenza**             | Maggiore (passaggio proxy)     | Minore (diretto)               |  
| **Infrastruttura**      | Complessa (richiede proxy)     | Semplice                       |  
| **Dipendenze CORS**     | Nessuna                        | Critiche (API deve supportare) |  
| **Controllo**           | Completo (trasformazione/cache)| Limitato (dipende dall'API)    |  

---

### **Conclusione: Trade-Off Principali**  
- **Proxy**: Scelto per sicurezza, controllo o API incompatibili con CORS.  
- **CORS Diretto**: Ideale per semplicità, velocità e API pubbliche/controllate.  
- **Autenticazione Moderna**: Protocolli come OAuth 2.0/OIDC spesso abbinati a CORS per gestione sicura dei token lato client.  

*Utilizza diagrammi per visualizzare i flussi: il proxy aggiunge un layer intermedio, mentre il CORS si basa su header preflight/risposta.*