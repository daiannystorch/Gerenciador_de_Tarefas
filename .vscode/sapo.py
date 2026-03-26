#N1 = 1 -> [1] = 1
#N2 = 2 -> [1,1], [2] =2
#N3 = 3 -> [1,1,1], [1,2], [2,1] =3
#N4 = 4 -> [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2] = 5
#N5 = 5 -> [1,1,1,1,1], [1,1,1,2], [1,1,2,1], [1,2,1,1], [2,1,1,1], [1,2,2], [2,1,2], [2,2,1] = 8
def contar_caminhos (num_pedras):
  if num_pedras <=1:
    return 1
  return contar_caminhos (num_pedras - 1) + contar_caminhos (num_pedras -2)
print (contar_caminhos (5))