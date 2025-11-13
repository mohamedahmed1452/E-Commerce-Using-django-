from ecommerce.models import Category, Brand, Product, Tag

def run():
    # (reuse your existing category, brand, and product creation)

    electronics = Category.objects.create(name="Electronics", description="Electronic gadgets and devices.")
    apple = Brand.objects.create(name="Apple", description="Premium electronics brand.")
    samsung = Brand.objects.create(name="Samsung", description="Electronics and home appliances.")

    iphone = Product.objects.create(name="iPhone 15", description="Latest Apple smartphone", price=999.99, Category=electronics, Brand=apple)
    galaxy = Product.objects.create(name="Galaxy S24", description="Flagship Samsung smartphone", price=899.99, Category=electronics, Brand=samsung)

    # ✅ Tags
    t1 = Tag.objects.create(name="Smartphones")
    t2 = Tag.objects.create(name="Flagship")
    t3 = Tag.objects.create(name="New Release")

    iphone.tags.add(t1, t2, t3)
    galaxy.tags.add(t1, t2)

    print("✅ Sample data with tags inserted successfully!")