class Character():
    def __init__(self,name,health,attack_pwr,defence_pwr,speed,morale):
        self.health = health
        self.attack_pwr = attack_pwr
        self.defense_pwr = defence_pwr
        self.speed = speed
        self.morale = morale
        self.name = name
    
    def info(self):
        attrs = vars(self)
        for key in attrs:
            print(f"{key}:{attrs[key]}")
            
    def change_health(self,amount):
        self.health += amount 
    
    
    def attrack(self, attackee, type="punch"):
        damage = (self.attack_pwr * 0.1 + 5) * -1
        attackee.health -= damage
        attackee.change_health(damage)
        

c1 = Character('tyler the strong',100,13,10,9,0)

c1.info()
