def elimina_duplicats(llista):
    """Retorna una nova llista sense elements duplicats."""
    return list(set(llista))

# Proves de la funció
print(elimina_duplicats([1, 2, 3, 2, 4, 5, 1]))  # Retorna [1, 2, 3, 4, 5]
print(elimina_duplicats(['a', 'b', 'c', 'a']))  # Retorna ['a', 'b', 'c']
print(elimina_duplicats([10, 20, 30, 10, 20]))  # Retorna [10, 20, 30]
print(elimina_duplicats([]))  # Retorna []