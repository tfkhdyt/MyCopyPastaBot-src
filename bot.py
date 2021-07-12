import telebot, time, os
from flask import Flask, request

token = "insert token here"
bot = telebot.TeleBot(token)
server = Flask(__name__)

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Selamat datang di Degenerator Bot, {name} 😉\nKetik /help untuk bantuan")

@bot.message_handler(commands=['help'])
def help(message):
    bantu = "Cara menggunakan:\n/wangy nama\nContoh:\n/wangy eimi\n\nKetik /list untuk melihat daftar copypasta"
    bot.reply_to(message, bantu)

# list

@bot.message_handler(commands=['list'])
def tampilkanDaftar(message):
    daftar = """Daftar copypasta:
• /wangy [nama] : Copypasta wangy wangy
• /simp [nama] : Copypasta simp sangean
• /halu [nama] : Copypasta halu Genshin Impact
• /gemeteran [nama] : Copypasta gemeteran
• /pregnant [nama] : Copypasta pregnant (English)
• /nenen [nama] : Copypasta nenen croooototototot
• /waifu [nama] : Copypasta claim waifu
• /mock [kalimat] : SeNtEnCe mOcKiFy"""
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
    
@bot.message_handler(commands=['gemeteran'])
def cpGemeteran(message):
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

    result = f'Bro, gue gemeteran. GUE GEMETERAN ANJING Gue gak pernah mau berkembangbiak dengan siapapun lebih daripada seorang {namaTitle}. Badannya yang cakep, TETE GEDE, pinggul seksi dari seorang BIDADARI. Jujur aja, sakit hati kalau tau KENYATAANNYA gue GAK AKAN PERNAH BISA BUAT KAWIN SAMA DIA, ngewarisin gen gue lewat dia, dan ngebiarin dia ngelahirin anak yang sempurna dari gue.Gue rela ngelakuin APAPUN demi kesempatan buat bikin {namaTitle} hamil. A P A P U N. Dan gue bener-bener gk bisa terima kenyataan. Kenapa Authornya rela bikin suatu hal yang sempurna kyk dia? Buat ngegoda kita? NGETAWAIN KITA DI DEPAN MUKA?SUMPAH BRO, GUE UDAH BENER BENER GAK TAHAN. ANJING.'
    msg = bot.reply_to(message, "Copypasta sedang diproses...")
    time.sleep(1)
    bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text=result)
    
@bot.message_handler(commands=['pregnant'])
def cpPregnant(message):
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

    result = f"I would literally never stop trying to impregnate {namaTitle}. Every day I would wake her up by coming in her and every night I would cum in her right before going to sleep, which I would do with my dick stuck insider her. I would take some viagra before bed just to maintain my erection so that she'll be ready in the morning when I thrust into her like an animal and slather her in kisses. Part of our wedding vows would be to have as many children as physically possible. I wouldn't even care if she's already pregnant, I'll fuck her while she's pregnant and she'll get double pregnant. I'll fill her with so much cum every day that she'll look pregnant even when she isn't (which she'll never be after we're married) I would do everything in my power to make {namaTitle} as fertile as possible. I'd give her fertility drugs, I'd give her uterus massages, breast massages, I wouldn't let her go 12 hours without at least one spastic orgasm. I'll even bake her home made lactation inducing biscuits to help her get to a point of hyperlactation syndrome so that she'll be seeping out multiple quarts of milk per day. Which I will save and drink just so that I can tell her how delicious it is. I'll make her so fertile that triplets will be the minimum number she's carrying at any given time. I would literally never stop doting on her, I would respond to her every beck and call and I would cum inside her again each time she asks for something. She would be so pregnant all the time that she would literally not be able to stand up straight anymore even after menopause. Her spine would be permanently bent out of shape to accommodate a pregnant belly. Even after she can't get pregnant anymore I would just keep putting more eggs into her. I would clone her purely so that I can put fresh eggs from the clone inside her after she runs out of them. She would have so much progesterone running through her veins at any given time that even the thought of not being pregnant would seem alien to her."
    msg = bot.reply_to(message, "Copypasta sedang diproses...")
    time.sleep(1)
    bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text=result)
    
@bot.message_handler(commands=['nenen'])
def cpNenen(message):
    nama = extract_arg(message.text)
    nama = " ".join(nama)
    namaTitle = nama.title()
    namaUpper = nama.upper()
    namaLower = nama.lower()
    """vokal = ["A","I","U","E","O"]
    if(namaUpper[-1] in vokal):
        namaPanjang = namaUpper + namaUpper[-1] * 14
    elif(namaUpper[-2] in vokal):
        namaPanjang = namaUpper[:-2] + namaUpper[-2] * 14 + namaUpper[-1] * 3
    else:
        namaPanjang = namaUpper[:-3] + namaUpper[-3] * 14 + namaUpper[-2] * 3 + namaUpper[-1] * 2"""

    result = f"NENEN NENEN KEPENGEN NENEN SAMA {namaUpper}. TETEK GEDE NAN KENCANG MILIK {namaUpper} MEMBUATKU KEPENGEN NENEN. DIBALUT PAKAIAN KETAT YANG ADUHAI CROOOOTOTOTOTOTOT ANJING SANGE GUA BANGSAT. {namaUpper}, PLIS DENGERIN BAIK BAIK. TOLONG BUKA BAJU SEBENTAR SAJA PLISSS TOLOOONG BANGET, BIARKAN MULUT KERINGKU BISA MENGECAP NENEN {namaUpper}. BIARKAN AKU MENGENYOT NENENMU {namaUpper}. AKU RELA NGASIH SESEMBAHAN APA AJA BERAPAPUN ITU DUIT YANG AKU BAKAR KHUSUS TERKHUSUS BUATMU. TAPI TOLOOOONG BANGET BUKA BAJUMU AKU MAU NENEN. NENEN NENEEEEN NENEN {namaUpper} WANGIIII"
    msg = bot.reply_to(message, "Copypasta sedang diproses...")
    time.sleep(1)
    bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text=result)
    
@bot.message_handler(commands=['waifu'])
def cpWaifu(message):
    nama = extract_arg(message.text)
    nama = " ".join(nama)
    namaTitle = nama.title()
    namaUpper = nama.upper()
    namaLower = nama.lower()
    """vokal = ["A","I","U","E","O"]
    if(namaUpper[-1] in vokal):
        namaPanjang = namaUpper + namaUpper[-1] * 14
    elif(namaUpper[-2] in vokal):
        namaPanjang = namaUpper[:-2] + namaUpper[-2] * 14 + namaUpper[-1] * 3
    else:
        namaPanjang = namaUpper[:-3] + namaUpper[-3] * 14 + namaUpper[-2] * 3 + namaUpper[-1] * 2"""

    result = f"Sejujurnya gw ga nyangka ama tindakan lo yg ga dewasa begini Kita udh temenan dri kecil ,melalui berbagai kenangan ,tapi sikaplo begini ke gw ,ga habis pikir. Padahal sudah berjanji tidak mengusik hubungan satu sama lain lagi ,tapi maksud tindakan mu sekarang ini apa? Tiba tiba di pagi bangun tidur lu make Pp {namaTitle}. Lu kira lucu begitu anjing? Make waifu pp org seenaknya? Ngeklaim pula bangsad maksudnya apa apaan coba . Pertemanan dari kecil kita ga dihargai sama sekali. Gw tunggu klarifikasi lo "
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
    # masukkan link hosting bot nya
    bot.set_webhook(url='https://mycopypastabot.herokuapp.com/' + token)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
