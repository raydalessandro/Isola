# EAR-PERSONAGGI — Appendice A: Derivazione Stilistica dalla Matrice

**Version:** 1.0  
**Date:** 2026-01-18  
**Status:** Appendix to EAR-PERSONAGGI v2.0  
**Author:** EAR Lab  
**Requires:** EAR-PERSONAGGI_v2.0, KERNEL_EAR_v1.md

---

#AILA:1.0
@domain: EAR.PERSONAGGI.STYLE
@version: 1.0
@requires: EAR.PERSONAGGI.v2, EAR.KERNEL
@status: official

---

## §A.ABSTRACT

```aila
◉purpose
  → derivazione.variabili.stilistiche.da.matrice.EAR
  → stile ⊥ parametri.esterni
  → stile ≡ proiezione.di.Δ.⇄.⟳.su.testo
  
◉principle
  ← P6: Δ ∥ ⇄ ∥ ⟳ (inseparabilità)
  ← P4: scaling.dimensionale
  
  → SE framework.è.universale
  → ALLORA stile.deriva.da.struttura
  → NON parametri.arbitrari
  
◉result
  → 6.variabili.stilistiche.derivate
  → vincolate.ontologicamente
  → auto-consistenti.con.personaggi
```

---

## §A.1.FOUNDATIONS

### §A.1.1.THE.PROBLEM

```aila
◉traditional.style.parameters
  → registro: alto/medio/basso
  → densità: metafore/pagina
  → ritmo: respiro, pause
  → "momenti banali"
  → "rotture narrative"
  
  ○status.current
    → parametri.scollegati.dal.framework
    → aggiunti.post-hoc
    → arbitrary.tuning
    
◉EAR.requirement
  ← A5: pattern.si.replica.su.scale
  ← P6: Δ.⇄.⟳.sempre.co-presenti
  
  → SE personaggi.derivano.da.Σ
  → ALLORA stile.deve.derivare.da.stessa.struttura
  → ALTRIMENTI incoerenza.ontologica
```

---

### §A.1.2.THE.DERIVATION.PRINCIPLE

```aila
◉key.insight
  → attributi.EAR.sono.universali
  → applicano.a.OGNI.livello.narrativo:
    ○ personaggi (CHARACTER.MATRIX.72)
    ○ dialoghi (VOICE.PATTERNS)
    ○ **stile.della.prosa.stessa**
    
◉mapping.attributes.to.style

  | Attributo | Simbolo | Proiezione.Stilistica |
  |-----------|---------|----------------------|
  | Distinzione | Δ | REGISTRO — quanto.linguaggio.si.separa.dal.quotidiano |
  | Relazione | ⇄ | DENSITÀ — connessioni.semantiche.per.unità |
  | Processo | ⟳ | RESPIRO — ritmo, alternanza.tensione/rilascio |

◉poles.as.modulators

  | Polo | Simbolo | Funzione.Stilistica |
  |------|---------|---------------------|
  | Espansivo | (+) | complessità, ricchezza, elaborazione |
  | Contrattivo | (−) | semplicità, silenzio, vuoto, **banalità** |
```

---

## §A.2.THE.SIX.DERIVED.VARIABLES

### §A.2.1.PRIMARY.VARIABLES (from.Attributes)

