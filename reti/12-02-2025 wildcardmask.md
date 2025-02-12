# Wildcard Mask

## Introduzione

Una wildcard mask viene utilizzata nel networking per specificare un intervallo di indirizzi IP. È comunemente usata nelle liste di controllo degli accessi (ACL) e nei protocolli di routing.

## Wildcard Mask vs Subnet Mask

- **Subnet Mask**: Utilizzata per dividere un indirizzo IP in porzioni di rete e host.
- **Wildcard Mask**: Utilizzata per specificare quali bit di un indirizzo IP devono essere ignorati durante il matching.

## Come Calcolare una Wildcard Mask

Per calcolare una wildcard mask, sottrai la subnet mask da 255.255.255.255.

### Esempio

- **Subnet Mask**: 255.255.255.0
- **Wildcard Mask**: 255.255.255.255 - 255.255.255.0 = 0.0.0.255

## Cosa Cambia da 1 a 0

Nella wildcard mask, un bit impostato a 0 indica che il bit corrispondente nell'indirizzo IP deve essere confrontato esattamente. Un bit impostato a 1 indica che il bit corrispondente nell'indirizzo IP può essere ignorato.

### Esempio di Wildcard Mask

Supponiamo di avere l'indirizzo IP `192.168.1.0` e la wildcard mask `0.0.0.255`.

- Indirizzo IP: `192.168.1.0`
- Wildcard Mask: `0.0.0.255`

La wildcard mask `0.0.0.255` significa che i primi tre ottetti devono essere confrontati esattamente, mentre l'ultimo ottetto può essere ignorato. Quindi, qualsiasi indirizzo IP che inizia con `192.168.1.` sarà considerato una corrispondenza.

Esempi di indirizzi IP che corrispondono:

- `192.168.1.1`
- `192.168.1.50`
- `192.168.1.255`

Esempi di indirizzi IP che non corrispondono:

- `192.168.2.1`
- `192.168.0.1`
- `10.0.0.1`

### Tabella di Esempio

| Indirizzo IP | Wildcard Mask | Risultato del Matching |
|--------------|---------------|------------------------|
| 192.168.1.1  | 0.0.0.0       | Solo 192.168.1.1       |
| 192.168.1.1  | 0.0.0.255     | 192.168.1.x            |
| 192.168.1.1  | 0.0.255.255   | 192.168.x.x            |
| 192.168.1.1  | 0.255.255.255 | 192.x.x.x              |

## Utilizzo nelle ACL

Le wildcard mask sono utilizzate nelle ACL per permettere o negare il traffico basato sugli indirizzi IP.

### Esempio di Voce ACL

```plaintext
access-list 10 permit 192.168.1.0 0.0.0.255
```

Questa voce permette il traffico da qualsiasi indirizzo IP nella rete 192.168.1.0/24.

## Wildcard Mask Comuni

- **0.0.0.0**: Corrisponde a un singolo indirizzo IP.
- **0.0.0.255**: Corrisponde a qualsiasi indirizzo IP nell'intervallo dell'ultimo ottetto (es. 192.168.1.x).
- **0.0.255.255**: Corrisponde a qualsiasi indirizzo IP nell'intervallo degli ultimi due ottetti (es. 192.168.x.x).

## Conclusione

Le wildcard mask sono uno strumento potente nella configurazione di rete, permettendo un controllo flessibile e preciso sul matching degli indirizzi IP.
