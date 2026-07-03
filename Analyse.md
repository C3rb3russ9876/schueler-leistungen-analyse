<img width="1689" height="1048" alt="gettyimages-1352603244-612x612" src="https://github.com/user-attachments/assets/8e34225a-1f3e-4428-9b22-20b3dc879f95" />

# Schüler-Daten unter der Lupe: Welche Faktoren beeinflussen die schulische Leistung von Schülerinnen und Schülern? Von Amar Beshiri #

## Einleitung und Projektbeschreibung ##
Im Modul 375 "Daten statistisch auswerten" habe ich ein e‑Portfolio erstellt, in dem ich einen Datensatz analysiere und auswerte. Ziel des Projekts ist es, grundlegende statistische Methoden anzuwenden, Daten zu untersuchen, Zusammenhänge zu finden und daraus aussagekräftige Erkenntnisse abzuleiten.
Als Grundlage dient ein Datensatz mit insgesamt 25'000 Schüler/innen. Dieser enthält sowohl qualitative als auch quantitative Informationen, beispielsweise zu persönlichen Merkmalen, Lernverhalten sowie schulischen Leistungen. Dadurch eignet sich der Datensatz besonders gut, um unterschiedliche statistische Verfahren anzuwenden und verschiedene Zusammenhänge zu untersuchen.
Im Verlauf des Projekts werde ich mehrere Schritte durchführen. Zunächst werde ich den Datensatz auswählen und die Qualität überprüfen. Danach werde ich wichtige Variablen beschrieben und anhand statistischer Kennzahlen analysieren. Zunächst werde ich die Verteilung und Streuung der Daten sowie die grafische Darstellung mithilfe geeigneter Diagramme untersuchen. Zum Abschliessen werde ich mögliche Zusammenhänge zwischen verschiedenen Einflussfaktoren und der schulischen Leistung analysieren und interpretieren.
Das Ziel dieses e‑Portfolios ist es, herauszufinden, welche Faktoren den schulischen Erfolg beeinflussen. Gleichzeitig sollen durch die Anwendung statistischer Methoden wichtige Kompetenzen im Umgang mit Daten aufgebaut und vertieft werden.

<img width="1689" height="1048" alt="gettyimages-2193881663-612x612" src="https://github.com/user-attachments/assets/2e5c4da9-8528-4c0d-aea9-05b5279a1af4" />

## Analyse eines Datensatzes zu Schülerleistungen (HZ1) ##
Warum ich diesen Datensatz gewählt habe

Ich habe diesen Datensatz aus mehreren Gründen ausgewählt.
Einerseits enthält er eine gute Mischung aus qualitativen und quantitativen Variablen. Es gibt zum Beispiel nominale Merkmale wie das Geschlecht oder die Lernmethode sowie messbare Werte wie die Prüfungsergebnisse, die Lernzeit oder die Anwesenheit (in %). Dadurch kann ich unterschiedliche statistische Methoden anwenden.

Andererseits lassen sich mit den Daten sinnvolle Fragestellungen untersuchen. Zum Beispiel:
- Hat die Lernzeit einen Einfluss auf die schulische Leistung?
- Hat die Bildung der Eltern einen Einfluss auf den akademischen Erfolg des Schülers?
- Hat die Anwesenheit einen Einfluss auf die erzielten Noten?
Zudem ist der Datensatz übersichtlich aufgebaut und enthält mehr als genügend Einträge, sodass aussagekräftige Ergebnisse möglich sind. Gleichzeitig bleibt die Datenmenge verständlich und eignet sich daher gut für ein e-Portfolio.

**Qualitätsprüfung**

Bevor ich mit der Analyse begonnen habe, habe ich den Datensatz auf seine Qualität überprüft. Dabei habe ich folgende Kriterien untersucht:

1. Vollständigkeit

    Der Datensatz ist vollständig, da keine fehlenden Werte vorhanden sind. Jede Zeile enthält für alle Variablen gültige Einträge. Dadurch musste ich keine Daten entfernen oder schätzen, was die Zuverlässigkeit der Analyse erhöht.

2. Struktur

    Die Daten liegen in einer strukturierten Tabellenform vor. Die Variablen sind sauber getrennt und können eindeutig den passenden Datentypen zugeordnet werden:
    - Qualitative Daten (z.B. Geschlecht, Schultyp, Lernmethode)
    - Quantitative Daten (z.B. Prüfungsergebnisse, Lernzeit, Anwesenheit)
Die strukturierte Form erleichtert die Verarbeitung und Auswertung der Daten enorm.

3. Konsistenz

    Die Werte im Datensatz sind konsistent und einheitlich dargestellt. Beispielsweise werden Kategorien wie "male", "female" und "other" durchgehend korrekt verwendet. Auch andere qualitativen Variablen wie Bildungsniveau, Lernmethoden sowie Ja / Nein Angaben ("yes" / "no") sind einheitlich formatiert.

   Die numerische Werte sind sauber dargestellt und weisen eine einheitliche Struktur auf. Zudem liegen alle Werte in möglichen Bereichen, beispielsweise zwischen 0 und 100 Punkten bei den Testergebnissen oder realistischen Werten bei Alter und Lernzeit.

   Unreinheiten wie doppelte Einträge, Tippfehler oder fehlerhafte Werte konnte ich nicht feststellen.
4. Eignung für Analyse und Visualisierung

    Der Datensatz eignet sich sehr gut für statistische Analysen, weil die Kombination aus Einflussfaktoren (z.B. Lernzeit, Elternbildung oder Lernmethode) und Testergebnisse es ermöglicht, Zusammenhänge zu untersuchen.

    Zudem lassen sich verschiedene Diagramme sinnvoll einsetzen, beispielsweise:
      - Histogramme zur Darstellung der Verteilung der Noten (Bspw. Normalverteilung)
      - Balkendiagramme für Vergleiche zwischen Gruppen
      - Boxplots zur Identifikation von Ausreissern

5. Datenquelle

    Der Datensatz stammt von Kaggle, einer bekannten Website für Datenanalyse und Machine Learning. Solche Datensätze werden häufig für Lernzwecke bereitgestellt und bieten eine solide Grundlage für statistische Untersuchungen.

**Datenbereinigung und Auswahl**

Der Datensatz lag ursprünglich im CSV-Format vor und wurde für die Analyse in Excel importiert. Dabei wurden die Daten korrekt erkannt und automatisch sauber formatiert, sodass keine zusätzliche Bereinigung erforderlich war.

