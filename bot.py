import telebot
import time
import os
from flask import Flask, request

token = ""
bot = telebot.TeleBot(token)
server = Flask(__name__)

def extract_arg(arg):
    return arg.split()[1:]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Selamat datang di bot Copypasta Generator, {name} 😉😉😉\nKetik /help untuk bantuan")

@bot.message_handler(commands=['help'])
def help(message):
    bantu = "Cara menggunakan:\n/wangy nama\nContoh:\n/wangy eimi\n\nKetik /list untuk melihat daftar copypasta"
    bot.reply_to(message, bantu)

@bot.message_handler(commands=['list'])
def tampilkanDaftar(message):
    daftar = "Daftar copypasta:\n• /wangy [nama] : Copypasta wangy wangy\n• /simp [nama] : Copypasta simp sangean\n• /halu [nama] : Copypasta halu Genshin Impact\n• /mock [kalimat] : SeNtEnCe mOcKiFy"
    bot.reply_to(message, daftar)

# daftar list copypasta
@bot.message_handler(commands=['wangy'])
def cpWangy(message):
    nama = extract_arg(message.text)
    nama = " ".join(nama)
    namaTitle = nama.title()
    namaUpper = nama.upper()
    namaLower = nama.lower()
    vokal = ["A","I","U","E","O"]
    if(namaUpper[-1] in vokal):
        namaPanjang = namaUpper + namaUpper[-1] * 14
    elif(namaUpper[-2] in vokal):
        namaPanjang = namaUpper[:-2] + namaUpper[-2] * 14 + namaUpper[-1] * 3
    else:
        namaPanjang = namaUpper[:-3] + namaUpper[-3] * 14 + namaUpper[-2] * 3 + namaUpper[-1] * 2

    result = f"{namaUpper}......... {namaUpper} {namaPanjang} AAAAAAAAAAAAAAAAAAAAAAAGH ❤ ❤ ❤ ❤ WANGI WANGI WANGI WANGI HU HA HU HA HU HA, aaaah baunya {namaLower} wangi aku mau nyiumin aroma wanginya {namaLower}AAAAAAAH ~~ Rambutnya.... aaah rambutnya juga pengen aku elus-elus ~~~~~ AAAAAH {namaUpper} keluar pertama kali juga manis ❤ ❤ ❤ dia pas ngedesah juga manis banget AAAAAAAAH {namaUpper}LUCCUUUUUUUUUUUUUUU............ GUA BAKAL BAKAR DUIT 12 JUTA RUPIAH BUAT {namaUpper} AAAAAAAAAAAAAAAAAAAAAAAAAAAAGH ❤ ❤ ❤ \napa ? {namaTitle} itu gak nyata ? Cuma karakter 2 dimensi katamu ? nggak, ngak ngak ngak ngak NGAAAAAAAAK GUA GAK PERCAYA ITU DIA NYATA NGAAAAAAAAAAAAAAAAAK BANGSAAAAAT !! GUA GAK PEDULI SAMA KENYATAAN POKOKNYA GAK PEDULI. {namaLower} ngeliat gw ... {namaUpper} di laptop ngeliatin gw. ❤ ❤ ❤ {namaLower}... kamu percaya sama aku ? aaaaaaaaaaah syukur {namaLower} gak malu merelakan aku aaaaaah ❤ ❤ ❤ YEAAAAAAAAAAAH GUA MASIH PUNYA {namaUpper} HU HA HU HI HU HA HU HI AKU SAYANG {namaUpper} AKU CINTA {namaUpper} AKU SUAMII {namaUpper}"
    msg = bot.reply_to(message, "Copypasta sedang diproses...")
    time.sleep(1)
    bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text=result)
    # bot.reply_to(message, result)

