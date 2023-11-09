#program for linear search product 
def LinearSearchProduct(productList, targetProduct):
  indices = []
  
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
      
  return indices

#example usage
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target1 = "shoes"
result = LinearSearchProduct(products, target1)
print(result)
