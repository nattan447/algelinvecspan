from vec import Vec
from  GF2 import  one;
from  vec import  add
from  vec import scalar_mul
D = ["A","B"]

a = Vec(D, {"A":one,"C": one})

c = Vec(D, {"B": one,"C":one})


lista = [a,c]


# transforma n em uma lista de binario com tamanho len(D)-1
def to_binary(n, size):
    # enche todo vetor com zeros

    binary_list = [0 for i in range(size)]

    binary_size = size - 1

    while (binary_size >= 0):
        # algoritimo para trnasformar em binario
        new_n = n
        if (n == 1):
            binary_list[binary_size] = 1
            break
        quociente = new_n // 2
        rest = new_n % 2
        binary_list[binary_size] = rest
        n = quociente
        binary_size += -1
    return binary_list


#L lista de vetores
def GF2_span(L):
    #lista de retorno
    span = []
    #total de combinção de escalares com base no tamanho do dominio dos vetores
    combinations = 2**len(D)

    #valor máximo de um vetor em binário com len(D)-1 entradas
    binary_max = [1 for i in range(len(D))]
    #valor maximo em decimal
    value_max = 0
    # calcula o valor de binary_max em decimal
    for j in  range(len(binary_max)):
        value_max += 2**j
    #coloca em listas binarios de 0 a 8
    for i in range(value_max+1):
        scalar_combinations = to_binary(i,len(D))
        #para cada scalar iremos distribuilos nos vetores
        for k  in range(len(scalar_combinations)):
            

            span.append(scalar_combinations)

    print(span)


    #for i in range(combinations):
        #bin_list = [int(x) for x in bin(i)[2:].zfill(len(D))]
        #span.append(bin_list)

GF2_span()




















