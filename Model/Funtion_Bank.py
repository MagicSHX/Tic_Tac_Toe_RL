import pandas as pd
import torch
def data_input(file_path):
    #to explore: remove duplicatioin - if both input and score are same, then remove duplication
    data_original = pd.read_csv(file_path)
    #data_original = data_original.drop_duplicates(subset=None, keep='first', inplace=False)
    torch_tensor = torch.tensor(data_original.values, dtype=torch.float)
    #print(torch_tensor)
    return torch_tensor