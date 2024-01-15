#!/usr/bin/env python3
# -*- coding: utf8 -*-

import flet as ft
import time
import random
from threading import Timer

f = open(r'russian.txt').readlines()
letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
           "х", "ц", "ч", "ш", "щ", "ы", "э", "ю", "я"]

sogls = ['б', "в", "г", "д", "ж", "з" "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ч", "щ", "ш"]
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]


def proverka(choser):
    if choser[0] in sogls and choser[1] in vse_gls:
        return True
    if choser[1] in sogls and choser[0] in vse_gls:
        return True
    return False


def create():
    while True:
        choser = ''.join(random.choices(letters, k=2))
        if proverka(choser):
            return choser


def task(message):
    # report the custom message

    print(message)

    raise NameError('HiThere')


def check_input(choser, f):
    while True:
        inn = input(f'{choser}:-')
        if f'{inn}\n' in f:

            break
        else:
            print('плох')
    return True


def main(page):
    historsis = []  # list of words

    def btn_click1(e):
        page.splash = ft.ProgressBar()
        btn_1.disabled = True
        btn_1.visible = False
        mycon.visible = False
        page.update()
        time.sleep(2)
        page.splash = None

        def btn_click(e):  # game backend
            if len(history.controls) > 1:
                history.controls.pop(0)
            if f'{typetext.value.lower()}\n' in f and len(typetext.value) > 2 and \
                    typetext.value.lower() not in historsis and tasker.controls[-1].value in typetext.value.lower():

                history.controls.append(ft.Text(f"{typetext.value.lower()}",size=20,
                                       font_family="RobotoSlab",
                                       weight=ft.FontWeight.W_100))
                points.value = str(int(points.value) + 1)
                #print(list(map(lambda x: x.value, history.controls)))
                tasker.controls.clear()
                typetext.value = ""

                chosere = create()
                tasker.controls.append(ft.Text(f"{chosere}",
                                               size=30, font_family="RobotoSlab", weight=ft.FontWeight.W_100))
                typetext.focus()
                page.update()
                historsis.append((history.controls[-1].value.lower()))
            else:

                history.controls.append(ft.Text(f"{typetext.value}-Не существует!", size=20,
                                       font_family="RobotoSlab",
                                       weight=ft.FontWeight.W_100))
                typetext.value = ""
                typetext.focus()
                page.update()



        def on_keyboard(e: ft.KeyboardEvent): #enter input
            if e.key == "Enter":
                btn_click(e)

        page.on_keyboard_event = on_keyboard
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        points = ft.Text("0", size=20,
                                       font_family="RobotoSlab",
                                       weight=ft.FontWeight.W_100)
        choser = create()
        tasker = ft.Column()
        tasker.controls.append(ft.Text(f"{choser}", size=30,
                                       font_family="RobotoSlab",
                                       weight=ft.FontWeight.W_100))
        typetext = ft.TextField(label="Погнали!", autofocus=True, cursor_color=ft.colors.BLUE, cursor_radius=100,
                                icon=ft.icons.CREATE_ROUNDED, border_radius=90, text_align=ft.TextAlign.CENTER)
        history = ft.Column()
        buttton = ft.ElevatedButton("проверка", on_click=btn_click)

        # --------------------------------------------------добавление на страницу
        page.add(points, tasker, typetext, buttton, history)

    # --------------------------------------------------start
    page.title = "JKLMru"
    page.scroll = "adaptive "
    page.bgcolor = "#363333"


    btn_1 = ft.Row(
        controls=[
            ft.ElevatedButton("погнали!", on_click=btn_click1,
                              scale=3,
                              width=200,
                              height=470,
                              color=ft.colors.BLUE_50,
                              )
        ],

    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    mycon = ft.Container(
        bgcolor="white",
        width=400,
        height=100,
        content=ft.Text("Добро пожаловать в русскую версию игры BоmbParty! Цель игры - ввести слово,"
                        " в состав которого будет входить данное вам словосочетание. Правила:"
                        " 1) Не повторяться 2) Не нервничать. Приятной игры!", color="black"),
        opacity=1,
        animate_opacity=ft.animation.Animation(duration=300, curve="easeInCubic"),
        margin=ft.margin.only(top=50, left=20),
        offset=ft.transform.Offset(0, 0),
        border_radius=10,)
    page.add(btn_1, mycon)


ft.app(target=main, view=ft.WEB_BROWSER)
