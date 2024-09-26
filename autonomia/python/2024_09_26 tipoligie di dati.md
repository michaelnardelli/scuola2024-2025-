# Le collezioni


## Le Liste
Una lista è una sequenza di elementi. Ciò che la differenzia da un vettore è che essa può crescere indefinitamente, basta aggiungere elementi. Però di solito non è indicizzata, quindi per trovare un elemento dovete attraversarla dall'inizio alla fine verificando per ogni elemento se si tratta di quello voluto. Python consente anche di usare indici sulle liste. 

Operazioni sulle liste
Python fornisce molte operazioni sulle collezioni. Quasi tutte si applicano alle liste ed un sottoinsieme di esse ad altri tipi di collezione, incluse le stringhe, che sono solo uno speciale tipo di liste di caratteri. Per creare una lista ed accedervi in Python si utilizzano le parentesi quadre. Potete creare una lista vuota usando una coppia di parentesi quadre con niente al loro interno, oppure creare una lista con qualche contenuto separando i valori fra parentesi con le virgole:

>>> unaLista = []
>>> unAltra = [1,2,3]
>>> print unAltra
[1, 2, 3]
Possiamo accedere ai singoli elementi usando un numero di indice, con il primo elemento con indice 0, all'interno delle parentesi quadre:

>>> print unAltra[2]
3
Possiamo anche cambiare i valori degli elementi di una lista in modo simile:

>>> unAltra[2] = 7
>>> print unAltra
[1, 2, 7]
Potete usare indici negativi per accedere agli elementi a partire dal fondo della lista. Il caso più comune è usare -1 per avere l'ultimo elemento:

>>> print unAltra[-1]
7
Possiamo anche aggiungere nuovi elementi al fondo di una lista usando l'operatore append():

>>> unaLista.append(42)
>>> print unaLista
[42]
Possiamo anche inserire una lista all'interno di un'altra, quindi se appendiamo la nostra seconda lista alla prima:

>>> unaLista.append(unAltra)
>>> print unaLista
[42, [1, 2, 7]]
Notate che il risultato è una lista con due elementi, ma il secondo elemento è a sua volta una lista (come si deduce dalle [ ] che la circondano). Questa caratteristica è utile in quanto consente di costruire rappresentazioni di tabelle o griglie usando una lista di liste. Possiamo quindi accedere all'elemento 7 usando un doppio indice:

>>> print unaLista[1][2]
7
Il primo indice, 1, estrae il secondo elemento che è a sua volta una lista. Il secondo indice, 2, estrae il terzo elemento della sottolista.

L'opposto di aggiungere elementi è, ovviamente, rimuoverli. Per farlo usiamo il comando del:

>>> del unaLista[1]
>>> print unaLista
[42]
Se vogliamo unire due liste per ottenerne una possiamo usare lo stesso operatore di concatenazione "+" che abbiamo visto per le stringhe:

>>> nuovaLista = unaLista + unAltra
>>> print nuovaLista
[42, 1, 2, 7]
Allo stesso modo possiamo applicare l'operatore di ripetizione per riempire una lista con molte copie dello stesso valore:

>>> listaZero = [0] * 5
>>> print listaZero
[0, 0, 0, 0, 0]
Infine, possiamo determinare la lunghezza di una lista usando la funzione incorporata len():

>>> print len(unaLista)
2
>>> print len(listaZero)
5

Le Tuple
Non tutti i linguaggi forniscono un costrutto per le tuple, ma in quelli che lo prevedono risulta estremamente utile. Una tupla è in realtà una collezione arbitraria di valori che possono essere trattati come una unità. Una tupla è per molti versi simile ad una lista, ma con l'importante differenza che le tuple sono immutabili ovvero non potete cambiarle, né aggiungere elementi una volta che sono state create. In Python le tuple si rappresentano semplicemente come liste di valori separati da virgola racchiuse fra parentesi tonde, così:

>>> unaTupla = (1,3,5)
>>> print unaTupla[1]    # si usano gli indici come per le liste
3
>> unaTupla[2] = 7       # errore, non si puo` modificare un elemento di una tupla
Traceback (innermost last):
  File "<pyshell >", line 1, in ?# Le collezioni


## Le Liste
Una lista è una sequenza di elementi. Ciò che la differenzia da un vettore è che essa può crescere indefinitamente, basta aggiungere elementi. Però di solito non è indicizzata, quindi per trovare un elemento dovete attraversarla dall'inizio alla fine verificando per ogni elemento se si tratta di quello voluto. Python consente anche di usare indici sulle liste. 

Operazioni sulle liste
Python fornisce molte operazioni sulle collezioni. Quasi tutte si applicano alle liste ed un sottoinsieme di esse ad altri tipi di collezione, incluse le stringhe, che sono solo uno speciale tipo di liste di caratteri. Per creare una lista ed accedervi in Python si utilizzano le parentesi quadre. Potete creare una lista vuota usando una coppia di parentesi quadre con niente al loro interno, oppure creare una lista con qualche contenuto separando i valori fra parentesi con le virgole:

>>> unaLista = []
>>> unAltra = [1,2,3]
>>> print unAltra
[1, 2, 3]
Possiamo accedere ai singoli elementi usando un numero di indice, con il primo elemento con indice 0, all'interno delle parentesi quadre:

>>> print unAltra[2]
3
Possiamo anche cambiare i valori degli elementi di una lista in modo simile:

>>> unAltra[2] = 7
>>> print unAltra
[1, 2, 7]
Potete usare indici negativi per accedere agli elementi a partire dal fondo della lista. Il caso più comune è usare -1 per avere l'ultimo elemento:

>>> print unAltra[-1]
7
Possiamo anche aggiungere nuovi elementi al fondo di una lista usando l'operatore append():

