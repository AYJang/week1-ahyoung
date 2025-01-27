# 1장 – 한눈에 보는 머신러닝

## 목차
1. [1. 데이터 준비](#1-데이터-준비)
2. [2. 가격 예측](#2-가격-예측)
3. [3. 사용자 만족도](#3-사용자-만족도)

---

## 1. 데이터 준비

### 데이터 시각화
```python
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 로드
data = {"GDP per capita (USD)": [30000, 40000, 50000, 60000],
        "Life satisfaction": [5.5, 6.0, 6.5, 7.0]}
df = pd.DataFrame(data)

# 데이터 시각화
df.plot(kind="scatter", x="GDP per capita (USD)", y="Life satisfaction")
plt.title("GDP와 삶의 만족도 관계")
plt.xlabel("GDP per capita (USD)")
plt.ylabel("Life satisfaction")
plt.show()
```
<img width="574" alt="스크린샷 2024-11-18 오후 9 11 31" src="https://github.com/user-attachments/assets/b78c0d0d-3fbb-4f40-97cb-a1d66c3ba91a">

### 데이터 설명
- 데이터는 **1인당 GDP**(독립 변수)와 **삶의 만족도**(종속 변수)로 구성
- 예제 데이터:
  | GDP per capita (USD) | Life satisfaction |
  |-----------------------|-------------------|
  | 30000                | 5.5               |
  | 40000                | 6.0               |
  | 50000                | 6.5               |
  | 60000                | 7.0               |
---

## 2. 가격 예측
- 아파트의 크기와 위치로 가격 예측

### 코드
```python
from sklearn.linear_model import LinearRegression

# 독립 변수(X)와 종속 변수(y)
X = df[["GDP per capita (USD)"]].values
y = df[["Life satisfaction"]].values

# 선형 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X, y)

# 예측
X_new = [[37655]]  # 키프로스의 1인당 GDP
prediction = model.predict(X_new)
print(f"선형 회귀 예측 결과: {prediction[0, 0]:.2f}")
```
### 출력 예시
```
선형 회귀 예측 결과: 5.88
```


## 3. 사용자 만족도
- GDP로 국가의 삶의 만족도 예측

### k-NN 회귀 코드

```python
from sklearn.neighbors import KNeighborsRegressor

# k-최근접 이웃 회귀 모델 생성
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)

# 예측
prediction_knn = model.predict(X_new)
print(f"k-최근접 이웃 예측 결과: {prediction_knn[0, 0]:.2f}")
```
### 출력 예시
```
k-최근접 이웃 예측 결과: 6.00
```
-- 



### 1. 데이터 준비
1. 아래의 데이터를 사용하여 **GDP**와 **삶의 만족도**를 생성하세요.
2. `pandas`를 사용해 데이터를 DataFrame으로 변환하세요.
3. `matplotlib`를 사용해 데이터를 시각화하세요.


### 2. 모델 학습
1. **선형 회귀 모델**:
   - **`LinearRegression`**을 사용해 모델을 정의하고 학습시키세요.
2. **k-최근접 이웃 모델**:
   - **`KNeighborsRegressor`**를 사용해 \( k=3 \)으로 모델을 정의하고 학습시키세요.

