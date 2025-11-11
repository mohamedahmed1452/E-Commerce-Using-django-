from ecommerce.models import Category, Brand, Product

def run():
    # Create Categories
    electronics = Category.objects.create(name="Electronics", description="Electronic gadgets and devices.")
    fashion = Category.objects.create(name="Fashion", description="Clothing and accessories.")
    home = Category.objects.create(name="Home", description="Home appliances and furniture.")
    sports = Category.objects.create(name="Sports", description="Sporting goods and equipment.")
    beauty = Category.objects.create(name="Beauty", description="Beauty and personal care products.")

    # Create Brands
    apple = Brand.objects.create(name="Apple", description="Premium electronics brand.")
    nike = Brand.objects.create(name="Nike", description="Sportswear and shoes.")
    samsung = Brand.objects.create(name="Samsung", description="Electronics and home appliances.")
    ikea = Brand.objects.create(name="IKEA", description="Home and furniture brand.")
    loreal = Brand.objects.create(name="L'Oreal", description="Beauty and skincare brand.")

    # Create Products
    Product.objects.create(name="iPhone 15", description="Latest Apple smartphone", price=999.99, Category=electronics, Brand=apple)
    Product.objects.create(name="Galaxy S24", description="Flagship Samsung smartphone", price=899.99, Category=electronics, Brand=samsung)
    Product.objects.create(name="Nike Air Max", description="Comfortable running shoes", price=120.00, Category=sports, Brand=nike)
    Product.objects.create(name="IKEA Chair", description="Stylish and comfortable chair", price=85.50, Category=home, Brand=ikea)
    Product.objects.create(name="L'Oreal Shampoo", description="Revitalizing hair shampoo", price=12.99, Category=beauty, Brand=loreal)

    print("✅ Sample data inserted successfully!")
