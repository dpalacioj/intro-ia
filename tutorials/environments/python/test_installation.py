import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.linear_model import LinearRegression

def check_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} is installed.")
    except ImportError:
        print(f"{package_name} is NOT installed.")




def generate_random_data():




    np.random.seed(42)
    x = np.random.rand(50)
    y = 2 * x + 1 + 0.2 * np.random.randn(50)
    return x, y

def create_dataframe(x, y):
    data = pd.DataFrame({'X': x, 'Y': y})
    return data

def fit_linear_regression(data):
    x = data['X'].values.reshape(-1, 1)
    y = data['Y'].values
    model = LinearRegression()
    model.fit(x, y)
    return model

def plot_regression_line(data, model):
    plt.scatter(data['X'], data['Y'])
    plt.plot(data['X'], model.predict(data['X'].values.reshape(-1, 1)), color='red')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scatter Plot with Regression Line")
    plt.savefig("scatter_plot_regression.png")
    plt.close()

if __name__ == "__main__":
    packages_to_check = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn"]

    for package in packages_to_check:
        check_package(package)

    # Generate random data
    x, y = generate_random_data()

    # Create a DataFrame using pandas
    data = create_dataframe(x, y)

    # Fit a simple linear regression model using scikit-learn
    model = fit_linear_regression(data)

    # Create a scatter plot with the regression line using matplotlib
    plot_regression_line(data, model)
    

    # Create a scatter plot using seaborn
    sns.set(style="darkgrid", palette="muted")
    sns.scatterplot(x='X', y='Y', data=data)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scatter Plot using Seaborn")
    plt.savefig("scatter_plot_seaborn.png")
    plt.close()

    print("Plots saved successfully.")