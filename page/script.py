import streamlit as st
import numpy as np

st.set_page_config(page_title="5AA - Algoritmo")

st.title('Distância entre países e suas respectivas capitais.')

st.text_input("Insira o primeiro local", key="loc1")
st.text_input("Insira o segundo local", key="loc2")


data1 = st.session_state.loc1 #'R Doutor José Maria 804'
data2 = st.session_state.loc2 #'Pátio de São Pedro'


with open('./data/capdist.csv', 'r', encoding='utf-8') as arquivo:
    f = arquivo.readlines()
city = []
count = 0
for i in f:
    a = i.split(',')
    city.append(a[0])
    count += 1

tmp=[]

for i in city:
    if tmp.__contains__(i):
        pass
    else:
        tmp.append(i)
        
#Armando o dicionário
dic = {}    
for i in f:
    a = i.split(',')
    dic[a[0]] = {}

for i in f:
    a = i.split(',')
    dic[a[0]][a[2]] = int(a[4])

#Encontrar pais pelo index
def findCountry(country):
    with open('./data/index.csv', 'r') as arquivo:
        for i in arquivo:
            a = i.split(',')
            if(a[0] == country):
                return a[1]

if not tmp.__contains__(data1) and data1 != "":
    st.text("O país "+data1+" não existe no banco de dados")
elif not tmp.__contains__(data2) and data2 != "":
    st.text("O país "+data2+" não existe no banco de dados")
elif not tmp.__contains__(data1) and not tmp.__contains__(data2):
    st.text("Os países "+data1+"e "+data2+" não existem no banco de dados")
else:

    def dijkstra(grafo,src,dest):
        shortest_distance = {}

        predecessor = {}

        n_vistos = grafo
        inf = 9999999

        path = []
        for node in n_vistos:
            shortest_distance[node] = inf
        shortest_distance[src] = 0

        while n_vistos:
            minNode = None
            for node in n_vistos:
                if minNode is None:
                    minNode = node
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node

            for childNode, weight in grafo[minNode].items():
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                    shortest_distance[childNode] = weight + shortest_distance[minNode]
                    predecessor[childNode] = minNode
            n_vistos.pop(minNode)

        currentNode = dest
        while currentNode != src:
            try:
                path.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('Não existe caminho')
                break
        path.insert(0,src)
        if shortest_distance[dest] != inf:
            # print('Menor distancia ' + str(shortest_distance[dest]))
            # print('Caminho ')
            # string = ''
            # for i in range(len(path)):
            #     var = findCountry(path[i])
            #     string += var 

            return path, shortest_distance[dest]



    paises, dist = dijkstra(dic,data1,data2)

    string = ''
    for i in range(len(paises)):
        paises[i] = findCountry(paises[i]).strip('\n')

    for i in range(len(paises)):
        if(i == len(paises) - 1):
            string += paises[i]
        else:
            string += paises[i] + ' -> '
        
    
    st.text("Distancia entre "+findCountry(data1).strip('\n')+" e "+findCountry(data2).strip('\n')+" é de "+str(dist)+" km")
    st.text("Caminho necessário : "+ string)



