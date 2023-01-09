def presentarse(nombre):
	return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
	return funcion_entrante("David")

def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()
	librerias()

print(funcion_mayor())