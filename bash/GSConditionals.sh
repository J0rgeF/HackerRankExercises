read character

if [ $character = "Y" -o $character = "y" ]; then
    echo 'YES'
elif [[ $character = "N" || $character = "n" ]]; then
    echo 'NO'
fi