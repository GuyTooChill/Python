class user:

    def __init__(self, first, last, email, age, rewards = 'False', points = 0) -> None:
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.is_rewards_member = rewards
        self.gold_card_points = points


    def display_info(self):
        print(f'First Name : {self.first_name}\nLast Name : {self.last_name}\nEmail : {self.email}\nAge : {self.age}\nRewards Member : {self.is_rewards_member}\nGold Card Points : {self.gold_card_points}')

    def enroll(self):
        if self.is_rewards_member == 'False':
            self.is_rewards_member = 'True'


    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount




user1 = user('Diego', 'Gonzalez', 'diego123456789@gmail.com', 29, 'False', 200)
user2 = user('Briona', 'Taylor', 'briona123456789@gmail.com', 24, 'False', 400)


user1.enroll()
user1.spend_points()
user1.display_info()
