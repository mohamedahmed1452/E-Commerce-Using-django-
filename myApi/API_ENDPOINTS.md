# E-Commerce API Endpoints Documentation

## Base URL

```
http://127.0.0.1:8000/api/
```

---

## PRODUCTS ENDPOINTS

### 1. List All Products (Function-based View)

- **URL:** `/api/product_list/`
- **Methods:** GET, POST
- **GET:** Retrieve all products
- **POST:** Create a new product
- **Request Body (POST):**

```json
{
  "name": "Product Name",
  "description": "Product Description",
  "price": "99.99",
  "Category": 1,
  "Brand": 1
}
```

- **Response:** List of all products or created product

---

### 2. Product CRUD Operations (Class-based View)

- **URL:** `/api/products/<int:pk>/`
- **Methods:** GET, PUT, PATCH, DELETE
- **GET:** Retrieve a specific product by ID
- **PUT:** Replace entire product
- **PATCH:** Partially update a product
- **DELETE:** Delete a product
- **Request Body (PUT/PATCH):**

```json
{
  "name": "Updated Name",
  "description": "Updated Description",
  "price": "149.99",
  "Category": 1,
  "Brand": 1
}
```

---

### 3. Product List/Create (Generic View)

- **URL:** `/api/products/list/create/`
- **Methods:** GET, POST
- **GET:** Retrieve all products with formatted response
- **POST:** Create a new product
- **Response (GET):**

```json
{
  "products": [
    {
      "id": 1,
      "name": "Product Name",
      "description": "Description",
      "price": "99.99",
      "Category": 1,
      "Brand": 1
    }
  ]
}
```

---

### 4. Product Detail View

- **URL:** `/api/product/<int:pk>/detail/`
- **Methods:** GET, PUT, DELETE
- **GET:** Retrieve product details
- **PUT:** Update entire product
- **DELETE:** Delete product

---

### 5. Products ViewSet (Router)

- **URL:** `/api/products/`
- **Methods:** GET, POST, PUT, PATCH, DELETE
- **Features:** Full CRUD operations via DRF router
- **Supports:** Filtering, searching, ordering

---

## CATEGORIES ENDPOINTS

### 1. Category ViewSet (Full CRUD)

- **URL:** `/api/categories/`
- **Methods:** GET, POST, PUT, PATCH, DELETE
- **List:** `/api/categories/` (GET)
- **Create:** `/api/categories/` (POST)
- **Retrieve:** `/api/categories/{id}/` (GET)
- **Update:** `/api/categories/{id}/` (PUT)
- **Partial Update:** `/api/categories/{id}/` (PATCH)
- **Delete:** `/api/categories/{id}/` (DELETE)
- **Request Body (POST/PUT):**

```json
{
  "name": "Electronics",
  "description": "Electronic products"
}
```

- **Features:** Filtering, searching, ordering

---

### 2. Category List View

- **URL:** `/api/categories/list/`
- **Methods:** GET
- **Features:** Search and ordering
- **Query Parameters:**
  - `search=name` - Search in name and description
  - `ordering=name` - Order by name

---

## BRANDS ENDPOINTS

### 1. Brand ViewSet (Full CRUD)

- **URL:** `/api/brands/`
- **Methods:** GET, POST, PUT, PATCH, DELETE
- **List:** `/api/brands/` (GET)
- **Create:** `/api/brands/` (POST)
- **Retrieve:** `/api/brands/{id}/` (GET)
- **Update:** `/api/brands/{id}/` (PUT)
- **Partial Update:** `/api/brands/{id}/` (PATCH)
- **Delete:** `/api/brands/{id}/` (DELETE)
- **Request Body (POST/PUT):**

```json
{
  "name": "Samsung",
  "description": "Samsung Electronics"
}
```

- **Features:** Filtering, searching, ordering

---

### 2. Brand List View

- **URL:** `/api/brands/list/`
- **Methods:** GET
- **Features:** Search and ordering

---

## ORDERS ENDPOINTS

### 1. Order ViewSet (Full CRUD)

- **URL:** `/api/orders/`
- **Methods:** GET, POST, PUT, PATCH, DELETE
- **List:** `/api/orders/` (GET)
- **Create:** `/api/orders/` (POST)
- **Retrieve:** `/api/orders/{id}/` (GET)
- **Update:** `/api/orders/{id}/` (PUT)
- **Partial Update:** `/api/orders/{id}/` (PATCH)
- **Delete:** `/api/orders/{id}/` (DELETE)
- **Request Body (POST/PUT):**

```json
{
  "product": 1,
  "quantity": 5
}
```

- **Response:**

```json
{
  "id": 1,
  "product": 1,
  "product_name": "Product Name",
  "quantity": 5,
  "order_date": "2025-12-07T10:30:00Z"
}
```

