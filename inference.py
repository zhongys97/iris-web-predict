import torch
import numpy as np
from commons import *
import json


with open('idx_to_name.json') as f:
    idx_to_name=json.load(f)


def get_species(input_dict):
    arr = np.array([float(input_dict["sepal_length"]), float(input_dict["sepal_width"]), float(input_dict["petal_length"]), float(input_dict["petal_width"])])
    tensor=get_tensor(arr)
    model = get_model()
    outputs=model(tensor)
    _,prediction=torch.max(outputs, 1)
    category=prediction.item()
    name = idx_to_name[str(category)]
    #print(name)

    return name

if __name__ == "__main__":
    get_species({'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2'})