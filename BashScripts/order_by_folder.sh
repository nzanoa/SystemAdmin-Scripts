#! /bin/bash


clear

echo
echo "Let's put things in order..."
echo

FOLDERS="Audios Binaries Compresseds Documents Exploits Pictures Videos"

for FOLDER in $FOLDERS
do
    # Associative Array to categorise all file types
    declare -A ITEMS=([Audios]="$(ls *mp3 *aac *wav 2> /dev/null)" 
    [Binaries]="$(ls *deb *AppImage *bundle *jar *exe 2> /dev/null)" 
    [Compresseds]="$(ls *zip *7z *gzip *tar *rar 2> /dev/null)" 
    [Documents]="$(ls *pdf  *docx *odt 2> /dev/null)" 
    [Exploits]="$(ls *sh *py *rb *html *php *txt 2> /dev/null)" 
    [Pictures]="$(ls *jpg *gif *jpeg *png 2> /dev/null)" 
    [Videos]="$(ls *mp4 *avi *flv 2> /dev/null)")

    if [ ! -e $FOLDER ]
    then
        # Propose to create folder since it doesn't exist
        echo "[!] We are going to create the folder $FOLDER "
        read -p "Type 'y' to proceed: " ANSWER
        echo
        
        if [ "$ANSWER" == "y" ]
        then
            mkdir $FOLDER
            echo "The folder $FOLDER has been successfully created"
        fi
    else
        for i in "${!ITEMS[@]}"
        do
            # Check and decide where each filetype should go
            if [ "$i" == "$FOLDER" ]
            then
                echo "[*] Move... ${ITEMS[$i]} ==> $FOLDER folder"
                mv ${ITEMS[$i]} $FOLDER 2> /dev/null
                echo
            fi
        done    
    fi
    sleep 0.5
done

echo "[*] Done !!! "

