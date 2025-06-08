import librosa
import numpy as np
import soundfile as sf

nome_arquivo = 'testes.wav'
lista_audio, amostra_segundo = librosa.load(nome_arquivo, sr=22050, mono=True)


intervalos = librosa.effects.split(lista_audio, top_db=30)
print(intervalos)

audio_sem_silencio = np.concatenate([lista_audio[inicio:fim] for inicio, fim in intervalos])
print(audio_sem_silencio)

novo_arquivo = 'sem_silencio.wav'
sf.write(novo_arquivo, audio_sem_silencio, amostra_segundo)
