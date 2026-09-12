# Confronti

[Catalogo dei pattern](README.it.md)

Strutture simili possono risolvere problemi diversi. Scegli in base a intento, variazione e responsibility.


## Strategy ↔ State

### Problema centrale

Entrambi delegano, ma Strategy sceglie algorithm e State gestisce risposte del lifetime.

### Differenza strutturale

Strategy viene solitamente fornita dal client; uno State può avviare una transizione dopo un event.

### Uso comune

Tariffe di spedizione con Strategy; porta aperta, chiusa o bloccata con State.

### Regola di scelta

Una politica scelta suggerisce Strategy; un event che cambia fase suggerisce State.

### Piccolo esempio di design

Checkout → ShippingRule scelta; Door → DoorState corrente → successivo.

[Strategy](behavioral/strategy/README.it.md) · [State](behavioral/state/README.it.md)

### Da ricordare

Strategy sceglie come agire; State lega il behavior alla fase corrente.

## Adapter ↔ Facade

### Problema centrale

Adapter risolve incompatibilità; Facade semplifica l'uso di un subsystem.

### Differenza strutturale

Adapter implementa il contratto atteso intorno a un'API; Facade offre un flusso ridotto sopra più servizi.

### Uso comune

Conversione Fahrenheit/Celsius con Adapter; checkout fra stock, pagamento e spedizione con Facade.

### Regola di scelta

Compatibilità specifica: Adapter. Ingresso più semplice: Facade, che può usare adattatori internamente.

### Piccolo esempio di design

Temperature ← CelsiusAdapter → LegacyThermometer; Client → Checkout → servizi.

[Adapter](structural/adapter/README.it.md) · [Facade](structural/facade/README.it.md)

### Da ricordare

Adapter traduce un contratto; Facade semplifica un flusso.

## Decorator ↔ Proxy

### Problema centrale

Decorator aggiunge responsibility; Proxy controlla l'accesso.

### Differenza strutturale

Entrambi possono implementare la stessa interface e delegare: l'intento distingue meglio della forma.

### Uso comune

Prezzo del latte o compressione con Decorator; caricamento differito e controlli con Proxy.

### Regola di scelta

Il wrapper aggiunge capacità facoltative o governa l'accesso? Può anche fare entrambe le cose.

### Piccolo esempio di design

Milk(Drink) aggiunge prezzo; LazyImage decide quando creare DiskImage.

[Decorator](structural/decorator/README.it.md) · [Proxy](structural/proxy/README.it.md)

### Da ricordare

Decorator aggiunge capacità; Proxy regola l’accesso.

## Factory Method ↔ Abstract Factory

### Problema centrale

Factory Method varia un passo di creazione; Abstract Factory fornisce una famiglia coerente di tipi diversi.

### Differenza strutturale

Il primo è un'operazione ridefinibile nel flusso del creatore; il secondo espone più operazioni per prodotti correlati.

### Uso comune

Sender in AlertJob con Factory Method; Button e Panel coordinati con Abstract Factory.

### Regola di scelta

Un punto di creazione nel flusso suggerisce Factory Method; una famiglia intercambiabile suggerisce Abstract Factory.

### Piccolo esempio di design

AlertJob::run → make_sender(); render → Theme.button() + Theme.panel().

[Factory Method](creational/factory-method/README.it.md) · [Abstract Factory](creational/abstract-factory/README.it.md)

### Da ricordare

Factory Method varia un passo di creazione; Abstract Factory fornisce una famiglia coerente.

## Builder ↔ Factory Method

### Problema centrale

Builder gestisce configurazioni complesse; Factory Method sceglie il prodotto concreto del flusso.

### Differenza strutturale

Builder raccoglie state in chiamate esplicite; Factory Method seleziona tramite override.

### Uso comune

Configura timeout e retry di una richiesta, oppure scegli il sender di un job comune.

### Regola di scelta

Molte scelte costruttive suggeriscono Builder; scelta tramite subclass suggerisce Factory Method. Un constructor semplice non richiede nessuno dei due.

### Piccolo esempio di design

RequestBuilder.endpoint(...).timeout(...).build(); EmailJob ridefinisce make_sender().

[Builder](creational/builder/README.it.md) · [Factory Method](creational/factory-method/README.it.md)

### Da ricordare

Builder configura per passi; Factory Method lascia scegliere il prodotto alla subclass.

## Observer ↔ Mediator

### Problema centrale

Observer distribuisce notifiche; Mediator organizza interazioni fra colleghi.

### Differenza strutturale

Observer gestisce iscrizioni senza codificare ogni flusso; Mediator conosce regole e ruoli specifici.

### Uso comune

Diffondi variazioni di stock alle viste; coordina campi e pulsante di invio.

### Regola di scelta

Reazioni indipendenti suggeriscono Observer; regole fra pari suggeriscono Mediator, che può ricevere notifiche Observer.

### Piccolo esempio di design

Stock → listener; Field → LoginForm → Button.

[Observer](behavioral/observer/README.it.md) · [Mediator](behavioral/mediator/README.it.md)

### Da ricordare

Observer annuncia un cambiamento; Mediator coordina un’interazione.

## Template Method ↔ Strategy

### Problema centrale

Entrambi riusano un flusso variando il behavior, ma collocano la variazione diversamente.

### Differenza strutturale

Template Method richiama hook della subclass; Strategy delega a un collaboratore o callable fornito.

### Uso comune

Ordine del report tramite hook; tariffa di spedizione tramite callable.

### Regola di scelta

Scegli Template Method per un protocollo ereditato stabile; Strategy per behavior indipendente dal tipo del contesto.

### Piccolo esempio di design

Report::generate → virtual format(); Checkout::total → ShippingRule.

[Template Method](behavioral/template-method/README.it.md) · [Strategy](behavioral/strategy/README.it.md)

### Da ricordare

Template Method eredita la sequenza; Strategy riceve il behavior.

## Composite ↔ Decorator

### Problema centrale

Composite rappresenta parte-tutto; Decorator aggiunge behavior a un componente.

### Differenza strutturale

Composite possiede generalmente più figli e aggrega; Decorator avvolge un componente e arricchisce la delega.

### Uso comune

Somma dimensioni di cartelle con Composite; aggiungi latte a Drink con Decorator.

### Regola di scelta

Un gruppo che agisce come foglia suggerisce Composite; strati facoltativi suggeriscono Decorator, che può avvolgere anche un Composite.

### Piccolo esempio di design

Folder[File, Folder[File]]; Milk(Milk(Coffee)).

[Composite](structural/composite/README.it.md) · [Decorator](structural/decorator/README.it.md)

### Da ricordare

Composite raggruppa figli; Decorator avvolge un componente.
