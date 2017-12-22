pc1 = [56, 48, 40, 32, 24, 16,  8,
		  0, 57, 49, 41, 33, 25, 17,
		  9,  1, 58, 50, 42, 34, 26,
		 18, 10,  2, 59, 51, 43, 35,
		 62, 54, 46, 38, 30, 22, 14,
		  6, 61, 53, 45, 37, 29, 21,
		 13,  5, 60, 52, 44, 36, 28,
		 20, 12,  4, 27, 19, 11,  3]
pc2 = [
		13, 16, 10, 23,  0,  4,
		 2, 27, 14,  5, 20,  9,
		22, 18, 11,  3, 25,  7,
		15,  6, 26, 19, 12,  1,
		40, 51, 30, 36, 46, 54,
		29, 39, 50, 44, 32, 47,
		43, 48, 38, 55, 33, 52,
		45, 41, 49, 35, 28, 31
	]



def re_per(table,data, ii):
	res = [-1]*ii
	for i in range(0,len(table)):
		res[table[i]] = data[i]
	return res

def rol(data):
	return data[len(data)-1:len(data)]+data[:len(data)-1]

Knn = [0] * 16
die = [8, 17, 21, 24, 34, 37, 42, 53]
for i in range(16):
	Knn[i] = re_per(pc2,DES.Kn[i],56)

for i in die:
	Knn[0][i] = Knn[1][i-1]

L = rol(L)
R = rol(R)

K = L + R
i_k = re_per(pc1,K,64)

for i in range(8):
	flag = 0
	for j in range(7):
		flag += i_k[i*8+j]
	i_k[i*8+7] = 0

key = b''
for i in range(8):
	flag = 0
	for j in range(8):
		flag += i_k[i*8+j] * pow(2,7 - j)
	key += bytes([flag])
print(key)