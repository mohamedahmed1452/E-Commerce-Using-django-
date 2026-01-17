# 🚀 High-Performance E-Commerce API with Django REST Framework

A robust, scalable RESTful API for an E-Commerce platform built with Django and Django REST Framework (DRF).

This project goes beyond basic CRUD operations. It serves as a comprehensive demonstration of **multiple DRF implementation patterns** (from simple function-based views to complex ViewSets) and focuses heavily on **Database Performance Optimization**, solving real-world issues like the N+1 query problem using advanced ORM techniques and profiling tools.

---

## ✨ Key Features

* **Comprehensive Product Management:** Full CRUD capability for Products, Categories, and Brands.
* **Order & Review System:** Complete workflow for customer orders and product reviews.
* **Advanced Filtering & Searching:** Utilizing `DjangoFilterBackend`, `SearchFilter`, and `OrderingFilter` for powerful list endpoints.
* **DRF Pattern Showcase:** Implementation of endpoints using FBVs, Class-Based Views, Generics, and ModelViewSets in the same project for educational comparison.
* **Performance Optimization:** Critical analysis and resolution of database bottlenecks (N+1 Query problem) using `select_related` and `prefetch_related`.
* **Advanced ORM Techniques:** Utilization of `Q` objects, `F` expressions, database indexing, and query field limiting (`only`/`defer`).
* **Profiling Integration:** Integrated **Django Silk** for real-time request inspection and query analysis.

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Django 4.x**
* **Django REST Framework (DRF)**
* **Django-Filter**
* **Django Silk** (Performance Profiling)
* **SQLite** (Development DB) / PostgreSQL (Recommended for Production)

---

## ⚡ Performance Optimization Case Study

One of the primary goals of this project was to ensure scalability through optimized database queries. We used **Django Silk** to profile endpoints and identify bottlenecks.

### The Challenge: The N+1 Query Problem

An initial implementation of the Product List endpoint created a classic N+1 query issue. For every product fetched, Django was executing separate queries to retrieve related `Category` and `Brand` information.

* **Scenario:** Fetching products along with their related Category info.
* **Unoptimized approach:** Resulted in 28 separate SQL queries for a small data set.

### The Solution: `select_related`

By optimizing the queryset using Django's ORM `select_related()` (for ForeignKey relationships), we forced Django to perform a SQL JOIN, fetching all necessary data in a single query.

### 📊 Silk Profiling Results (Before vs. After)

Testing the endpoint: `GET /api/products/?Category_id=5`

| Metric | Unoptimized | Optimized (using `select_related`) | Impact |
| :--- | :--- | :--- | :--- |
| **Total Database Queries** | 28 Queries | **9 Queries** | 🔻 Massive Reduction |
| **Total Response Time** | 559 ms | **374 ms** | 🚀 ~35-40% Faster |

> **Conclusion:** The optimization significantly reduced database chatter and latency. For Many-to-Many relationships (e.g., Tags), `prefetch_related()` is similarly applied.

---

## 🧠 Advanced Django ORM Concepts Explored

This project demonstrates deeper knowledge of the Django ORM beyond simple `.all()` and `.filter()`.

### 1. Dynamic Complex Filtering (`Q` Objects)
Used for creating complex queries with logical OR/AND conditions.
```python
from django.db.models import Q
# Find products that are Electronics AND cost more than 500
Product.objects.filter(Q(Category__name="Electronics") & Q(price__gt=500))
2. Atomic Database Updates (F Expressions)Updating fields directly at the database level without loading objects into Python memory, avoiding race conditions.Pythonfrom django.db.models import F
# Increase the price of all products by 10% atomically
Product.objects.update(price=F('price') * 1.1)
3. Query Optimization (only & defer)Optimizing memory usage by fetching only the necessary columns from the database table.Python# Only fetch 'name' and 'price' columns
Product.objects.only('name', 'price')

# Fetch everything EXCEPT the heavy 'description' text field
Product.objects.defer('description')
4. Database IndexingAdding db_index=True to frequently searched model fields (like name or price) to significantly speed up lookup times.📂 API Structure ShowcaseThis project deliberately uses mixed methodologies to demonstrate DRF proficiency:Endpoint ImplementationExample Used In ProjectDescriptionFunction-Based Views (@api_view)product_listSimple, direct control over request/response. Good for basic logic.Class-Based Views (APIView)ProductClassBasedViewMore structured, separates HTTP methods (GET, POST, PUT, DELETE).Generic ViewsListCreateAPIView, RetrieveUpdateDestroyAPIViewReduces boilerplate for standard CRUD actions.ModelViewSetsProductsViewSet, OrderViewSet, etc.Maximum abstraction. Handles full CRUD and routing automatically. The most efficient for standard resources.⚙️ Local Installation & SetupFollow these steps to run the project locally:Clone the repository:Bashgit clone [https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/YOUR_USERNAME/REPO_NAME.git)
cd REPO_NAME
Create and activate a virtual environment:Bash# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies:Bashpip install -r requirements.txt
Apply database migrations:Bashpython manage.py migrate
Create a superuser (admin):Bashpython manage.py createsuperuser
Run the development server:Bashpython manage.py runserver
Access the API at http://127.0.0.1:8000/.
