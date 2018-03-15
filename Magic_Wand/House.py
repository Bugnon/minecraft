import pymedia

player = pymedia.Player() #Création de l'objet player
player.start()
player.startPlayback('unFichierSon.mp3') #Chemin du fichier son à lire
  
while player.isPlaying(): #On boucle tant que la lecture n'est pas terminée
    time.sleep( 0.01 )