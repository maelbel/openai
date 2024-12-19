## Exercice

1. Création de méthodes pour DALL-E

Méthode openai_create_image : Cette méthode devrait prendre en entrée un prompt textuel et utiliser l'API DALL-E d'OpenAI pour générer une image en fonction du prompt fourni. L'image générée devrait être renvoyée en sortie de la méthode.
Méthode openai_create_image_variation : Cette méthode devrait prendre en entrée une image existante et un prompt textuel et utiliser l'API DALL-E d'OpenAI pour créer une variante de l'image en fonction du prompt. La variante de l'image devrait être renvoyée en sortie de la méthode.

2. Bonus - Connexion à l'API ChatGPT

Vous pouvez ajouter une fonctionnalité bonus en intégrant la connexion à l'API ChatGPT pour améliorer la génération de prompts textuels. Voici comment vous pourriez le faire :
Méthode generate_prompt_with_chatgpt : Cette méthode devrait prendre en entrée un texte fourni par l'utilisateur et utiliser l'API ChatGPT pour générer un prompt textuel amélioré en fonction du texte fourni. Le prompt amélioré devrait être renvoyé en sortie de la méthode. Le prompt amélioré devrait être renvoyé en sortie de la méthode.

-> Intégrer ces fonctionnalités dans une nouvelle page Streamlit
-> Bonus : Ajouter la possibilité de télécharger les images générés via un bouton


[Exercice]
Créer un assistant vocal basé sur le chatbot.
Vous devez utiliser whisper pour prendre l'entrée utilisateur afin de l'envoyer à l'api gpt-4o-mini. Enfin il faudra convertir la réponse de l'assistant en audio via l'api TTS.



[Exercice]
Créez une application interactive qui raconte une histoire dont vous êtes le héros.
Utilisation combinée des différentes fonctionnalités vues jusqu'ici, votre application doit prendre un thème suggéré par l'utilisateur puis vous retourner une histoire pour enfants sur le sujet.
L'application proposera page par page du texte (+/- 1 paragraphe), une narration/lecture audio, une image adaptée au texte actuel et enfin, des boutons représentants différentes suites possibles.
Lorsque l'utilisateur clique sur un de ces boutons, votre application doit fournir une nouvelle page proposant la suite de l'histoire.
Il faudra utiliser gpt-4o-mini, l'api tts et dall-e.
 
[Bonus]
Donnez à l'utilisateur la possibilité de revenir en arrière pour explorer d'autres choix, il faudra garder toutes les pages en mémoire pour que ce soit possible.