
import numpy as np
import pandas as pd

#CREATE SIMULATED DATA
#Hypothetical mathematical model for organism thatresponds to two nutrients.
def true_response(nutrient_a, nutrient_b): #INPUT: 2 nutrient concentrations scaled between 0 and 1
    """
    Synthetic response function.

    Nutrient concentrations are scaled between 0 and 1.
    The output is an arbitrary, normalised response,
    not a measured biological quantity.
    """
    peak_a = np.exp(-((nutrient_a - 0.65) ** 2) / 0.035) # response dependance on nutrient A is a Gaussian peak centered at 0.65 with a width of 0.035
    peak_b = np.exp(-((nutrient_b - 0.40) ** 2) / 0.060)

    interaction = 0.15 * nutrient_a * nutrient_b #interaction between 2 nutrients
    '''
    Nonlinear response surface: 
    a hypothetical landscape describing how the response changes across different combinations of nutrient A and nutrient B.
    '''
    return peak_a * peak_b + interaction



def generate_data(n_samples=100, noise_sd=0.03, seed=42):
    """Generate synthetic nutrient-response measurements."""
    rng = np.random.default_rng(seed)

    nutrient_a = rng.uniform(0, 1, n_samples)
    nutrient_b = rng.uniform(0, 1, n_samples)

    expected_response = true_response(nutrient_a, nutrient_b)
    measured_response = (
        expected_response
        + rng.normal(0, noise_sd, n_samples) #add some noise to the expected response to simulate measurement error
    )

    return pd.DataFrame({
        "nutrient_a": nutrient_a,
        "nutrient_b": nutrient_b,
        "response": measured_response,
    })


if __name__ == "__main__":
    data = generate_data()

    print(data.head())
    print()
    print(data.describe())
