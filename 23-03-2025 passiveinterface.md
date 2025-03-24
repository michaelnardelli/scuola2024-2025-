# Autenticazione e Interfacce Passive in OSPF

---

**Collegamenti al documento completo**:  

- [Capitolo 1: Aree OSPF e Summarization](./10-03-2025%20ospf.md)
- [Capitolo 2:LSA](./17-03-2024%20lsa.md.md)  

## Autenticazione in OSPF  

L'autenticazione in OSPF garantisce che solo router autorizzati possano partecipare al dominio di routing, prevenendo l'ingresso di dispositivi non legittimi.  

### Tipologie di Autenticazione  

1. **Autenticazione con Password Semplice (Nulla)**  
   - **Funzionamento**: Una password condivisa viene inviata **in chiaro** nei pacchetti OSPF.  
   - **Vulnerabilità**: Facilmente intercettabile, adatta solo a reti isolate o testing.  

2. **Autenticazione con Hash (Message Digest)**  
   - **Funzionamento**: Utilizza algoritmi come MD5 o SHA per generare un hash della password.  
   - **Sicurezza**:  
     - La password non è trasmessa direttamente.  
     - MD5 è ancora supportato ma considerato obsoleto; preferire SHA (es. SHA-256) se disponibile.  
   - **Autenticazione per Area vs. Interfaccia**:  
     - **A livello di area**: Tutti i router nell'area devono condividere la stessa configurazione.  
     - **A livello di interfaccia**: Configurazione specifica per singola interfaccia.  

---

### Configurazione dell'Autenticazione  

#### Autenticazione MD5 per Area 0  

```bash
router ospf 1
 area 0 authentication message-digest  # Abilita autenticazione MD5 per l'area 0
!
interface GigabitEthernet0/0
 ip ospf message-digest-key 1 md5 Cisco123  # Configura la chiave MD5 sull'interfaccia
```

#### Autenticazione SHA (esempio su Cisco IOS XR)  

```bash
router ospf 1
 area 0 authentication sha256
!
interface GigabitEthernet0/0
 ospf authentication sha256 key-string Cisco123
```

**Note Importanti**:  

- Le chiavi di autenticazione devono corrispondere tra router adiacenti.  
- È possibile configurare più chiavi per facilitare il rollover.  

---

## Interfacce Passive in OSPF  

Le interfacce passive non inviano pacchetti OSPF Hello, impedendo la formazione di adiacenze su interfacce non necessarie (es. quelle collegate a LAN utente).  

### Vantaggi  

- **Riduzione del traffico**: Elimina pacchetti Hello non necessari.  
- **Sicurezza**: Previene attacchi tramite interfacce esposte (es. interfacce verso Internet).  
- **Ottimizzazione delle risorse**: Le reti connesse a interfacce passive sono comunque annunciate in OSPF.  

---

### Configurazione  

#### Impostazione Predefinita su Tutte le Interfacce  

```bash
router ospf 1
 passive-interface default  # Tutte le interfacce sono passive
 no passive-interface GigabitEthernet0/1  # Attiva OSPF solo su Gig0/1
```

#### Configurazione Manuale per Singola Interfaccia  

```bash
router ospf 1
 passive-interface GigabitEthernet0/2  # Disabilita OSPF su Gig0/2
```

**Effetti sulle Route**:  

- Le interfacce passive **non inviano Hello** ma le relative subnet sono incluse nei LSA (annunciate ai vicini).  

---

## Considerazioni di Sicurezza e Best Practice  

1. **Priorità all'Autenticazione con Hash**:  
   - Evitare l'autenticazione con password semplice in reti pubbliche o non trusted.  
   - Utilizzare algoritmi moderni (SHA-256/512) dove supportati.  

2. **Gestione delle Chiavi**:  
   - Cambiare periodicamente le chiavi e utilizzare più chiavi per transizioni senza downtime.  

3. **Interfacce Passive**:  
   - Applicare `passive-interface default` su router edge o in reti con molte interfacce non OSPF.  
   - Verificare con `show ip ospf interface brief` quali interfacce sono attive/passive.  

---

## Esempio Completo di Configurazione  

```bash
! Abilita autenticazione MD5 nell'Area 0
router ospf 1
 area 0 authentication message-digest
 passive-interface default
 no passive-interface GigabitEthernet0/1
!
! Configura la chiave MD5 sulle interfacce attive
interface GigabitEthernet0/1
 ip ospf message-digest-key 1 md5 SecurePass123
!
interface GigabitEthernet0/2
 description Collegamento a LAN utente
 ip ospf passive-interface  # Alternativa per impostare l'interfaccia come passiva
```

---

## Verifica della Configurazione  

1. **Controllo Autenticazione**:  

   ```bash
   show ip ospf interface GigabitEthernet0/1  # Verifica "Message Digest authentication"
   ```

2. **Stato Interfacce Passive**:  

   ```bash
   show ip ospf interface | include Passive  # Mostra interfacce passive
   ```

3. **Debug Autenticazione**:  

   ```bash
   debug ip ospf adj  # Monitora errori di autenticazione durante l'adjacency
   ```

---

**Conclusioni**: L'integrazione di autenticazione robusta e interfacce passive ottimizza sicurezza e prestazioni in reti OSPF, bilanciando protezione ed efficienza.
