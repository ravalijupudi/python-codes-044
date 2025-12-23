product_id=int(input("enter product id:"))
product_name=input("enter product name:")
price=float(input("price:"))
categories=input("categories(comma seperated):").split(",")
available=int(input("available stock:"))
sold=int(input("sold stock:"))
stock = (available, sold)
discount=float(input("discount percentage:"))
features=set(input("product features(comma seperated): ").split(","))
supplier_name=input("supplier name: ")
supplier_contact=input("supplier contact: ")
supplier_location=input("supplier location: ")
supplier={
    "name":supplier_name,
    "contact":supplier_contact,
    "location":supplier_location
}
print("\n---product details---\n")
print("id,name,price",product_id,product_name,price,sep=",")
print("discount:")
print(f"product:{product_name}")
print(f"price:{price}")
print(f"available stock:{stock}")
print("supplier:{},{},{}".format(
    supplier["name"],
    supplier["contact"],
    supplier["location"]
))