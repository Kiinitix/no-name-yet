import numpy as np
import pandas as pd

def validate_user_input(user_input, expected_length):
    """
    Validates user input by checking if the length of the input matches the expected length
    and if all inputs can be converted to floats.

    Parameters:
        user_input (list): The list of user input values.
        expected_length (int): The expected number of features.

    Returns:
        bool: True if valid, False otherwise.
    """
    if len(user_input) != expected_length:
        print(f"Invalid input. Expected {expected_length} feature values.")
        return False

    # Check if all inputs can be converted to float
    for value in user_input:
        try:
            float(value)  # Attempt conversion to float
        except ValueError:
            print("Invalid input. Please ensure all feature values are numbers.")
            return False

    return True


def convert_input_to_float(user_input):
    """
    Converts user input strings to float values.

    Parameters:
        user_input (list): The list of user input values as strings.

    Returns:
        list: A list of converted float values.
    """
    try:
        return list(map(float, user_input))
    except ValueError:
        print("Invalid input. Please ensure all feature values are numbers.")
        return None

def log_message(message):
    """
    Logs a message to the console with a timestamp.
    
    Parameters:
        message (str): The message to log.
    """
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def display_dataframe_summary(dataframe):
    """
    Displays a summary of the given DataFrame, including basic statistics.

    Parameters:
        dataframe (pd.DataFrame): The DataFrame to summarize.
    """
    print("\nDataFrame Summary:")
    print(dataframe.describe(), "\n")

def check_model_trained(model):
    """
    Checks if the model is trained and returns a boolean.

    Parameters:
        model: The machine learning model to check.

    Returns:
        bool: True if the model is trained, False otherwise.
    """
    return model is not None and model.trained