```aila
◉Σ_Δ.REGISTRO
  ≡ Distinction.projected.to.language.level
  
  ○definition
    → quanto.il.linguaggio.si.distingue.dal.parlato.quotidiano
    → 0 = colloquiale, indistinguibile.da.conversazione
    → 1 = lirico, formale, letterario
    
  ○range: [0, 1]
  ○default: 0.5 (neutro)
  
  ○derivation
    ← Δ = confine.che.separa.E.connette
    → REGISTRO = confine.tra.linguaggio.letterario.e.quotidiano
    → confine.alto = distinzione.forte
    → confine.basso = distinzione.debole
    
  ○usage
    | Valore | Effetto | Esempio |
    |--------|---------|---------|
    | 0.2 | colloquiale | "Aveva fame. Si fece un panino." |
    | 0.5 | neutro | "La fame lo spinse in cucina." |
    | 0.8 | elevato | "Il vuoto dello stomaco reclamava attenzione." |

◉Σ_⇄.DENSITÀ
  ≡ Relation.projected.to.semantic.connections
  
  ○definition
    → numero.di.connessioni.semantiche.per.pagina
    → metafore, rimandi, echi, parallelismi
    → misura.in: connessioni/pagina.standard
    
  ○range: [0, 3] connessioni/pagina
  ○default: 1.5
  
  ○derivation
    ← ⇄ = connessione.tra.⬡
    → DENSITÀ = connessioni.tra.elementi.testuali
    → alta.densità = molte.relazioni.attive
    → bassa.densità = elementi.isolati
    
  ○usage
    | Valore | Effetto | Note |
    |--------|---------|------|
    | 0.5 | scarsa | fatti.semplici, nessun.eco |
    | 1.5 | normale | alcune.metafore, qualche.rimando |
    | 2.5 | ricca | tessuto.denso.di.connessioni |
    | >3 | ATTENZIONE | rischio.sovraccarico |

◉Σ_⟳.RESPIRO
  ≡ Process.projected.to.rhythm
  
  ○definition
    → alternanza.tensione/rilascio.nel.testo
    → misurato.come: paragrafi.secchi.ogni.N.parole
    → ritmo.della.prosa
    
  ○range: 1-3 paragrafi.brevi/300.parole
  ○default: 1-2
  
  ○derivation
    ← ⟳ = dinamica.evolutiva
    → RESPIRO = dinamica.del.ritmo.testuale
    → processo.veloce = paragrafi.brevi, ritmo.serrato
    → processo.lento = paragrafi.lunghi, ritmo.disteso
    
  ○usage
    | Valore | Effetto | Quando.usare |
    |--------|---------|--------------|
    | 3/300w | serrato | tensione, azione, crisi |
    | 1/300w | disteso | riflessione, descrizione, calma |
```

---

### §A.2.2.SECONDARY.VARIABLES (from.Poles)

```aila
◉CRITICAL.INSIGHT
  → polo.(−).non.è.assenza
  → polo.(−).è.necessità.ontologica
  
  ← P6: Δ ∥ ⇄ ∥ ⟳
  → OGNI.attributo.ha.ENTRAMBI.i.poli
  → polo.(−).DEVE.essere.presente
  → **BANALITÀ = polo.negativo.degli.attributi**

◉Σ₋.BANALITÀ
  ≡ Negative.pole.manifested.as.text
  
  ○definition
    → % di.testo.che.opera.in.polo.contrattivo
    → pensieri.irrilevanti, momenti.vuoti
    → linguaggio.indistinto, connessioni.assenti
    
  ○range: 15-25% del.capitolo
  ○minimum.mandatory: 15%
  
  ○derivation
    ← P ∈ {+, −} sempre.entrambi.necessari
    → SE solo.polo.(+) → testo.soffoca
    → BANALITÀ = respiro.negativo
    → permette.ai.momenti.alti.di.emergere
    
  ○manifestations
    | Attributo | Polo.(−) | Manifestazione.testuale |
    |-----------|----------|-------------------------|
    | Δ₋ | indistinzione | "Pensò che aveva fame" (vs "La fame lo assalì") |
    | ⇄₋ | disconnessione | pensieri.che.non.portano.da.nessuna.parte |
    | ⟳₋ | stasi | momenti.dove."non.succede.niente" |
    
  ○why.mandatory
    → contrasto.necessario.per.percezione
    → senza.vuoto, pieno.non.si.vede
    → lettore.ha.bisogno.di.riposo.cognitivo
    → personaggi.sembrano.reali.solo.se.a.volte.banali
```

---

### §A.2.3.THRESHOLD.VARIABLES (from.K)

