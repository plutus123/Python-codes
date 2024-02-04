import matplotlib.pyplot as plt
sizes=[1,6,4,3,2]
plt.title("Laptop sales in 2018")
company_name=['Apple','HP','Asus','Tuf','Vivobook']
plt.pie(sizes,labels=company_name,autopct='%.1f',counterclock=False,startangle=100)
plt.show()
