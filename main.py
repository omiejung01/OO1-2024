import account as acc

class Account:
    def __init__(self, account_name, opening_balance):
        self.account_name = account_name
        self.balance = opening_balance

    def display(self):
        return self.account_name + ' ' + f"{self.balance:,.2f}"

    def setAccountName(self, new_name):
        self.account_name = new_name

class Character:
    def __init__(self, character_name, vision, weapon_type):
        self.__character_name = character_name
        self.__vision = vision
        self.__weapon = ''
        self.__weapon_type = weapon_type

    def setCharacterName(self,new_name):
        self.__character_name = new_name

    def display(self):
        return self.__character_name + " " + self.__vision + " " + self.__weapon.getName()

    def setWeapon(self, weapon):
        if (weapon.getType() == self.__weapon_type):
            self.__weapon = weapon
        else:
            print("Weapon types are mismatch")

    def getWeapon(self):
        return self.__weapon

class Weapon:
    def __init__(self,name,weapon_type):
        self.__name = name
        self.__weapon_type = weapon_type
        self.__level = 1

    def getType(self):
        return self.__weapon_type

    def getName(self):
        return self.__name


if __name__ == '__main__':
    accountA = Account('Mr. A', 2000.50)
    print(accountA.account_name)
    print(accountA.display())
    accountB = Account('Ms. B', 1000)
    print(accountB.display())
    accountB.setAccountName('Mrs. B')
    print(accountB.display())

    # Class --> Account
    # Instance --> accountA (Mr.A's account)

    raiden = Character("Makoto","Electro","Polearm")
    print(raiden.display())

    #raiden.character_name = "Ei"
    raiden.setCharacterName("Ei")

    polearmA = Weapon("Polearm A","Polearm")
    bowA = Weapon("Bow A","Bow")

    raiden.setWeapon(polearmA)
    print(raiden.display())