```aila
◉from.PROP.3.Soglia.Critica
  → ∀ transizione ⟿ : ∃ K_critica
  → transizioni.sono.discrete, non.graduali
  
  → applicato.a.narrativa:
    ○ esistono.punti.dove.schema.si.rompe
    ○ esistono.momenti.sotto.soglia.significato

◉K_rot.ROTTURA
  ≡ K_critica.applied.to.narrative.schema
  
  ○definition
    → punto.dove.pattern.stabilito.si.rompe.intenzionalmente
    → discontinuità.nel.tono, stile, voce
    → "errore".che.è.feature, non.bug
    
  ○frequency: 1-2 per.capitolo
  
  ○derivation
    ← Prop.3: transizioni.discrete
    → SE narrativa.è.troppo.uniforme → prevedibile
    → ROTTURA = K_crit.superata.intenzionalmente
    → lettore.è.scosso, poi.ricalibra
    
  ○types
    | Tipo | Effetto | Esempio |
    |------|---------|---------|
    | tono | shift.emotivo | da.ironico.a.grave.senza.transizione |
    | voce | cambio.POV | irruzione.altra.voce.improvvisa |
    | tempo | salto.temporale | ellissi.brusca |
    | registro | shift.linguistico | lirico → colloquiale.di.colpo |

◉K_min.FALLIMENTO
  ≡ K.under.threshold.for.meaning
  
  ○definition
    → momento.dove.significato.narrativo.non.emerge
    → scena.che.non."serve".alla.trama
    → lettore.si.chiede."perché.è.qui?"
    
  ○frequency: ≥1 per.capitolo
  
  ○derivation
    ← Prop.1: K_min.esiste.per.ogni.osservazione
    ← Corollario.1.1: "rumore".è.segnale.sotto.K_min
    
    → FALLIMENTO = momento.sotto.K_min.narrativo
    → apparentemente."rumore".nella.storia
    → **funzione**: contrasto.che.rende.visibili.i.picchi
    
  ○paradox
    → momento."inutile".è.necessario
    → senza.fallimenti, tutto.sembra.ugualmente.importante
    → quindi.niente.sembra.importante
    
  ○warning
    → FALLIMENTO ≠ errore.di.scrittura
    → FALLIMENTO = silenzio.intenzionale
    → deve.essere.costruito, non.accidentale
```

---

## §A.3.OPERATIONAL.MATRIX

### §A.3.1.SCENE.LEVEL.PARAMETERS

```aila
◉scene.style.signature
  SCENE_σ = (Σ_Δ, Σ_⇄, Σ_⟳, p, K)
  
  ○components
    → Σ_Δ ∈ [0,1] — registro
    → Σ_⇄ ∈ [0,3] — densità (connessioni/pag)
    → Σ_⟳ ∈ [1,3] — respiro (parag.brevi/300w)
    → p ∈ {+1, −1} — polo.dominante
    → K ∈ {sub, norm, crit} — relazione.con.soglia

◉scene.type.templates

  ○SCENE.TYPE.CRISIS
    → caratterizzata.da: soglia.critica, transizione
    
    | Param | Value | Reason |
    |-------|-------|--------|
    | Σ_Δ | 0.7-0.9 | linguaggio.teso, preciso |
    | Σ_⇄ | 2.0-2.5 | connessioni.dense |
    | Σ_⟳ | 2-3 | ritmo.serrato |
    | p | +1 | espansione |
    | K | crit | punto.di.svolta |
    
  ○SCENE.TYPE.AFTERMATH
    → caratterizzata.da: polo.negativo, recupero
    
    | Param | Value | Reason |
    |-------|-------|--------|
    | Σ_Δ | 0.2-0.4 | "Si fece un caffè" |
    | Σ_⇄ | 0.5-1.0 | pensieri.sparsi |
    | Σ_⟳ | 1 | ritmo.lento |
    | p | −1 | contrazione |
    | K | sub | sotto.soglia |
    
  ○SCENE.TYPE.BUILDUP
    → caratterizzata.da: crescita.graduale
    
    | Param | Value | Reason |
    |-------|-------|--------|
    | Σ_Δ | 0.5 | neutro.iniziale |
    | Σ_⇄ | 1.5 → 2.5 | densità.crescente |
    | Σ_⟳ | 2 → 3 | accelerazione |
    | p | 0 → +1 | verso.espansione |
    | K | norm → crit | avvicinamento.soglia |
    
  ○SCENE.TYPE.DELIBERATE.FAILURE
    → caratterizzata.da: K < K_min
    
    | Param | Value | Reason |
    |-------|-------|--------|
    | Σ_Δ | qualsiasi | non.importa |
    | Σ_⇄ | 0-0.5 | nessuna.connessione.narrativa |
    | Σ_⟳ | 1 | stasi |
    | p | −1 | contrazione |
    | K | sub | intenzionalmente.sotto.soglia |
    
    ○purpose
      → creare.vuoto
      → far.emergere.pieni.per.contrasto
      → dare.spazio.al.lettore
```