Um die Analyse übersichtlich und einfach zu halten, habe ich mich meiner Meinung nach auf die wichtigsten Variablen konzentriert:
- Alter (age)
- Geschlecht (gender)
- Schultyp (school_type)
- Bildungsniveau der Eltern (parent_education)
- Lernzeit (study_hours)
- Anwesenheit in % (attendance_percentage)
- Lernmethode (study_method)
- Gesamtnote (overall_score)

Andere Variablen habe ich bewusst weggelassen, um die Analyse verständlich zu halten. Diese Auswahl ermöglicht es mir, die relevanten Zusammenhänge klar darzustellen und die Handlungsziele sinnvoll abzudecken.

Variablen wie Alter, Geschlecht, Lernmethode und Schultyp habe ich zwar berücksichtigt, jedoch bewusst nicht weiter analysiert, da sie für meine Fragestellung weniger relevant waren.

**Reflexion und Verbesserungspotential**

Rückblickend war die Auswahl des Datensatzes das wichtigste Teils für mein gesamtes e-Portfolio. Ich habe mich bewusst für einen Datensatz entschieden, der sowohl qualitative als auch quantitative Variablen enthält, um möglichst viele statistische Methoden anwenden zu können.

Ich finde, diese Entscheidung war sinnvoll, da ich dadurch die Handlungsziele gut abdecken konnte. Gleichzeitig wurde mir klar, dass ich nicht alle vorhandenen Variablen verwenden muss, sondern gezielt auswählen sollte, welche für meine Fragestellung relevant sind.

Eine mögliche Verbesserung wäre, dass ich weitere Variablen wie Alter oder Geschlecht ebenfalls analysieren könnte, um zusätzliche Zusammenhänge zu untersuchen. Insgesamt bin ich jedoch mit meiner Auswahl zufrieden, da sie eine klare und verständliche Analyse ermöglicht hat.

Für die Themenfindung habe ich Copilot als Brainstorming-Tool genutzt (siehe Prompt im Anhang). Die Entscheidung für den spezifischen Thema fiel jedoch bewusst, da dieser eine hohe Datenqualität für die geforderten statistischen Berechnungen (HZ2-HZ5) aufwies.

**Wichtig zu beachten**

Der Datensatz scheint auf den ersten Blick perfekt zu sein, da keine fehlenden oder inkonsistenten Werte vorhanden sind. Jedoch ist diese "Perfektion" problematisch, da reale Datensätze in der Praxis meist Unvollständigkeiten oder Ausreisser enthalten. Dies könnte darauf hindeuten, dass der Datensatz synthetisch generiert wurde, was die Aussagekraft bezüglich realer Zusammenhänge einschränken kann.

<img width="1689" height="1048" alt="gettyimages-535847793-612x612" src="https://github.com/user-attachments/assets/48b2dfe0-a2ad-4d46-be31-c1440aa1e725" />

## Statistische Analyse und Beschreibung der Variablen (HZ2) ##
1. Skalenniveaus der Variablen

    Die im Datensatz zu findenden Variablen lassen sich verschiedenen Skalenniveaus zuordnen. Diese Unterscheidung ist wichtig, da sie bestimmt, welche statistischen Methoden auf die entsprechende Variable angewendet werden dürfen.

    Nominalskala

      Nominalskalierte Variablen besitzen keine natürliche Reihenfolge. Sie dienen nur zur Unterscheidung von Gruppen und um das Erkennen der häufigste Werte.

      Mögliche statistische Methoden: Modus

    Beispiele aus dem Datensatz:
      - Geschlecht (gender)
      - Schultyp (school_type)
      - Lernmethode (study_method)

    Diese Variablen werden hauptsächlich für Häufigkeitsverteilungen und Vergleiche zwischen Gruppen verwendet.

    Ordinalskalierte Variablen

      Ordinalskalierte Variablen weisen eine natürliche Reihenfolge auf, allerdings ohne klare Abstände zwischen den Stufen.

      Mögliche statistische Methoden: Modus, Median

    Beispiel aus dem Datensatz:
      - Bildungsniveau der Eltern (parent_education)

    Hier besteht grundsätzlich eine Rangordnung (z.B. "no formal" bis "phd"), auch wenn die Abstände zwischen den Kategorien nicht genau messbar sind.

    Intervallskalierte Variablen

      Diese besitzen gleiche Abstände, aber keinen absoluten Nullpunkt im praktischen Sinn.

      Mögliche statistische Methoden: Modus, Median, Mittelwert, Arithmetik (+ / -), Varianz, Standardabweichung

   Beispiele aus dem Datensatz:
      - Gesamtnote (overall_score)

    Die Punktzahlen (z. B. overall_score) besitzen formal einen natürlichen Nullpunkt und könnten daher als verhältnisskaliert betrachtet werden. Jedoch werden sie in der praktischen statistischen Analyse häufig wie intervallskalierte Daten behandelt, da hauptsächlich die Unterschiede zwischen den Werten und nicht deren Verhältnisse im Vordergrund stehen.

    Verhältnisskalierte Variablen

      Diese besitzen einen natürlichen Nullpunkt und erlauben sinnvolle Verhältnisaussagen.

      Mögliche statistische Methoden: Modus, Median, Mittelwert, Arithmetik, Varianz, Standardabweichung, Verhältnisaussagen

    Beispiele aus dem Datensatz:
      - Alter (age)
      - Lernzeit (study_hours)
      - Anwesenheit in % (attendance_percentage)

    In diesem Fall kann man beispielsweise sagen, dass jemand doppelt so lange gelernt hat.

