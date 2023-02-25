# Сценарии использования

1. Одиночная игра против ботов
```py
game = load.Load()
game_menu = menu.Menu()
game_camera = camera.Camera()
game_settings = settings.Settings()
game_currency = currency.Currency()
game_inventory = inventory.Inventory()
game_weapon = choose.Choose()
game_equipment = equipment.Equipment()
game_health = health.Health()
game_kill = kill.Kill()
game_enemy = game_kill.kill()
```
2. Многопользовательская игра против ботов
```py
game = load.Load()
game_menu = menu.Menu()
game_camera = camera.Camera()
game_settings = settings.Settings()
game_currency = currency.Currency()
game_inventory = inventory.Inventory()
game_weapon = choose.Choose()
game_equipment = equipment.Equipment()
game_health = health.Health()
game_kill = kill.Kill()
game_enemy = game_kill.kill()
game_friends = friends.Friends()
game_initialization = initialization.Initialization()
```
3. Многопользовательская игра против других игроков
```py
game = load.Load()
game_menu = menu.Menu()
game_camera = camera.Camera()
game_settings = settings.Settings()
game_currency = currency.Currency()
game_inventory = inventory.Inventory()
game_weapon = choose.Choose()
game_equipment = equipment.Equipment()
game_health = health.Health()
game_kill = kill.Kill()
game_enemy = game_kill.kill()
game_friends = friends.Friends()
game_initialization = initialization.Initialization()
game_chat = chat.Chat()
game_reports = reports.Reports()
```