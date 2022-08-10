import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from language import Language

dict_key = Language.read_dict()


#region Read_Languages
list_languages = []

language_ar = Language.read_languages("Language_ar.xml")
language_bg = Language.read_languages("Language_bg.xml")
language_ch = Language.read_languages("Language_ch.xml")
language_cs = Language.read_languages("Language_cs.xml")
language_da = Language.read_languages("Language_da.xml")
language_de = Language.read_languages("Language_de.xml")
language_el = Language.read_languages("Language_el.xml")
language_en = Language.read_languages("Language_en.xml")
language_en_AU = Language.read_languages("Language_en-AU.xml")
language_en_US = Language.read_languages("Language_en-US.xml")
language_es = Language.read_languages("Language_es.xml")
language_es_MX = Language.read_languages("Language_es-MX.xml")
language_et = Language.read_languages("Language_et.xml")
language_fi = Language.read_languages("Language_fi.xml")
language_fr = Language.read_languages("Language_fr.xml")
language_fr_CA = Language.read_languages("Language_fr-CA.xml")
language_hr = Language.read_languages("Language_hr.xml")
language_hu = Language.read_languages("Language_hu.xml")
language_is = Language.read_languages("Language_is.xml")
language_it = Language.read_languages("Language_it.xml")
language_ja = Language.read_languages("Language_ja.xml")
language_lt = Language.read_languages("Language_lt.xml")
language_lv = Language.read_languages("Language_lv.xml")
language_nl = Language.read_languages("Language_nl.xml")
language_no = Language.read_languages("Language_no.xml")
language_pl = Language.read_languages("Language_pl.xml")
language_pt = Language.read_languages("Language_pt.xml")
language_pt_BR = Language.read_languages("Language_pt-BR.xml")
language_ro = Language.read_languages("Language_ro.xml")
language_ru = Language.read_languages("Language_ru.xml")
language_sk = Language.read_languages("Language_sk.xml")
language_sl = Language.read_languages("Language_sl.xml")
language_sr = Language.read_languages("Language_sr.xml")
language_sv = Language.read_languages("Language_sv.xml")
language_tr = Language.read_languages("Language_tr.xml")
language_uk = Language.read_languages("Language_uk.xml")

list_languages.append(language_ar)
list_languages.append(language_bg)
list_languages.append(language_ch)
list_languages.append(language_cs)
list_languages.append(language_da)
list_languages.append(language_de)
list_languages.append(language_el)
list_languages.append(language_en)
list_languages.append(language_en_AU)
list_languages.append(language_en_US)
list_languages.append(language_es)
list_languages.append(language_es_MX)
list_languages.append(language_et)
list_languages.append(language_fi)
list_languages.append(language_fr)
list_languages.append(language_fr_CA)
list_languages.append(language_hr)
list_languages.append(language_hu)
list_languages.append(language_is)
list_languages.append(language_it)
list_languages.append(language_ja)
list_languages.append(language_lt)
list_languages.append(language_lv)
list_languages.append(language_nl)
list_languages.append(language_no)
list_languages.append(language_pl)
list_languages.append(language_pt)
list_languages.append(language_pt_BR)
list_languages.append(language_ro)
list_languages.append(language_ru)
list_languages.append(language_sk)
list_languages.append(language_sl)
list_languages.append(language_sr)
list_languages.append(language_sv)
list_languages.append(language_tr)
list_languages.append(language_uk)

#endregion

