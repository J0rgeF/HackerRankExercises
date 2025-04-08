counter=1

while [ $counter -le 50 ]
do
echo $counter
((counter+=1))
done