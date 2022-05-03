# OOP

1. class_and_object
2. method_overloading
3. **encapsulation**
4. **inheritance**
5. abstract_class / interface
6. **polymorphism** 

# UML

1. 關聯關係(Association)：A類中**使用**B類當作「成員變數」，但是A和B並沒有「擁有」的關係，只能說是**「有個」**的關係，就稱為：A關聯到B，英文為"has-a"的關係。

e.g. 飛機 has-a 排程   

2. 聚合關係(Aggregation)：A類中**使用**B類當作「成員變數」，而且A和B有一個弱的「擁有」關係，**A包含B**，但B不是A的一部分，拔掉B，A依然能存在，就稱為：A聚合到B，英文為"owns-a"關係。

eg. 機場 owns-a 飛機
   
3. 合成（組合）關係(Composition)：A類中使用B類當作「成員變數」，而且A和B有一個強的「擁有」關係，B是A的組成的一部分，拔掉B，A就不完整，就稱為：A合成到B，英文為"is-part-of"關係。

e.g. 引擎 is-part-of 飛機

4. 依賴關係(Dependency)：A類中使用到B類，但僅僅是弱連結，譬如：B類作為A類方法的參數、B類作為A類的局域變數、A類調用B類的靜態方法、B類作為A類方法的回傳值，就稱為：A依賴B，英文為"uses-a"的關係。

e.g. 機長 uses-a 飛機

Reference:
1. [物件導向武功秘笈（1）：認知篇 — 什麼是好的程式？](https://www.ycc.idv.tw/introduction-object-oriented-programming_1.html)
2. [物件導向武功秘笈（2）：招式篇 — Python與Java的物件導向編程介紹](https://www.ycc.idv.tw/introduction-object-oriented-programming_2.html)
3. [物件導向武功秘笈（3）：內功篇 — 物件導向指導原則SOLID](https://www.ycc.idv.tw/introduction-object-oriented-programming_3.html)