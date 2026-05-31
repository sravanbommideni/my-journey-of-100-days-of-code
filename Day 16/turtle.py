from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Name" , "Grade" , "City"]
table.add_row(["sravan",10,"jammikunta"])
table.add_row(["Vishnu",1,"siddipet"])
table.add_column("college" , ["JNTU","Geetanjali"])
print(table)