2. Berechnung statistischer Kennzahlen

    Die statistischen Methoden wurden insbesondere für die Variable "overall_score" berechnet, da diese die Gesamtleistung der Schüler/innen widerspiegelt und sich somit besonders gut für die Analyse eignet.

    Mittelwert (Durchschnitt)

      Der Mittelwert gibt den durchschnittlichen Wert einer Variable an. Er ist besonders nützlich, um eine erste Einschätzung der Daten zu erhalten.

      In diesem Fall ist der Mittelwert von "overall_score": 64.006172 Punkte -> gerundet auf eine Dezimalstelle: 64.0 Punkte

      Das zeigt, dass die durchschnittliche Leistung im mittleren Bereich liegt. Allerdings ist zu beachten, dass der Mittelwert durch extreme Werte beeinflusst werden kann.

    Median

      Der Median ist der mittlere Wert einer geordneten Datenreihe. Er ist weniger anfällig für Ausreisser als der Mittelwert und gibt daher oft ein realistischeres Bild der Verteilung.

      In diesem Fall ist der Median von "overall_score": 64.2 Punkte

      Der Median signalisiert, dass 50 % der Schüler/innen weniger oder 64.2 Punkte erzielen, während die andere Hälfte mehr erzielt. Daraus erkennt man, dass es keine grosse Ausreisser gibt, denn der Mittelwert und der Median liegen nahe beieinander.

    Modus

      Der Modus ist der Wert, der am häufigsten vorkommt. Der Modus eignet sich besonders gut für nominale Daten.

      In diesem Fall ist der Modus von "overall_score": 100 Punkte

      Der Modus deutet darauf hin, dass besonders viele Schüler/innen die maximale Punktzahl erreicht haben. Allerdings ist der Modus in diesem Fall nur bedingt aussagekräftig, da viele Werte nur selten oder gleich häufig auftreten. Daher eignet sich der Median in diesem Fall besser, um die zentrale Tendenz der Daten zu beschreiben.

    Minimum und Maximum

      Der Minimum und Maximum zeigen den kleinsten und grössten Wert einer Datenreihe. Sie geben einen Überblick über den gesamten Wertebereich und legen die Grundlage fest für die Berechnung der Spannweite.

      In diesem Fall ist:
      - Der Minimum von "overall_score": 14.5 Punkte
      - Der Maximum von "overall_score": 100 Punkte

      Das deutet darauf hin, dass es eine relativ grosse Streuung vorhanden ist.

    Quartile

      "Quartil" stamm aus dem lateinischen und heisst "Viertel". Die Quartile teilen die Datenreihe in vier gleich grossen Teile, wobei der zweite Quartil der Median ist.

      In diesem Fall sind:
      - Q1 (unteres Quartil 25%): 49 Punkte
      - Q2 (Median 50%): 64.2 Punkte
      - Q3 (oberes Quartil 75%): 79 Punkte

      Diese Werte zeigen, dass 25% der Schüler/innen über 79 Punkte in der Gesamtnote erreicht haben, während 75% der Schüler/innen bis zu 79 Punkte erreicht haben.

Reflexion und Verbesserungspotential

  Ich habe gelernt, wie wichtig das Skalenniveau für die Wahl der richtigen statistischen Methoden ist. Anfangs war ich mir unsicher, ob ich einige Variablen korrekt einordne, insbesondere bei der Gesamtnote. Durch einer tiefen Recherche wurde mir klar, dass manche Variablen zwar theoretisch verhältnisskaliert sind, in der Praxis aber oft intervallskaliert verwendet werden.

  Die Berechnung der Kennzahlen ist mir gut gelungen, jedoch war die Interpretation anspruchsvoller. Besonders hilfreich war der Vergleich von Mittelwert und Median, da ich dadurch besser beurteilen konnte, ob die Daten gleichmässig verteilt sind oder nicht.

  Insgesamt könnte ich noch stärker begründen, warum ich bestimmte Kennzahlen bevorzuge, z. B. wann der Median aussagekräftiger ist als der Mittelwert.

<img width="1689" height="1048" alt="gettyimages-2189637718-612x612" src="https://github.com/user-attachments/assets/6cd7e8cf-2452-4522-9891-228c60f34934" />

## Streuungs- und Dispersionsparameter (HZ3) ##

Spannweite

  Die Spannweite ergibt sich aus der Differenz zwischen Maximum und Minimum. Sie zeigt, wie stark die Daten streuen.

  In diesem Fall ist die Spannweite: 85.5 Punkte

  Das deutet darauf hin, dass die Daten sich relativ fest streuen.

Interquartilabstand (IQA)

  Der Interquartilabstand beschreibt die Streuung der mittleren 50 % der Daten (25% - 75%). Er wird berechnet als Differenz zwischen dem dritten Quartil (Q3) und dem ersten Quartil (Q1).

  In diesem Fall beträgt der Interquartilabstand:

  IQA: 79 Punkte - 49 Punkte = 30 Punkte

  Das bedeutet, dass die mittleren 50 % der Schüler/innen zwischen 49 und 79 Punkten liegen.

Varianz

  Die Varianz beschreibt, wie stark die Werte im Durchschnitt vom Mittelwert abweichen. Sie ist ein Mass für die Streuung der Daten.

  Eine hohe Varianz bedeutet, dass die Werte stark voneinander abweichen, während eine niedrige Varianz darauf hinweist, dass die Werte nahe beim Mittelwert liegen.

  Hier beträgt die Varianz: 358.4215527685338 Punkte² -> gerundet: 358.4 Punkte²

  In diesem Fall zeigt die Varianz, dass die Gesamtnoten eine gewisse Streuung aufweisen, was darauf hindeutet, dass die Leistungen der Schüler/innen unterschiedlich sind.

Standardabweichung

  Die Standardabweichung ist die Quadratwurzel der Varianz und wird häufig zur Interpretation der Streuung verwendet, da sie in derselben Einheit wie die ursprünglichen Daten angegeben ist.

  Sie zeigt, wie stark die einzelnen Werte im Durchschnitt vom Mittelwert (64 Punkte) abweichen.

  Eine grössere Standardabweichung bedeutet, dass die Leistungen stärker streuen, während eine kleinere Standardabweichung darauf hinweist, dass viele Werte nahe beim Durchschnitt liegen.

  Hier beträgt die Standardabweichung: 18.93202452904955 Punkte -> gerundet: 18.9 Punkte

  Die Standardabweichung von 18.9 Punkten ist relativ hoch, was signalisiert, dass die Leistungen stark variieren. Das könnte problematisch sein, da dadurch der Mittelwert weniger aussagekräftig wird.

Ausreisseranalyse

  Um mögliche Ausreisser im Datensatz zu identifizieren, wurden die Grenzen mithilfe der Tukey-Methode (Q1 - 1.5 * IQA, Q3 + 1.5 * IQA) bestimmt. Dabei ergibt sich, dass Werte unter 4 Punkten sowie Werte über 124 Punkten als Ausreisser betrachtet werden.

  Da im vorliegenden Datensatz die minimalen und maximalen Werte bei 14.5 Punkten bzw. 100 Punkten liegen, befinden sich alle beobachteten Werte innerhalb dieser Grenzen. Das bedeutet, dass keine statistischen Ausreisser im Datensatz vorhanden sind.

  Dies ist besonders relevant für die Interpretation der Ergebnisse, da extreme Werte ansonsten den Mittelwert oder die Streuungsmasse stark beeinflussen könnten. In diesem Fall kann ausgegangen werden, dass die berechneten Kennzahlen, insbesondere der Mittelwert und die Standardabweichung, die Verteilung der Daten zuverlässig widerspiegeln.

  Gleichzeitig zeigt die relativ grosse Spannweite, dass dennoch Unterschiede zwischen den Leistungen bestehen, auch wenn keine Werte als extreme Ausreisser eingestuft werden.

