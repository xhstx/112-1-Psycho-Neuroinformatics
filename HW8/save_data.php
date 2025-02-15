<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = $_POST['data']; // This should contain the trial data in JSON format.

    if (!empty($data)) {
        $filename = 'data.txt';
        $file = fopen($filename, 'a'); // Open the file for appending data.
        
        if ($file) {
            fwrite($file, $data . PHP_EOL); // Write the data to the file.
            fclose($file); // Close the file.
            echo "Data recorded successfully.";
        } else {
            echo "Error opening the file.";
        }
    } else {
        echo "No data received.";
    }
} else {
    echo "Invalid request.";
}
?>