- **Features:** Filtering by product/quantity, searching, ordering by date

---

### 2. Order List View

- **URL:** `/api/orders/list/`
- **Methods:** GET
- **Features:** Filtering, searching, ordering

---

## REVIEWS ENDPOINTS

### 1. Review ViewSet (Full CRUD)

- **URL:** `/api/reviews/`
- **Methods:** GET, POST, PUT, PATCH, DELETE
- **List:** `/api/reviews/` (GET)
- **Create:** `/api/reviews/` (POST)
- **Retrieve:** `/api/reviews/{id}/` (GET)
- **Update:** `/api/reviews/{id}/` (PUT)
- **Partial Update:** `/api/reviews/{id}/` (PATCH)
- **Delete:** `/api/reviews/{id}/` (DELETE)
- **Request Body (POST/PUT):**

```json
{
  "product": 1,
  "name": "John Doe",
  "description": "Great product!",
  "rating": 5
}
```

- **Response:**

```json
{
  "id": 1,
  "product": 1,
  "product_name": "Product Name",
  "name": "John Doe",
  "description": "Great product!",
  "date": "2025-12-07"
}
```

- **Features:** Filtering by product/name, searching, ordering by date

---

### 2. Review List View

- **URL:** `/api/reviews/list/`
- **Methods:** GET
- **Features:** Filtering, searching, ordering

---

## QUERY PARAMETERS

### Filtering

```
?product=1
?quantity=5
?name=Samsung
```

### Searching

```
?search=phone
?search=electronics
```

### Ordering

```
?ordering=name
?ordering=-price
?ordering=-created_at
```

---

## HTTP STATUS CODES

- **200 OK** - Successful GET request
- **201 CREATED** - Successful POST request
- **204 NO CONTENT** - Successful PUT/PATCH/DELETE request
- **400 BAD REQUEST** - Invalid data
- **404 NOT FOUND** - Resource not found
- **500 INTERNAL SERVER ERROR** - Server error

---

## EXAMPLE REQUESTS

### Create a Product

```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 15",
    "description": "Latest iPhone model",
    "price": "999.99",
    "Category": 1,
    "Brand": 1
  }'
```

### Get All Products

```bash
curl http://127.0.0.1:8000/api/products/
```

### Get Specific Product

```bash
curl http://127.0.0.1:8000/api/products/1/
```

### Update Product

```bash
curl -X PUT http://127.0.0.1:8000/api/products/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 15 Pro",
    "description": "Updated description",
    "price": "1099.99",
    "Category": 1,
    "Brand": 1
  }'
```

### Delete Product

```bash
curl -X DELETE http://127.0.0.1:8000/api/products/1/
```

### Search Products

```bash
curl "http://127.0.0.1:8000/api/products/?search=phone"
```

### Filter Orders by Product

```bash
curl "http://127.0.0.1:8000/api/orders/?product=1"
```

### Order by Price (Descending)

```bash
curl "http://127.0.0.1:8000/api/products/?ordering=-price"
```

---

## DATA MODELS

### Product

- `id` (Integer, Read-only)
- `name` (String, Max 100 chars)
- `description` (Text)
- `price` (Decimal, Max 10 digits)
- `Category` (Foreign Key)
- `Brand` (Foreign Key)
- `created_at` (DateTime, Auto)
- `updated_at` (DateTime, Auto)

### Category

- `id` (Integer, Read-only)
- `name` (String, Max 100 chars)
- `description` (Text)

### Brand

- `id` (Integer, Read-only)
- `name` (String, Max 100 chars)
- `description` (Text)

### Order

- `id` (Integer, Read-only)
- `product` (Foreign Key)
- `quantity` (Integer)
- `order_date` (DateTime, Auto)

### Review

- `id` (Integer, Read-only)
- `product` (Foreign Key)
- `name` (String, Max 255 chars)
- `description` (Text)
- `rating` (Integer, 1-5)
- `date` (Date, Auto)

---

## VALIDATION RULES

### Product

- `name` cannot be "Mohamed"
- All fields are required except `created_at`, `updated_at`

### Category, Brand

- `name` and `description` are required

### Order

- `product` and `quantity` are required
- `quantity` must be a positive integer

### Review

- `product`, `name`, and `description` are required
- `rating` must be between 1-5 (default: 5)

---

## FEATURES

✅ Full CRUD operations for all resources
✅ Filtering by specific fields
✅ Search functionality across relevant fields
✅ Ordering/sorting capabilities
✅ DRF ViewSets with automatic router
✅ Class-based and function-based views
✅ Proper HTTP status codes
✅ Nested field serialization
✅ Input validation
✅ Related name support for reverse relationships
