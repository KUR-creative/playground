# PLAYGROUND
샘플 코드 레포지토리

## 규칙
어떤 것 foo를 사용해보는 샘플코드를 만들고, foo 디렉토리에 저장한다. \
foo 디렉토리에는 어떻게 설치하는지(init.md) 사용하는 방법과 샘플 코드를 저장한다.

아무튼 다른 디렉토리를 침범하지만 않으면 된다.

## 유지 보수
추후 디렉토리 구조는 변경될 수 있다. 지금은 flat 구조로 

```
playground/ 
  /dvc 
  /TRAINS 
  ... 
```
  
이렇게 가지만 나중에 묶일 수도 있음. (디렉토리 내부를 건드리진 않음)

```
playground/ 
  /machine-learning
    /dvc 
    /TRAINS 
    ... 
  /functional-programming 
    /funcy
    /fp
    ...
  /or-others
    /pp
    /ap
    ...
```
