import random

def playgame():
    choices = ["Batu", "Gunting", "Kertas"]
    
    # nyawa player dan nyawa bot sebanyak 3
    playerLives = 3
    botLives = 3

    while playerLives > 0 and botLives > 0:
        botChoices = random.choice(choices)
        playerChoices = input("Masukkan Pilihan anda : ")
        print("Kamu memilih: ", playerChoices)
        print("Bot memilih: ", botChoices)

        if botChoices == playerChoices:
            print("Hasilnya seri!")
        elif (botChoices == "Batu" and playerChoices == "Gunting") or (botChoices == "Kertas" and playerChoices == "Batu") or (botChoices == "Gunting" and playerChoices == "Kertas"):
            print("Silahkan coba lagi😊")
            playerLives -= 1
        else:
            print("Selamat anda lolos ke babak selanjutnya")
            botLives -= 1

        print(f"Sisa nyawa kamu: {playerLives}, Sisa nyawa Bot: {botLives}")

        if playerLives == 0:
            print("Nyawa kamu habis. Bot Menang!")
            break
        elif botLives == 0:
            print("Bot Kehabisan nyawa. Selamat anda menang!")
            break

playgame()
