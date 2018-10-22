<?php
# Verbindungsaufbau
if(mysql_connect("mysql27.1blu.de", "s260795_2796303", "nVw9F)FnY0lqd@%")) {
    echo "Server-Verbindung erfolgreich, wähle Datenbank aus...";

    if(mysql_select_db("db260795x2796303")) {
        echo "Datenbank erfolgreich ausgewält, alle Tests abgeschlossen.";
    }
    else {
        echo "Die angegebene Datenbank konnte nicht ausgewählt werden, bitte die Eingabe prüfen!";
    }
}
else {
    echo "Verbindung nicht möglich, bitte Daten prüfen!";
    echo mysql_error();
}
?>