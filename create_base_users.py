from billingstore.models import Company, Brand
from people.models import Person
from users.models import CustomUser

company = Company()
company.document_id = "1768028470001"
company.name = "Carniceria"
company.direction = "Cuenca"
company.save()

#city = City()
#city.name = "Cuenca"
#city.save()

brand = Brand()
brand.name = "Sucural 1"
brand.direction = "Borrero"
brand.company = company
brand.save()
#brand.cities.add(city)
#brand.save()

person = Person()
person.document_type = "cedula"
person.document_id = "3050597412"
person.first_name = "Mileidy"
person.last_name = "Tacuri"
person.direction = "Cuenca"
person.save()

user = CustomUser.objects.create_user("Milebet", password="django1234", email="milebet.tacuri@gmail.com", brand=brand, person=person)
user.is_superuser=True
user.is_staff=True
user.save()