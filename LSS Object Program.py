company = 'Pixelle Specialty Solutions'
print(company)

###Array digesters by size
x1=int(input("# of Small Digesters:"))
x2=int(input("# of Medium Digesters:"))
x3=int(input("# of Large Digesters:"))

Total_Number_of_Digesters = (x1+x2+x3)
print("Total # of Digesters:", Total_Number_of_Digesters )

y1=int(input("Maximum Daily Sustainable Production Rate of Small Digester:")) ### measured in Tons/Day
y2=int(input("Maximum Daily Sustainable Production Rate of Medium Digester:")) ### measured in Tons/Day
y3=int(input("Maximum Daily Sustainable Production Rate of Large Digester:")) ### measured in Tons?

z1=int(input("Tons per small digester blow:"))
z2=int(input("Tons per medium digester blow:"))
z3=int(input("Tons per large digester blow:")) 

Output_per_small_digester=(x1*y1*z1)
Output_per_medium_digester=(x2*y2*z2)
Output_per_large_digester=(x3*y3*z3)
Total_Theoretical_Production_Output_per_day = (Output_per_small_digester+Output_per_medium_digester+Output_per_large_digester)

print ("Total output from small digesters each day:", Output_per_small_digester)
print ("Total output from medium digesters each day:", Output_per_medium_digester)
print ("Total output from large digesters each day:", Output_per_large_digester)

