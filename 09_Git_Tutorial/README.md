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
| cd   | change directory 切換目錄     |   ``` cd 目錄 ```     |
| cd   | change directory 切換上一層     |   ``` cd .. ```     |
| tab   | 系統提示該指令  |   (需搭配其他指令，例如 cd 搭配 tab 可以直接看到可以切換目錄)  ``` cd (按tab) ```    |
| ls   | list 列出目錄有的檔案 |  -l 顯示完成檔案權限(可不加) -a 顯示.開頭的檔案(可不加) ``` ls -al ```     |
| mkdir   | make directory建立一個資料夾 |   ``` mkdir 資料夾名稱 ```     |
| cp   | copy 複製檔案或資料夾 | -r 代表是資料夾操作(可不加)  ``` cp -r 原檔案或資料夾路徑 新檔案或資料夾路徑```     |
| rm   | remove 刪除檔案或資料夾 | -r 代表是資料夾操作(可不加)  ``` rm -r 檔案或資料夾路徑```     |
| mv   | move 移動或重新命名 | - 將檔案由 oldfile.txt 更名為 newfile.txt，所在目錄不變： ``` mv ./oldfile.txt ./newfile.txt ```  <br>   - 將檔案 ./dir1/filename.txt 移動到 ./dir2/ 目錄下，檔案名稱不變：``` mv ./dir1/filename.txt ./dir2/```     |
| pwd   | print working directory 顯示目前路徑 | ``` pwd ```     |
| crtl+c   | 強制停止目前指令執行 |   |
| cat | concatenate 由第一行開始顯示檔案內容 | ``` cat 檔案 ``` | 
| tac | 由最後一行開始顯示檔案內容 | ``` tac 檔案 ``` | 
| more | 一頁一頁顯示檔案內容 | ``` more 檔案 ``` | 
| less | 與more相似，此指令可以往前翻頁 | ``` less 檔案 ``` | 

