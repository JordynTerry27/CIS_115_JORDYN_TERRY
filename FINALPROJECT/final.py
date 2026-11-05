prod_catalog = [
    {"Product ID":"1", "SKU":"usb_k981","Price":"$12.00", "Description":"USB 128 GB drive.", "Qty on Hand":"1000", "Abbreviation": "USB Drive(128 GB)"},
    {"Product ID":"2", "SKU":"mbpro_490","Price":"$2900.00", "Description":"Mac Book Pro 15 inch.", "Qty on Hand":"45", "Abbreviation": "Mac Book Pro(15 inch)"},
    {"Product ID":"3", "SKU":"chip_1010","Price":"$48.00", "Description":"Arduino microprocessor", "Qty on Hand":"325", "Abbreviation": "Arduino 1010(with blue tooth)"},
    {"Product ID":"4", "SKU":"cam_78","Price":"$156.00", "Description":"Ring Camera Model 78.", "Qty on Hand":"98", "Abbreviation": "Ring Camera(wireless)"},
    {"Product ID":"5", "SKU":"smt_tv_100","Price":"$359.00", "Description":"TCL Smart TV.", "Qty on Hand":"225", "Abbreviation": "Smart TV(TCL 70 inch)"}
]

hyphens = "-" * 50
spaces = " " * 20
bars = "|"
print(hyphens)
print(" " * 17 + "PRODUCT CATALOG")
print(hyphens)

for prod_item in prod_catalog:
      length = len("Abbreviation") - len(spaces)
      full_length = length * " "
      print(prod_item["Abbreviation"] + full_length + spaces + "|" + prod_item["Price"])
      print(len(prod_catalog["Abbreviation"]))


  