Fazit

  Die Standardabweichung von 18.9 Punkten zeigt, dass die Leistungen der Schüler relativ stark streuen. Das bedeutet, dass viele Werte deutlich vom Durchschnitt abweichen und nicht alle Leistungen nahe beieinander liegen.

  Gleichzeitig zeigt der Interquartilabstand von 30 Punkten, dass die mittleren 50 % der Daten in einem deutlich kleineren Bereich liegen. Die Spannweite ist mit 85.5 Punkten zwar sehr gross, jedoch ist sie weniger aussagekräftig, da sie stark von einzelnen Extremwerten beeinflusst werden kann.

  Mithilfe der Tukey-Methode konnte festgestellt werden, dass Werte unter 4 Punkten bzw. über 124 Punkten als Ausreisser gelten würden. Da alle beobachteten Werte innerhalb dieses Bereichs liegen, sind keine statistischen Ausreisser im Datensatz vorhanden.

  Insgesamt zeigt sich, dass die Leistungen unterschiedlich sind, sich der Grossteil der Schüler jedoch im mittleren bis höheren Bereich befindet.

Reflexion und Verbesserungspotential

  Die Analyse der Streuungsmasse hat mir geholfen zu verstehen, wie unterschiedlich die Leistungen der Schüler/innen tatsächlich sind. Ich habe erkannt, dass nicht nur der Durchschnitt wichtig ist, sondern auch, wie stark die Werte um diesen Durchschnitt streuen.

  Besonders interessant war für mich der Vergleich zwischen Spannweite und Standardabweichung. Während die Spannweite sehr gross ist, zeigt die Standardabweichung, dass sich die meisten Werte in einem kleineren Bereich befinden.

  Eine Schwäche meiner Analyse ist, dass ich mich hauptsächlich auf eine Variable konzentriert habe. Eine Kombination mit weiteren Variablen hätte ein vollständigeres Bild der Streuung geben können. Trotzdem konnte ich zeigen, dass ich die Bedeutung von Streuungskennzahlen verstanden habe.

<img width="1689" height="1048" alt="gettyimages-2197655235-612x612" src="https://github.com/user-attachments/assets/c9729b47-a3c2-47d2-a27d-ffdbcd82dd9a" />

## Visualisierung der Daten mittels Diagrammen (HZ4) ##

<img width="1689" height="1548" alt="Boxplot-py" src="https://github.com/user-attachments/assets/f7ddd1a9-7ae1-48fa-ae62-160ed7187af2" />

### 1 - Darstellung Boxplot ###

Um die Verteilung der Gesamtnoten der Schüler/innen übersichtlich darzustellen, habe ich einen Boxplot verwendet. Der Boxplot eignet sich gut, um Kennwerte wie Median, Quartile sowie mögliche Ausreisser auf einen Blick sichtbar zu machen.

Die Box in der Mitte des Diagramms zeigt den Bereich, in dem sich die mittleren 50% (25% - 75%) der Werte befinden. Dieser Bereich liegt zwischen dem ersten Quartil (Q1) und dem dritten Quartil (Q3). Innerhalb der Box ist der zweite Quartil / Median als Linie eingezeichnet, während der Kreuz den Mittelwert darstellt.

Die Quartilwerte sind oben schon berechnet:
- Q1 liegt bei 49 Punkten
- Der Median / Q2 liegt bei 64.2 Punkten
- Q3 liegt bei 79 Punkten

Das bedeutet:
  Ein Viertel der Schüler/innen hat eine Gesamtpunktzahl von weniger als 49 Punkten erreicht, während die Hälfte unter 64.2 Punkten liegt. Rund 75 % der Werte liegen unter 79 Punkten. Die meisten Leistungen befinden sich somit im mittleren Bereich zwischen etwa 50 und 79 Punkten.

Interpretation der Verteilung

  Der Boxplot zeigt, dass sich die meisten Werte im mittleren Bereich befinden. Die Box ist relativ kompakt, was darauf hindeutet, dass die Mehrheit der Schüler/innen ähnliche Leistungen erzielt hat.

  Die Spannweite ist dennoch relativ gross, da der minimale Wert bei 14.5 Punkten und der maximale Wert bei 100 Punkten liegt. Auffällige Ausreisser sind im Diagramm nicht klar erkennbar.

Bedeutung des Boxplots

  Der Boxplot eignet sich besonders gut, um die Verteilung der Gesamtnoten kompakt zusammenzufassen. Während andere Diagramme wie das Histogramm die Häufigkeit bestimmter Wertebereiche zeigen, ermöglicht der Boxplot einen schnellen Überblick über:
  - die Lage der zentralen Werte (Median / Mittelwert)
  - die Streuung der Daten (Quartile, Spannweite und Interquartilabstand)
  - sowie mögliche extreme Werte (Ausreisser)

  Gerade bei den Schülerleistungen ist dies hilfreich, da sich so schnell erkennen lässt, wie stark die Leistungen auseinandergehen und wo sich die Mehrheit der Schüler/innen befindet.

<img width="1689" height="1548" alt="histogramm-py" src="https://github.com/user-attachments/assets/cd4bbee2-62a7-4957-bc6a-3454ddb1ae09" />

### 2 - Darstellung Histogramm ###

Um die Verteilung der Gesamtnoten der Schüler/innen noch genauer zu untersuchen, habe ich ein Histogramm erstellt. Diese Diagrammform eignet sich besonders gut, um die Häufigkeit von bestimmten Wertebereichen darzustellen und die Verteilung der Daten sichtbar zu machen.

Die x-Achse zeigt die verschiedenen Wertebereiche der Gesamtnoten, während die y-Achse angibt, wie viele Schüler/innen in den jeweiligen Bereich fallen. Jeder Balken repräsentiert somit die Anzahl von Beobachtungen innerhalb eines bestimmten Intervalls.

Interpretation der Verteilung

  Das Histogramm zeigt eine annähernd glockenförmige Verteilung der Werte. Die meisten Noten liegen im Bereich zwischen etwa 45 und 83 Punkten.

  Es ist erkennbar, dass höhere Punktbereiche häufiger vorkommen als tiefere, wodurch die Verteilung leicht nach rechts verschoben wirkt.

