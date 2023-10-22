#Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found￼
def linear_search_product(products: list[Product], target_product_name: str) -> list[int]:
  """Performs a linear search to find the target product in the list and returns a list of indices of all occurrences of the product if found, or an empty list if the product is not found.

  Args:
    products: A list of products.
    target_product_name: The name of the target product to search for.

  Returns:
    A list of indices of all occurrences of the target product if found, or an empty list if the product is not found.
  """

  product_indices = []
  for i in range(len(products)):
    product = products[i]
    if product.name == target_product_name:
      product_indices.append(i)
  return product_indices


products = [
    Product("Apple", 1.99),
    Product("Banana", 0.99),
    Product("Orange", 0.79),
    Product("Apple", 1.99),
]

target_product_name = "Apple"

product_indices = linear_search_product(products, target_product_name)

print(product_indices)


#[0, 3]