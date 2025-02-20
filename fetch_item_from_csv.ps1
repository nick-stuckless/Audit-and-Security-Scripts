# Define the path to CSV file
$csvPath = "C:\Users\nicks\Downloads\packets.csv"

# Read the CSV file as plain text
$lines = Get-Content $csvPath

# Iterate through each line and extract the last item
foreach ($line in $lines) {
    # Split the line by commas
    $fields = $line -split ","
    
    # Get the item
    $Item = $fields[-2]

    # Output the item
    Write-Output $Item
}