Bedeutung des Histogramms

  Das Histogramm ermöglicht einen guten Überblick über die Verteilung der Gesamtnoten. Im Gegensatz zum Boxplot, der zentrale Kennwerte kompakt darstellt, zeigt das Histogramm detailliert, wie häufig bestimmte Werte auftreten.

  Dadurch lässt sich erkennen, in welchen Leistungsbereichen die meisten Schüler/innen liegen und ob die Daten gleichmässig verteilt sind oder eine Verzerrung aufweisen.

<img width="1689" height="1548" alt="punkte-lernzeit-py" src="https://github.com/user-attachments/assets/15d6e242-89e3-4159-becf-e9dce65c3e3f" />

### 3 - Darstellung Balkendiagramm ###

Um den Zusammenhang zwischen Lernzeit und den erzielten Punktzahlen der Schüler/innen übersichtlich darzustellen, habe ich ein Balkendiagramm verwendet. Diese Diagrammform eignet sich besonders gut, um Durchschnittswerte zwischen verschiedenen Gruppen zu vergleichen.

Die x‑Achse zeigt die verschiedenen Lernzeit‑Gruppen (z.B. weniger als 1 Stunde, 1-2 Stunden usw.), während die y‑Achse die durchschnittliche Punktzahl (overall_score) darstellt.

Ergebnisse

  Die Auswertung zeigt folgende durchschnittlichen Punktzahlen:
  - < 1 Stunde: ca. 36.1 Punkte
  - 1-2 Stunden: ca. 41.8 Punkte
  - 3-4 Stunden: ca. 54.6 Punkte
  - 5-6 Stunden: ca. 70.4 Punkte
  - mehr als 6 Stunden: ca. 85.9 Punkte

  Das bedeutet, dass mit steigender Lernzeit auch die durchschnittliche Punktzahl deutlich zunimmt.

Interpretation der Ergebnisse

  Im Diagramm ist ein klarer Anstieg der durchschnittlichen Punktzahl mit zunehmender Lernzeit erkennbar. Die Unterschiede zwischen den Gruppen sind deutlich sichtbar.

Warum ein Balkendiagramm?

  Ich habe mich für ein Balkendiagramm entschieden, weil es besonders gut geeignet ist, Werte zwischen verschiedenen Gruppen zu vergleichen.
  - Unterschiede zwischen den Lernzeit‑Gruppen sind sofort sichtbar
  - Die Darstellung ist übersichtlich und leicht verständlich

<img width="1689" height="1548" alt="punkte-anwesenheit-py" src="https://github.com/user-attachments/assets/395c31ed-df2d-4f7f-a66f-1a193e4db481" />

### 4 - Darstellung Balkendiagramm ###

Um den Zusammenhang zwischen der Anwesenheit der Schüler/innen und den erzielten Punktzahlen übersichtlich darzustellen, habe ich erneut ein Balkendiagramm verwendet. Diese Diagrammform eignet sich besonders gut, um Durchschnittswerte zwischen verschiedenen Gruppen zu vergleichen.

Die x‑Achse zeigt die verschiedenen Anwesenheits‑Gruppen (40%-60%, 60%-80% und 80%-100%), während die y‑Achse die durchschnittliche Punktzahl (overall_score) darstellt.

Ergebnisse

  Die Auswertung zeigt folgende durchschnittlichen Punktzahlen:
  - 40%-60% Anwesenheit: ca. 56 Punkte
  - 60%-80% Anwesenheit: ca. 62 Punkte
  - 80%-100% Anwesenheit: ca. 69 Punkte

  Das bedeutet, dass mit steigender Anwesenheit auch die durchschnittliche Punktzahl zunimmt.

Interpretation der Ergebnisse

  Das Diagramm zeigt, dass mit steigender Anwesenheit auch die durchschnittliche Punktzahl zunimmt. Die Unterschiede sind sichtbar, jedoch weniger stark ausgeprägt als bei der Lernzeit.

<img width="1689" height="1548" alt="punkte-bildung-py" src="https://github.com/user-attachments/assets/0e5c77e6-adcf-492c-9e34-ad926d7e8e0b" />

### 5 - Darstellung Balkendiagramm ###

Um den Zusammenhang zwischen dem Bildungsniveau der Eltern und den erzielten Punktzahlen der Schüler/innen darzustellen, habe ich wieder ein Balkendiagramm verwendet, wegen den gleichen Gründe wie in den zwei anderen Analysen.

Die x‑Achse zeigt die verschiedenen Bildungsstufen der Eltern (z.B. high school, diploma, phd), während die y‑Achse die durchschnittliche Gesamtnote ("overall_score") darstellt.

Ergebnisse

  Die durchschnittlichen Punktzahlen unterscheiden sich leicht zwischen den verschiedenen Bildungsstufen:
  - diploma: ca. 64.7 Punkte
  - graduate: ca. 64 Punkte
  - high school: ca. 63.4 Punkte
  - no formal: ca. 63.9 Punkte
  - phd: ca. 63.5 Punkte
  - post graduate: ca. 64.6 Punkte

  Die Unterschiede zwischen den Gruppen sind insgesamt eher klein.

Interpretation der Ergebnisse

  Im Diagramm sind nur geringe Unterschiede zwischen den einzelnen Gruppen erkennbar. Die Balken liegen nahe beieinander.

Reflexion und Verbesserungspotential

  Bei der Visualisierung habe ich gelernt, wie wichtig die Wahl des richtigen Diagramms ist. Anfangs war ich mir unsicher, welches Diagramm sich für welche Darstellung eignet, aber im Verlauf der Arbeit wurde mir klar, dass unterschiedliche Diagramme unterschiedliche Informationen betonen.

  Ich habe mich bewusst für Boxplot, Histogramm und Balkendiagramme entschieden, da sie jeweils verschiedene Aspekte der Daten darstellen. Besonders hilfreich war es, die Diagramme nicht nur zu beschreiben, sondern auch zu erklären, warum ich sie verwendet habe.

  Rückblickend hätte ich gerne noch mehr verschiedene Diagrammtypen ausprobiert, um meine Analyse zu erweitern. Dennoch bin ich sicher, dass meine gewählten Visualisierungen passend sind und die Daten gut verständlich darstellen.

<img width="1689" height="1048" alt="gettyimages-521983603-612x612" src="https://github.com/user-attachments/assets/1c7268d3-3580-4999-9b05-5f3109e58c68" />

