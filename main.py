from vec import Vec
from  GF2 import  one;
from  vec import  add
from  vec import scalar_mul
do = ["A","B","C"]

a = Vec(do, {"A":one,"C": one})

c = Vec(do, {"B": one,"C":one})





lista = [a,c]





#L lista de vetores
def GF2_span(D,L):
    #lista de retorno
    span = []

    #se L for vazio retorna o vetor nulo
    if (len(L) == 0):
        empty_vec = Vec(D,{})
        span.append((empty_vec))
        return empty_vec

    # transforma n em uma lista de binario com tamanho len(L)
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


    #valor máximo de um vetor em binário com len(l)  entradas
    binary_max = [1 for i in range(len(L))]

    #valor maximo em decimal
    value_max = 0

    # calcula o valor de binary_max em decimal
    for j in  range(len(binary_max)):
        value_max += 2**j
    #coloca em listas todos binarios de 0 a value_max, essa lista sera toda combinacao de escalares possiveis para multiplicar os vetores em ordem
    for i in range(value_max+1):
        scalar_combinations = to_binary(i,len(L))
        vec_mul = [] #ira guadar a multiplicacao esacalar de uma combinacao de escalares por todos vetores em L

        #cada vetor em L multiplicamos por um escalar
        for k in range(len(scalar_combinations)):
            vec_mul.append(scalar_mul(L[k],scalar_combinations[k]))

        sum = Vec(D,{}) #guarda a soma dos vetores multiplicados pelo escalar
        for vec in vec_mul:
            temporary = add(sum,vec)
            sum = temporary

        span.append(sum)

    span_no_repeat = []

    #garantia de que nao ira ter vetores repetidos
    for vec in span:
        if vec not in span_no_repeat:
            span_no_repeat.append(vec)

    return span_no_repeat





output = GF2_span(do,lista)


print(output)




