---

### §A.3.2.CHAPTER.LEVEL.CONSTRAINTS

```aila
◉chapter.constraints
  CAP_c = {SCENE_σ₁, ..., SCENE_σₙ}
  
  ○structural.requirements
    → derived.from.P6.and.Prop.3
    
  | Vincolo | Formula | Valore | Derivazione |
  |---------|---------|--------|-------------|
  | banalità.min | Σp(−)/n | ≥15% | polo.(−).necessario |
  | rotture | count(K=crit) | 1-2 | Prop.3.soglie |
  | fallimenti | count(K<K_min) | ≥1 | Prop.1.K_min |
  | distribuzione.Σ_Δ | variance(Σ_Δ) | >0.1 | P6.dinamica |
  
◉validation.check

  ○test.banalità
    → SE banalità < 15%
    → ALLORA testo.soffoca
    → AZIONE: aggiungere.momenti.polo.(−)
    
  ○test.rotture
    → SE rotture = 0
    → ALLORA testo.prevedibile
    → AZIONE: inserire.discontinuità.intenzionale
    
  ○test.fallimenti
    → SE fallimenti = 0
    → ALLORA tutto.sembra.ugualmente.importante
    → AZIONE: inserire.momento."inutile"
    
  ○test.varianza
    → SE tutti.Σ_Δ ≈ stesso.valore
    → ALLORA monotonia.di.registro
    → AZIONE: introdurre.oscillazione
```

---

## §A.4.INTEGRATION.WITH.CHARACTERS

### §A.4.1.CHARACTER.STYLE.COHERENCE

```aila
◉principle
  → personaggio.con.Σ_ijkp
  → influenza.stile.delle.sue.scene
  
  ← A5: frattale — stesso.pattern.diverse.scale
  → CHARACTER.Σ ↔ SCENE.STYLE.Σ

◉mapping.character.to.scene.style

  ○rule.1.attribute.dominance
    → SE personaggio.ha.Δ.dominante (i=1)
    → ALLORA sue.scene.tendono.a.Σ_Δ.alto
    → distinzione.nel.linguaggio.riflette.distinzione.caratteriale
    
  ○rule.2.pole.influence
    → SE personaggio.è.polo.(−)
    → ALLORA sue.scene.hanno.più.momenti.banalità
    → es: L'Isolatore (Σ₁₂₁₋) → scene.sparse, disconnesse
    
  ○rule.3.dimension.rhythm
    → D1.lineare → ritmo.sequenziale
    → D2.planare → ritmo.ciclico
    → D3.volumetrica → ritmo.stratificato
    → D4.temporale → ritmo.causale

◉example

  ○character: Lo.Spiralista (Σ₂₃₂₊)
    → D2.planare + A3.processo + X2.ricorsivo + polo.(+)
    
  ○derived.scene.style.when.POV
    | Param | Value | Derivation |
    |-------|-------|------------|
    | Σ_Δ | 0.5-0.6 | neutro-medio |
    | Σ_⇄ | 2.0+ | alta.densità (D2.planare = pattern) |
    | Σ_⟳ | 2-3 | ritmo.ciclico.ma.veloce (⟳.processo) |
    | p | +1 | espansivo |
    
  ○voice.sample
    "È come quando pensi a quella volta — sai cosa intendo?
     E ti rendi conto che forse era già successo prima,
     in un altro modo, ma la stessa cosa."
```

