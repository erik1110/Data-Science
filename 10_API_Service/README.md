## 網路概念

### 超文本傳輸協定(HyperText Transfer Protocol，縮寫：HTTP)
是一種在網頁伺服器及網頁瀏覽器，負責處理網頁資料的通訊協定，一般來說傳輸資料的兩端會分為 客戶端(Client) 跟 伺服器端(Server)

- Client： 以網頁來說就是你的瀏覽器、電腦，主要會發送 「 請求 request 」到 Server 端
- Server： 收到 request 開始處理資料，完成後會回傳 「回應 response 」到 Client 端

我們是怎麼看到網頁的畫面？
[參考資訊](https://yakimhsu.com/project/project_w4_Network_http.html)

- 1. 一開始先發送 request 到副檔名為 .html 的 url
- 2. DNS 解析成 IP 位置
     當瀏覽器發送 request 的時候，其實是發送一個網址，但要怎麼知道網址的 IP 位置呢？就是靠 DNS 啦
     ![](https://i.imgur.com/ReQY4ju.png)
- 3. Server 接收到 request、 回傳 response
- 4. 瀏覽器解析 html 檔案
- 5. 根據 html 內容，一但發現有 CSS、JS、圖片檔案，再發送各檔案的 request(如同步驟 1.2.3)
- 6. 發送完包含在 html 所有資源的 request
- 7. 開始下載資源(CSS、JS、圖片檔)
- 8. 進行渲染網頁

### 狀態碼
| 分類 | 代碼 | 白話文 |
| --------  | -------- |-------- |
| 資訊回應    | 100–199  | 再等等 |
| 成功回應    | 200–299  | 成功啦 |
| 重定向      | 300–399  | 去其他地方 |
| 用戶端錯誤   | 400–499  | 你挫賽了(客戶端)|
| 伺服器端錯誤 | 500–599  | 我挫賽了(伺服器端)|

### 請求方法

發送的 Request 根據不同的用途，有查詢、新增、修改或者是刪除，稱為「 Request Method 」，是為了讓 Server 能夠清楚辨別 request 的目的

| 名稱 | 功能 | 案例 
| -------- | -------- | -------- |
| GET      | 單純的跟 server 要一個連結或圖片，通常網頁都是 Get 的 request 比較多  | 例如要去某個網址、看某張圖片 |
| HEAD     | 只要獲取 request 的 header，不要 body     |
| POST     | 需要執行一些動作時，會傳送 Post 的 request    | 例如登入會員
| PUT      | 取代掉整個 request     |
| DELETE   | 刪除資源    |
| CONNECT  | 指定資源標明的伺服器之間，建立隧道（tunnel）     |
| OPTION   | 描述指定資源的溝通方法（communication optiont)     |
| TRACE    | 指定資源標明的伺服器之間，執行迴路返回測試（loop-back test）     |
| PATCH    | 修改部分 request     |
  
## FastAPI

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
