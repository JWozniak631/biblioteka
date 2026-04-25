def pokaz_katalog(ksiazki):
    print("\n--- KATALOG KSIĄŻEK ---")
    for ksiazka in ksiazki:
        print(f"Tytuł: {ksiazka['tytul']}")
        print(f"Autor: {ksiazka['autor']}")
        print(f"Dostępne sztuki: {ksiazka['liczba_sztuk']}")
        print("-" * 30)


def znajdz_ksiazke(ksiazki, tytul):
    for ksiazka in ksiazki:
        if ksiazka["tytul"].lower() == tytul.lower():
            return ksiazka
    return None


def wypozycz_ksiazke(ksiazki, uzytkownik):
    print("\n--- WYPOŻYCZANIE KSIĄŻKI ---")
    tytul = input("Podaj tytuł książki: ")

    ksiazka = znajdz_ksiazke(ksiazki, tytul)

    if ksiazka is None:
        print("Nie znaleziono książki o takim tytule.")
    elif ksiazka["liczba_sztuk"] <= 0:
        print("Brak dostępnych sztuk tej książki.")
    else:
        ksiazka["liczba_sztuk"] -= 1
        uzytkownik["wypozyczenia"].append(ksiazka["tytul"])
        print("Książka została wypożyczona.")


def pokaz_moje_wypozyczenia(uzytkownik):
    print("\n--- MOJE WYPOŻYCZENIA ---")

    if len(uzytkownik["wypozyczenia"]) == 0:
        print("Nie masz aktualnie wypożyczonych książek.")
    else:
        for tytul in uzytkownik["wypozyczenia"]:
            print(f"- {tytul}")


def zaloguj(uzytkownicy):
    print("--- LOGOWANIE ---")

    proby = 0

    while proby < 3:
        login = input("Login: ")
        haslo = input("Hasło: ")

        for uzytkownik in uzytkownicy:
            if uzytkownik["login"] == login and uzytkownik["haslo"] == haslo:
                print("Zalogowano pomyślnie.")
                return uzytkownik

        proby += 1
        print(f"Nieprawidłowy login lub hasło. Pozostało prób: {3 - proby}")

    print("Przekroczono limit prób logowania. Program zostanie zakończony.")
    return None


def pokaz_menu():
    print("\n--- MENU GŁÓWNE ---")
    print("1. Przeglądaj katalog")
    print("2. Wypożycz książkę")
    print("3. Moje wypożyczenia")
    print("4. Wyloguj")


def uruchom_program():
    ksiazki = [
        {"tytul": "Pan Tadeusz", "autor": "Adam Mickiewicz", "liczba_sztuk": 3},
        {"tytul": "Lalka", "autor": "Bolesław Prus", "liczba_sztuk": 2},
        {"tytul": "Quo Vadis", "autor": "Henryk Sienkiewicz", "liczba_sztuk": 4},
        {"tytul": "Kamienie na szaniec", "autor": "Aleksander Kamiński", "liczba_sztuk": 1},
        {"tytul": "Ferdydurke", "autor": "Witold Gombrowicz", "liczba_sztuk": 2}
    ]

    uzytkownicy = [
        {"login": "jan", "haslo": "1234", "rola": "czytelnik", "wypozyczenia": []},
        {"login": "anna", "haslo": "abcd", "rola": "czytelnik", "wypozyczenia": []},
        {"login": "piotr", "haslo": "haslo", "rola": "czytelnik", "wypozyczenia": []}
    ]

    zalogowany_uzytkownik = zaloguj(uzytkownicy)

    if zalogowany_uzytkownik is None:
        return

    wybor = ""

    while wybor != "4":
        pokaz_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_katalog(ksiazki)
        elif wybor == "2":
            wypozycz_ksiazke(ksiazki, zalogowany_uzytkownik)
        elif wybor == "3":
            pokaz_moje_wypozyczenia(zalogowany_uzytkownik)
        elif wybor == "4":
            print("Wylogowano. Koniec programu.")
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


uruchom_program()