---

### §A.4.2.DIALOGUE.VS.NARRATION.STYLE

```aila
◉distinction
  → DIALOGUE: governato.da.CHARACTER.Σ
  → NARRATION: governato.da.SCENE.STYLE.Σ
  → ma: devono.essere.coerenti

◉POV.scenes
  → SE scena.in.POV.di.personaggio.X
  → ALLORA narrazione.influenzata.da.Σ_X
  → pensieri.in.voce.di.X
  → descrizioni.filtrate.da.percezione.di.X
  
  ○example
    → POV: L'Incisore (Σ₁₁₁₊)
    → narrazione: frasi.brevi, definitive
    → "La porta. La aprì. Dentro: niente."
    
  → POV: Il.Dissolvente (Σ₁₁₁₋)
  → narrazione: frasi.che.sfumano
  → "La porta, o forse era più una soglia, 
     qualcosa che separava e insieme no..."

◉omniscient.narration
  → SE narratore.onnisciente
  → ALLORA SCENE.STYLE.Σ ⊥ legato.a.personaggio
  → può.variare.liberamente
  → MA: deve.mantenere.coerenza.interna
```

---

## §A.5.PRACTICAL.EXAMPLES

### §A.5.1.SAME.CONTENT.DIFFERENT.STYLE

```aila
◉content
  → "Marco entra in casa, vede che Elena non c'è,
     si siede, aspetta."

◉style.A: Σ_Δ=0.8, Σ_⇄=2.5, Σ_⟳=3, p=+1, K=crit
  → crisis.style
  
  "Marco varcò la soglia come chi attraversa un confine 
   senza ritorno. Il silenzio della casa — lo stesso 
   silenzio che aveva temuto per mesi — gli confermò 
   quello che già sapeva. Si lasciò cadere sulla sedia.
   Aspettò. Non lei. L'inevitabile."

◉style.B: Σ_Δ=0.2, Σ_⇄=0.5, Σ_⟳=1, p=−1, K=sub
  → deliberate.failure.style
  
  "Marco entrò. Elena non c'era. 
   Si sedette. 
   Fuori c'era un cane che abbaiava. 
   Si chiese se avesse fame. 
   Probabilmente no."
   
  ○note
    → seconda.versione.sembra."inutile"
    → MA: crea.spazio.vuoto
    → contrasto.con.scene.intense
    → personaggio.sembra.reale.(a.volte.pensa.al.cane)

◉style.C: rottura.intenzionale
  → inizia.come.A, poi.break
  
  "Marco varcò la soglia come chi attraversa un confine 
   senza ritorno. Il silenzio della casa—
   
   Quanto pesa una sedia?
   
   Si sedette. Aspettò."
   
  ○note
    → domanda.irrompe.senza.preparazione
    → rompe.registro.lirico
    → K_crit.attraversata
    → lettore.spiazzato, poi.ricalibra
```

---

### §A.5.2.CHAPTER.STRUCTURE.EXAMPLE

```aila
◉chapter.outline
  → 5.scene.structure
  → ~3000.parole

  | # | Tipo | Σ_Δ | Σ_⇄ | Σ_⟳ | p | K | % |
  |---|------|-----|-----|-----|---|---|---|
  | 1 | buildup | 0.5 | 1.5 | 2 | 0 | norm | 20% |
  | 2 | **failure** | 0.3 | 0.3 | 1 | −1 | **sub** | 15% |
  | 3 | buildup | 0.6 | 2.0 | 2 | +1 | norm | 25% |
  | 4 | **rottura** | 0.8 | 2.5 | 3 | +1 | **crit** | 25% |
  | 5 | aftermath | 0.3 | 1.0 | 1 | −1 | sub | 15% |

◉validation
  ○banalità: scenes.2+5 = 30% → ✓ (>15%)
  ○rotture: scene.4 = 1 → ✓ (1-2)
  ○fallimenti: scene.2 = 1 → ✓ (≥1)
  ○varianza.Σ_Δ: [0.3, 0.3, 0.5, 0.6, 0.8] → var=0.04 → marginal
    → consider.increasing.range
```

