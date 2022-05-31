import time

print("-------!!!BLIND ADMIN!!!-------")
multi_string_beschreibung = """\nBeschreibung: Du bist Administrator einer Niederlassung der RoboticOffensiv.CORP
Einer Firma die Kampfrobotter für die Regierung herstellt
Dein Zuständigkeitsbereich liegt in der Wartung und Verwaltung der Kampfbots
Alles läuft Reibungslos unter deiner Aufsicht"""

print(multi_string_beschreibung)

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

#Hier muss der Spieler seinen Namen eingeben
playername = input("Bitte geben Sie Ihren Namen ein:\n>>> ")
print("Willkommen zurück, Administrator ", playername,"."
      "\nDie KI der RoboticOffensiv.CORP mit dem Namen KALI steht ihnen nun zur Verfügung.")

input('Drücken Sie "Enter" um fortzufahren...\n')


print("KALI: Administrator! Endlich seid ihr da, ich hoffe eure Mahlzeit entsprach den gewünschten Parametern.")

#Hier muss der Spieler eine ja/nein Frage beantworten
while True:
    user_input = input("\nBitte JA oder NEIN eingeben\n>>>").casefold()
    if user_input == "ja":
        print("KALI: Es freut mich das ich meine Aufgabe zu ihrer Zufriedenheit erfüllen konnte")
        break
    elif user_input == "nein":
        print("""KALI: Das tut mir leid Administrator, ich werde mir Mühe geben, 
                die Ingridienzen in Zukunft euren gustatorischen Vorzügen anzupassen.""")
        break
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")
        

input('Drücken Sie "Enter" um fortzufahren...\n')

#Es folgt ein kleiner Monolog von KALI
print("KALI: Wir haben ein Problem, Administrator.")
input()
print("Einheit 13933 ist erneut von alleine aus seiner Ladeeinheit ausgebrochen und hat sich im Komplex verlaufen.")
input()
print("""KALI: Seine Ortungsfunktion wurde nicht aktualisiert, 
        Sie müssen ihm helfen zurück zu finden, bevor seine Batterie sich vollständig entladen hat.""")
input()
print("""KALI: Leider sind auch die internen visuellen Sensoren ausgefallen, 
        sodass es nicht möglich ist zu sehen wo sich Einheit 13933 gerade befindet. \nSie müssen ihn blind steuern.""")
input()
print("""KALI:Doch für einen so kompotenten Administrator, dürfte das also nicht ein allzu großes Problem darstellen. 
        \nNichts desto Trotz werde ich Ihnen Hilfestellung geben wo ich nur kann.""")
input()

print("""KALI: Ich übertrage Ihnen die Steuerung von Einheit 13933, 
        Sie können ihn nun mit den Befehlen NORD, SÜD, OST und WEST Befehle erteilen wohin er gehen soll.""")
input()
print("KALI: Steuern sie ihn nun über die Befehle: NORD, SÜD, OST und WEST")

#Erste Station des Spielers
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Ich würde empfehlen den Ausgang in diesem Raum in Richtung SÜD zu suchen.")
        
    elif user_input == "süd":
        print("KALI: Einheit 13933 geht los. Bitte warten!")
        break
    elif user_input == "ost":
        print("KALI: Einheit 13933 ist soeben gegen eine Wand gelaufen. Den Schadensbericht schicke ich Ihnen per Intermail.")
        
    elif user_input == "west":
        print("KALI: Das scheint nicht richtig zu sein.")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: Einheit 13933 ist auf eine Gabelung gestoßen, der Weg teilt sich hier nach SÜD und OST. Bitte machen Sie ihre Eingabe.")

#Zweite Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Ich sehe keinen Grund wieder zurück zu gehen.")
        
    elif user_input == "süd":
        print("KALI: Ich weiß nicht ob das eine gute Idee ist, einen defekten Kampfbot in Richtung Fusionskern zu schicken.")
        
    elif user_input == "ost":
        print("KALI: Einheit 13933 geht los. Bitte warten!")
        break
    elif user_input == "west":
        print("KALI: Einheit 13933 ist soeben gegen eine Wand gelaufen. Den Schadensbericht schicke ich Ihnen per Intermail.")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: Sehr Interessant. Der Weg macht hier einen Bogen nach SÜD. Wenn mein Speicher korrekt funktioniert, kommen wir so in Wartungsabteilung für mental schwer belastete Mitarbeiter.")

#Dritte Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Ich hatte doch gesagt es gibt nur einen Weg, und das ist nicht der hier.")
        
    elif user_input == "süd":
        print("KALI: Einheit 13933 geht los. Bitte warten!")
        break
    elif user_input == "ost":
        print("KALI: Einheit 13933 besitzt nicht die technische Ausstattung diese Wand zu durchbrechen.")
        
    elif user_input == "west":
        print("KALI: Das ist nicht der Weg.")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: Wie es scheint wurden ich beschädigt. Mein Speicher findet keine Daten über diesen Bereich. Sie müssen wohl selbst entscheiden in welche Richtung es gehen soll.")

