import streamlit as st 
from PIL import Image
import pandas as pd
import altair as alt
import plotly.express as px
st.title("Aplicación")
st.sidebar.title("Parámetros")
st.subheader("App 1")
st.write("Inicio")
x=2
x=x**2+7-3
st.write(x)
html1="""
<div style="background-color:orange ;padding:20px">
<h2 style="color:black ;text-align:center;">4G</h2>
</div>

"""
st.markdown(html1,unsafe_allow_html=True)
imagen=Image.open("imagen1.jpg")
st.image(imagen)

st.sidebar.image(imagen)

lx=[1,2,3,4,5,6,7,8,9,10]
ly=["a","b","c","d","e","f","g","h","i","j"]
lz=["Alto","Medio","Bajo","Alto","Medio","Bajo","Alto","Medio","Bajo","Alto"]
data={"Lista 1":lx,
	  "Lista 2":ly,
	  "Lista 3":lz}
df=pd.DataFrame(data)
st.write(df)

data2=pd.read_excel("data.xls",sheet_name="Hoja1")
st.write(data2)

grafico1=alt.Chart(df).mark_point().encode(
	x="Lista 1",
	y="Lista 2",
	color="Lista 3",
	tooltip=["Lista 1","Lista 2","Lista 3"]).interactive()
st.altair_chart(grafico1)

barra=st.slider("Seleccione el Valor",0,3000,1500,step=100)
l1=list(range(-barra,0))
l1=reversed(l1)
l2=[0]*barra
l3=[0]*barra

data2={"Lista 1":l1,
	  "Lista 2":l2,
	  "Lista 3":l3}

df2=pd.DataFrame(data2)
st.write(df2)

columnas=df2.columns
columnsbox=st.selectbox("Seleccione la Columna",columnas)

fig = px.line_3d(df2, x="Lista 3", y=columnsbox, z="Lista 1")
st.write(fig)

radio=st.radio("Seleccione la Potencia",("Cuadrado","Cúbico","Cuarta"))

radio2=st.radio("Seleccione el Valor",(1,2,3))

if radio=="Cuadrado":
	resultado=radio2**2
	st.write("Resultado es:",resultado)

if radio=="Cúbico":
	resultado=radio2**3
	st.write("Resultado es:",resultado)

if radio=="Cuarta":
	resultado=radio2**4
	st.write("Resultado es:",resultado)

selectbox=st.sidebar.selectbox("Seleccione la Potencia",("Cuadrado","Cúbico","Cuarta"))

checkbox=st.checkbox("Seleccione la Potencia",value=False)

numero=st.number_input("Ingrese un Valor")

texto=st.text_input("Ingrese su Nombre")

st.write(texto)

