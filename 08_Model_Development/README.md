## 機器學習演算法

機器學習的演算法可以大致分為監督式學習與非監督式學習，兩者的差別在於是否知道標準答案

- 監督式學習好比說學生寫作業對答案，我們從錯誤中學習，有老師跟我們說標準答案，告訴我們這個世界的基準是什麼
  - 分類
  - 預測
- 非監督式學習會讓小孩去自己學習，例如你帶他去一趟動物園之後，他可能會歸納說猴子跟猩猩很像，老虎跟貓很像，藉此從資料中學習一套法則，但你並沒有跟他說答案
  - 分群
  - 降維
<img width="524" alt="螢幕快照 2021-08-29 上午11 07 01" src="https://user-images.githubusercontent.com/40282726/131237087-733c4146-2d5d-435d-93fa-e77412d427f2.png">

## 過度擬合
若實作機器學習之後會常常聽見的名詞，過度擬合(overfitting)

機器會根據資料來進行學習，但倘若它過度擬合這些圓點，而使用一個過度複雜的模型(右圖)，雖然在訓練的時候得到比較好的成效，但通常在沒看過的資料成效會大打折扣

![image](https://user-images.githubusercontent.com/40282726/131237697-dc98f81d-ada3-4d4c-b953-a33a1fc33c46.png)

為了防止這種情況，我們可以...
- 收集更多資料(但也意味者成本提高)
- 用資料增補(Data Augmentation)
  這招常常使用在影像辨識，由於收集的資料有限，我們可以將既有的資料進行旋轉、光暗調整、縮小放大等等進行調整，就可以倍增很多資料
- 重新進行資料探索，合併或減少沒有用的特徵
- 正規化，有 L1、L2 regularization。在演算法的 loss 計算加上懲罰項，如此一來機器在進行訓練時來約束模型不要過度擬合

## 交叉驗證
前面有提過在資料進行預測之前，通常會將資料進行分割。

但是我們很可能會遇到極端的狀況是，我們剛好切出來的驗證集資料跟訓練集很有相關，為了避免這種狀況發生，我們可以進行交叉驗證。

所謂的交叉驗證是將訓練資料進行多次不同的切割，輪流當驗證集，最後計算的時候取平均，比較能了解資料在不同情況下的成效。

![image](https://user-images.githubusercontent.com/40282726/131237686-e4552637-a4dd-4567-bafc-8a26b6211f08.png)

## 集成式學習
集成式學習(Ensemble Learning)，是將數個監督式學習的模型集合起來，可以達到更好的模型成效。俗話說的話，三個臭皮匠勝過一個諸葛亮，就是這個道理！

若使用單一個模型，可能會有過度擬合資料等缺點；但是我們可以集眾人之力量，雖然每個模型可能是一個弱的分類器，但是有多個模型並綜合評估，可以達到互補且加分的效果。

依照處理方式的不同，又可以分為 Bagging、Boosting、Stacking。

- 資料面：用不同的訓練資料、同一種模型，進行多次的訓練綜合的預測結果
- 特徵面：用同樣的資料、不同的模型，綜合的預測結果

| 面向  | 方法 | 例子 |
| -------- | -------- | -------- |
| 資料面  | Bagging     | Random Forest     |
| 資料面  | Boosting     | XGBoost、LightGBM、GBDT、AdaBoost、CatBoost    |
| 特徵面  | Blending     |   Voting  |
| 特徵面  | Stacking     |     |

### Bagging
裝袋法(Bootstrap Aggregating, Bagging)，把訓練資料重新採樣之後，就可以產生不同組的訓練資料。常見的例子有隨機森林。

少數服從多數，透過不同的子集合進行不同子模型訓練，最終由子模型進行投票。

- 每次將資料抽後放回
- 建立多個相互獨立的模型
- 最後進行平均或是依照權重進行多數決投票

### Boosting
目標是為了要避免學習錯誤，讓自己往學正確的東西。根據預測錯誤的資料調整其權重值，讓模型下次能學習比較好。

迭代訓練某個模型，根據 i-1 輪預測錯誤得到的情況來修正第 i 輪訓練樣本的權重。

舉例來說，老師會在之前學生錯過的題目增加配分的比重，若再次寫錯代表沒有學好。

### Blending

混合不同種的模型，進行投票(權重可以自己定)

![image](https://user-images.githubusercontent.com/40282726/132982951-d7a0a599-cf1a-4e77-bf23-c102b2fcdd8b.png)

### Stacking

將預測的結果當作特徵，可以當作另一個模型的輸入值，因此又可以訓練一個新模型，如此重複地手段可以稱之為推疊(Stacking)

![image](https://user-images.githubusercontent.com/40282726/132977708-4fde26f0-f902-4a81-bc37-16bbf0245404.png)

### 參考資料
- [Blending and Bagging :: Uniform Blending @ Machine Learning Techniques (機器學習技法)](https://www.youtube.com/watch?v=DAFkKJYTMW4&list=PLXVfgk9fNX2IQOYPmqjqWsNUFl2kpk1U2&index=27&ab_channel=Hsuan-TienLin)
- [数据挖掘竞赛利器-Stacking和Blending方式](https://blog.csdn.net/maqunfi/article/details/82220115?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link)
- [[Day25] 模型選擇-集成方法](https://ithelp.ithome.com.tw/articles/10228200?sc=hot)
