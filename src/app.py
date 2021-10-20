from src.room import Room
from src.game_logic import GameLogic
from src.player import Player

if __name__ == '__main__':
    room = Room(GameLogic())
    player = Player(("127.0.0.1", 702232))
    player2 = Player(("127.0.0.1", 702233))
    player3 = Player(("127.0.0.1", 702234))

    room.set_dialler(player)
    room.connect_room(player2)
    room.connect_room(player3)

    while room.current_player() is not None:
        command = input("Take ?\n")
        if command == "y":
            room.current_player().take_card(room.deck)
            print(room.current_player().display_card())

        elif command == "s":
            print(room.current_player().score)

        elif command == "n":
            room.next_player()

    player.take_card(room.deck)
    player.take_card(room.deck)

    room.win_con()
