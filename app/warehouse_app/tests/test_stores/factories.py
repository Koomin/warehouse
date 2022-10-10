import factory

from stores.models import Store


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store
    uuid = factory.faker.Faker('uuid4')
    optima_id = factory.faker.Faker('pyint')
    name = factory.faker.Faker('name')
    short_name = factory.lazy_attribute(lambda o: o.name[:2])
    description = factory.faker.Faker('text', max_nb_chars=50)
    register = factory.faker.Faker('text', max_nb_chars=50)
    status = factory.faker.Faker('pyint', min_value=0, max_value=1, step=1)
