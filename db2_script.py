import pymongo
from faker import Faker
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["sdb2"]

dblist = myclient.list_database_names()
print(dblist)

myclient.drop_database('sdb2')

guest = mydb["guest"]

fake = Faker()

guestData = []

for i in range(500):
    guestData.append({ "name" : fake.name(), "phone_number" : fake.phone_number(), "points_earned" : fake.pyint()})

guests = guest.insert_many(guestData)

print(len(guests.inserted_ids), " guests inserted.")

restaurant = mydb["restaurant"]

genres = ['Italian/French', 'Dining bar', 'Yakiniku/Korean food', 'Cafe/Sweets', 'Izakaya', 'Okonomiyaki/Monja/Teppanyaki', 'Bar/Cocktail', 'Japanese food', 'Creative cuisine', 'Other', 'Western food', 'International cuisine', 'Asian', 'Karaoke/Party']
regions = ["Alma" ,"Fleurimont" ,"Longueuil" ,"Amos" ,"Gaspe" ,"Marieville" ,"Anjou" ,"Gatineau" ,"Mount Royal" ,"Aylmer" ,"Hull" ,"Montreal" ,"Beauport" ,"Joliette" ,"Montreal Region" ,"Bromptonville" ,"Jonquiere" ,"Montreal-Est" ,"Brosssard" ,"Lachine" ,"Quebec" ,"Chateauguay" ,"Lasalle" ,"Saint-Leonard" ,"Chicoutimi" ,"Laurentides" ,"Sherbrooke" ,"Coaticook" ,"LaSalle" ,"Sorel" ,"Coaticook" ,"Laval" ,"Thetford Mines" ,"Dorval" ,"Lennoxville" ,"Victoriaville" ,"Drummondville" ,"Levis"]

# print(len(regions))
restaurantData = []

for i in range(1000):
    restaurantData.append({"genre": random.choice(genres), "region": regions[random.randint(0, 37)], "name": fake.company()})

restaurants = restaurant.insert_many(restaurantData)
print(len(guests.inserted_ids), " restaurants inserted.")

# print(restaurants.inserted_ids[4])

reservation = mydb["reservation"]

reservationData = []

for i in range(2000):
    reservationData.append({ "gid": guests.inserted_ids[random.randint(0, 99)], "rid": restaurants.inserted_ids[random.randint(0, 99)], "amount_spent": fake.pyint(), "transaction_date": fake.date_time_between(start_date='-4y', end_date='now', tzinfo=None), "guest_count": random.randint(1,10) })

reservations = reservation.insert_many(reservationData)

print(len(reservations.inserted_ids), " reservations inserted.")

print(mydb.list_collection_names())