#### 絕對路徑與相對路徑
- 絕對路徑：/usr/lib 
- 相對路徑： 若系統目前在 /usr/lib 這個目錄，可以用 cd ../bin 切換到 /usr/bin
#### 目錄相關
- . 代表此層的目錄
- .. 代表上層的目錄
- ~ 代表自己的家目錄
#### 更詳細資訊
[鳥哥的 Linux 私房菜-第六章、Linux 檔案與目錄管理](http://linux.vbird.org/linux_basic/0220filemanager.php)
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
假設剛剛的檔案反悔不想要放到暫存區或是等一下教的commit要取消， 操作``` git reset ``` 即可

![image](https://user-images.githubusercontent.com/40282726/128317486-6715663a-531a-4948-9579-12a09cd389c3.png)

可以利用 ``` git log ``` 查詢紀錄，也可以直接某一次的版號
 ``` git reset 號碼(前6碼即可) ``` 

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

#### 更改訊息
- 改最後一次
  利用 ``` --amend ``` 來修改 git commit 的訊息
  ``` git commit --amend -m "Hello World!" ```
- 改之前
  利用 ``` git rebase commit_id號碼(6碼即可) ``` 來修改 git commit 的訊息
  - 先看 git log 知道 commit id
  ![螢幕快照 2021-08-26 下午4 01 54](https://user-images.githubusercontent.com/40282726/130924968-7ab9ba97-d494-412f-b6e4-5c9a83f2c7e5.png)
  - 輸入 git rebase
  - 進入 vim 編輯器進行修改
    會顯示從現在到這個 commit id 的所有 commit 紀錄
    將 pick 改成 reword 或是 r ，並修改後面的訊息
    ``` 
    按 i 進入編輯模式 
    按 esc 輸入 :wq! 存擋離開
    ``` 
    ![螢幕快照 2021-08-26 下午4 21 03](https://user-images.githubusercontent.com/40282726/130927838-69bc49d3-a213-4896-b2a8-ff1fee90df3b.png)
    ![螢幕快照 2021-08-26 下午4 21 57](https://user-images.githubusercontent.com/40282726/130927984-a2a220a5-5f74-4ce2-9620-1637ac654fc1.png)
  - 會再進人第二次 vim 編輯器
    再輸入一次
 
看起來只有簡單改訊息，但大家可以看 commit id 都變了，實際上是修改一個 commit 
基本上不建議大家用這招，因為把過去訊息改掉可能會造成錯亂呀！
  

### (5) git push
接著就可以將本地端程式碼推到遠端啦！操作 ``` git push ```

![image](https://user-images.githubusercontent.com/40282726/128320828-fcad674d-d7fe-4d73-9edc-da18882ce166.png)

## 5. 分支 (Branch)
### Git Flow
有人制定了規則讓大家一起遵守
https://nvie.com/posts/a-successful-git-branching-model/

用比較簡單的流程跟大家說明
![image](https://user-images.githubusercontent.com/40282726/131025287-dfe84993-a502-4cf6-892b-525353f7c067.png)

- Main: 穩定、可以上線的版本，而且這個版本只能從別的分支合併過來，基本上開發者不能直接對這個分支進行 commit
- develop: 這個分支紀錄所有開發者的基礎分支，所有的 feature 分支必須從此分支切出，而 feature 分支完成後也都會合併回來此分支
- feature: 新增功能的意思，通常我們會從 develop 分支切出來，並加上此次要新增的功能。 feature/名稱，名稱通常可以取有意義的名稱，讓專案或其他成員可以看懂你這次要幹麼。
### 查看分支
``` git branch -a``` 
![image](https://user-images.githubusercontent.com/40282726/131027001-e1297835-d323-4b6a-9e5d-ba5423e0f5f6.png)
- 星號代表你現在在哪一個分支
- 按 Q 可以離開
- remote/origin/HEAD -> origin/main 本地端追蹤分支
- remote/origin/develop -> 遠端分支 develop
- remote/origin/main -> 遠端分支 main
- origin 是遠端儲存庫的別名，可以 ``` git remote -v ``` 查看遠端儲存庫的路徑
### 新增分支
``` git branch <branch name>``` 
``` git checkout -b <branch name>``` 
### 刪除分支
``` git branch -d <branch name>``` 

### 切換分支
``` git checkout <branch name>``` 
### 合併分支
``` git merge <branch name>``` 
更詳細的說明：https://gitbook.tw/chapters/branch/merge-branch.html
### 遠端協作
- 拉遠端分支
  ``` git checkout origin/develop -b develop ``` 
- FETCH
  可以更新遠端儲存庫的資料在本地端 ``` git fetch ```
  ![image](https://user-images.githubusercontent.com/40282726/131031256-5647b42b-af4c-448d-be79-90ba45cf4a16.png)
  基本上對本地端的 main 來說 origin/main 也是一種分支，結果在 fetch 之後 main 居然落後 origin/main，這時候就可以利用合併分支``` git merge origin/master``` 
  ![image](https://user-images.githubusercontent.com/40282726/131031638-55a5d3fa-b224-4329-8086-b9776d949f7c.png)
- PULL
  - ``` git pull ```
  這個指令也是更新遠端儲存庫的資料在本地端，而這個指令的功用是 git pull = git fetch + git merge ，會自動幫你做完 merge 快轉模式（Fast Forward）的步驟
  - ``` git pull --rebase``` 加上此參數之後會自動做 rebase
    多人開發的時候，大家會在自己分支commit並在遠端協作，你拉回本地端的時候也會因為合併而產生一個額外的commit，如果你不想要這個多餘的commit可以加上此參數
### 衝突
假設你與同事或專案成員共用開發，你的同事在 develop 分支上先改了一下操作(這邊遠端用 master 示範)

![image](https://user-images.githubusercontent.com/40282726/135757304-11792557-6417-4e5e-b4b3-02c8b124b0ef.png)


但你的 local 端，沒有先更新到最新，也對同一行程式碼進行編輯修改。你一樣先 git add 、 git commit，當你發現 git push 時候悲劇了！

![image](https://user-images.githubusercontent.com/40282726/135757798-fe336952-6b31-48a1-8ea8-2c1f3450c60c.png)


怎麼會有衝突呢？ 這時候什麼東西

![image](https://user-images.githubusercontent.com/40282726/135757444-5608dfda-a7ee-4ac1-b323-89b4b11d233d.png)

衝突發生在不同的分支紀錄要合併時，發現居然不同的狀況。 git 很貼心會把衝突的部分秀出來，這時候好好找你同事聊一聊討論一下要改成什麼吧！把標記刪除再重新推一次就可以解衝突囉！

![image](https://user-images.githubusercontent.com/40282726/135757593-92dc15d4-df67-4b4d-b1ae-9fc02d2f02a0.png)

把標記刪除再重新推一次就可以解衝突囉！

![image](https://user-images.githubusercontent.com/40282726/135757713-861fbd8d-61f1-40ea-b51d-0eb3cd4ebd2c.png)


## 6. 標籤 (Tag)
### 列出標籤
``` git tag```
### 建立標籤
```git tag -a v1.5 -m "my version 1.5 and it add some ..." ```
### 查看標籤資訊
``` git show v1.5 ```
### 分享標籤
- git push 指令預設不會將標籤傳送到遠端伺服器，你必須要用以下指令才能推送
  ```git push origin v1.5 ```
- 傳送多個標籤
  ```git push origin --tags ```
- [參考資訊](https://git-scm.com/book/zh-tw/v2/Git-%E5%9F%BA%E7%A4%8E-%E6%A8%99%E7%B1%A4)
## 7. 其他操作
### (1) 刪除檔案
你可以直接砍檔案 ``` rm 檔案```

把特！你會看到這個
![螢幕快照 2021-08-26 下午3 39 20](https://user-images.githubusercontent.com/40282726/130921677-7e64af90-f336-46ed-9dc4-fa95673c0949.png)

因此你要繼續做 git add 和 commit 的動作

484很麻煩！！所以貼心的 git 有這個功能 ``` git rm 檔案``` 可以一鍵呵成

![螢幕快照 2021-08-26 下午3 42 43](https://user-images.githubusercontent.com/40282726/130922134-de924e3a-df13-4ba7-84cf-3d7bcaeee24b.png)

### （2）更換檔名
跟剛剛一樣，你可以使用 mv 指令換檔名然後再 add commit 

但 git 一樣有提供一鍵呵成
![螢幕快照 2021-08-26 下午3 48 14](https://user-images.githubusercontent.com/40282726/130923030-cfd4f29c-c89e-4fae-99f5-c78f12d182a5.png)



