# TA_EEE4178_Project_2021


## Final Project (~12/14)


1. [프로젝트 개요](https://drive.google.com/file/d/1EJj2ONjp0MemNHjRUQhCcxQtJqRknm1a/view?usp=sharing)
2. 데이터셋 [[train](https://drive.google.com/file/d/12RLV2Vgg9WBhU9ceIaNtYm77w4NQGB7M/view?usp=sharing)] / [[valid](https://drive.google.com/file/d/19m2D4ehI6gZ1JMgM4SedNIHmSwWwFDMp/view?usp=sharing)] / test 는 평가 시 공개
3. 데이터 다운로드, 마운트 등 참고 코드 [[Project_utils.ipynb](https://github.com/seunghyeon528/TA_EEE4178_Project_2021/blob/main/Project_utils.ipynb)]
4. 데이터 로드를 위한 custom dataset 참고 코드 [[dataset.py](https://github.com/seunghyeon528/TA_EEE4178_Project_2021/blob/main/dataset.py)]






## 기타 참고 사항


**1. GPU 종류**
```python
!nvidia-smi
```

![image](https://user-images.githubusercontent.com/77431192/144526328-cf7c7a2b-7814-49fe-b4c9-dfd14d553416.png)




**2. Train 소요 시간**


  학습 들어가기 직전 (for epoch in range(num_epochs) 반복문 들어가기 전) 
```python
import time
start = time.time() # Train 시작 시간 정보 저장
```

  학습 끝난 직후 (for epoch in ~ 반복문 끝난 직후)
```python
end = time.time() # Train 종료 시간 정보 저장

duration = end - start # 종료 시간 - 시작 시간
print("Training takes {:.2f}minutes".format(duration/60)) #초 단위로 저장되므로, 60으로 나누어 분으로 표시
```




**3. Test.py**
  
  train.py 를 통해 학습한 model을 model.pth 형태로 저장 및 다운로드하여 test.py 파일이 있는 곳에 업로드하고, 이를 torch.load 로 불러와서 동작하도록 작성
  (Validation set 에 대해서 test 하도록 작성, 제출 후 조교가 Test set 으로 변경하여 성능 측정할 예정)
  
예시 코드       [[test.py](https://github.com/seunghyeon528/TA_EEE4178_Project_2021/blob/main/test.py)]




---
## 추가 공지


  학습 도중 valid dataloader 를 이용해서 valid 성능을 측정할 때, 기존의 실습 때 사용하였던 아래와 같은 방식은 batch size 가 valid dataset 길이 (7800) 의 약수일 때만 정확합니다.
 ```python
     print('Accuracy of the last_model network on the {} valid images: {} %'.\
           format(len(valid_loader)*batch_size, 100 * correct / (len(valid_loader)*batch_size)))
 ```
  Torch dataloader 는 기본적으로 마지막에 남는 데이터를 그대로 전달 (예를 들어 batch size 를 1000 으로 하면 마지막에 800개만 남음.) 하기 때문에, 위와 같은 방식으로 하면 valid accuracy 가 더 낮게 나옵니다.
  
  이 경우에 아래 방식으로 print 를 하면 정확힌 valid accuracy 값을 확인하실 수 있습니다. 
   ```python
    print('Accuracy of the last_model network on the {} valid images: {} %'.\
          format(len(valid_data), 100 * correct / len(valid_data)))
 ```       
