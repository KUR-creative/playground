## 설치 방법
`pip install dvc`

## 용도
??

## 원리
**.dvc 파일로 데이터를 관리...

## 사용 방법
### 초기화
git repo에서 init dvc

## 노트

#### git add 하지 말고 dvc add를 해야 함.
```
$ dvc add data
data/               data_versioning.py
$ dvc add data/data.txt 
Adding...
ERROR:  output 'data/data.txt' is already tracked by SCM (e.g. Git).
    You can remove it from Git, then add to DVC.
        To stop tracking from Git:
            git rm -r --cached 'data/data.txt'
            git commit -m "stop tracking data/data.txt" 
```

#### 반드시 git 아래에 있어야 하나? 데이터가 외부에 있다면?
#### 