## Analyse von Zusammenhängen (HZ5) ##

Im letzten Schritt der Analyse werde ich die Beziehungen zwischen verschiedenen Variablen untersucht. Ziel ist es, herauszufinden, welche Faktoren die schulische Leistung beeinflussen und welche Bedeutung diese Zusammenhänge haben.

<img width="1695" height="1353" alt="korr-p-l-py" src="https://github.com/user-attachments/assets/3794b01c-6979-4e84-9468-16556b31aaa6" />

### 6 - Darstellung Punktdiagramm / Scatterplot ###

Zur zusätzlichen Visualisierung des Zusammenhangs zwischen Lernzeit und Gesamtnote habe ich noch ein Punktdiagramm erstellt.

Die x‑Achse zeigt die Lernzeit in Stunden, während die y‑Achse die erzielten Punktzahlen darstellt. Jeder Punkt entspricht einer einzelnen Beobachtung im Datensatz.

Beschreibung der Darstellung

  Im Diagramm ist eine klare diagonale Struktur erkennbar. Die Punkte verlaufen von unten links nach oben rechts, wodurch ein zusammenhängendes Muster sichtbar wird. Die Werte liegen relativ dicht beieinander und bilden eine kompakte Punktwolke entlang dieser diagonalen Linie.

Zusammenhang zwischen Lernzeit und Leistung

  Die Analyse der Daten zeigt, dass mit zunehmender Lernzeit auch die durchschnittlichen Punktzahlen steigen.

  Korrelationskoeffizient: 0.9057714454088271


  Der Korrelationskoeffizient signalisiert, dass es sich um eine starke positive Korrelation behandelt. Das heisst, wenn die Lernzeit steigt, dann steigt die Gesamtnote auch.

  Der Zusammenhang überrascht mich nicht viel, denn es ist besonders klar, dass wenn man mehr lernt, den Stoff besser einprägen kann.

Interpretation

  Dies deutet darauf hin, dass Lernzeit einen positiven Einfluss auf die schulische Leistung haben könnte. Die wahrscheinliche Erklärung ist, dass Schüler/innen, die mehr Zeit in das Lernen investieren, den Unterrichtsstoff besser verstehen und sich intensiver auf Prüfungen vorbereiten können.

  Besonders ab mehreren Stunden Lernzeit steigt die Leistung deutlich an. Dies könnte darauf hinweisen, dass regelmässiges und kontinuierliches Lernen einen wichtigen Beitrag zum schulischen Erfolg leistet.

  Allerdings ist zu beachten, dass die ungewöhnlich hohe Stärke dieses Zusammenhangs durch die idealisierte Struktur des Datensatzes verstärkt sein könnte und wäre in realen Daten vermutlich weniger ausgeprägt.

<img width="1701" height="1347" alt="korr-p-a-py" src="https://github.com/user-attachments/assets/962b4865-6fdd-46c7-a1d9-027fb79135f9" />

### 7 - Darstellung Punktdiagramm / Scatterplot ###

Zur Darstellung der Beziehung zwischen Anwesenheit und Gesamtnote habe ich ebenfalls ein Punktdiagramm verwendet.
Die x‑Achse zeigt die Anwesenheit in Prozent, während die y‑Achse die Punktzahlen darstellt. Jeder Punkt repräsentiert eine einzelne Beobachtung.

Beschreibung der Darstellung

  Die Punkte verteilen sich über einen grösseren Bereich und bilden eine breite Punktwolke. Innerhalb dieser Wolke ist eine leichte Struktur erkennbar, wobei die Punkte insgesamt in einem steigenden Muster angeordnet sind. Im Vergleich zum Diagramm der Lernzeit ist die Streuung jedoch deutlich grösser.

Zusammenhang zwischen Anwesenheit und Leistung

  Auch bei der Anwesenheit zeigt sich ein Trend: Mit steigender Anwesenheit nehmen die durchschnittlichen Punktzahlen leicht zu.

  Korrelationskoeffizient: 0.29276151938517925

  Der Korrelationskoeffizient weist darauf hin, dass es sich um eine moderate positive Korrelation handelt. Das heisst, wenn die Lernzeit steigt, dann steigt die Gesamtnote auch leicht.

  Das Ergebnis hat mich leicht überrascht, nicht weil es unerwartet war, sondern weil es anscheinend einen kleineren Einfluss auf die Punktzahl hat als die Eigenarbeit (Lernzeit). Ich dachte, dass Unterrichtsteilnahme einer der wichtigsten Faktoren war, sogar wichtiger als die Eigenarbeit, scheint aber nicht der Fall zu sein.

Interpretation

  Dies lässt darauf schliessen, dass die Anwesenheit im Unterricht einen teils wichtigen Einfluss auf die Leistung haben kann. Schüler/innen, die regelmässig am Unterricht teilnehmen, verpassen weniger Inhalte und können aktiv am Lernprozess teilnehmen.

  Die Unterschiede zwischen den Gruppen sind nicht extrem gross, jedoch ist eine Tendenz erkennbar. Dies unterstreicht, dass Anwesenheit ein relevanter, aber nicht alleiniger Einflussfaktor ist.

  Hier ist es ebenfalls wichtig zu beachten, dass der vergleichsweise schwache Zusammenhang in realen Datensätzen durch Drittvariablen wie Motivation oder Unterrichtsqualität zusätzlich überlagert werden könnte.

<img width="1920" height="1353" alt="korr-p-b-py" src="https://github.com/user-attachments/assets/af7ebbcf-efc7-4397-9107-cc70acc962dc" />

### 8 - Darstellung Punktdiagramm / Scatterplot ###

Auch für das Bildungsniveau der Eltern habe ich ein Punktdiagramm erstellt, um die Verteilung der Punktzahlen über die verschiedenen Kategorien hinweg darzustellen.

Die y‑Achse zeigt die einzelnen Bildungsstufen, während die x‑Achse die erzielten Punktzahlen darstellt.

Beschreibung der Darstellung

  Die Punkte verteilen sich gleichmässig über alle Kategorien hinweg. Es sind mehrere horizontale Linien erkennbar, die den einzelnen Bildungsstufen entsprechen. Innerhalb dieser Linien sind die Punktzahlen breit gestreut, ohne dass eine klare Struktur oder ein auffälliges Muster sichtbar ist.

