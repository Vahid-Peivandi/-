#! /usr/bin/python
# -*- coding: utf- -*-
# khat aval shebangeh ke baesse mishe moshkell khord az address jari run beshe
import time
# module zaman seda zadeh shodeh
import sys
# modules khasi ra seda zadeh
import os
# in module baese mishe in file be sorat ghable hamle dar beyad
from PyQt4.QtCore import *
# vared karden tamame class haye qt barayeh paython
from PyQt4.QtGui import *


# vared karden tamame class haye qt barayeh panjreh graphiki
def window():
    # taref moteghayereh panjereh
    app = QApplication(sys.argv)
# barayeh greftan vorodi reshteh be kar mireh
    win = QDialog()
    # panjreh dialog ro taref mikoneh
    b1 = QPushButton(win)
    # esme dokmeh b1 ro vaghte feshar bedeen mishe nesbat mideh be panjreh win
    b1.setText(u"خواندن از فایل و مرتب کردن")
# gozashtan name barayeh dokmeh
    b1.move(325, 80)
# mokhtasat dokmeh
    b1.clicked.connect(b1_clicked)
    # vaghti clide b1 zadeh shod tabee b1_clicked seda zadeh mishe
    b2 = QPushButton(win)
    # esme dokmeh b2 zadeh shode nesbat mideh be panjreh win
    b2.setText(u"نوشتن فایل مرتب شده")
    # gozashtan name barayeh dokmeh
    b2.move(355, 140)
    # mokhtasat dokmeh
    QObject.connect(b2, SIGNAL("clicked()"), b2_clicked)
    """ vaghti roydadi etefagh oftad signali fresetadeh va codi ejra mishe,
    argoman aval name objecti hast ke signal ro mifresteh, argoman dovom signal
    hast, sevomin argoman codi ke ejra midhe hast"""
    b3 = QPushButton(win)
    """esme dokmeh b3 ro vaghte feshar dadan anjam mishe nesbat mideh be
     panjreh win"""
    b3.setText(u"ایجاد الویت پایین")
    # gozashtan name barayeh dokmeh
    b3.move(390, 200)
    # mokhtasat dokmeh
    b3.clicked.connect(b3_clicked)
# vaghti clide b3 zadeh shod tabee b3_clicked seda zadeh mishe

    b4 = QPushButton(win)
    b4.setText(u"پخش ویدئو")
    b4.move(420, 20)
    b4.clicked.connect(b4_clicked)

    b5 = QPushButton(win)
    b5.setText(u"سناریو ۱:ایجاد تاخیر در پخش کننده")
    b5.move(10, 20)
    b5.clicked.connect(b5_clicked)

    b6 = QPushButton(win)
    b6.setText(u"سناریو ۲:ایجاد تاخیر در مرورگر وب")
    b6.move(10, 80)
    b6.clicked.connect(b6_clicked)

    b7 = QPushButton(win)
    b7.setText(u"cpu میزان بکارگیری")
    b7.move(10, 140)
    b7.clicked.connect(b7_clicked)

    b8 = QPushButton(win)
    b8.setText(u"خروج")
    b8.move(10, 200)
    b8.clicked.connect(b8_clicked)

    b9 = QPushButton(win)
    b9.setText(u"قابلیت ها و اهداف برنامه")
    b9.move(100, 200)
    b9.clicked.connect(b9_clicked)

    win.setGeometry(365, 275, 610, 250)
# mokhtasat panjreh  va andazeh panjreh
    win.setWindowTitle(u"به نام خدا")
    # name panjreh
    win.show()
# neshan dadan panjreh va negah dashtanesh ta vaghti karbar bebendatesh
    sys.exit(app.exec_())
    # khoroj az python ba adade sefre ke yani vazeyat aadi

    content = 0


# meghdar shomarandeh barabar sefr ast
def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

    # moratab sazi hobabi


def b1_clicked():
    # tarif moteghayereh b1 vaghti click mishe
    global content
    # tarif sarasari bodan content
    start = time.time()
    # somarandeh zaman
    with open('unsort', 'r') as f:
        # file morde nazar ra faghat be sorate khandani baz kon
        content = [x.strip('\n') for x in f.readline()]
    # khandan khat be khat vorodi ke ba \n payan har khat moshakhas mishe
    bubble(content)
    # khototi ke khandeh shode ra be tabee moratab sazi hobabi mifrestad
    end = time.time()
    # pas az payan shomarandeh zaman motevaghef mishe
    print "Sorted succesfully and Time is:"
    # payami chap mikonad
    print (end - start)
    # zaman ra bar asase saniyeh va maghadir riz tar neshan midahad


def b3_clicked():
    # tarif moteghayereh b3 vaghti click mishe
    os.system("sudo renice -n 19 `pgrep -f qt.py`")
    # ejraye yek dastor shell


def b4_clicked():
    os.system("totem /home/hgfhgfghf/Desktop/Adrenaline.mkv &")


def b5_clicked():
    os.system("sudo renice -n 19  -p $(ps -ef | grep pulseaudio | grep -v grep\
      | awk '{print $2}') && totem /home/hgfhgfghf/Desktop/1.mp3 &")


def b7_clicked():
    os.system("gnome-terminal -e 'sh -c htop;bash'")


def b6_clicked():
    os.system("ps ex -o pid,fname|grep firefox > f && NUMBER=$(cat /home/hgfhgf\
      ghf/Desktop/f | tr -dc '0-9') && renice -n 19 -p $NUMBER")


def b8_clicked():
    os.system("ps ex -o pid,fname|grep qt.py > g && NUM=$(cat /home/hgfhgfghf/D\
      esktop/g | tr -dc '0-9') && kill $NUM")


def b9_clicked():
    os.system("gedit /home/hgfhgfghf/Desktop/guide &")


def b2_clicked():
    # tarif moteghayereh b2 vaghti click mishe
    f = open("sorted", 'w')
    """ fileli ra ba name morede nazar baz mikoneh va ba dastrsiyeh neveshtan
    min viseh"""
    f.writelines(["%s\n" % item for item in content])
    """ fileli ke moratab shode khat be khat neveshteh mishe ke reshteh ham
    ghabool mikoneh"""
    f.close()
    # file basteh mishe


if __name__ == '__main__':
    # barayeh dastrsiyeh majolle be sorate sarasari ast
window()

