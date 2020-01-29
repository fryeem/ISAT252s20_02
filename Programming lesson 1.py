x1=int(input("Number of Small Digesters:"))
x2=int(input("Number of Medium Digesters:"))
x3=int(input("Number of Large Digesters:"))

y1=int(input("Blows per each small digester:"))
y2=int(input("Blows per each medium digester:"))
y3=int(input("Blows per each large digester:"))

z1=int(input("Tons per small digester blow:"))
z2=int(input("Tons per medium digester blow:"))
z3=int(input("Tons per large digester blow:"))

Output_per_small_digester=(x1*y1*z1)
Output_per_medium_digester=(x2*y2*z2)
Output_per_large_digester=(x3*y3*z3)

print ("Total output from small digesters each day:", Output_per_small_digester)
print ("Total output from medium digesters each day:", Output_per_medium_digester)
print ("Total output from large digesters each day:", Output_per_large_digester)
