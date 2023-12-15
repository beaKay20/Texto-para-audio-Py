import pyttsx3

# Carrega a lib #
engine = pyttsx3.init()

# Texto que a engine vai falar 

engine.say('Olá, tudo bem?.')
engine.say('Como está seu dia?.')
engine.say('Qual a sua dúvida?.')


# Executa #
engine.runAndWait()