class LanguageGenerator(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        self.combo_label = ttk.Label(text="Language.xml Key:")
        self.combo_label.grid(column=0, row=0, sticky='nw', **options)

        self.combo_key = ttk.Combobox(values=dict_key, width='50', postcommand=self.get_new_dict)
        self.combo_key.grid(column=0, row=1, sticky='nw', **options)
        self.combo_key.bind("<<ComboboxSelected>>", self.on_selection_changed)

        #region ttk.Entry
        self.entry_str_ar = tk.StringVar()
        self.entry_label_ar = ttk.Label(text="[arabic]", justify=tk.RIGHT)
        self.entry_label_ar.grid(column=1, row=1, sticky='ne', **options)
        self.entry_entry_ar = ttk.Entry(textvariable=self.entry_str_ar, width=50)
        self.entry_entry_ar.grid(column=2, row=1, sticky='ne', **options)


        self.entry_str_bg = tk.StringVar()
        self.entry_label_bg = ttk.Label(text="[bulgarian]", justify=tk.RIGHT)
        self.entry_label_bg.grid(column=1, row=2, sticky='ne', **options)
        self.entry_entry_bg = ttk.Entry(textvariable=self.entry_str_bg, width=50)
        self.entry_entry_bg.grid(column=2, row=2, sticky='ne', **options)

        self.entry_str_ch = tk.StringVar()
        self.entry_label_ch = ttk.Label(text="[chinese]", justify=tk.RIGHT)
        self.entry_label_ch.grid(column=1, row=3, sticky='ne', **options)
        self.entry_entry_ch = ttk.Entry(textvariable=self.entry_str_ch, width=50)
        self.entry_entry_ch.grid(column=2, row=3, sticky='ne', **options)

        self.entry_str_cs = tk.StringVar()
        self.entry_label_cs = ttk.Label(text="[czech]", justify=tk.RIGHT)
        self.entry_label_cs.grid(column=1, row=4, sticky='ne', **options)
        self.entry_entry_cs = ttk.Entry(textvariable=self.entry_str_cs, width=50)
        self.entry_entry_cs.grid(column=2, row=4, sticky='ne', **options)

        self.entry_str_da = tk.StringVar()
        self.entry_label_da = ttk.Label(text="[danish]", justify=tk.RIGHT)
        self.entry_label_da.grid(column=1, row=5, sticky='ne', **options)
        self.entry_entry_da = ttk.Entry(textvariable=self.entry_str_da, width=50)
        self.entry_entry_da.grid(column=2, row=5, sticky='ne', **options)

        self.entry_str_de = tk.StringVar()
        self.entry_label_de = ttk.Label(text="[german]", justify=tk.RIGHT)
        self.entry_label_de.grid(column=1, row=6, sticky='ne', **options)
        self.entry_entry_de = ttk.Entry(textvariable=self.entry_str_de, width=50)
        self.entry_entry_de.grid(column=2, row=6, sticky='ne', **options)

        self.entry_str_el = tk.StringVar()
        self.entry_label_el = ttk.Label(text="[greek]", justify=tk.RIGHT)
        self.entry_label_el.grid(column=1, row=7, sticky='ne', **options)
        self.entry_entry_el = ttk.Entry(textvariable=self.entry_str_el, width=50)
        self.entry_entry_el.grid(column=2, row=7, sticky='ne', **options)

        self.entry_str_en = tk.StringVar()
        self.entry_label_en = ttk.Label(text="[englisch]", justify=tk.RIGHT)
        self.entry_label_en.grid(column=1, row=8, sticky='ne', **options)
        self.entry_entry_en = ttk.Entry(textvariable=self.entry_str_en, width=50)
        self.entry_entry_en.grid(column=2, row=8, sticky='ne', **options)

        self.entry_str_en_AU = tk.StringVar()
        self.entry_label_en_AU = ttk.Label(text="[australian-englisch]", justify=tk.RIGHT)
        self.entry_label_en_AU.grid(column=1, row=9, sticky='ne', **options)
        self.entry_entry_en_AU = ttk.Entry(textvariable=self.entry_str_en_AU, width=50)
        self.entry_entry_en_AU.grid(column=2, row=9, sticky='ne', **options)

        self.entry_str_en_US = tk.StringVar()
        self.entry_label_en_US = ttk.Label(text="[american english]", justify=tk.RIGHT)
        self.entry_label_en_US.grid(column=1, row=10, sticky='ne', **options)
        self.entry_entry_en_US = ttk.Entry(textvariable=self.entry_str_en_US, width=50)
        self.entry_entry_en_US.grid(column=2, row=10, sticky='ne', **options)

        self.entry_str_es = tk.StringVar()
        self.entry_label_es = ttk.Label(text="[spanish]", justify=tk.RIGHT)
        self.entry_label_es.grid(column=1, row=11, sticky='ne', **options)
        self.entry_entry_es = ttk.Entry(textvariable=self.entry_str_es, width=50)
        self.entry_entry_es.grid(column=2, row=11, sticky='ne', **options)

        self.entry_str_es_MX = tk.StringVar()
        self.entry_label_es_MX = ttk.Label(text="[mexican spanish]", justify=tk.RIGHT)
        self.entry_label_es_MX.grid(column=1, row=12, sticky='ne', **options)
        self.entry_entry_es_MX = ttk.Entry(textvariable=self.entry_str_es_MX, width=50)
        self.entry_entry_es_MX.grid(column=2, row=12, sticky='ne', **options)

        self.entry_str_et = tk.StringVar()
        self.entry_label_et = ttk.Label(text="[estonian ]", justify=tk.RIGHT)
        self.entry_label_et.grid(column=1, row=13, sticky='ne', **options)
        self.entry_entry_et = ttk.Entry(textvariable=self.entry_str_et, width=50)
        self.entry_entry_et.grid(column=2, row=13, sticky='ne', **options)

        self.entry_str_fi = tk.StringVar()
        self.entry_label_fi = ttk.Label(text="[finnish]", justify=tk.RIGHT)
        self.entry_label_fi.grid(column=1, row=14, sticky='ne', **options)
        self.entry_entry_fi = ttk.Entry(textvariable=self.entry_str_fi, width=50)
        self.entry_entry_fi.grid(column=2, row=14, sticky='ne', **options)

        self.entry_str_fr = tk.StringVar()
        self.entry_label_fr = ttk.Label(text="[french]", justify=tk.RIGHT)
        self.entry_label_fr.grid(column=1, row=15, sticky='ne', **options)
        self.entry_entry_fr = ttk.Entry(textvariable=self.entry_str_fr, width=50)
        self.entry_entry_fr.grid(column=2, row=15, sticky='ne', **options)

        self.entry_str_fr_CA = tk.StringVar()
        self.entry_label_fr_CA = ttk.Label(text="[canadian french]", justify=tk.RIGHT)
        self.entry_label_fr_CA.grid(column=1, row=16, sticky='ne', **options)
        self.entry_entry_fr_CA = ttk.Entry(textvariable=self.entry_str_fr_CA, width=50)
        self.entry_entry_fr_CA.grid(column=2, row=16, sticky='ne', **options)

        self.entry_str_hr = tk.StringVar()
        self.entry_label_hr = ttk.Label(text="[kroatian]", justify=tk.RIGHT)
        self.entry_label_hr.grid(column=1, row=17, sticky='ne', **options)
        self.entry_entry_hr = ttk.Entry(textvariable=self.entry_str_hr, width=50)
        self.entry_entry_hr.grid(column=2, row=17, sticky='ne', **options)

        self.entry_str_hu = tk.StringVar()
        self.entry_label_hu = ttk.Label(text="[hungarian]", justify=tk.RIGHT)
        self.entry_label_hu.grid(column=1, row=18, sticky='ne', **options)
        self.entry_entry_hu = ttk.Entry(textvariable=self.entry_str_hu, width=50)
        self.entry_entry_hu.grid(column=2, row=18, sticky='ne', **options)

        self.entry_str_is = tk.StringVar()
        self.entry_label_is = ttk.Label(text="[icelandic]", justify=tk.RIGHT)
        self.entry_label_is.grid(column=3, row=1, sticky='ne', **options)
        self.entry_entry_is = ttk.Entry(textvariable=self.entry_str_is, width=50)
        self.entry_entry_is.grid(column=4, row=1, sticky='ne', **options)

        self.entry_str_it = tk.StringVar()
        self.entry_label_it = ttk.Label(text="[italian]", justify=tk.RIGHT)
        self.entry_label_it.grid(column=3, row=2, sticky='ne', **options)
        self.entry_entry_it = ttk.Entry(textvariable=self.entry_str_it, width=50)
        self.entry_entry_it.grid(column=4, row=2, sticky='ne', **options)

        self.entry_str_ja = tk.StringVar()
        self.entry_label_ja = ttk.Label(text="[japanese]", justify=tk.RIGHT)
        self.entry_label_ja.grid(column=3, row=3, sticky='ne', **options)
        self.entry_entry_ja = ttk.Entry(textvariable=self.entry_str_ja, width=50)
        self.entry_entry_ja.grid(column=4, row=3, sticky='ne', **options)

        self.entry_str_lt = tk.StringVar()
        self.entry_label_lt = ttk.Label(text="[lithuanian]", justify=tk.RIGHT)
        self.entry_label_lt.grid(column=3, row=4, sticky='ne', **options)
        self.entry_entry_lt = ttk.Entry(textvariable=self.entry_str_lt, width=50)
        self.entry_entry_lt.grid(column=4, row=4, sticky='ne', **options)

        self.entry_str_lv = tk.StringVar()
        self.entry_label_lv = ttk.Label(text="[latvian]", justify=tk.RIGHT)
        self.entry_label_lv.grid(column=3, row=5, sticky='ne', **options)
        self.entry_entry_lv = ttk.Entry(textvariable=self.entry_str_lv, width=50)
        self.entry_entry_lv.grid(column=4, row=5, sticky='ne', **options)

        self.entry_str_nl = tk.StringVar()
        self.entry_label_nl = ttk.Label(text="[dutch]", justify=tk.RIGHT)
        self.entry_label_nl.grid(column=3, row=6, sticky='ne', **options)
        self.entry_entry_nl = ttk.Entry(textvariable=self.entry_str_nl, width=50)
        self.entry_entry_nl.grid(column=4, row=6, sticky='ne', **options)

        self.entry_str_no = tk.StringVar()
        self.entry_label_no = ttk.Label(text="[norwegian]", justify=tk.RIGHT)
        self.entry_label_no.grid(column=3, row=7, sticky='ne', **options)
        self.entry_entry_no = ttk.Entry(textvariable=self.entry_str_no, width=50)
        self.entry_entry_no.grid(column=4, row=7, sticky='ne', **options)

        self.entry_str_pl = tk.StringVar()
        self.entry_label_pl = ttk.Label(text="[polish]", justify=tk.RIGHT)
        self.entry_label_pl.grid(column=3, row=8, sticky='ne', **options)
        self.entry_entry_pl = ttk.Entry(textvariable=self.entry_str_pl, width=50)
        self.entry_entry_pl.grid(column=4, row=8, sticky='ne', **options)

        self.entry_str_pt = tk.StringVar()
        self.entry_label_pt = ttk.Label(text="[portuguese]", justify=tk.RIGHT)
        self.entry_label_pt.grid(column=3, row=9, sticky='ne', **options)
        self.entry_entry_pt = ttk.Entry(textvariable=self.entry_str_pt, width=50)
        self.entry_entry_pt.grid(column=4, row=9, sticky='ne', **options)

        self.entry_str_pt_BR = tk.StringVar()
        self.entry_label_pt_BR = ttk.Label(text="[brasilian portuguese]", justify=tk.RIGHT)
        self.entry_label_pt_BR.grid(column=3, row=10, sticky='ne', **options)
        self.entry_entry_pt_BR = ttk.Entry(textvariable=self.entry_str_pt_BR, width=50)
        self.entry_entry_pt_BR.grid(column=4, row=10, sticky='ne', **options)

        self.entry_str_ro = tk.StringVar()
        self.entry_label_ro = ttk.Label(text="[romanian]", justify=tk.RIGHT)
        self.entry_label_ro.grid(column=3, row=11, sticky='ne', **options)
        self.entry_entry_ro = ttk.Entry(textvariable=self.entry_str_ro, width=50)
        self.entry_entry_ro.grid(column=4, row=11, sticky='ne', **options)

        self.entry_str_ru = tk.StringVar()
        self.entry_label_ru = ttk.Label(text="[russian]", justify=tk.RIGHT)
        self.entry_label_ru.grid(column=3, row=12, sticky='ne', **options)
        self.entry_entry_ru = ttk.Entry(textvariable=self.entry_str_ru, width=50)
        self.entry_entry_ru.grid(column=4, row=12, sticky='ne', **options)

        self.entry_str_sk = tk.StringVar()
        self.entry_label_sk = ttk.Label(text="[slowak]", justify=tk.RIGHT)
        self.entry_label_sk.grid(column=3, row=13, sticky='ne', **options)
        self.entry_entry_sk = ttk.Entry(textvariable=self.entry_str_sk, width=50)
        self.entry_entry_sk.grid(column=4, row=13, sticky='ne', **options)

        self.entry_str_sl = tk.StringVar()
        self.entry_label_sl = ttk.Label(text="[slovenian]", justify=tk.RIGHT)
        self.entry_label_sl.grid(column=3, row=14, sticky='ne', **options)
        self.entry_entry_sl = ttk.Entry(textvariable=self.entry_str_sl, width=50)
        self.entry_entry_sl.grid(column=4, row=14, sticky='ne', **options)

        self.entry_str_sr = tk.StringVar()
        self.entry_label_sr = ttk.Label(text="[serbian]", justify=tk.RIGHT)
        self.entry_label_sr.grid(column=3, row=15, sticky='ne', **options)
        self.entry_entry_sr = ttk.Entry(textvariable=self.entry_str_sr, width=50)
        self.entry_entry_sr.grid(column=4, row=15, sticky='ne', **options)

        self.entry_str_sv = tk.StringVar()
        self.entry_label_sv = ttk.Label(text="[swedisch]", justify=tk.RIGHT)
        self.entry_label_sv.grid(column=3, row=16, sticky='ne', **options)
        self.entry_entry_sv = ttk.Entry(textvariable=self.entry_str_sv, width=50)
        self.entry_entry_sv.grid(column=4, row=16, sticky='ne', **options)

        self.entry_str_tr = tk.StringVar()
        self.entry_label_tr = ttk.Label(text="[turkish]", justify=tk.RIGHT)
        self.entry_label_tr.grid(column=3, row=17, sticky='ne', **options)
        self.entry_entry_tr = ttk.Entry(textvariable=self.entry_str_tr, width=50)
        self.entry_entry_tr.grid(column=4, row=17, sticky='ne', **options)

        self.entry_str_uk = tk.StringVar()
        self.entry_label_uk = ttk.Label(text="[ukrainian]", justify=tk.RIGHT)
        self.entry_label_uk.grid(column=3, row=18, sticky='ne', **options)
        self.entry_entry_uk = ttk.Entry(textvariable=self.entry_str_uk, width=50)
        self.entry_entry_uk.grid(column=4, row=18, sticky='ne', **options)
        #endregion

        self.button_add_entry = ttk.Button(text="Clear fields", command=self.clear_on_click)
        self.button_add_entry.grid(column=0, row=3, sticky='e', **options)

        self.label_add_key = ttk.Label(text="Enter new key:")
        self.label_add_key.grid(column=0, row=4, sticky='w', **options)
        self.entry_new_key_var = tk.StringVar()
        self.entry_new_key = ttk.Entry(textvariable=self.entry_new_key_var, width=35)
        self.entry_new_key.grid(column=0, row=4, sticky='e', **options)

        self.button_add_entry = ttk.Button(text="Add to file", command=self.add_to_dict)
        self.button_add_entry.grid(column=0, row=5, sticky='w', **options)

        self.button_add_entry = ttk.Button(text="Rename entries", command=self.rename_to_dict)
        self.button_add_entry.grid(column=0, row=5, sticky='n', **options)

        self.button_add_entry = ttk.Button(text="Save files", command=self.save_to_files)
        self.button_add_entry.grid(column=0, row=5, sticky='e', **options)

    def on_selection_changed(self, event):
        key_text = self.combo_key.get()

        #region Set ttk.Entry
        self.entry_str_ar.set(list_languages[0][key_text])
        self.entry_str_bg.set(list_languages[1][key_text])
        self.entry_str_ch.set(list_languages[2][key_text])
        self.entry_str_cs.set(list_languages[3][key_text])
        self.entry_str_da.set(list_languages[4][key_text])
        self.entry_str_de.set(list_languages[5][key_text])
        self.entry_str_el.set(list_languages[6][key_text])
        self.entry_str_en.set(list_languages[7][key_text])
        self.entry_str_en_AU.set(list_languages[8][key_text])
        self.entry_str_en_US.set(list_languages[9][key_text])
        self.entry_str_es.set(list_languages[10][key_text])
        self.entry_str_es_MX.set(list_languages[11][key_text])
        self.entry_str_et.set(list_languages[12][key_text])
        self.entry_str_fi.set(list_languages[13][key_text])
        self.entry_str_fr.set(list_languages[14][key_text])
        self.entry_str_fr_CA.set(list_languages[15][key_text])
        self.entry_str_hr.set(list_languages[16][key_text])
        self.entry_str_hu.set(list_languages[17][key_text])
        self.entry_str_is.set(list_languages[18][key_text])
        self.entry_str_it.set(list_languages[19][key_text])
        self.entry_str_ja.set(list_languages[20][key_text])
        self.entry_str_lt.set(list_languages[21][key_text])
        self.entry_str_lv.set(list_languages[22][key_text])
        self.entry_str_nl.set(list_languages[23][key_text])
        self.entry_str_no.set(list_languages[24][key_text])
        self.entry_str_pl.set(list_languages[25][key_text])
        self.entry_str_pt.set(list_languages[26][key_text])
        self.entry_str_pt_BR.set(list_languages[27][key_text])
        self.entry_str_ro.set(list_languages[28][key_text])
        self.entry_str_ru.set(list_languages[29][key_text])
        self.entry_str_sk.set(list_languages[30][key_text])
        self.entry_str_sl.set(list_languages[31][key_text])
        self.entry_str_sr.set(list_languages[32][key_text])
        self.entry_str_sv.set(list_languages[33][key_text])
        self.entry_str_tr.set(list_languages[34][key_text])
        self.entry_str_uk.set(list_languages[35][key_text])
        #endregion

    def clear_on_click(self):
        self.entry_str_ar.set("")
        self.entry_str_bg.set("")
        self.entry_str_ch.set("")
        self.entry_str_cs.set("")
        self.entry_str_da.set("")
        self.entry_str_de.set("")
        self.entry_str_el.set("")
        self.entry_str_en.set("")
        self.entry_str_en_AU.set("")
        self.entry_str_en_US.set("")
        self.entry_str_et.set("")
        self.entry_str_es.set("")
        self.entry_str_es_MX.set("")
        self.entry_str_fi.set("")
        self.entry_str_fr.set("")
        self.entry_str_fr_CA.set("")
        self.entry_str_hr.set("")
        self.entry_str_hu.set("")
        self.entry_str_is.set("")
        self.entry_str_it.set("")
        self.entry_str_ja.set("")
        self.entry_str_lt.set("")
        self.entry_str_lv.set("")
        self.entry_str_nl.set("")
        self.entry_str_no.set("")
        self.entry_str_pl.set("")
        self.entry_str_pt.set("")
        self.entry_str_pt_BR.set("")
        self.entry_str_ro.set("")
        self.entry_str_ru.set("")
        self.entry_str_sk.set("")
        self.entry_str_sl.set("")
        self.entry_str_sr.set("")
        self.entry_str_sv.set("")
        self.entry_str_tr.set("")
        self.entry_str_uk.set("")

    def add_to_dict(self):
        if self.entry_new_key_var != "" and self.entry_new_key_var != dict_key:
            for file in list_languages:
                file.update({self.entry_new_key_var.get(): self.entry_str_de.get()})
                dict_key.append(self.entry_new_key_var.get())

        else:
            return

    def rename_to_dict(self):
        pass

    def get_new_dict(self):
        self.combo_key['values'] = dict_key

    def save_to_files(self):
        languages = os.listdir("Source/")

        j = 0
        for lang in languages:
            i = 0
            lang_splitted = lang.split("_")[1].split(".")[0]
            with open(f"Target/{lang}", "w", encoding="UTF-8") as file:
                file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                file.write('<l:langdata xmlns:l="http://www.schema.de/XSL/ST4DocuManagerlang">\n')
                file.write(f'\t<l:langblock xml:lang="{lang_splitted}">\n')
                list = list_languages[j]
                for i in range(len(dict_key)):
                    if dict_key[i] not in list.keys():
                        file.writelines(f'\t\t<l:gentext key="{dict_key[i]}" value="-"/>\n')
                    else:
                        file.writelines(f'\t\t<l:gentext key="{dict_key[i]}" value="{list[dict_key[i]]}"/>\n')
                file.write('\t</l:langblock>\n')
                file.write('</l:langdata>\n')
                j += 1
        mb.showinfo("Successful", "Language.xml successfully generated.")










class Root (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language XML")
        self.geometry("1200x900")
        self.resizable(False, False)


root = Root()
LanguageGenerator(root)
root.mainloop()