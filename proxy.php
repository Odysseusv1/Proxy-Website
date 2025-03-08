<?php
if (isset($_GET['url'])) {
    $url = $_GET['url'];

    // Validate the URL
    if (filter_var($url, FILTER_VALIDATE_URL)) {
        // Fetch the content from the URL
        $content = file_get_contents($url);

        // Check if the content was fetched successfully
        if ($content !== false) {
            // Output the content
            echo $content;
        } else {
            echo "Error fetching the content.";
        }
    } else {
        echo "Invalid URL.";
    }
} else {
    echo "No URL provided.";
}
?>
