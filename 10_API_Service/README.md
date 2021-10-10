## [FastAPI](https://fastapi.tiangolo.com/)

FastAPI 是近期受到矚目的網頁框架，是一款專用於建構 API 、高性能的 web 框架。

![image](https://user-images.githubusercontent.com/40282726/135760002-935c6738-29d5-46ec-9d12-d0b2141e8284.png)


與之相同建立 web 框架的還有 Flask、Django，而其他兩個框架通常是專注於開發網頁，FastAPI則更聚焦在提供 API 的服務。

### 特色

- 很快：如名字一樣，執行速度很快
- 使用 python 3.6+ 並基於 pydantic 的類型提示
- 有漂亮 Swagger UI 介面，提供 API 文檔

### Learning Material
[Link](https://www.youtube.com/watch?v=7t2alSnE2-I&t=1055s)

#### 1. Run Fastapi
- Debug mode
```
uvicorn main:app --reload
```

#### 2. Swagger UI
- docs
  ```
  http://127.0.0.1:8000/docs
  ```
- redoc
  ```
  http://127.0.0.1:8000/redoc
  ```
#### 3. Parameters
```
http://127.0.0.1:8000/blog?limit=50&published=false
```
