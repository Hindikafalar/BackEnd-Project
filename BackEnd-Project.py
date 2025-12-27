from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    rastgele_bilgi = ["Sivrisineklerin 47 tane dişi vardır.", "Bukalemunların dilleri,vücutlarından iki kat uzundur.", "Ördeğin sesi yankı yapmaz.", "Bir kağıdı yalnızca 40 defa ikiye katlarsanız uzunluğu aya kadar gidebilir.", "Hiçbir kağıt 7 defadan fazla 2'ye katlanamaz.", "Bal bozulmayan tek gıdadır.", "Dünyada insanlardan daha çok tavuk var.", "Otomobil sayısı insan sayısından 3 kat daha hızlı artıyor.", "El tırnakları ayak tırnaklarından 4 kat daha hızlı uzar.", "Sabahları elma kahveden daha fazla uykunuzu açar.", "Yerçekimsiz ortamda mum alevi küre şeklinde olur.", "Error", "Minecraft'ın yeni sürümü 1.20 artık yayında!", "hmm.. bilgi?", "Çok düşünen file ne denir? Filozof!", "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.", "Rocket League Sezon 12 Eylül'ün 9'unda geliyor.", "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.", "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
    secim = random.choice(rastgele_bilgi)
    return f"<p>Rastgele bilgi: {secim}</p>"

@app.route("/hilmi")
def hilmi():
    return "<h1> | Hilmi | </h1>"


#Yazı Tura
@app.route("/yazı-tura")
def yazıtura():
    liste = ["Yazı", "Tura"]
    yazitura = random.choice(liste)
    if yazitura == "Tura":
        return f"<h1>Yazı Tura</h1> <p>Sonuç: {yazitura}</p>"

    elif yazitura == "Yazı":
        return f"<h1>Yazı Tura</h1> <p>Sonuç: {yazitura}</p>"



#Zar Atma
@app.route("/zar-at")
def zaratma():
    zar = random.randint(1,6)
    if zar == 1:
        return f"<h1>Zar At</h1> <p>Zar: {zar}</p> <p>Şansın çok kötü çıktı..</p> <p><img src='https://elements-cover-images-0.imgix.net/4452067a-740e-4bae-b81c-bb9f8e972ac4?auto=compress%2Cformat&fit=max&w=1019&s=b0fbd2b16c0e6f0756051dd010598b67'</p>"

    elif zar == 2:
        return f"<h1>Zar At</h1> <p>Zar: {zar}</p> <p>Kötü.</p> <p><img src='https://elements-cover-images-0.imgix.net/4452067a-740e-4bae-b81c-bb9f8e972ac4?auto=compress%2Cformat&fit=max&w=1019&s=b0fbd2b16c0e6f0756051dd010598b67'</p>"

    elif zar == 3:
        return f"<h1>Zar At</h1> <p>Zar: {zar}</p> <p>İdare eder.</p> <p><img src='https://elements-cover-images-0.imgix.net/4452067a-740e-4bae-b81c-bb9f8e972ac4?auto=compress%2Cformat&fit=max&w=1019&s=b0fbd2b16c0e6f0756051dd010598b67'</p>"

    elif zar == 4:
        return f"<h1>Zar At</h1> <p>Zar: {zar}</p> <p>Güzel</p> <p><img src='https://elements-cover-images-0.imgix.net/4452067a-740e-4bae-b81c-bb9f8e972ac4?auto=compress%2Cformat&fit=max&w=1019&s=b0fbd2b16c0e6f0756051dd010598b67'</p>"

    elif zar == 5:
        return f"<h1>Zar At</h1> <p>Zar: {zar}</p> <p>Hoş!</p> <p><img src='https://elements-cover-images-0.imgix.net/4452067a-740e-4bae-b81c-bb9f8e972ac4?auto=compress%2Cformat&fit=max&w=1019&s=b0fbd2b16c0e6f0756051dd010598b67'</p>"

    elif zar == 6:
        return f"<h1>Zar At</h1> <p>Zar: {zar}</p> <p>*Şahane!*</p> <p><img src='https://elements-cover-images-0.imgix.net/4452067a-740e-4bae-b81c-bb9f8e972ac4?auto=compress%2Cformat&fit=max&w=1019&s=b0fbd2b16c0e6f0756051dd010598b67'</p>"




app.run(debug=True)
