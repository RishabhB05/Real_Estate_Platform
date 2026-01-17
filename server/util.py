import json
import pickle
import os
import numpy as np


__location = None
__data_columns = None
__model = None



def get_estimated_price(location, sqft, bath, bhk):
    # this function estimates the price based on location, sqft, bath, bhk
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath 
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0], 2)














def get_location():
    # this function reads the locaion from columns.csv file and returns the location
    global __location
    if __location is None:
        load_save_artifacts()
    return __location


def load_save_artifacts():
    # this function loads the saved artifacts needed for the application
    print("Loading saved artifacts...")
    # .we gonna store the artifact in global variables

    global __data_columns
    global __location
    global __model

    base_dir = os.path.dirname(__file__)
    columns_path = os.path.join(base_dir, "artifacts", "columns.json")
    model_path = os.path.join(base_dir, "artifacts", "bangalore_home_prices_model.pickle")

    with open(columns_path, "r") as f:
        # here we are loading the data columns from the json file
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]  # assuming first 3 columns are not location

    try:
        with open(model_path, "rb") as f:
            # here we are loading the model from the pickle file
            __model = pickle.load(f)
    except FileNotFoundError:
        # model file missing is ok for just location lookups
        __model = None
    print("Artifacts loaded successfully.")







if __name__ == '__main__':
    load_save_artifacts()
    print(get_location()) 
    get_estimated_price('1st Phase JP Nagar', 1000, 2, 2)