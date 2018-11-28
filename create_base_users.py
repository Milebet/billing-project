from billingstore.models import Company, City, Brand
from people.models import DocumentType, PersonType, Person
from users.models import CustomUser

company = Company()
company.document_id = "1768028470001"
company.name = "Carniceria"
company.direction = "Cuenca"
company.save()

city = City()
city.name = "Cuenca"
city.save()

brand = Brand()
brand.name = "Sucural 1"
brand.direction = "Borrero"
brand.company = company
brand.save()
brand.cities.add(city)
brand.save()

doc = DocumentType()
doc.save()

person_type = PersonType()
person_type.save()

person = Person()
person.document_id = "3050597412"
person.first_name = "Mileidy"
person.last_name = "Tacuri"
person.email = "milebet.tacuri@gmail.com"
person.direction = "Cuenca"
person.document_type = doc
person.person_type = person_type
person.save()

user = CustomUser.objects.create_user("Milebet", password="django1234", brand=brand, person=person)
user.is_superuser=True
user.is_staff=True
user.save()