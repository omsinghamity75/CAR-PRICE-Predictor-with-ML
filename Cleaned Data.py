car.to_csv('Cleaned_Car_data.csv')
car.info()
car.describe(include='all')

car=car[car['Price']<6000000]