Zusammenhang zwischen Elternbildung und Leistung

  Ein weiterer untersuchter Zusammenhang besteht zwischen dem Bildungsniveau der Eltern und der schulischen Leistung der Schüler/innen.

  Korrelationskoeffizient: 0.002691873349375122

  Der Korrelationskoeffizient zeigt, dass praktisch kein Zusammenhang zwischen diesen beiden Variablen vorliegt.

  Das Ergebnis hat mich leicht überrascht. Mir wurde oft gesagt, dass der Bildungsniveau der Eltern wichtig für den schulischen Erfolg sei. Die Analyse meiner Daten legt nahe, dass keine Korrelation zwischen dem Bildungsniveau der Eltern und dem schulischen Erfolg besteht.

Interpretation

  Mit den Ergebnissen lässt sich sagen, dass in diesem Datensatz kein Zusammenhang zwischen der Bildung der Eltern und der schulischen Leistung erkennbar ist, jedoch lässt sich daraus keine allgemeine Aussage über reale Zusammenhänge ableiten

  Jedoch ist zu beachten, dass hier kein Zusammenhang erkennbar ist. Das heisst es könnte im Gegensatz zu vielen realen Studien stehen und auf einen synthethischen Datensatz hinweist.

**Wichtiger Hinweis**

  Bei der Analyse der Zusammenhänge fällt auf, dass insbesondere der Zusammenhang zwischen Lernzeit und Leistung sehr klar und linear verläuft.

  Dies könnte darauf hindeuten, dass es sich bei dem verwendeten Datensatz um synthetisch erzeugte Daten handelt (sehr wahrscheinlich bei Kaggle). Solche Datensätze werden häufig für Lernzwecke erstellt und weisen oft "ideale" Muster auf als reale Daten.

  In der Realität sind Daten meist stärker durch Zufallseinflüsse, Ausreisser und individuelle Unterschiede geprägt. Die hier beobachteten sehr klaren Strukturen könnten daher weniger ausgeprägt sein als in echten Datensätzen.

  Dies heisst jedoch nicht, dass die Analyse falsch ist, sondern dass die Ergebnisse im Kontext eines möglicherweise vereinfachten Datensatzes interpretiert werden müssen.

Vergleich der Einflussfaktoren

  Sowohl Lernzeit als auch Anwesenheit zeigen einen positiven Zusammenhang mit der Leistung. Dabei scheint die Lernzeit einen etwas stärkeren Einfluss zu haben, da die Unterschiede zwischen den Gruppen deutlich grösser sind. Währenddessen zeigt die Bildung der Eltern keinen eindeutigen Zusammenhang mit der Leistung.

  Dies deutet darauf hin, dass sowohl Eigenarbeit (Lernzeit) als auch Unterrichtsteilnahme (Anwesenheit) wichtige Faktoren für den schulischen Erfolg sind, während die Bildung der Eltern keinen scheinbaren Einfluss für den schulischen Erfolg hat.

  In diesem Datensatz konnte kein signifikanter Zusammenhang festgestellt werden.

  Das bedeutet jedoch nicht, dass generell kein Einfluss besteht.

Korrelation und Kausalität

  Es ist wichtig zu beachten, dass es sich bei den Zusammenhängen um Korrelationen handelt.

  Das bedeutet, dass zwar ein Zusammenhang zwischen den Variablen erkennbar ist, jedoch keine eindeutige Ursache‑Wirkung‑Beziehung nachgewiesen werden kann. Drittvariablen könnten ebenfalls eine Rolle spielen, wie zum Beispiel:
  - Motivation der Schüler/innen
  - individuelle Lernfähigkeit
  - Unterstützung durch das Umfeld

  Diese Faktoren wurden im Datensatz nicht berücksichtigt, könnten die Ergebnisse jedoch beeinflussen.

Reflexion und Verbesserungspotential

  Die Analyse der Zusammenhänge war für mich der spannendste Teil des Projekts. Ich konnte erkennen, dass Faktoren wie Lernzeit und Anwesenheit einen Einfluss auf die schulische Leistung haben.

  Besonders interessant war, dass einige Ergebnisse meine Erwartungen bestätigt haben, während andere mich überrascht haben. Zum Beispiel hätte ich erwartet, dass die Anwesenheit einen stärkeren Einfluss hat als die Lernzeit, was sich jedoch nicht bestätigt hat.

  Zudem habe ich korrekt erkannt, dass Korrelation nicht gleich Kausalität ist. Auch wenn ein Zusammenhang besteht, bedeutet das nicht automatisch, dass eine Ursache‑Wirkung‑Beziehung vorliegt.

  Insgesamt könnte ich die Analyse noch vertiefen, indem ich weitere Variablen kombiniert untersuche. Trotzdem bin ich mit meiner Arbeit zufrieden, da ich die Zusammenhänge nicht nur berechnet, sondern auch hinterfragt habe.

Schlussreflexion

  Im Rahmen dieses e‑Portfolios habe ich einen Datensatz mit 25'000 Schüler/innen analysiert und verschiedene statistische Methoden angewendet, um die Daten zu untersuchen und zu interpretieren.

  Während des Projekts entwickelte ich ein besseres Verständnis für die Auswertung von Daten. Besonders hilfreich war dabei die Arbeit mit statistischen Kennzahlen wie Mittelwert, Median und Standardabweichung, um die Lage und Streuung der Daten zu beschreiben.

  Ein weiterer wichtiger Aspekt war die Wahl geeigneter Diagrammtypen. Histogramme und Boxplots eignen sich besonders für die Darstellung von Verteilungen, während Balkendiagramme den Vergleich zwischen verschiedenen Gruppen erleichtern.

  Bei der Analyse der Zusammenhänge zeigte sich, dass Faktoren wie Lernzeit und Anwesenheit einen erkennbaren Einfluss auf die schulische Leistung haben. Gleichzeitig wurde deutlich, dass nicht alle vermuteten Einflussfaktoren, wie beispielsweise das Bildungsniveau der Eltern, tatsächlich einen Zusammenhang aufweisen.

  Hilfreich war für mich das Beispielportfolio von Andrin Hutterli, da es mir ermöglicht hat, systematisch vorzugehen und die Arbeit verständlich zu strukturieren. Eine Herausforderung bestand jedoch darin, die Ergebnisse korrekt zu interpretieren.

