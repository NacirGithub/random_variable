import random
import numpy as np
import matplotlib.pyplot as plt

class RandomNumberGenerator:
    def __init__(self, group_number):
        self.group_number = group_number
        # Set the seed value
        random.seed(group_number)
        np.random.seed(group_number)
    
    # Generate uniformly distributed integers between min and max
    def generate_uniform_int(self, min_val, max_val, n):
        return [random.randint(min_val, max_val) for _ in range(n)]
    
    # Generate uniformly distributed doubles between min and max
    def generate_uniform_double(self, min_val, max_val, n):
        return [random.uniform(min_val, max_val) for _ in range(n)]
    
    # Generate normally distributed numbers with mean m and standard deviation s
    def generate_normal(self, m, s, n):
        return np.random.normal(m, s, n)
    
    # Generate exponentially distributed numbers with mean e
    def generate_exponential(self, e, n):
        return np.random.exponential(e, n)
    
    # Generate geometrically distributed numbers
    def generate_geometric(self, p, n):
        return np.random.geometric(p, n)
    
    # Plot histogram
    def plot_histogram(self, data, title, filename=None, range_min=None, range_max=None):
        if all(isinstance(x, int) for x in data):
            min_val = min(data)
            max_val = max(data)
            # Create a range of values from 10 to 30 for Uniform (int)
            x_values = list(range(10, 31))  # Include values from 10 to 30
            unique_values, counts = np.unique(data, return_counts=True)
            plt.bar(unique_values, counts)
            plt.xticks(x_values)  # Set the x-axis ticks to include values from 10 to 30
        else:
            min_val = min(data)
            max_val = max(data)
            # Calculate a reasonable number of ticks based on the range of values
            num_ticks = min(10, int((max_val - min_val) * 10) + 1)  # Limit to a maximum of 10 ticks
            step = (max_val - min_val) / (num_ticks - 1)  # Calculate the step size
            x_values = [round(min_val + i * step, 1) for i in range(num_ticks)]  # Generate the ticks
            
            # Clip data to specified range
            data = [val for val in data if range_min is None or val >= range_min]
            data = [val for val in data if range_max is None or val <= range_max]
            
            plt.hist(data, bins='auto', alpha=0.7, rwidth=0.85, zorder=1)  # Set z-order for histogram bars
            plt.xticks(x_values)  # Set the x-axis ticks to evenly spaced values
        
        plt.grid(axis='y', alpha=0.5, zorder=0)  # Set z-order for grid lines
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title(title)
        if filename:
            plt.savefig(filename, format='png')
        plt.show()


group_number = int(input("Enter your group number: "))
rng = RandomNumberGenerator(group_number)

sample_sizes = [10, 100, 1000, 10000]
    
# Generate and plot random numbers for different distributions and sample sizes
distributions = [
    ('Uniform (int)', lambda n: rng.generate_uniform_int(10, 30, n)),
    ('Uniform (double)', lambda n: rng.generate_uniform_double(1.0, 3.0, n)),
    ('Normal', lambda n: rng.generate_normal(0, 0.75, n)),
    ('Exponential', lambda n: rng.generate_exponential(2, n)),
    ('Geometric', lambda n: rng.generate_geometric(group_number / 10.0, n)),
]

# Generate and plot random numbers for different distributions and sample sizes   
for distribution_name, distribution_func in distributions:
    print(f'Distribution: {distribution_name}')
    for n in sample_sizes:
        data = distribution_func(n)
        print(f'Sample Size: {n}')
        print(data)
        # Plot the histogram
        filename = f'{distribution_name.replace(" ", "_")}_sample_{n}.png'
        rng.plot_histogram(data, f'{distribution_name} (Sample Size: {n})', filename=filename)
