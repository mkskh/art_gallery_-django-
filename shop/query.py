from shop.models import Product
from django.db.models import Q, Value, F, Count



# def create_product(n, p, q, c):
#     Product.objects.create(name=n, price=p, quantity=q, condition=c)


#p = Product.objects.create(name="Keyboard", price=22.22, quantity=10, condition="Used")
    
# create_product('Monitor', 444.44, 3, 'New')
# create_product('Mouse', 11.11, 30, 'Used')
# create_product('iPad', 555.55, 20, 'New')
# create_product('Bike', 8888.88, 8, 'New')
# create_product('Bike', 7777.77, 2, 'Used')

# range(20,300)
# <Field_name>__<lookup_key> = <Lookup_value>

# q = Product.objects.filter(name__icontains = 'bi')
    
# q = Product.objects.filter(price__range = (20,50))


# q = Product.objects.filter(Q(name='Monitor') or Q(price=555.55))


# q = Product.objects.filter( ~ Q(name='Monitor'))

# print(q.values())


#-------------


# q = Product.objects.filter( ~ Q(name='Headphone')).filter(condition='New').filter(price__gte=1000)

# q2 = q.filter(name='Harddisk')

# print(q2.values())


#--------------


# q = Product.objects.filter(price__gte=1000).annotate(description=Value('Discount 30%'))

# q = Product.objects.annotate(total_price= F('price') * F('quantity'))

# q = Product.objects.filter(name='Bike').annotate(amount=Count('name'))


# q = Product.objects.values('name')

# q2 = q.annotate(amount=Count('name'))


q = Product.objects.values('quantity').order_by('quantity')

print(q)