Selbsteinschätzung

  Im Verlauf der Erstellung dieses e‑Portfolios habe ich mich intensiv mit der statistischen Analyse von Daten auseinandergesetzt.

  Besonders gut gelungen ist mir die strukturierte Gliederung meiner Arbeit entlang der verschiedenen Handlungsziele, wobei mir das Beispiel von Andrin Hutterli sehr geholfen hat. Ich konnte die einzelnen Schritte, von der Auswahl des Datensatzes über die Berechnung statistischer Kennzahlen bis hin zur Visualisierung und Analyse, logisch und nachvollziehbar aufbauen (hoffentlich).

  Auch die Berechnung von Kennzahlen wie Mittelwert, Median und Standardabweichung ist mir gut gelungen. Relativ anspruchsvoller war jedoch die korrekte Interpretation der Ergebnisse. Ich habe darauf geachtet, nicht nur zu rechnen, sondern die Resultate verständlich zu erklären, wie es in den Anforderungen verlangt wurde.

  Im Bereich der Visualisierung konnte ich passende Diagramme auswählen und deren Einsatz begründen. Dabei war mir die klare Trennung zwischen der reinen Beschreibung der Diagramme (HZ4) und der vertieften Analyse der Zusammenhänge (HZ5) wichtig. Ich hätte gerne mehr verschiedene Diagrammtypen eingesetzt, um meinen e-Portfolio zu diversifizieren. Für die analysierten Zusammenhänge war jedoch das Balkendiagramm die passendste Wahl.

  Eine weitere Herausforderung war es Wiederholungen zwischen den Handlungszielen zu vermeiden. Ich musste lernen, meine Ergebnisse zu hinterfragen und realistisch zu bewerten, auch wenn die Unterschiede teilweise nur gering waren.

  Insgesamt bin ich mit meiner Arbeit grösstenteils zufrieden. Ich konnte mein Verständnis für den Umgang mit Daten und statistischen Methoden verbessern. Für zukünftige Projekte nehme ich mit, wie wichtig eine klare Struktur und kritisches Hinterfragen der Ergebnisse sind.

<img width="1689" height="1048" alt="gettyimages-2092128110-612x612" src="https://github.com/user-attachments/assets/0f4b5ad2-ce4b-42fd-bd74-cfed0922e1c8" />

## Quellen / Anhang ##

Beispiel-Portfolio:
- e-Portfolio von Andrin Hutterli: https://sway.cloud.microsoft/5E2VstyXqDeUp1ey?ref=Link&loc=play

Datenquelle:
- Kaggle: https://www.kaggle.com/datasets/kundanbedmutha/student-performance-dataset?resource=download
- CSV / Roh-Datei (siehe CSV in Repository): Student_Performance (1).csv

Titel:
- https://www.gettyimages.ch/detail/foto/shot-of-an-unrecognizable-businessman-working-on-his-lizenzfreies-bild/1352603244?searchscope=image%252Cfilm&adppopup=true

Abschnitt HZ1:
- https://www.gettyimages.ch/detail/nachrichtenfoto/elementary-school-classroom-in-jericho-new-york-on-nachrichtenfoto/2193881663?adppopup=true

Abschnitt HZ2:
- https://www.gettyimages.ch/detail/foto/cropped-view-of-group-of-teenagers-taking-a-test-lizenzfreies-bild/535847793?searchscope=image%252Cfilm&adppopup=true

Abschnitt HZ3:
- https://www.gettyimages.ch/detail/illustration/abstract-pixel-dispersion-effect-on-a-white-lizenfreie-illustration/2189637718?searchscope=image%252Cfilm&adppopup=true

Abschnitt HZ4:
- https://www.gettyimages.ch/detail/foto/close-up-of-three-people-looking-at-financial-data-lizenzfreies-bild/2197655235?searchscope=image%252Cfilm&adppopup=true

Abschnitt HZ5:
- https://www.gettyimages.ch/detail/foto/electromagnetic-pollution-results-on-computer-screen-lizenzfreies-bild/521983603?searchscope=image%252Cfilm&adppopup=true

Abschnitt Quelle:
- https://www.gettyimages.ch/detail/illustration/cloud-abstract-technical-background-lizenfreie-illustration/2092128110?searchscope=image%252Cfilm&adppopup=true

KI-Verwendung:

Zur Unterstützung bei der Erstellung dieses e‑Portfolios wurde Microsoft 365 Copilot verwendet.

Die KI wurde hauptsächlich genutzt für:
- Strukturierung des e‑Portfolios
- Formulierung von Sätze
- Unterstützung bei statistischen Erklärungen

Alle Inhalte wurden eigenständig überprüft, angepasst und verstanden

Einige verwendete Prompts:
- "Kannst du mir eine Struktur / Aufbau für den Inhalt (HZ2, HZ3, HZ4, HZ5) erstellen anhand eines Beispiels von letztes Jahr?"
- "Kannst du diesen Text grammatikalisch korrigieren und stilistisch verbessern, ohne die Aussage zu verändern?"
- "Könntest du mal die Handlungsziele lesen und somit einen geeigneten Thema für mich finden inklusive Datensatz, welcher geeignet ist zum Thema und zu den Handlungsziele." + Screenshot der HZ
- "Was könnte man als Titel eingeben, sodass es direkt Interesse weckt?"
- "Erkläre den Unterschied zwischen HZ4 und HZ5"
- "Wo denkst du gehört der Boxplot und Histogramm, HZ3 oder HZ4?"
- "Warum zählen Variablen wie math_score usw. als Intervallskala? Die haben ja einen Nullpunkt"
- "Kannst du den Portfolio als Lehrer bewerten nach den Anforderungen?"
- "Soll ich alle Variablen verwenden oder kann ich einige auslassen?"
- "Warum wird der Mittelwert weniger Aussagekräftig durch die Standardabweichung?"
- "Was kann man als Überschrift nehmen? Bspw. Ein Datensatz mit Erfolg und Misserfolg (HZ1)"
- "Die statistische Berechnungen werden in diesem Datensatz am besten bei der Variable 'overall_score' durchgeführt, korrekt?"
- "Warum gehören die Beschreibungen des Boxplots / Histogramms (HZ4) in HZ3, während die Beschreibungen der Balkendiagramme (HZ4) in HZ5 sind?"
- "Ist es egal, wenn es keinen grossen Unterschied im Diagramm hat?"
- "Ist es möglich einen Wert an einem String zuzuweisen, um eine statistische Rechnung durchzuführen?"
- "Wie kann ich in Excel bspw. study_hours in Bereiche Gruppieren? Bspw. 1-2 Stunden, 3-4 Stunden"
- "Wie kann man den Wert, um als Ausreisser zu gelten, berechnen?"
Kopiertes Code:
- fig, ax = plt.subplots()
- df.plot(
    kind="scatter",
    color="darkblue",
    x="overall_score",
    y="parent_education_group",
    ax=ax
)
