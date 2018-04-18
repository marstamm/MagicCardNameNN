for i in `seq 0 181`
do
 wget "http://gatherer.wizards.com/Pages/Search/Default.aspx?page=$i&action=advanced&cmc=|%3E[0]|=[0]" &
done