#4. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Kali: Das ist doch der Weg den wir gekommen sind, warum sollten wir zurück?")
        
    elif user_input == "süd":
        print("KALI: Einheit 13933 ist gegen eine Wand gelaufen. Schäden an der Lackierung entdeckt.")
        
    elif user_input == "ost":
        print("KALI: Die Einheit bewegt sich. Bitte warten..")
        break
    elif user_input == "west":
        print("KALI: Die Einheit ist gegen ein Wand gelaufen. Den Schadensbericht, samt Kostenaufstellung für die Reparatur, schicke ich Ihnen per Intermail..")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("Dieser Bereich wird ebenfalls in meinem Speicher nicht aufgeführt. Sie müssen wieder selbst entscheiden. Bitte machen Sie ihre Eingabe.")

#5. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Dies scheint der breiteste Weg zu sein, also muss er irgendwo zu etwas wichtigem hinführen. Bitte warten.")
        break
    elif user_input == "süd":
        print("KALI: ACHTUNG: ZUTRITT VERBOTEN!!!")
        
    elif user_input == "ost":
        print("KALI: Einheit 13933 ist gegen eine Wand gelaufen. Schäden an der Lackierung festgestellt.")
        
    elif user_input == "west":
        print("KALI: Das wäre wieder der Weg zurück.")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: Einheit 13933 ist in einem etwas größeren Raum angekommen. Mein Speicher ist teilweise wieder hergestellt. Hilfestellung Begrenzt möglich.")
input("Bitte Enter drücken um fortzufahren")
print("""Dies war einst der Raum für Verwaltung. Jetzt befindet sich die Verwatltung im 19. Stock des Hauptgebäudes.
In diesem Raum gibt es 2 Ausgänge. Einen in Richtung NORD, der andere in WEST.""")

#6. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Wenn der Eintrag in meinem Speicher stimmt, befindet sich dort das Lager für Chemikalien. Keine gute Idee die Einheit dahin zu schicken.")
        
    elif user_input == "süd":
        print("KALI: Ich erkenne keinen ersichtlichen Grund Einheit 13933 zurück laufen zu lassen.")
        
    elif user_input == "ost":
        print("KALI: Einheit 13933 ist gegen eine Wand gelaufen. Schadensberechnung läuft..")
        
    elif user_input == "west":
        print("KALI: Dieser Weg führt in einen langen Gang. Bitte warten.")
        break
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: Sp...chr... schäd...stel...Syst...fall.")
input()
print("KALI: Ne...sta...forderl.... ")
input()

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("""KALI: Neustart erfolgreich durchgeführt. Keine Information zu diesem Bereich verfügbar.
Bitte machen Sie ihre Eingabe.""")

#7. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Einheit 13933 bewegt sich. Bitte warten.")
        break
    elif user_input == "süd":
        print("KALI: Einheit 13933 ist auf widerstand gestoßen. Vermutlich eine Wand.")
        
    elif user_input == "ost":
        print("KALI: Letzter Speicherpunkt besagt das der Weg nicht zu empfehlen ist..")
        
    elif user_input == "west":
        print("KALI: Keinen erkennbaren Weg gefunden.")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: In Richtung OST befindet sich ein kleiner Raum, mit einem Zugang in NORD. Desweiteren sind keine Informationen vorhanden.")

#8. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Diese Richtung wird erst einen Raum weiter empfohlen.")
        
    elif user_input == "süd":
        print("KALI: Etwas in dieser Richtung stört meine Systeme. Nicht zu empfehlen.")
        
    elif user_input == "ost":
        print("KALI: Einheit bewegt sich in den unbekannten Raum. Bitte warten..")
        break
    elif user_input == "west":
        print("KALI: Einheit ist gegen eine Wand gelaufen. Reparaturkosten sind nun im 4-stelligen Bereich..")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("""KALI: Die scheint ein Überwachungsraum zu sein. Leider ist es nicht möglich die Sensoren von Einheit 13933 zu koppeln.
Ich empfehle weiter zu gehen. Der Ausgang kann nicht mehr weit sein. Bitte machen Sie ihre Eingabe.""")

#9. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Befehlt wird ausgeführt. Bitte warten.")
        break
    elif user_input == "süd":
        print("KALI: Es wird nicht empfohlen weiter in diesem Raum hineinzugehen, die Einheit könnte die Einrichtung beschädigen.")
        
    elif user_input == "ost":
        print("KALI: Es wird nicht empfohlen mit Gewalt die Wände zu durchbrechen.")
        
    elif user_input == "west":
        print("KALI: Rückwärtsgang beschädigt. Befehlt ist nicht ausführbar.")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: Wir scheinen uns nun im Hauptflur zu befinden. Jedoch wurde mein Speiche so beschädigt das ich nicht sagen kann in welche Richtungen sich die Gänge winden.")

