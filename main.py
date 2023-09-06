import numpy as np
import pygame
import time



def update(matrix):
    n, m = np.shape(matrix)

    for i in range(n):
        for j in range(m):
            neighbour_count = 0
            neighbour_count += matrix[(i - 1) % n][(j - 1) % m]
            neighbour_count += matrix[(i - 1) % n][j]
            neighbour_count += matrix[(i - 1) % n][(j + 1) % m]
            neighbour_count += matrix[i][(j - 1) % m]
            neighbour_count += matrix[i][(j + 1) % m]
            neighbour_count += matrix[(i + 1) % n][(j - 1) % m]
            neighbour_count += matrix[(i + 1) % n][j]
            neighbour_count += matrix[(i + 1) % n][(j + 1) % m]

            # we now have the number of neighbours

            if neighbour_count < 2:
                matrix[i][j] = 0

            elif 2 <= neighbour_count <= 3:
                matrix[i][j] = 1

            else:
                matrix[i][j] = 0

    return matrix








def main(n, m):


    def draw(matrix):

        SIZE = 10

        for i in range(n):
            for j in range(m):
                x1 = i * SIZE
                y1 = j * SIZE
                x2 = x1 + SIZE
                y2 = y1 + SIZE

                if matrix[i][j] == 1:
                    canvas.create_rectangle((x1, y1, x2, y2), fill="White")
                else:
                    canvas.create_rectangle((x1, y1, x2, y2), fill="Black")

        canvas.update()

    matrix = np.ones((n, m), int)

    while True:
        time.sleep(0.1)

        matrix = update(matrix)
        draw(matrix)
        print(matrix)

    root.mainloop()


main(100, 100)
