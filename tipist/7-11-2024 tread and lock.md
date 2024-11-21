### Appunti TPSIT 5CI 2024-2025

---

### Argomenti di Laboratorio

#### Introduzione ai Thread in Java

- **Lezione: Concorrenza - Java Tutorials**
- **Definizione di Thread**: Un thread è la più piccola sequenza di istruzioni programmabili che può essere gestita indipendentemente dallo scheduler.
- **All'interno dei Processi**: I thread esistono all'interno dei processi; ogni processo ha almeno un thread principale (il main thread).
- **Risorse Condivise**: I thread dello stesso processo condividono lo spazio di memoria e le risorse, facilitando la comunicazione, ma richiedono meccanismi di sincronizzazione per evitare problemi come le "race conditions".

#### Differenze tra Processo e Thread

| Aspetto           | Processo                                  | Thread                                               |
|-------------------|-------------------------------------------|------------------------------------------------------|
| **Definizione**   | Istanza esecutiva di un programma         | Unità di esecuzione all'interno di un processo       |
| **Spazio di Memoria** | Possiede uno spazio di memoria separato  | Condivide lo spazio di memoria con altri thread       |
| **Comunicazione** | Richiede meccanismi di comunicazione inter-processo (IPC) | Comunica direttamente all'interno del processo       |
| **Overhead**      | Più elevato da creare e gestire           | Più leggero, cambio di contesto più veloce           |
| **Isolamento**    | Processi sono isolati tra loro           | I thread non sono isolati                            |

#### Concorrenza e Parallelismo

- **Concorrenza con i Processi**
  - **Processi Concorrenti**: Molteplici processi possono essere in esecuzione simultanea, gestiti dallo scheduler del sistema operativo.
  - **Comunicazione Inter-processo (IPC)**: Usata per la comunicazione tra processi, tramite meccanismi come pipe, socket, memoria condivisa, e messaggi.

- **Parallelismo con i Processi**
  - Su sistemi con più CPU o core, i processi possono essere eseguiti in parallelo, migliorando le prestazioni.

- **Thread all'interno dei Processi**
  - **Concorrenza con i Thread**: I thread consentono l'esecuzione concorrente all'interno di un singolo processo, con minore overhead rispetto ai processi.
  - **Parallelismo con i Thread**: Su sistemi multi-core, i thread possono effettivamente essere eseguiti in parallelo.

- **Esempi in Java**
  - **Programma Java**: Una collezione di file `.java` che viene compilata in bytecode `.class`.
  - **Processo Java**: Eseguito tramite la JVM (Java Virtual Machine).
  - **Creazione di Thread in Java**: I thread addizionali possono essere creati usando la classe `Thread` o le API di concorrenza.

- **Creazione di un Nuovo Processo in Java**:
  - Java può creare nuovi processi usando `ProcessBuilder` o `Runtime.exec()`.

  ```java
  public class ProcessDemo {
      public static void main(String[] args) {
          try {
              Process process = new ProcessBuilder("notepad.exe").start();
          } catch (IOException e) {
              e.printStackTrace();
          }
      }
  }
  ```

#### Gestione dei Processi nei Sistemi Operativi

- **Responsabilità del Sistema Operativo (OS)**
  - **Scheduling dei Processi**: Decidere quale processo eseguire in ogni momento.
  - **Allocazione delle Risorse**: Gestione del tempo CPU, memoria, e dispositivi I/O tra i processi.
  - **Isolamento dei Processi**: Assicurare che i processi non interferiscano nella memoria altrui.
  - **Comunicazione Inter-processo**: Fornire meccanismi per la comunicazione tra processi.

- **Stati di un Processo**:
  - **Nuovo**: Il processo è in fase di creazione.
  - **Pronto**: Il processo è pronto per essere eseguito, ma attende il tempo CPU.
  - **Esecuzione**: Il processo è attualmente in esecuzione.
  - **Bloccato**: Il processo attende un evento esterno (es. completamento di I/O).
  - **Terminato**: Il processo ha completato l’esecuzione.

#### Stati di un Thread in Java

1. **NEW**: Il thread è stato creato ma non ancora avviato.
2. **RUNNABLE**: Il thread è in esecuzione o pronto per essere eseguito.
3. **BLOCKED**: Il thread è in attesa di acquisire un lock.
4. **WAITING**: Il thread attende indefinitamente un’azione di un altro thread.
5. **TIMED_WAITING**: Il thread attende per un periodo specifico.
6. **TERMINATED**: Il thread ha completato la sua esecuzione.

#### Transizioni di Stato dei Thread

- **NEW → RUNNABLE**: Quando si chiama `start()` su un nuovo thread.
- **RUNNABLE → BLOCKED**: Quando un thread tenta di acquisire un lock già in uso.
- **RUNNABLE → WAITING**: Quando un thread chiama `wait()` o `join()` senza timeout.
- **RUNNABLE → TERMINATED**: Quando il metodo `run()` completa.

#### Esempio Pratico: Blocco su un Lock

```java
public class BlockingExample {
    private final Object lock = new Object();

    public void firstThread() {
        synchronized (lock) {
            try {
                System.out.println("Primo thread in possesso del lock.");
                Thread.sleep(5000); // Simulazione lavoro
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void secondThread() {
        synchronized (lock) {
            System.out.println("Secondo thread ha acquisito il lock.");
        }
    }

    public static void main(String[] args) {
        BlockingExample example = new BlockingExample();
        Thread t1 = new Thread(example::firstThread);
        Thread t2 = new Thread(example::secondThread);

        t1.start();
        try { Thread.sleep(100); } catch (InterruptedException e) {}
        t2.start();
    }
}
```

#### Multithreading in Java

- **Il Keyword Synchronized**: Utilizzato per assicurare che solo un thread alla volta possa eseguire un blocco di codice sincronizzato.

---

### Registro delle Lezioni

- **20 Settembre 2024**: Introduzione ai Thread in Java, definizione e avvio dei thread.
- **27 Settembre 2024**: Stati dei Thread in Java.
- **4 Ottobre 2024**: Concorrenza vs. Parallelismo, esercizi assegnati su `synchronized`.
- **11 Ottobre 2024**: Prenotazione di biglietti online usando i locks.
- **18 Ottobre 2024**: Thread Pool e sistema bancario con lock multipli.
- **25 Ottobre 2024**: Esempi con `ReentrantLock`, elaborazione immagini usando Thread Pool.
- **8 Novembre 2024**: Multithreading per processare immagini, assegnazione esercizi.
- **15 Novembre 2024**: Test sugli argomenti: Sockets Java e Servizi REST.
