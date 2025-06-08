import matplotlib.pyplot as plt
import numpy
import librosa

nome_musica = "teste.wav"
lista_audio, amostra_segundo= librosa.load(nome_musica, sr=22050, mono=True)

D = librosa.stft(lista_audio, n_fft=2048, hop_length=512)
S_db = librosa.amplitude_to_db(D, ref=numpy.max)

plt.figure(figsize=(10, 4))

librosa.display.waveshow(lista_audio)
plt.title("Forma de Onda de {}".format(nome_musica))
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
