import numpy as np

def generate_random_data(num_points, num_dimensions, value_range):
    return np.random.uniform(value_range[0], value_range[1], size=(num_points, num_dimensions))

def save_to_txt(data, filename):
    with open(filename, 'w') as f:
        for i, point in enumerate(data, 0):
            formatted_point = ' '.join(str(x) for x in point)
            f.write(f"{i}: [{formatted_point}]\n")

if __name__ == "__main__":
    num_points = 10000
    num_dimensions = 50
    value_range = (-10, 10)

    data = generate_random_data(num_points, num_dimensions, value_range)
    save_to_txt(data, "database.txt")