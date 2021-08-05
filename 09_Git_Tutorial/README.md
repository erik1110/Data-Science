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
### 查看狀態(常用)
使用 ``` git status ``` ，我們可以查看目前修改了什麼檔案(modified)、刪除什麼檔案(deleted)以及哪些檔案尚未被追蹤(Untracked files)
![image](https://user-images.githubusercontent.com/40282726/128315588-0890fbd8-ce4c-4e90-a645-f56697332a7f.png)

### Commit

## 5. 分支 (Branch)

## 6. 標籤 (Tag)

## 7. 遠端協作 (GitHub)

