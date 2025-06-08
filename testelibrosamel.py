import numpy
import librosa
import matplotlib.pyplot as plt

lista_audio, amostra_segundo = librosa.load('teste.wav', sr=22050, mono=True)

valores_matriz = librosa.feature.melspectrogram(
    y=lista_audio,
    sr=amostra_segundo,
    n_fft=2048,
    hop_length=512,
    fmin = 0.0,
    fmax = amostra_segundo/2
)

valores_matriz_emDb = librosa.power_to_db(valores_matriz, ref=numpy.max)

plt.figure(figsize=(10,4))
librosa.display.specshow(
    valores_matriz_emDb,
    sr=amostra_segundo,
    hop_length=512
)

plt.title('Espectrograma de "teste.wav"')
plt.ylabel('Escala Mel')
plt.xlabel('Tempo(s)')
plt.colorbar(label="Decibéis (Db)")
plt.tight_layout()
plt.show()