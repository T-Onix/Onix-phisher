import random
from colorama import Fore 

Banner_color = (Fore.RED , Fore.MAGENTA , Fore.BLUE , Fore.GREEN)
def banner():
   global Banner_color

   print(fr"""{random.choice(Banner_color)}

    .-'''-.                                                                                                                                       
'   _    \                                                                                                                                     
/   /` '.   \    _..._   .--.                            _________   _...._        .        .--.         .              __.....__              
.   |     \  '  .'     '. |__|                            \        |.'      '-.   .'|        |__|      .'|          .-''         '.            
|   '      |  '.   .-.   ..--.                             \        .'```'.    '.<  |        .--.     <  |         /     .-''"'-.  `. .-,.--.  
\    \     / / |  '   '  ||  | ____     _____               \      |       \     \| |        |  |      | |        /     /________\   \|  .-. | 
`.   ` ..' /  |  |   |  ||  |`.   \  .'    /                |     |        |    || |  .'''-. |  |     _| | .'''-. |                  || |  | | 
    '-...-'`   |  |   |  ||  |  `.  `'    .'                 |      \      /    . | |/.'''. \|  |   .' |  | |/.'''. \\    .-------------'| |  | | 
            |  |   |  ||  |    '.    .'                   |     |\`'-.-'   .'  |  /    | ||  |  .   | /|  /    | | \    '-.____...---.| |  '-  
            |  |   |  ||__|    .'     `.   version : 1.3  |     | '-....-'`    | |     | ||__|.'.'| |//| |     | |  `.             .' | |      
            |  |   |  |      .'  .'`.   `.               .'     '.             | |     | |  .'.'.-'  / | |     | |    `''-...... -'   | |      
            |  |   |  |    .'   /    `.   `.           '-----------'           | '.    | '. .'   \_.'  | '.    | '.                   |_|      
            '--'   '--'   '----'       '----'                                  '---'   '---'           '---'   '---'                           
            
      {Fore.RESET}""")