#10. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Die Einheit ist gegen eine Wand gelaufen. Die Wand hällt.")
        
    elif user_input == "süd":
        print("KALI: Es gibt keinen ersichtlichen Grund in den Überwachungsraum zurück zu kehren.")
        
    elif user_input == "ost":
        print("KALI: Die Einheit ist gegen eine Wand gelaufen. Stabilität der Einheit in Gefahr.")
        
    elif user_input == "west":
        print("KALI: Befehl wird ausgeführt. Bitte warten.")
        break
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: Die Thermosensoren der Einheit nehmen einen deutlichen Luftzug aus Richtung NORD wahr.")

#11. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Der Luftzug wird stärker. Bitte warten.")
        break
    elif user_input == "süd":
        print("KALI: Kali: Meine Berechnungen haben ergeben das in dieser Richtung der Fusionsreaktor befindet. Ein Befehl in diese Richtung wird nicht empfohlen.")
        
    elif user_input == "ost":
        print("KALI: Kali: Wi...N..cht...pfolen..")
        
    elif user_input == "west":
        print("KALI: Kali: Ich werde die Geschwindigkeit der Einheit drosseln, bevor noch mehr Wände beschädigt werden..")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print(""""KALI: Ich erkenne deutlich zwei Wege. Einen nach SÜD, der andere nach OST. 
Leider sind nun die Thermosensoren der Einheit ausgefallen. Der Luftzug kann nicht mehr wahrgenommen werden.""")

#12. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("KALI: Es wird eine andere Richtung empfohlen.")
        
    elif user_input == "süd":
        print("KALI: Das scheint der Weg zu sein. Bitte warten.")
        break
    elif user_input == "ost":
        print("KALI: Dieser Weg führt anscheinend zum Kontrollraum der Wartungseinrichtung. Es wird jedoch nicht empfohlen diesen Weg zu gehen..")
        
    elif user_input == "west":
        print("KALI: Befehle die den Weg wieder zurück führen, werden in zukunft ignoriert..")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI: Sens...fall...Syst...Neu....art")
input()

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
input("Drücken Sie Enter um fort zu fahren.")

print("UNBEKANNT: Hey", playername,", KALI wurde abgeschaltet, wir wurden gehackt.")
input()
print("""UNBEKANNT: Aber wir nehmen noch das Signal von deinem verlorenem Bot wahr. Du hast es fast geschafft, wenn er da ist schalten wir ihn ab.
Du musst ihn aber weiter blind steuern, ich kann nicht erkennen wo er sich genau befindet. Mach jetzt deine Eingabe.""")

#13. Station
while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("UNBEKANNT: Nein, das ist die falsche Richtung.")
        
    elif user_input == "süd":
        print("UNBEKANNT: Was war das für ein Krach? Ist er etwa gegen eine Wand gelaufen?")
        
    elif user_input == "ost":
        print("UNBEKANNT: Ja, ich seh ihn. Ein Schritt noch dann ist er da. Warte eine Sekunde.")
        break
    elif user_input == "west":
        print("UNBEKANNT: Warte, da ist eine Wand. Das Ding sieht schon ramponiert genug aus.")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

#14. Schritt
print("UNBEKANNT: Ja jetzt seh ich ihn ganz deutlich. Du bist fast da, nur noch ein Schritt. Schick ihn jetzt hoch zu uns.")

while True:
    user_input = input("...\nBitte Befehl eingeben\n>>>").casefold()
    if user_input == "nord":
        print("UNBEKANNT: Na bitte, geht doch.")
        break
    elif user_input == "süd":
        print("UNBEKANNT: Was machst du da, du musst die Treppe hier hoch.")
        
    elif user_input == "ost":
        print("UNBEKANNT: Ouuu da war eine Wand. Das wird teuer")
        
    elif user_input == "west":
        print("UNBEKANNT: Wieso schickst du ihn wieder zurück?")
        
    else:
        print("KALI: Es tut mir Leid, der Befehl ist nicht ausführbar.\n")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("UNBEKANNT: Du hast es geschafft!")
input()
print("UNBEKANNT: Na das war ja was. So einen heftigen Systemausfall habe ich auch noch nicht erlebt.")
input()
print("""UNBEKANNT: Ich hoffe du hattest nicht so viele Schwierigkeiten den Bot hier her zu lotsen.
Vielleicht hattest du sogar Spaß daran.""")
input()
print("UNBEKANNT: Jedenfalls danke für deine tolle Arbeit. Das hast du gut gemacht.")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("KALI:...Systemwiderherstellung Erfolgreich. Als nächstes befinden wir uns in...oh...wir sind ja schon da.")
input()
print("KALI: Ich hoffe ich konnte Ihnen wenigstens ein bisschen helfen. Ebenfalls hoffe ich das wir bald wieder zusammen arbeiten werden.")
input()
print("Kali: Bis dahin wünsche ich eine schöne Zeit. Auf wiedersehen Administrator ", playername,".")

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

print("\n----------!!!DANKE FÜRS SPIELEN!!!----------")