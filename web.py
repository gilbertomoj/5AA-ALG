import streamlit as st
import pandas as pd

st.set_page_config(page_title="5AA - Algoritmo")

st.title('Distância entre países e suas respectivas capitais.')

st.text("Paises e reus respectivos ID's")
df = pd.read_csv('./page/data/index.csv')

st.dataframe(df, 200, 200)

st.text_input("Insira o ID do primeiro pais", key="loc1")
st.text_input("Insira o ID do segundo pais", key="loc2")

if st.button('Buscar'):

    data1 = st.session_state.loc1 # Definido pelas chaves no st.text_input
    data2 = st.session_state.loc2 #'Definido pelas chaves no st.text_input
    
    # Leitura dos dados
    with open('./page/data/capdist.csv', 'r', encoding='utf-8') as arquivo:
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

    dic = {}    
    for i in f:
        a = i.split(',')
        dic[a[0]] = {}

    for i in f:
        a = i.split(',')
        dic[a[0]][a[2]] = int(a[4])

    #Encontrar pais pelo index
    def achaPais(country):
        with open('./page/data/index.csv', 'r') as arquivo:
            for i in arquivo:
                a = i.split(',')
                if(a[0] == country):
                    return a[1]

    if not tmp.__contains__(data1) or data1 == "":
        st.text("O país "+data1+" não existe no banco de dados")
    elif not tmp.__contains__(data2) or data2 == "":
        st.text("O país "+data2+" não existe no banco de dados")
    elif not tmp.__contains__(data1) and not tmp.__contains__(data2):
        st.text("Os países "+data1+"e "+data2+" não existem no banco de dados")
    else:
        # Algoritmo Dijkstra
        def Dijkstra(grafo,src,dest):

            n_vistos = grafo
            inf = 9999999

            caminho = []

            menor_dist = {}
            for vertice in n_vistos:
                menor_dist[vertice] = inf

            predecessor = {}
            menor_dist[src] = 0
            while n_vistos:
                menor = None
                for node in n_vistos:
                    if menor is None:
                        menor = node
                    elif menor_dist[node] < menor_dist[menor]:
                        menor = node

                for adjacente, distancia in grafo[menor].items():
                    if distancia + menor_dist[menor] < menor_dist[adjacente]:
                        menor_dist[adjacente] = distancia + menor_dist[menor]
                        predecessor[adjacente] = menor
                n_vistos.pop(menor)

            atual = dest          
            while atual != src:
                try:
                    caminho.insert(0,atual)
                    atual = predecessor[atual]
                except KeyError:
                    st.text("Este caminho não existe")
                    break
            caminho.insert(0,src)
            if menor_dist[dest] != inf:
                return caminho, menor_dist[dest]

        paises, dist = Dijkstra(dic,data1,data2)

        string = ''
        for i in range(len(paises)):
            paises[i] = achaPais(paises[i]).strip('\n')

        for i in range(len(paises)):
            if(i == len(paises) - 1):
                string += paises[i]
            else:
                string += paises[i] + ' -> '
            
        st.text("Distancia entre "+achaPais(data1).strip('\n')+" e "+achaPais(data2).strip('\n')+" é de "+str(dist)+" km")
        st.text("Caminho necessário : "+ string)