>>> unaLista.append(42)
>>> print unaLista
[42]
Possiamo anche inserire una lista all'interno di un'altra, quindi se appendiamo la nostra seconda lista alla prima:

>>> unaLista.append(unAltra)
>>> print unaLista
[42, [1, 2, 7]]
Notate che il risultato è una lista con due elementi, ma il secondo elemento è a sua volta una lista (come si deduce dalle [ ] che la circondano). Questa caratteristica è utile in quanto consente di costruire rappresentazioni di tabelle o griglie usando una lista di liste. Possiamo quindi accedere all'elemento 7 usando un doppio indice:

>>> print unaLista[1][2]
7
Il primo indice, 1, estrae il secondo elemento che è a sua volta una lista. Il secondo indice, 2, estrae il terzo elemento della sottolista.

L'opposto di aggiungere elementi è, ovviamente, rimuoverli. Per farlo usiamo il comando del:

>>> del unaLista[1]
>>> print unaLista
[42]
Se vogliamo unire due liste per ottenerne una possiamo usare lo stesso operatore di concatenazione "+" che abbiamo visto per le stringhe:

>>> nuovaLista = unaLista + unAltra
>>> print nuovaLista
[42, 1, 2, 7]
Allo stesso modo possiamo applicare l'operatore di ripetizione per riempire una lista con molte copie dello stesso valore:

>>> listaZero = [0] * 5
>>> print listaZero
[0, 0, 0, 0, 0]
Infine, possiamo determinare la lunghezza di una lista usando la funzione incorporata len():

>>> print len(unaLista)
2
>>> print len(listaZero)
5

Le Tuple
Non tutti i linguaggi forniscono un costrutto per le tuple, ma in quelli che lo prevedono risulta estremamente utile. Una tupla è in realtà una collezione arbitraria di valori che possono essere trattati come una unità. Una tupla è per molti versi simile ad una lista, ma con l'importante differenza che le tuple sono immutabili ovvero non potete cambiarle, né aggiungere elementi una volta che sono state create. In Python le tuple si rappresentano semplicemente come liste di valori separati da virgola racchiuse fra parentesi tonde, così:

>>> unaTupla = (1,3,5)
>>> print unaTupla[1]    # si usano gli indici come per le liste
3
>> unaTupla[2] = 7       # errore, non si puo` modificare un elemento di una tupla
Traceback (innermost last):
  File "<pyshell >", line 1, in ?
  	unaTupla[2] = 7
TypeError: object doesn't support item assignment
Gli aspetti principali da ricordare sono che, mentre si usano parentesi tonde per definire la tupla, si usano parentesi quadre per l'indice e che una tupla non può essere modificata una volta creata. A parte questo gran parte delle operazioni su liste sono anche applicabili alle tuple.


Memorie associative o Dizionari
Una memoria associativa, o dizionario, come il nome suggerisce, contiene un valore associato ad una chiave, allo stesso modo in cui un dizionario di parole associa un significato ad una parola. Il valore può essere recuperato per mezzo di un "indice" che costituisce la chiave. Differentemente dai dizionari cartacei la chiave non deve essere necessariamente una stringa di caratteri (anche se spesso lo è) ma può essere un qualunque tipo immutabile, inclusi numeri e tuple. Analogamente i valori associati con le chiavi possono essere qualunque tipo di dato valido per Python. Le memorie associative sono spesso implementate internamente usando una particolare tecnica di programmazione detta tabella hash. Per questo motivo le memorie associative vengono anche dette hash.

Poiché l'accesso ai valori del dizionario avviene tramite la chiave è possibile introdurre solo elementi con chiave univoca. I dizionari sono strutture estremamente utili fornite da Python come tipo di base sebbene in altri linguaggi sia necessario usare un modulo o anche crearli personalmente. Possiamo usare i dizionari in molti modi e vedremo molti esempi nel seguito, ma per ora vediamo come creare un dizionario in Python, come introdurvi valori e come leggerli:

>>> diz = {}
>>> diz['boolean'] = "Valore che puo` essere vero oppure falso"
>>> diz['integer'] = "Numero intero"
>>> print diz['boolean']
Valore che puo` essere vero oppure falso
Notate che si usano le parentesi graffe per creare un dizionario e le parentesi quadre per assegnare e leggere i valori.

A causa della loro struttura interna i dizionari non supportano molti degli operatori sulle collezioni che abbiamo visto fino ad ora. Le operazioni di concatenazione, ripetizione, aggiunta di un elemento non funzionano. Per accedere più facilmente alle chiavi del dizionario possiamo usare la funzione keys(), che riporta una lista contenente tutte le chiavi del dizionario.


Poiché l'accesso ai valori del dizionario avviene tramite la chiave è possibile introdurre solo elementi con chiave univoca. I dizionari sono strutture estremamente utili fornite da Python come tipo di base sebbene in altri linguaggi sia necessario usare un modulo o anche crearli personalmente. Possiamo usare i dizionari in molti modi e vedremo molti esempi nel seguito, ma per ora vediamo come creare un dizionario in Python, come introdurvi valori e come leggerli:

>>> diz = {}
>>> diz['boolean'] = "Valore che puo` essere vero oppure falso"
>>> diz['integer'] = "Numero intero"
>>> print diz['boolean']
Valore che puo` essere vero oppure falso
Notate che si usano le parentesi graffe per creare un dizionario e le parentesi quadre per assegnare e leggere i valori.

A causa della loro struttura interna i dizionari non supportano molti degli operatori sulle collezioni che abbiamo visto fino ad ora. Le operazioni di concatenazione, ripetizione, aggiunta di un elemento non funzionano. Per accedere più facilmente alle chiavi del dizionario possiamo usare la funzione keys(), che riporta una lista contenente tutte le chiavi del dizionario.

