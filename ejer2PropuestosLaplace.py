import numpy.linalg as l
import numpy as np
import matplotlib.pyplot as plt


def solve_laplace_equation(left_boundary, right_boundary, top_boundary, bottom_boundary, num_rows, num_columns, max_iterations, error):
    # Crear una matriz para almacenar los valores de la solución
    solution = np.array([[0 for i in range(num_columns+2)] for j in range(num_rows+2)])


    # Establecer los valores en los bordes
    for i in range(num_rows+2):
        solution[i][0] = top_boundary
        solution[i][num_columns+1] = bottom_boundary


    for j in range(num_columns+2):
        solution[0][j] = left_boundary
        solution[num_rows+1][j] = right_boundary


    # Establecer el valor promedio en el interior de la región
    average_boundary_value = (left_boundary + right_boundary + top_boundary + bottom_boundary) / 4


    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            solution[i][j] = average_boundary_value


    iteration = 0
    converged = False


    while iteration < max_iterations and not converged:
        iteration += 1


        # Hacer una copia de la solución anterior para calcular la convergencia
        previous_solution = solution.copy()


        # Calcular los nuevos valores en el interior de la región
        for i in range(1, num_rows+1):
            for j in range(1, num_columns+1):
                solution[i][j] = 0.25 * (solution[i+1][j] + solution[i-1][j] + solution[i][j+1] + solution[i][j-1])


        # Calcular la diferencia entre la solución anterior y la actual
        difference = np.subtract(solution, previous_solution)


        # Calcular la norma infinito de la diferencia dividida por la norma infinito de la solución actual
        relative_difference = l.norm(difference, np.inf) / l.norm(solution, np.inf)


        # Verificar si la solución ha convergido por debajo del umbral de convergencia
        if relative_difference < error:
            converged = True


    if converged:
        # Crear las coordenadas x e y para la visualización en 3D
        x = np.array([i+1 for i in range(num_columns+2)])
        y = np.array([i+1 for i in range(num_rows+2)])
        xx, yy = np.meshgrid(x, y)


        print("Solución: \n", solution, "\n x: \n", xx, "\n y: \n", yy)


        # Graficar la solución en 3D
        fig = plt.figure(figsize=(14, 9))
        ax = plt.axes(projection='3d')


        hm = ax.plot_surface(xx, yy, solution, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        fig.colorbar(hm, ax=ax, shrink=0.5, aspect=5)


        ax.set_title('Ecuación de Laplace')


    else:
        print("No se pudo alcanzar la convergencia")

# En este caso unicamente el cambio se daria en el inreso de las restricciones
solve_laplace_equation(120, 0, 120, 0, 10, 10, 100, 1)
plt.show()