import numpy as np
import torch
import os
import glob

import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from torchvision import models, transforms


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


## -- hyperparameters 모델 isntance 생성에 필요한 argument 들 적어주기
num_classes = 52 
batch_size = 50
///


## -- dataset & dataloader (test -> valid 로 바꿔서 돌아가는 것 확인하고 제출)
class MyDataset(Dataset):
    def __init__(self, npy_dir):
        self.dir_path = npy_dir
        self.to_tensor = transforms.ToTensor()

        # all npy path
        self.npy_path = glob.glob(os.path.join(npy_dir, '*','*.npy')) 

    def __getitem__(self, index):
        # load data
        single_data_path = self.npy_path[index]
        data = np.load(single_data_path, allow_pickle=True)
        
        image = data[0]
        image = self.to_tensor(image)
        label = data[1]
       
        return (image, label)

    def __len__(self):
        return len(self.npy_path)

test_data = MyDataset("./Font_npy_90_test")
test_loader = torch.utils.data.DataLoader(dataset=test_data,
                                           batch_size=batch_size,
                                           shuffle=False)




## -- model class
class Mynet(nn.Module):
    def __init__(self, num_classes=num_classes):
        super(Mynet, self).__init__()
        self.layer1 = nn.Sequential(
                ///

    def forward(self, x):
                ///
        return x


            

## -- load model
model_test = Mynet().to(device)
model_test.load_state_dict(torch.load("20161517_model.pth"))



## -- measure testset accuracy 
model_test.eval()
with torch.no_grad():
    correct = 0
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)
        outputs = model_test(images)
        _,predicted = torch.max(outputs.data,1)
        correct += (predicted==labels).sum()
        
    print('Accuracy of the last_model network on the {} test images: {} %'.\
          format(len(test_loader)*batch_size, 100 * correct / (len(test_loader)*batch_size)))
