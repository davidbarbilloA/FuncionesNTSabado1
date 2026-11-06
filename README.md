# FuncionesNTSabado1 – Ejemplos de clase de funciones y listas

Ejercicios de clase para practicar funciones y listas, principalmente en Python. Es un fork de [profejuanjosegallego/FuncionesNTSabado1](https://github.com/profejuanjosegallego/FuncionesNTSabado1).

## Tech stack

| Capa | Tecnologías |
|------|-------------|
| **Lenguaje principal** | Python 3 (solo biblioteca estándar) |
| **Apuntes** | Fragmentos de Java y JavaScript |

## Estructura del proyecto

```text
FuncionesNTSabado1/
├── funcionUno.py   # Crea una lista de estudiantes (diccionarios) con datos por consola
├── funcionDos.py   # Define una función que crea una lista de N notas aleatorias
├── listas.py       # Métodos de listas: append, insert, remove, pop, sort, clear
├── bicicletas.py   # Enunciado de un ejercicio, solo en comentarios (sin implementar)
├── eje.java        # Apunte de lectura por consola (no compila)
├── eje.js          # Apunte de una función (incompleto)
└── README.md
```

## Contenido

| Archivo | Qué practica |
|---------|--------------|
| `funcionUno.py` | Funciones con parámetros, `input()`, diccionarios y listas de diccionarios |
| `funcionDos.py` | Funciones con retorno y números aleatorios con `random.randint` |
| `listas.py` | Manipulación de listas y datos simulados |
| `bicicletas.py` | Planteamiento: promediar notas de eficiencia, parecido y estabilidad para calcular un ganador |

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/davidbarbilloA/FuncionesNTSabado1.git
cd FuncionesNTSabado1
```

### 2. Ejecutar los ejemplos

**Requisitos:** Python 3

```bash
python funcionUno.py
```

`funcionUno.py` pide por consola los datos de 5 estudiantes.

```bash
python listas.py
```

`listas.py` aplica los métodos de lista y, al final, imprime la lista vacía porque usa `clear()`.

> `funcionDos.py` solo define la función, así que ejecutarlo no muestra nada. Para probarla, impórtala o agrega una llamada a `crear_lista_notas`.

## Autor

- [@davidbarbilloA](https://github.com/davidbarbilloA)
- Repositorio original: [@profejuanjosegallego](https://github.com/profejuanjosegallego)
