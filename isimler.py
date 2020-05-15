from random import randint


adlar = ["enes" , "hasan" , "hüseyin" , "mete", "Mehmet","Mustafa",
"Ahmet","Ali","Hüseyin","Hasan","İbrahim","İsmail","Osman","Yusuf","Murat",
"Ömer","Ramazan","Halil","Süleyman","Abdullah","Mahmut","Recep","Salih","Fatih",
"Fatma","Ayşe","Emine","Hatice","Zeynep","Elif",
"Meryem","Şerife","Sultan","Zehra","Hanife","Merve",
"Havva","Zeliha","Fadime","Esra","Özlem","Hacer","Yasemin","Hülya"]

rasgelead = adlar[randint(0,44)]

soyadlar = ["YILMAZ","KAYA","DEMİR","ÇELİK","ŞAHİN","YILDIZ","YILDIRIM","ÖZTÜRK",
"AYDIN","ÖZDEMİR","ARSLAN","DOĞAN","KILIÇ","ASLAN","ÇETİN",
"KARA","KOÇ","KURT","ÖZKAN","ŞİMŞEK","POLAT","ÖZCAN","KORKMAZ","ÇAKIR","ERDOĞAN","YAVUZ",
"CAN","ACAR","ŞEN","AKTAŞ","GÜLER","YALÇIN","GÜNEŞ","BOZKURT",
"BULUT","KESKİN","ÜNAL","TURAN","GÜL","ÖZER","IŞIK","KAPLAN",
"AVCI","SARI","TEKİN""TAŞ","KÖSE","YÜKSEL","ATEŞ","AKSOY"]

rasgelesoyad = soyadlar[randint(0,48)]


rasgele_ad_soyad = rasgelead + " " + rasgelesoyad
