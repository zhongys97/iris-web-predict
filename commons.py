
import torch 
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

class Net(nn.Module):
    # define nn
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(4, 100)
        self.fc2 = nn.Linear(100, 100)
        self.fc3 = nn.Linear(100, 3)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, X):
        X = F.relu(self.fc1(X))
        X = self.fc2(X)
        X = self.fc3(X)
        X = self.softmax(X)
  
        return X
    

def get_model():
	checkpoint_path='iris_model.pth'
	model=Net()
	model.load_state_dict(torch.load(checkpoint_path,map_location='cpu'),strict=False)
	model.eval()
	return model

def get_tensor(input_arr):
	ret = Variable(torch.from_numpy(input_arr).float()).unsqueeze(0)
	return ret