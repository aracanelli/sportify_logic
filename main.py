import pickleball_monday, pickleball_tuesday

if __name__ == "__main__":

    day = "monday"
    generate_games = False

    if day == "tuesday":
        player_list = [
            "Anthony",
            "Erica",
            "Falcone",
            "Cha-Nel",
            "Steve",
            "Chris",
            "Sandra",
            "Vick",
            "Sam",
            "Felix",
            "Marcella",
            "Taurasi",
            "Scarfo",
            "Matt S",
            "Baller",
            "Szymbo",
            "Jenna",
            "Sarah",
            "James",
            "James C"
        ]
        pickleball_tuesday.play(player_list, generate_games=generate_games)

    elif day == "monday":
        player_list = [
            "Mario",
            "Anthony",
            "Frank",
            "Anthony P",
            "Stephane",
            "Sebastien",
            "Dominic",
            "Tony",
            "David",
            "Patrick",
            "Francis",
            "Marcello",
            "Vince D",
            "Panos",
            "Nick",
            "Dino"
        ]
        pickleball_monday.play(player_list, generate_games=generate_games)