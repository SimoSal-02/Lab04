import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view


    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def languageChange(self,e):
        language = self._view._ddLingua.value
        if language != None:
            self._view._lv.controls.append(ft.Text("Il campo LINGUA è inserito correttamente!!",
                                                   color="blue"))
            self._view.page.update()
            return
    def searchModalityChange(self,e):
        modality = self._view._ddSearchModality.value
        if modality != None:
            self._view._lv.controls.append(ft.Text("Il campo MODALITY è inserito correttamente!!",
                                                   color="blue"))
            self._view.page.update()
            return
    def spellCheck(self,e):
        language = self._view._ddLingua.value
        self._view._ddLingua.value = None
        if language == None:
            self._view._lv.controls.append(ft.Text("Il campo LINGUA è vuoto!!",
                                                   color="red"))
            self._view.page.update()
            return

        modality = self._view._ddSearchModality.value
        self._view._ddSearchModality.value = None
        if modality == None:
            self._view._lv.controls.append(ft.Text("Il campo MODALITY è vuoto!!",
                                                   color="red"))
            self._view.page.update()
            return

        txtIn = self._view._txtIn.value
        self._view._txtIn.value = ""
        if txtIn == "":
            self._view._lv.controls.append(ft.Text("Il campo TESTO è vuoto!!",
                                                   color="red"))
            self._view.page.update()
            return
        if modality == "Contains":
            modality = "Default"

        lista = self.handleSentence(txtIn,language,modality)
        self._view._lv.controls.append(ft.Text(f"Frase inserita: {txtIn}"))
        self._view._lv.controls.append(ft.Text(f"Parole errate: {lista[0]}"))
        self._view._lv.controls.append(ft.Text(f"Il tempo impiegato è: {lista[1]}"))
        self._view.page.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

