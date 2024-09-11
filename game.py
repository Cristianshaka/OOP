class Character:
    def __init__(self, name: str, health: int ,damage: int) -> None: #metodo construtor, define o estado inicial do objeto, sem ele teria que configurar os atributos manualmente 
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage
    
    def attack(self, target) -> None:
        target.health -= self.damage
        target.health = max(target.health, 0)
        

hero = Character(name= "Hero", health=100, damage=5)
enemy = Character(name= "Enemy", health=100, damage=3)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
print(f"health of {hero.name}: {hero.health}") #f é usado quando quero colocar uma variavel numa string
print(f"health of {enemy.name}: {enemy.health}")

input()
    