@bot.message_handler(commands=['simp'])
def cpSimp(message):
    nama = extract_arg(message.text)
    nama = " ".join(nama)
    namaTitle = nama.title()
    # namaUpper = nama.upper()
    # namaLower = nama.lower()
    """vokal = ["A","I","U","E","O"]
    if(namaUpper[-1] in vokal):
        namaPanjang = namaUpper + namaUpper[-1] * 14
    elif(namaUpper[-2] in vokal):
        namaPanjang = namaUpper[:-2] + namaUpper[-2] * 14 + namaUpper[-1] * 3
    else:
        namaPanjang = namaUpper[:-3] + namaUpper[-3] * 14 + namaUpper[-2] * 3 + namaUpper[-1] * 2"""

    result = f"Buruan, panggil gue SIMP, ato BAPERAN. ini MURNI PERASAAN GUE. Gue pengen genjot bareng {namaTitle}. Ini seriusan, suaranya yang imut, mukanya yang cantik, apalagi badannya yang aduhai ningkatin gairah gue buat genjot {namaTitle}. Setiap lapisan kulitnya pengen gue jilat. Saat gue mau crot, gue bakal moncrot sepenuh hati, bisa di perut, muka, badan, teteknya, sampai lubang burit pun bakal gue crot sampai puncak klimaks. Gue bakal meluk dia abis gue moncrot, lalu nanya gimana kabarnya, ngrasain enggas bareng saat telanjang. Dia bakal bilang kalau genjotan gue mantep dan nyatain perasaannya ke gue, bilang kalo dia cinta ama gue. Gue bakal bilang balik seberapa gue cinta ama dia, dan dia bakal kecup gue di pipi. Terus kita ganti pakaian dan ngabisin waktu nonton film, sambil pelukan ama makan hidangan favorit. Gue mau {namaTitle} jadi pacar, pasangan, istri, dan idup gue. Gue cinta dia dan ingin dia jadi bagian tubuh gue. Lo kira ini copypasta? Kagak cok. Gue ngetik tiap kata nyatain prasaan gue. Setiap kali elo nanya dia siapa, denger ini baik-baik : DIA ISTRI GUE. Gue sayang {namaTitle}, dan INI MURNI PIKIRAN DAN PERASAAN GUE."
    msg = bot.reply_to(message, "Copypasta sedang diproses...")
    time.sleep(1)
    bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text=result)


@bot.message_handler(commands=['halu'])
def cpHalu(message):
    nama = extract_arg(message.text)
    nama = " ".join(nama)
    namaTitle = nama.title()
    # namaUpper = nama.upper()
    namaLower = nama.lower()
    """vokal = ["A","I","U","E","O"]
    if(namaUpper[-1] in vokal):
        namaPanjang = namaUpper + namaUpper[-1] * 14
    elif(namaUpper[-2] in vokal):
        namaPanjang = namaUpper[:-2] + namaUpper[-2] * 14 + namaUpper[-1] * 3
    else:
        namaPanjang = namaUpper[:-3] + namaUpper[-3] * 14 + namaUpper[-2] * 3 + namaUpper[-1] * 2"""

    result = f'Usiaku 22 tahun. Aku sangat mencintai {namaTitle}, aku punya semua Figurine dan wallpapernya. Aku berdoa setiap malam dan berterima kasih atas segala hal yang telah ia berikan kepadaku. "{namaTitle} adalah cinta" aku bilang "{namaTitle} adalah Tujuan Hidupku". Temanku datang ke kamarku dan berkata "HALU LU ANJING !!". Aku tau dia cemburu atas kesetiaanku kepada {namaLower}. Lalu kukatakan padanya "BACOT NJING !!". Temanku menampol kepalaku dan menyuruhku untuk tidur. Kepalaku sakit dan aku menangis. Aku rebahan di kasur yang dingin, lalu ada sesuatu yang hangat menyentuhku. Ternyata {namaTitle} datang ke dalam kamarku, Aku begitu senang bertemu {namaLower}. Dia membisikan ke telingaku, "Kamu adalah impianku" Dengan tangannya dia meraih diriku. Aku melebarkan pantatku keatas demi {namaTitle}. Dia menusukan sesuatu kedalam Anggusku. begitu sakit, tapi kulakukan itu demi {namaTitle}. Aku ingin memberikan kepuasan kepada {namaTitle}. Dia meraum bagaikan singa, disaat dia melepaskan cintanya kedalam Anggusku. Temanku masuk kekamarku dan berkata "....... Anjing". {namaTitle} melihat temanku dan berkata " Semua sudah berakhir" Dengan menggunakan kemampuannya Stellar Restoration {namaTitle} pergi meninggalkan kamarku. "{namaTitle} itu cinta" "{namaTitle} itu kehidupan".'
    msg = bot.reply_to(message, "Copypasta sedang diproses...")
    time.sleep(1)
    bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text=result)
#bot.polling()

@bot.message_handler(commands=['mock'])
def cpMock(message):
    str = extract_arg(message.text)
    str = " ".join(str)
    strBaru = ""
    panjang = len(str)
    for i in range(0,panjang):
        if((i % 2) == 0):
            strBaru = strBaru + f"{str[i].upper()}"
        else:
            strBaru = strBaru + f"{str[i].lower()}"
    msg = bot.reply_to(message, "MoCkIfY SeDaNg dIpRoSeS...")
    time.sleep(1)
    bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text=strBaru)

@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://mycopypastabot.herokuapp.com/' + token)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
