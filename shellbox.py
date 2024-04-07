##Python 3##
# Author : 0-Gram 
# Github : https://0-gram.github.io/shellbox
# Contact : admin@exploitnews.net
#before writing your fucking name try to see ur fucking self in the mirror :)

import csv
import colorama

colorama.init()
RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
GREEN = colorama.Fore.GREEN
MAGENTA = colorama.Fore.MAGENTA
YELLOW = colorama.Fore.YELLOW
ENDCOLOR = colorama.Style.RESET_ALL

banner = f"""{MAGENTA}
███████ ██   ██ ███████ ██      ██      ██████   ██████  ██   ██ 
██      ██   ██ ██      ██      ██      ██   ██ ██    ██  ██ ██  
███████ ███████ █████   ██      ██      ██████  ██    ██   ███   
     ██ ██   ██ ██      ██      ██      ██   ██ ██    ██  ██ ██  
███████ ██   ██ ███████ ███████ ███████ ██████   ██████  ██   ██ 
"""


class ProgramSederhana:
    def __init__(self):
        self.data_pengguna = []
        self.baca_data_dari_file()

    def input_data_user(self):
        print(f"{MAGENTA}{banner}{ENDCOLOR}")
        url_shell = input(f"{GREEN}Enter your Shell Url: {ENDCOLOR}")
        pass_shell = input(f"{GREEN}Enter your Shell Password: {ENDCOLOR}")
        poc = input(f"{GREEN}Enter your Poc: {ENDCOLOR}")
        status_root = input(f"{GREEN}Enter Root Status: (y/n) {ENDCOLOR}").lower()

        if status_root == "y":
            user_root = input(f"{GREEN}Enter your root username: {ENDCOLOR}")
            pass_root = input(f"{GREEN}Enter your Root Shell Password: {ENDCOLOR}")
            self.data_pengguna.append({
                "url_shell": url_shell,
                "pass_shell": pass_shell,
                "poc": poc,
                "status_root": status_root,
                "user_root": user_root,
                "pass_root": pass_root,
            })
        elif status_root == "n":
            print(f"{RED}Shell belum di root!!!{ENDCOLOR}")
            self.data_pengguna.append({
                "url_shell": url_shell,
                "pass_shell": pass_shell,
                "poc": poc,
                "status_root": status_root
            })

    def baca_data_dari_file(self):
        try:
            with open("data_shell.csv", "r") as file_csv:
                reader = csv.DictReader(file_csv)
                for row in reader:
                    self.data_pengguna.append(dict(row))
        except FileNotFoundError:
            pass

    def simpan_ke_txt(self):
        with open("data_shell.txt", "a") as file_txt:
            for data in self.data_pengguna:
                for key, value in data.items():
                    file_txt.write(f"{key}: {value}\n")  
                file_txt.write("\n")  
        print(f"{GREEN}The data has been saved to data_shell.txt{ENDCOLOR}")

    def jalankan_program(self):
        while True:
            self.input_data_user()
            tipe_file = input(f"{GREEN}Select the file type to save the data (txt/csv): {ENDCOLOR}")
            if tipe_file.lower() == 'txt':
                self.simpan_ke_txt()  
            elif tipe_file.lower() == 'csv':
                self.simpan_ke_csv()  
            else:
                print(f"{RED}Invalid file type. Select 'txt' or 'csv'.{ENDCOLOR}")
                continue

            lanjut = input(f"{BLUE}Do you want to continue? (y/n): {ENDCOLOR}").lower()
            if lanjut != "y":
                break

            # Membersihkan data_pengguna setelah setiap iterasi program
            self.data_pengguna = []

        # Pesan harus ditempatkan di sini agar dicetak setiap kali program selesai menjalankan iterasi
        print(f"{GREEN}The data has been saved to data_shell.txt{ENDCOLOR}")


# Instansiasi objek ProgramSederhana
program_sederhana = ProgramSederhana()
program_sederhana.jalankan_program()
