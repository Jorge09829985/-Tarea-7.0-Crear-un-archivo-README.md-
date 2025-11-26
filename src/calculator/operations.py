"""
Módulo de operaciones matemáticas básicas.
"""

class Calculator:
    """Calculadora con operaciones básicas."""
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def power(self, base, exponent):
        return base ** exponent
