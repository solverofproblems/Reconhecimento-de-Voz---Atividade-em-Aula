import matplotlib.pyplot as plt
import librosa, librosa.display

nome_musica = "teste.wav"
valor_y, sr= librosa.load(nome_musica, sr=22000, mono=True)

#O Sr (samples per second) é responsável por medir quantas vezes o som será medido por segundo. Quanto maior for, mais claro é a representação
#visual das características do som.

# Cria a figura
plt.figure(figsize=(10, 4))
#O 10 é o valor em x (comprimento), e o 4 é o valor em y (largura)

#características do gráfico
librosa.display.waveshow(valor_y)
plt.title("Forma de Onda de {}".format(nome_musica))
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
#Serve para evitar que a formatação do eixo x, y, título e o próprio gráfico fiquem espalhados demais, ou então muito
#esprimidos. Em geral, ele prioriza a estética do gráfico de forma automática, sem precisar fazer isso na mão.
plt.show()