---

## §A.6.IMPLEMENTATION.CHECKLIST

```aila
◉pre.writing

  □ identificare.tipo.scena (crisis/aftermath/buildup/failure)
  □ assegnare.SCENE_σ = (Σ_Δ, Σ_⇄, Σ_⟳, p, K)
  □ verificare.coerenza.con.CHARACTER.Σ.se.POV
  
◉during.writing

  □ mantenere.registro.coerente.con.Σ_Δ
  □ controllare.densità.metaforica.vs.Σ_⇄
  □ inserire.paragrafi.brevi.secondo.Σ_⟳
  □ SE p=−1 → permettere.banalità
  
◉post.writing.chapter

  □ calcolare.%.polo.(−) → deve.essere.≥15%
  □ contare.rotture → deve.essere.1-2
  □ verificare.presenza.≥1.fallimento
  □ controllare.varianza.Σ_Δ → evitare.monotonia

◉integration.check

  □ voci.personaggi.distinguibili.senza.etichette? ← LEZIONI.APPRESE
  □ framework.invisibile.al.lettore? ← REGOLA.D'ORO
  □ momenti.banali.sembrano.naturali, non.forzati?
  □ rotture.spiazzano.ma.non.confondono?
```

---

## §A.7.FORMALIZATION.SUMMARY

```aila
◉complete.style.formula

  STYLE(scene) = f(Δ, ⇄, ⟳, P, K)
  
  WHERE:
    Δ → Σ_Δ ∈ [0,1] (registro)
    ⇄ → Σ_⇄ ∈ [0,3] (densità)
    ⟳ → Σ_⟳ ∈ [1,3] (respiro)
    P → p ∈ {+1,−1} (polo)
    K → relazione.soglia ∈ {sub, norm, crit}

◉constraints

  ∀ chapter C:
    1. Σp(−)/n ≥ 0.15 (polo.negativo.obbligatorio)
    2. ∃ scene σᵢ : K(σᵢ) = crit (almeno.1.rottura)
    3. ∃ scene σⱼ : K(σⱼ) = sub (almeno.1.fallimento)
    4. var(Σ_Δ) > 0.05 (evitare.monotonia)

◉derivation.chain

  EAR.KERNEL
      ↓
  Attributes (Δ, ⇄, ⟳)
      ↓
  Poles (+, −)
      ↓
  Thresholds (K)
      ↓
  STYLE.VARIABLES
  
  → stile.è.proiezione.di.ontologia.su.testo
  → non.parametro.esterno
  → auto-consistente.con.personaggi
```

---

## §A.8.QUICK.REFERENCE.TABLE

```aila
◉variables.at.glance

| Variable | Symbol | Range | Default | Derives.From |
|----------|--------|-------|---------|--------------|
| Registro | Σ_Δ | 0-1 | 0.5 | Δ (Distinction) |
| Densità | Σ_⇄ | 0-3/pag | 1.5 | ⇄ (Relation) |
| Respiro | Σ_⟳ | 1-3/300w | 1-2 | ⟳ (Process) |
| Banalità | p(−) | ≥15% | 15-20% | Polo (−) |
| Rottura | K_crit | 1-2/cap | 1 | Prop.3 Soglia |
| Fallimento | K<K_min | ≥1/cap | 1 | Prop.1 K_min |

◉scene.type.presets

| Type | Σ_Δ | Σ_⇄ | Σ_⟳ | p | K |
|------|-----|-----|-----|---|---|
| crisis | 0.7-0.9 | 2.0-2.5 | 2-3 | +1 | crit |
| buildup | 0.5→0.7 | 1.5→2.5 | 2→3 | 0→+1 | norm→crit |
| aftermath | 0.2-0.4 | 0.5-1.0 | 1 | −1 | sub |
| failure | any | 0-0.5 | 1 | −1 | sub |
| neutral | 0.5 | 1.5 | 2 | 0 | norm |
```

---

**END APPENDIX A**

*Lo stile non è decorazione. È la matrice che si manifesta nel testo.*
