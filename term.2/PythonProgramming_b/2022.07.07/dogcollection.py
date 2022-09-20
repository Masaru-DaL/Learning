from dog import Dog

dog1 = Dog("てんてん", "ちわわ")
dog2 = Dog("らんらん", "まるちーず")
print(Dog.dog_count)
print(dog2.last_dog_name)


dog3 = Dog("ちゃんまる", "どーべるまん")
print(Dog.dog_count)
print(Dog.last_dog_name)

Dog.collection_info()
