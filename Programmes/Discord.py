from Options.Options import *

TitrePage("Serveur Discord (site)")

site = discord
navigateur = "Edge"

s=Service("./Driver/msedgedriver.exe")
driver = webdriver.Edge(service=s)

print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Démarrage de {couleur.CYAN}\"{navigateur}\"\n" + couleur.RESET)

driver.get(site)

print(f"\n{couleur.RED}[INFORMATION] |{couleur.LIGHTRED_EX} Accès au serveur Discord {couleur.CYAN}\"{site}\"\n" + couleur.RESET)

input(couleur.RED + "\nFais entrer pour continuer -> " + couleur.RESET)
Reset()

os.system("pause")