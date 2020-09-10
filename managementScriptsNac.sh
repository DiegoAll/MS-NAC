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
echo "(4) Monthly reports"
echo "(5) About"
echo "(9) Exit"
echo ""
echo "      Type the number of the option you want and press enter"
read opcion
case $opcion in

1)sh unregNodes.py; exit;;
2)sh serverMaint.py; exit ;;
3)python snortG3N; exit;;
4)sh montlyReports.py; exit ;;
5)python about.py;;
9)exit;;
esac
sleep 2
date
done
