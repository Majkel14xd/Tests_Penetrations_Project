<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];
    $filepath = "uploads/" . $file;

    if (file_exists($filepath)) {
        echo "<pre>" . htmlspecialchars(file_get_contents($filepath)) . "</pre>";
    } else {
        echo "Plik nie istnieje!";
    }
} else {
    echo "Podaj nazwę pliku jako parametr 'file'.";
}
