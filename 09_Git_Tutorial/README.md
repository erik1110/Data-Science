## 1. 為什麼要學 Git ?
學習到現在大家一定累積很多的程式碼或是各式的檔案，如何去做有效的控管其實是非常重要！
想像有個情境是你上線了一段程式碼，但顧客抱怨使用上有問題，你需要緊急還原到上一版，這是就可以
靠 Git 來協助你進行程式碼或檔案版控，快速還原上一版，就不用急忙打電話給同事找程式碼。
我們可以利用 Git 指令將程式碼每次的版本記錄起來，當哪一天需要回頭檢視的時候就可以直接查看。

## 2. 環境設定
### 安裝 Git
- [Windows](https://git-scm.com/download/win)
- MacOS
  ```
  brew install git
  ```
### 終端機常用指令簡介
由於 Git 指令是打在終端機，因此有必要認識一下基本的終端機指令。
以下指令在 MacOs 與 Linux 通用
| 指令 | 說明 | 範例 |
| -------- | -------- | -------- |
| cd   | 切換目錄     |   ``` cd 目錄 ```     |
| cd   | 切換上一層     |   ``` cd .. ```     |
| tab   | 系統提示該指令  |   (需搭配其他指令，例如 cd 搭配 tab 可以直接看到可以切換目錄)  ``` cd (按tab) ```    |
| ls   | 列出目錄有的檔案 |  -l 顯示完成檔案權限(可不加) -a 顯示.開頭的檔案(可不加) ``` ls -al ```     |
| mkdir   | 建立一個資料夾 |   ``` mkdir 資料夾名稱 ```     |
| cp   | 複製檔案或資料夾 | -r 代表是資料夾操作(可不加)  ``` cp -r 原檔案或資料夾路徑 新檔案或資料夾路徑```     |
| rm   | 刪除檔案或資料夾 | -r 代表是資料夾操作(可不加)  ``` rm -r 檔案或資料夾路徑```     |
| pwd   | 顯示目前路徑 | ``` pwd ```     |
| crtl+c   | 強制停止目前指令執行 |   |

### 設定 Git Config
設定帳號名稱和信件
```
$ git config --global user.name "your github id"
$ git config --global user.email "your email@gmail.com"
```
查看設定的資訊，按Ｑ可以離開 
```
git config --list
```

## 3. Git 工作流程
- `git add` 會將檔案從工作目錄推到暫存區
- `git commit` 會將檔案從暫存區推到本地端儲存庫
- `git push` 會將檔案從本地端儲存庫推到遠端儲存庫
- `git pull` 會將檔案從遠地端儲存庫同步回工作目錄
- `git fetch` 會將檔案從遠地端儲存庫同步回本地端的儲存庫
- `git merge` 合併

![image](https://user-images.githubusercontent.com/40282726/128288079-71e55e2f-514c-4e84-a511-f6e92dcc29c9.png)

## 4. 開始使用 Git
### (1) 查看狀態
使用 ``` git status ``` ，我們可以查看目前修改了什麼檔案(modified)、刪除什麼檔案(deleted)以及哪些檔案尚未被追蹤(Untracked files)

![image](https://user-images.githubusercontent.com/40282726/128316621-580140fb-6097-490c-acef-62ed338d87db.png)

新增一個 test.txt 檔案，會在 Untracked files 列出
![image](https://user-images.githubusercontent.com/40282726/128316719-dc59f0fe-d5b1-4f4e-bf45-d3b761bf53ae.png)

### (2) git add
使用 ``` git add 檔案 ``` ，我們將檔案或資料夾推到暫存區，若我們再用一次 ``` git status ``` 就會發現有提示一個新檔案(new file)

![image](https://user-images.githubusercontent.com/40282726/128317174-5aa428b3-d079-411c-8c92-2bb57e567ef5.png)
不建議使用 ``` git add * ```，這個動作雖然可以一次把所有檔案加上，但可能會加到你不要的檔案

### (3) git reset
假設剛剛的檔案反悔不想要放到暫存區， 操作``` git rest 檔案 ``` 即可

![image](https://user-images.githubusercontent.com/40282726/128317486-6715663a-531a-4948-9579-12a09cd389c3.png)

### (4) git commit
接著就可以進行提交 commit， 操作``` git commit -m "這次提交想要傳達的訊息" ```
為了讓每次的提交都知道在做什麼，會寫有意義的內容(你或你的同事要看Ｒ)，記得訊息一定要寫！！

![image](https://user-images.githubusercontent.com/40282726/128318681-8b86968a-1f00-4f96-b459-0925a4367103.png)

通常我們訊息為了要分別，有一些原則可以參考，會將下列中括號替換成下面的文字

| 原則文字 | 說明 |
| -------- | -------- |
| feature   | 新增功能     | 
| fix   | 修 bug     |
| refactor   | 重構(不是新增功能也不是修 bug )     |
| docs   | 文件   |
| style   | 格式   |
| revert   | 回上一個版本   |

### (5) git push
接著就可以將本地端程式碼推到遠端啦！操作 ``` git push ```

![image](https://user-images.githubusercontent.com/40282726/128320828-fcad674d-d7fe-4d73-9edc-da18882ce166.png)

## 5. 分支 (Branch)

## 6. 標籤 (Tag)

## 7. 遠端協作 (GitHub)

