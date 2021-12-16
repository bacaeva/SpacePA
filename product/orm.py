#select
#select * from products;
#Product.objects.all()

#select from pr.. where

# select * from product where price = 100000;
# product.objects.filter(price = 10000)

# select * from products where price !=10000;
# product.objects.filter(~Q(price = 100000))
# product.objects.f=exclude(price= 10000)
#
# select * from product where price >10000;
# Product.object.filter(price__gt=100000)
#
#
# select * from product where price<1000
# product.object.filter(price__lt=1000)
#
# select * from product where price<=1000
# product.object.filter(price__lte=1000)

# select * from product where category_id in ('phones','tv');
# product.object.filter(category_id__in=['phones','tv'])
#
#
# select * from product where price between 20000 and 50000;
# product.object.filter(price__range=[2000,5000])
#
# like
# select * from product where name like 'test';
# product.object.filter(name__exact='test')
# select * from product where name like 'test';
# product.object.filter(name__iexact='test')

# select * from product where name like '%test%';
# product.object.filter(name__contans ='test')
# product.object.filter(name__endswith ='test')
# product.object.filter(name__iendswith ='test')

#для получение одной записи in и get
#select * from product where id=1;

#ограничение набора полей
# select name,price from product;;

# product.objects.only('name','price')

#select id, desctription, category_id from products;
# product.object.only('id','description','cotegory_id')
# #product.obkects.defer('name','price')
#
# select  * from product order by price;
# product.object.order_by('price')
#

# insert
# insert into product (name, description,price,category)
# values('mi10','telefon','2000','phones')
# product.object.creat(mi10','telefon','2000','phones')
#
#
# product.object.bulk_create(
#     [
#         ..............
#     ]
# )
#
#
# product = Product(...)
# product.save()
#
#update
# update products set price = 100000;
# product.objects.update(price = 1000)
# update products set price = 10000 where cotegory = 'phones'
# product.objects.filter(category = 'phones').update('price=20000')
#
# #обновить один обьект
# product = product.objects.get(id=1)
# product.price = 2000
# product.save()


# delete
# delete from product
# product.objects.delele()
# delete from product where category = 'tv';
# product.objects.filter(category='tv').delete()




