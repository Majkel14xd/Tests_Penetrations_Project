<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];
    $baseDir = realpath("uploads");
    $filepath = realpath($baseDir . DIRECTORY_SEPARATOR . $file);

    // Sprawdzenie, czy plik istnieje i czy znajduje się w katalogu uploads
    if ($filepath && strpos($filepath, $baseDir) === 0 && file_exists($filepath)) {
        echo "<pre>" . htmlspecialchars(file_get_contents($filepath)) . "</pre>";
    } else {
        echo "Plik nie istnieje lub dostęp zabroniony!";
    }
} else {
    echo "Podaj nazwę pliku jako parametr 'file'.";
}
