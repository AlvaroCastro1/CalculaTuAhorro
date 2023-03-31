# Trabajo bajo un Entotno virtual

## intalacion modulo para entotno virtual
pip install virtualenv
## Crear y activar el entotno virtual
```
python -m venv proyecto_CalculaTuAhorro
```

## activar y trabajar con el entorno virtual
1. posicionarse en la carpeta ''' proyecto_CalculaTuAhorro '''
2. ejecutar EN CMD
```
Scripts\activate
```
3. instalar las dependencias/modulos
```
pip install -r requirements.txt
```

# despues de haber instalado mas dependencias hará falta colocarlas (desde la carpeta raiz)
```
pip freeze > requirements.txt
```