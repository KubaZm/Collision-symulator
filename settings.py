radius = 1
max_v = 10
mass = 1
n_H = 20
n_L = 20
height = n_H * radius
width = n_L * radius
max_atoms_number = int(0.25 * n_H * n_L)
k = 10
dt = 1/(k * max_v) #krok czasu
M = 50 #ilość odświeżeń
Dt = M * dt #czas eksperymentu
