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

    # Output the item, sorting over output with regex to only include urls
    Write-Output $Item | 
    ForEach-Object { 
        if ($_ -match "\S* \S* \S* \S* \S* (\S*\.\S*\.\S*) .*") { 
            $matches[1] 
        } 
    } | 
    Sort-Object
}
