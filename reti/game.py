import random

def battle(player, enemy):
    print(f"\n🔥 A wild {enemy['name']} appeared! 🔥")
    while player['hp'] > 0 and enemy['hp'] > 0:
        print(f"\n🛡️ {player['name']} HP: {player['hp']} | ⚔️ {enemy['name']} HP: {enemy['hp']}")
        print(f"⭐ Special Attacks Remaining: {'💥' * player['special']}")
        move = input("Choose attack (1. Punch 🥊 2. Kick 🦵 3. Special Attack 💥): ")
        
        if move == '1':
            damage = random.randint(5, 10)
        elif move == '2':
            damage = random.randint(8, 12)
        elif move == '3':
            if player['special'] > 0:
                damage = random.randint(12, 20)
                player['special'] -= 1
                print(f"{player['special']} special attacks left!")
            else:
                print("❌ No special attacks left!")
                continue
        else:
            print("⚠️ Invalid move!")
            continue
        
        enemy['hp'] -= damage
        print(f"💥 You dealt {damage} damage to {enemy['name']}!")
        
        if enemy['hp'] <= 0:
            print(f"🏆 You defeated {enemy['name']}!")
            player['xp'] += enemy['xp']
            break
        
        enemy_damage = random.randint(5 + player['level'] * 2, 15 + player['level'] * 2)
        player['hp'] -= enemy_damage
        print(f"⚔️ {enemy['name']} attacked you for {enemy_damage} damage!")
    
    if player['hp'] <= 0:
        print("💀 You have been defeated...")
        exit()

def level_up(player):
    if player['xp'] >= player['xp_needed']:
        player['level'] += 1
        player['xp'] = 0
        player['xp_needed'] += 20
        player['hp'] = 100
        player['special'] = 3
        print(f"🎉 Congratulations! You leveled up to Level {player['level']}!")

def game():
    player = {'name': 'Hero', 'hp': 100, 'xp': 0, 'xp_needed': 20, 'level': 1, 'special': 3}
    enemies = [
        {'name': 'Goblin', 'hp': 30, 'xp': 10},
        {'name': 'Orc', 'hp': 50, 'xp': 15},
        {'name': 'Dark Mage', 'hp': 70, 'xp': 20},
        {'name': 'Demon Lord', 'hp': 100, 'xp': 50}
    ]
    
    print("🗺️ Welcome to the world of adventure!")
    print("You are a young warrior, exploring dangerous lands to become the greatest fighter.")
    
    while True:
        print("\n⚔️ What do you want to do?")
        print("1. Explore the dark forest 🌲")
        print("2. Rest at the campfire 🔥")
        print("3. Check stats 📜")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            enemy = random.choice(enemies)
            battle(player, enemy)
            level_up(player)
        elif choice == '2':
            print("⛺ You take a rest and restore your HP.")
            player['hp'] = 100
        elif choice == '3':
            print(f"📊 Level: {player['level']} | XP: {player['xp']}/{player['xp_needed']} | HP: {player['hp']} | Special Attacks: {'💥' * player['special']}")
        else:
            print("⚠️ Invalid choice.")

game()
