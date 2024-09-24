#!/bin/bash

# Today's challenges is to create a script in bash that naviagetes to the document directory and list the files in there
# Then ask the user to create or edit a file and opens the file up in the termina

    #!/bin/bash
cd ~/Documents
ls -l
echo "Enter the name of the file you want to create or edit:"
read filename
${EDITOR:-nano} "$filename"
