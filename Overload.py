from abc import ABC, abstractmethod

# Abstraction and Encapsulation
class AbstractVector(ABC):
    def __init__(self, *components):
        self._components = list(components)  # Encapsulation

    @abstractmethod
    def __add__(self, other):
        pass

    def __str__(self):
        return f"Vector({', '.join(str(x) for x in self._components)})"

    @classmethod
    def from_string(cls, s):  # Class Method: alternative constructor
        components = [float(x) for x in s.split(",")]
        return cls(*components)

    @staticmethod
    def dimension_info():  # Static Method
        return "Dimension is determined by the number of components."


# Inheritance and Polymorphism
class Vector(AbstractVector):
    def __init__(self, *components):
        super().__init__(*components)

    def __add__(self, other):  # Operator Overloading (Polymorphism)
        if isinstance(other, Vector) and len(self._components) == len(other._components):
            result_components = [a + b for a, b in zip(self._components, other._components)]
            return Vector(*result_components)
        else:
            raise ValueError("Vectors must be of the same dimension.")

    def get_components(self):  # Instance Method
        return self._components


def main():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = v1 + v2

    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v3)
    print("Created using from_string:", Vector.from_string("7,8,9"))
    print("Dimension info:", Vector.dimension_info())


if __name__ == "__main__":
    main()
