

---

## **TEST FINALE OOP - "La Battaglia dei Regni"**

### **Obiettivo**

Realizza un **gioco a turni da terminale** in cui il **giocatore** e una **IA** si sfidano con eserciti medievali. Ogni giocatore ha un **budget** iniziale per acquistare soldati. Gli eserciti combattono in più **round**, e dopo ogni battaglia si ricevono nuove risorse da spendere. Vince chi elimina tutte le unità nemiche.

---

###  **Requisiti strutturali (OOP)**

#### 🔹 **Classe Astratta: `Soldato`**

* Attributi protetti: `_nome`, `_costo`, `_attacco`, `_difesa`, `_salute`
* Metodo astratto: `attacca(avversario)`
* Metodi comuni:

  * `difenditi(danno)`
  * `è_vivo() → bool`
  * `stato() → stampa salute e ruolo`

#### **Classi Derivate:**

Ciascuna classe implementa il metodo `attacca()` con logiche **diverse** (polimorfismo):

1. **Cavaliere**

   * Alto costo, alta difesa, attacco medio
   * 20% di possibilità di **colpo critico** (attacco × 2)

2. **Arciere**

   * Costo medio, attacco alto, bassa difesa
   * Attacca **per primo** in ogni scontro 1v1

3. **Guaritore**

   * Costo medio, bassa difesa e attacco
   * Invece di attaccare, **cura un alleato vivo random**

4. **Mago**

   * Costo alto, attacco variabile (10–40), difesa bassa
   * 25% di chance di **saltare il turno** per stanchezza

---

### **Sistema di gioco**

### **Fase iniziale: Preparazione**

* Ogni giocatore ha un **budget iniziale di 1000 monete**
* Può acquistare soldati scegliendo nome e tipo
* I soldati vanno salvati in una lista `esercito`

#### **Ciclo di gioco: Round**

* Ogni round:

  1. I soldati vivi si scontrano in ordine (es. primo contro primo)
  2. I danni sono calcolati in base agli attacchi e difese
  3. I caduti vengono rimossi dall'esercito
* Alla fine del round:

  * Ogni giocatore riceve **+300 monete**
  * Può **acquistare nuovi soldati**
* Il gioco termina quando **uno dei due eserciti è vuoto**

#### **Vittoria**

Mostrare messaggio finale con:

* Vincitore
* Numero di round giocati
* Numero di soldati rimasti

---

### **Requisiti tecnici obbligatori**

 Uso di `ABC` e `@abstractmethod`
 Incapsulamento corretto (`__attributi` e proprietà dove necessario)
 Override del metodo `attacca()` in ciascuna sottoclasse
 Gestione delle liste e scontri in funzioni
 Interfaccia da **terminale** con menu e input controllati
 Buona **organizzazione del codice**: classi, funzioni, pulizia

---









 Bonus Avanzati (non obbligatori)
 

 1. Abilità Speciali Uniche (Polimorfismo Avanzato)
Aggiungi un metodo astratto usa_abilità_speciale() in Soldato e implementalo in ogni sottoclasse.

Esempi:

Cavaliere: assorbe metà del danno ricevuto per 1 turno

Arciere: attacca tutti i nemici contemporaneamente con danno ridotto

Guaritore: rianima un alleato caduto con metà salute (solo una volta per partita)

Mago: evoca una creatura fantasma (soldato temporaneo con 1 vita, attacco alto)

Puoi permettere una sola attivazione per round o per soldato.

 2. Posizionamento Tattico (Gestione Avanzata della Lista)
Permetti al giocatore di riordinare il proprio esercito prima del combattimento, influenzando l’ordine degli scontri. Es:

1. Sposta un soldato in alto
2. Sposta un soldato in basso
3. Conferma schieramento

Questo introduce la strategia di prima linea / seconda linea, utile per proteggere guaritori o maghi.

 3. Attacchi ad Area e Critici Multipli

Aggiungi un tipo di soldato avanzato:

Catapulta: attacco ad area → colpisce fino a 3 soldati nemici con danno 15 ciascuno

Implementa un loop per far sì che attacca() coinvolga più bersagli

 4. Effetti Status e Turni Persistenti
Implementa effetti di stato:

Avvelenamento: toglie 5 HP per 2 turni

Stordimento: salta il turno successivo

Benedizione: aumenta difesa del 50% per 1 turno


