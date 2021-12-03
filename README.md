# TA_EEE4178_Project_2021


## Final Project


1. 프로젝트 개요
2. 데이터셋 [[train]()] / [[valid]()] / test 는 평가 시 공개
3. 데이터 로드를 위한 참고 코드 [[Project_utils.ipynb](https://github.com/seunghyeon528/TA_EEE4178_Project_2021/blob/main/Project_utils.ipynb)]







## 보고서에 첨부하여야 하는 사항 & test.py template


1. GPU 종류
```python
!nvidia-smi
```

![image](https://user-images.githubusercontent.com/77431192/144525273-5bc55187-385c-4dff-b45a-57222b3fc1bb.png)



2. Train 소요 시간


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


3. loss log

최하단부만 캡처


4. Test.py

