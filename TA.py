#mport ime

SFFRON = "\03[38;5;208m"      
SAFFRON_BG = "\033[48;5;208m"   
WHITE_BG = "\033[47m"           
GREEN_BG = "\033[48;5;34m"      
BLUE = "\033[38;5;27m"          
BOLD = "\033[1m"
RESET = "\033[0m"

def print_tiranga():
    width = 40
    
    #print(f"{BOLD}{SAFFRON}           🇮🇳  Dev Kushwaha 🇮🇳{RESET}\n")
    print(f"{BOLD}Jai Hind! Vande Mataram{RESET}\n")
    print(f"{BOLD}Happy independence day{RESET}\n")
    print(f"{BOLD}{SAFFRON}           🇮🇳  JAI HIND  🇮🇳{RESET}\n")
    time.sleep(0.3)
        
    for i in range(3):
        print(f"{SAFFRON_BG}{' ' * width}{RESET}")
        time.sleep(0.1)
    
    print(f"{WHITE_BG}{' ' * width}{RESET}")
    
    chakra = " ☸ "
    space = " " * ((width - len(chakra)) // 2)  
    print(f"{WHITE_BG}{space}{BLUE}{BOLD}{chakra}{WHITE_BG}{space}{RESET}")
    
    print(f"{WHITE_BG}{' ' * width}{RESET}")
    time.sleep(0.1)
        
    for i in range(3):
        print(f"{GREEN_BG}{' ' * width}{RESET}")
        time.sleep(0.1)
    
    print(f"\n{BOLD}{SAFFRON}Vande Mataram!{RESET}")

if __name__ == "__main__":
    print_tiranga()##Dev_kushwaha
import time

SAFFRON = "\033[38;5;208m"      
SAFFRON_BG = "\033[48;5;208m"   
WHITE_BG = "\033[47m"           
GREEN_BG = "\033[48;5;34m"      
BLUE = "\033[38;5;27m"          
BOLD = "\033[1m"
RESET = "\033[0m"

def print_tiranga():
    width = 40
    
    #print(f"{BOLD}{SAFFRON}           🇮🇳  Dev Kushwaha 🇮🇳{RESET}\n")
    print(f"{BOLD}Jai Hind! Vande Mataram{RESET}\n")
    print(f"{BOLD}Happy independence day{RESET}\n")
    print(f"{BOLD}{SAFFRON}           🇮🇳  JAI HIND  🇮🇳{RESET}\n")
    time.sleep(0.3)
        
    for i in range(3):
        print(f"{SAFFRON_BG}{' ' * width}{RESET}")
        time.sleep(0.1)
    
    print(f"{WHITE_BG}{' ' * width}{RESET}")
    
    chakra = " ☸ "
    space = " " * ((width - len(chakra)) // 2)  
    print(f"{WHITE_BG}{space}{BLUE}{BOLD}{chakra}{WHITE_BG}{space}{RESET}")
    
    print(f"{WHITE_BG}{' ' * width}{RESET}")
    time.sleep(0.1)
        
    for i in range(3):
        print(f"{GREEN_BG}{' ' * width}{RESET}")
        time.sleep(0.1)
    
    print(f"\n{BOLD}{SAFFRON}Vande Mataram!{RESET}")

if __name__ == "__main__":
    print_tiranga()
