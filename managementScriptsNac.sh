echo " __  __ ____        _   _    _    ____ 
|  \/  / ___|      | \ | |  / \  / ___|
| |\/| \___ \ _____|  \| | / _ \| |    
| |  | |___) |_____| |\  |/ ___ \ |___ 
|_|  |_|____/      |_| \_/_/   \_\____|
                                       
"
echo "By DiegoAll"
echo "contact: dposadallano@gmail.com"
echo ""
echo "MANAGEMENT SCRIPTS NAC"
while :
do
echo "(1) Unregister Nodes"
echo "(2) Server Maintenance"
echo "(3) SnortG3N"
echo "(4) Config File Extractor"
echo "(5) About"
echo "(6) Documentation"
echo "(9) Exit"
echo ""
echo "      Type the number of the option you want and press enter"
read opcion
case $opcion in

1)python unregNodes.py; exit;;
2)sh serverMaint.sh; exit ;;
3)python snortG3N.py; exit;;
4)python configFileExtractor.py; exit ;;
5)python about.py;;
6)more documentation;;
9)exit;;
esac
sleep 2
date
done
