# Імпортуємо необхідні бібліотеки
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Визначаємо координати вершин тетраедра
vertices = np.array([
    [0, 0, 1],
        [np.sqrt(3)/3, 0, -1/3],
            [-np.sqrt(3)/6, 0.5, -1/3],
                [-np.sqrt(3)/6, -0.5, -1/3]
                ])

                # Визначаємо індекси граней тетраедра
                faces = np.array([
                    [0, 1, 2],
                        [0, 2, 3],
                            [0, 3, 1],
                                [1, 2, 3]
                                ])

                                # Створюємо фігуру і осі 3D
                                fig = plt.figure()
                                ax = fig.add_subplot(111, projection='3d')

                                # Встановлюємо межі осей
                                ax.set_xlim(-1, 1)
                                ax.set_ylim(-1, 1)
                                ax.set_zlim(-1, 1)

                                # Встановлюємо назву графіка
                                ax.set_title('Тетраедр в 3D')

                                # Створюємо функцію, яка буде малювати тетраедр на кожному кроці анімації
                                def draw_tetrahedron(frame):
                                    # Очищаємо попередній малюнок
                                        ax.clear()
                                            # Встановлюємо межі осей
                                                ax.set_xlim(-1, 1)
                                                    ax.set_ylim(-1, 1)
                                                        ax.set_zlim(-1, 1)
                                                            # Встановлюємо назву графіка
                                                                ax.set_title('Тетраедр в 3D')
                                                                    # Обчислюємо кут обертання в радіанах
                                                                        angle = np.radians(frame)
                                                                            # Створюємо матрицю обертання навколо осі Z
                                                                                rotation_matrix = np.array([
                                                                                        [np.cos(angle), -np.sin(angle), 0],
                                                                                                [np.sin(angle), np.cos(angle), 0],
                                                                                                        [0, 0, 1]
                                                                                                            ])
                                                                                                                # Обертаємо вершини тетраедра за допомогою матриці обертання
                                                                                                                    rotated_vertices = np.dot(vertices, rotation_matrix)
                                                                                                                        # Малюємо кожну грань тетраедра окремим кольором
                                                                                                                            colors = ['red', 'green', 'blue', 'yellow']
                                                                                                                                for i in range(4):
                                                                                                                                        # Беремо індекси вершин поточної грані
                                                                                                                                                face = faces[i]
                                                                                                                                                        # Беремо координати вершин поточної грані
                                                                                                                                                                x = rotated_vertices[face, 0]
                                                                                                                                                                        y = rotated_vertices[face, 1]
                                                                                                                                                                                z = rotated_vertices[face, 2]
                                                                                                                                                                                        # Малюємо грань за допомогою функції plot_trisurf
                                                                                                                                                                                                ax.plot_trisurf(x, y, z, color=colors[i], alpha=0.8)

                                                                                                                                                                                                # Створюємо анімацію, яка буде викликати функцію draw_tetrahedron 360 разів з інтервалом в 20 мілісекунд
                                                                                                                                                                                                ani = FuncAnimation(fig, draw_tetrahedron, frames=360, interval=20)

                                                                                                                                                                                                # Показуємо анімацію на екрані
                                                                                                                                                                                                plt.show()
                                                                                                                                                                                                