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

1. 聚合關係(Aggregation)：A類中**使用**B類當作「成員變數」，而且A和B有一個弱的「擁有」關係，**A包含B**，但B不是A的一部分，拔掉B，A依然能存在，就稱為：A聚合到B，英文為"owns-a"關係。

eg. 機場 owns-a 飛機
   
3. 合成（組合）關係(Composition)：A類中使用B類當作「成員變數」，而且A和B有一個強的「擁有」關係，B是A的組成的一部分，拔掉B，A就不完整，就稱為：A合成到B，英文為"is-part-of"關係。

e.g. 引擎 is-part-of 飛機

4. 依賴關係(Dependency)：A類中使用到B類，但僅僅是弱連結，譬如：B類作為A類方法的參數、B類作為A類的局域變數、A類調用B類的靜態方法、B類作為A類方法的回傳值，就稱為：A依賴B，英文為"uses-a"的關係。

e.g. 機長 uses-a 飛機

Reference:
1. [物件導向武功秘笈（1）：認知篇 — 什麼是好的程式？](https://www.ycc.idv.tw/introduction-object-oriented-programming_1.html)
2. [物件導向武功秘笈（2）：招式篇 — Python與Java的物件導向編程介紹](https://www.ycc.idv.tw/introduction-object-oriented-programming_2.html)
3. [物件導向武功秘笈（3）：內功篇 — 物件導向指導原則SOLID](https://www.ycc.idv.tw/introduction-object-oriented-programming_3.html)
4. [淺談物件導向 SOLID 原則對工程師的好處與如何影響能力](https://ithelp.ithome.com.tw/articles/10223329)
5. [再談 SOLID 原則，Why SOLID?](https://ithelp.ithome.com.tw/articles/10228740)
6. [物件導向設計原則：單一職責原則，定義、解析與實踐](https://ithelp.ithome.com.tw/articles/10229226)
7. [物件導向設計原則：開放封閉原則，定義、解析與實踐](https://ithelp.ithome.com.tw/articles/10229362)
8. [Design Patterns: Single Responsibility Principle Explained Practically in C# (The S in SOLID)](https://www.youtube.com/watch?v=5RwhyZnVRS8)
9. [Design Patterns: Open Closed Principle Explained Practically in C# (The O in SOLID)](https://www.youtube.com/watch?v=VFlk43QGEgc)
10. [Design Patterns: Liskov Substitution Principle Explained Practically in C# (The L in SOLID)](https://youtu.be/-3UXq2krhyw)
11. [Design Patterns: Interface Segregation Principle Explained Practically in C# (The I in SOLID)](https://youtu.be/y1JiMGP51NE)
12. [Design Patterns: Dependency Inversion Principle Explained Practically in C# (The D in SOLID)](https://youtu.be/NnZZMkwI6KI) 