print("______________")
print("   |\n  a|_b_\n-r-  q")
print("______________\na = b.q + r\n______________")

a_origi = int(input("Digite o valor de a: "))
b_origi = int(input("Digite o valor de b: "))
conta = 1
def Euclides(a, b, contador=0):
  contador += 1
  q = int(a/b)
  r = a%b
  if(r != 0):
    
    return print("________________\n"+str(contador)+". "+str(a)+' = '+str(b)+"("+str(q)+") + "+str(r)+"\n"+"   |\n  "+str(a)+"|_"+str(b)+"_\n-"+str(r)+"-  "+str(q)), Euclides(b, r, contador=contador)
  else:
    print("________________\n"+str(contador)+". "+str(a)+' = '+str(b)+"("+str(q)+") + "+str(r)+"\n"+"   |\n  "+str(a)+"|_"+str(b)+"_\n-"+str(r)+"-  "+str(q)+"\nMDC de ("+str(a_origi)+", "+str(b_origi)+") = "+str(b))
Euclides(a_origi,b_origi)
