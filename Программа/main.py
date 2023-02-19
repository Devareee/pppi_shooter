import pygame

from shop import currency, inventory
from multiplayer import friends, chat, choose, equipment

game_currency = currency.Currency()
game_inventory = inventory.Inventory()
game_friends = friends.Friends()
game_chat = chat.Chat()
game_weapon = choose.Choose()
game_equipment = equipment.Equipment()
