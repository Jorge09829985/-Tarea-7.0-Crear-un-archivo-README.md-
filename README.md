#  CI/CD Pipeline - Ejemplo Práctico Completo

##  Tabla de Contenidos
- [Introducción](#introducción)
- [¿Qué es CI/CD?](#qué-es-cicd)
- [Ciclo de CI/CD Explicado](#ciclo-de-cicd-explicado)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Configuración Paso a Paso](#configuración-paso-a-paso)
- [Ejecución del Pipeline](#ejecución-del-pipeline)
- [Resultados y Artefactos](#resultados-y-artefactos)

---

##  Introducción

Este repositorio demuestra un **pipeline completo de CI/CD** (Integración Continua y Despliegue Continuo) utilizando **GitHub Actions**. El proyecto incluye:

-  Pruebas unitarias automatizadas
-  Construcción de un paquete Python
-  Integración continua en cada commit
-  Generación de artefactos descargables

---

##  ¿Qué es CI/CD?

**CI/CD** es una práctica de desarrollo que automatiza la integración y entrega de código:

### **CI (Continuous Integration - Integración Continua)**
Proceso automatizado que:
1. Integra cambios de código frecuentemente
2. Ejecuta pruebas automáticas
3. Detecta errores tempranamente
4. Verifica la calidad del código

### **CD (Continuous Delivery/Deployment - Entrega/Despliegue Continuo)**
Extensión de CI que:
1. Empaqueta la aplicación
2. Prepara para producción
3. Despliega automáticamente (opcional)

---

##  Ciclo de CI/CD Explicado

```
┌─────────────────────────────────────────────────────────────────┐
│                     CICLO CI/CD COMPLETO                        │
└─────────────────────────────────────────────────────────────────┘

1. DESARROLLO
   │
   ├─► Programador escribe código
   ├─► Agrega pruebas unitarias
   └─► Hace commit al repositorio
          │
          ▼
2. TRIGGER (Disparador)
   │
   ├─► Push a rama main/develop
   ├─► Pull Request abierto
   └─► Tag de versión creado
          │
          ▼
3. BUILD (Construcción)
   │
   ├─► Clona el repositorio
   ├─► Instala dependencias
   └─► Configura entorno
          │
          ▼
4. TEST (Pruebas)
   │
   ├─► Ejecuta pruebas unitarias
   ├─► Genera reportes de cobertura
   └─► Valida calidad de código
          │
          ▼
5. PACKAGE (Empaquetado)
   │
   ├─► Construye el artefacto
   ├─► Genera distribuciones (.whl, .tar.gz)
   └─► Almacena artefactos
          │
          ▼
6. DEPLOY (Despliegue) [Opcional]
   │
   ├─► Publica en PyPI/NPM
   ├─► Despliega en servidores
   └─► Actualiza producción
          │
          ▼
7. MONITOR (Monitoreo)
   │
   ├─► Notificaciones de éxito/fallo
   ├─► Logs del pipeline
   └─► Métricas de rendimiento
```

---

##  Arquitectura del Proyecto

```
cicd-pipeline-example/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Configuración del pipeline
│
├── src/
│   └── calculator/
│       ├── __init__.py        # Inicialización del paquete
│       └── operations.py      # Código fuente principal
│
├── tests/
│   ├── __init__.py
│   └── test_operations.py     # Pruebas unitarias
│
├── setup.py                   # Configuración del paquete
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Esta documentación
└── .gitignore                 # Archivos ignorados por Git
```

---

##  Configuración Paso a Paso

### **Paso 1: Estructura del Proyecto**

#### `src/calculator/__init__.py`
```python
"""
Calculator Package
Un paquete simple para operaciones matemáticas básicas.
"""

__version__ = "1.0.0"
__author__ = "Tu Nombre"

from .operations import Calculator

__all__ = ['Calculator']
```

#### `src/calculator/operations.py`
```python
"""
Módulo de operaciones matemáticas básicas.
"""

class Calculator:
    """Calculadora con operaciones básicas."""
    
    def add(self, a, b):
        """Suma dos números."""
        return a + b
    
    def subtract(self, a, b):
        """Resta dos números."""
        return a - b
    
    def multiply(self, a, b):
        """Multiplica dos números."""
        return a * b
    
    def divide(self, a, b):
        """Divide dos números."""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def power(self, base, exponent):
        """Calcula la potencia de un número."""
        return base ** exponent
```

---

### **Paso 2: Pruebas Unitarias**

#### `tests/test_operations.py`
```python
"""
Pruebas unitarias para el módulo Calculator.
"""

import unittest
import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator.operations import Calculator


class TestCalculator(unittest.TestCase):
    """Suite de pruebas para la clase Calculator."""
    
    def setUp(self):
        """Configuración antes de cada prueba."""
        self.calc = Calculator()
    
    def test_add(self):
        """Prueba la suma de números."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Prueba la resta de números."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        """Prueba la multiplicación de números."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Prueba la división de números."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
    
    def test_divide_by_zero(self):
        """Prueba que la división por cero lanza excepción."""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Prueba la potenciación."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)


if __name__ == '__main__':
    unittest.main()
```

---

### **Paso 3: Configuración del Paquete**

#### `setup.py`
```python
"""
Configuración para construir el paquete Calculator.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="calculator-cicd",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu.email@example.com",
    description="Una calculadora simple para demostrar CI/CD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/cicd-pipeline-example",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[],
)
```

#### `requirements.txt`
```
setuptools>=65.0.0
wheel>=0.37.0
```

---

### **Paso 4: Workflow de CI/CD**

#### `.github/workflows/ci-cd.yml`
```yaml
name: CI/CD Pipeline

# Trigger: Cuándo se ejecuta el pipeline
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:  # Permite ejecución manual

# Variables de entorno
env:
  PYTHON_VERSION: '3.10'

jobs:
  # ═══════════════════════════════════════════════════════════
  # JOB 1: PRUEBAS (Testing)
  # ═══════════════════════════════════════════════════════════
  test:
    name:  Ejecutar Pruebas
    runs-on: ubuntu-latest
    
    steps:
      # 1. Checkout del código
      - name:  Checkout código
        uses: actions/checkout@v3
      
      # 2. Configurar Python
      - name:  Configurar Python ${{ env.PYTHON_VERSION }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      # 3. Instalar dependencias
      - name:  Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      # 4. Ejecutar pruebas
      - name:  Ejecutar pruebas unitarias
        run: |
          python -m unittest discover -s tests -p "test_*.py" -v
      
      # 5. Mostrar información del sistema
      - name: ℹ Información del sistema
        run: |
          echo "Sistema Operativo: $(uname -a)"
          echo "Versión Python: $(python --version)"
          echo "Directorio actual: $(pwd)"
          echo "Contenido:"
          ls -la

  # ═══════════════════════════════════════════════════════════
  # JOB 2: CONSTRUCCIÓN DEL PACKAGE (Build)
  # ═══════════════════════════════════════════════════════════
  build:
    name:  Construir Package
    needs: test  # Solo se ejecuta si las pruebas pasan
    runs-on: ubuntu-latest
    
    steps:
      # 1. Checkout del código
      - name:  Checkout código
        uses: actions/checkout@v3
      
      # 2. Configurar Python
      - name:  Configurar Python ${{ env.PYTHON_VERSION }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      # 3. Instalar herramientas de construcción
      - name:  Instalar herramientas de build
        run: |
          python -m pip install --upgrade pip
          pip install build twine
          pip install -r requirements.txt
      
      # 4. Construir el paquete
      - name:  Construir distribuciones
        run: |
          python -m build
          echo " Paquete construido exitosamente"
          ls -lh dist/
      
      # 5. Verificar el paquete
      - name:  Verificar paquete con twine
        run: |
          twine check dist/*
      
      # 6. Subir artefactos
      - name:  Subir artefactos
        uses: actions/upload-artifact@v3
        with:
          name: python-package-distributions
          path: dist/
          retention-days: 7
      
      # 7. Resumen del build
      - name:  Resumen del build
        run: |
          echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
          echo " BUILD COMPLETADO EXITOSAMENTE"
          echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
          echo " Artefactos generados:"
          ls -lh dist/
          echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
          echo " Detalles de los archivos:"
          file dist/*
          echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  # ═══════════════════════════════════════════════════════════
  # JOB 3: REPORTE FINAL (Summary)
  # ═══════════════════════════════════════════════════════════
  report:
    name:  Generar Reporte
    needs: [test, build]
    runs-on: ubuntu-latest
    if: always()
    
    steps:
      - name:  Reporte del Pipeline
        run: |
          echo "╔════════════════════════════════════════╗"
          echo "║     REPORTE DEL PIPELINE CI/CD         ║"
          echo "╚════════════════════════════════════════╝"
          echo ""
          echo " Tests: ${{ needs.test.result }}"
          echo " Build: ${{ needs.build.result }}"
          echo ""
          echo " Fecha: $(date)"
          echo " Repositorio: ${{ github.repository }}"
          echo " Branch: ${{ github.ref_name }}"
          echo " Autor: ${{ github.actor }}"
          echo ""
          if [ "${{ needs.test.result }}" == "success" ] && [ "${{ needs.build.result }}" == "success" ]; then
            echo " Pipeline ejecutado exitosamente"
            exit 0
          else
            echo " Pipeline falló"
            exit 1
          fi
```

---

##  Ejecución del Pipeline

### **Cómo Activar el Pipeline**

1. **Push a la rama principal:**
```bash
git add .
git commit -m "feat: agregar calculadora con CI/CD"
git push origin main
```

2. **Crear Pull Request:**
   - Ir a GitHub → Pull Requests → New Pull Request
   - El pipeline se ejecutará automáticamente

3. **Ejecución Manual:**
   - Ir a GitHub → Actions → CI/CD Pipeline
   - Click en "Run workflow"

### **Monitoreo en GitHub Actions**

1. Ve a tu repositorio en GitHub
2. Click en la pestaña **Actions**
3. Selecciona el workflow **CI/CD Pipeline**
4. Observa el progreso en tiempo real

---

##  Resultados y Artefactos

### **Salida de Pruebas Exitosas**
```
test_add (test_operations.TestCalculator) ... ok
test_divide (test_operations.TestCalculator) ... ok
test_divide_by_zero (test_operations.TestCalculator) ... ok
test_multiply (test_operations.TestCalculator) ... ok
test_power (test_operations.TestCalculator) ... ok
test_subtract (test_operations.TestCalculator) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### **Artefactos Generados**

Después de un build exitoso, se generan:

```
dist/
├── calculator_cicd-1.0.0-py3-none-any.whl  # Wheel distribution
└── calculator_cicd-1.0.0.tar.gz             # Source distribution
```

**Para descargar los artefactos:**
1. Ve a Actions → Workflow ejecutado
2. Scroll hasta "Artifacts"
3. Descarga `python-package-distributions`

### **Instalación del Paquete**

```bash
# Desde el archivo wheel
pip install dist/calculator_cicd-1.0.0-py3-none-any.whl

# Uso del paquete
python
>>> from calculator import Calculator
>>> calc = Calculator()
>>> calc.add(5, 3)
8
>>> calc.multiply(4, 7)
28
```

---

##  Explicación de Cada Etapa

### **1. Checkout**
```yaml
- uses: actions/checkout@v3
```
Descarga el código del repositorio al runner de GitHub Actions.

### **2. Setup Python**
```yaml
- uses: actions/setup-python@v4
  with:
    python-version: '3.10'
```
Configura el entorno Python con la versión especificada.

### **3. Install Dependencies**
```yaml
- run: pip install -r requirements.txt
```
Instala todas las librerías necesarias para el proyecto.

### **4. Run Tests**
```yaml
- run: python -m unittest discover -s tests
```
Ejecuta todas las pruebas unitarias en el directorio `tests/`.

### **5. Build Package**
```yaml
- run: python -m build
```
Construye el paquete generando archivos `.whl` y `.tar.gz`.

### **6. Upload Artifacts**
```yaml
- uses: actions/upload-artifact@v3
```
Almacena los artefactos generados para descarga posterior.

---

##  Beneficios del CI/CD

| Beneficio | Descripción |
|-----------|-------------|
|  **Rapidez** | Integración y despliegue automáticos |
|  **Detección temprana** | Errores encontrados inmediatamente |
|  **Calidad** | Todas las pruebas deben pasar |
|  **Consistencia** | Mismo proceso en cada build |
|  **Colaboración** | Múltiples desarrolladores trabajando |
|  **Trazabilidad** | Historial completo de cambios |

---

##  Conceptos Clave

### **Runner**
Máquina virtual que ejecuta los workflows (ej: `ubuntu-latest`).

### **Job**
Conjunto de pasos que se ejecutan en el mismo runner.

### **Step**
Tarea individual dentro de un job (ejecutar comando, usar action).

### **Artifact**
Archivos generados durante el workflow que se pueden descargar.

### **Trigger**
Evento que inicia el workflow (`push`, `pull_request`, etc.).

---

##  Comandos Útiles

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/cicd-pipeline-example.git
cd cicd-pipeline-example

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pruebas localmente
python -m unittest discover -s tests -v

# Construir el paquete localmente
python -m build

# Instalar el paquete localmente
pip install dist/calculator_cicd-1.0.0-py3-none-any.whl
```

---

##  Recursos Adicionales

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Packaging Guide](https://packaging.python.org/)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Setuptools Documentation](https://setuptools.pypa.io/)

---

##  Autor

** Jorge Escobar**
- GitHub: [@Jorge09829985](https://github.com/Jorge09829985/-Tarea-7.0-Crear-un-archivo-README.md-.git)
- Email: jdv.escobar@yavirac.edu.ec

---


##  Conclusión

Este proyecto demuestra un pipeline CI/CD completo y funcional que:

- Ejecuta pruebas automáticas en cada commit  
- Construye paquetes Python distribuibles  
- Genera artefactos descargables  
- Proporciona feedback inmediato  
- Mantiene la calidad del código