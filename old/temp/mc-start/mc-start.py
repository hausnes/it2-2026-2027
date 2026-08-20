import subprocess

# Stien til Minecraft-serveren si JAR-fil
server_jar = "minecraft_server.1.20.1.jar"  # Endre til riktig filnavn
minne_allokering = "-Xmx8G -Xms4G"  # Juster minne etter behov, xmx er maks, xms er start

# Kommando for å starte serveren
kommando = f"java {minne_allokering} -jar {server_jar} nogui"

try:
    print("Startar Minecraft-serveren...")
    subprocess.run(kommando, shell=True, check=True)
    print("Minecraft-serveren blei starta.")
except subprocess.CalledProcessError as e:
    print(f"Feil ved oppstart av serveren: {e}")