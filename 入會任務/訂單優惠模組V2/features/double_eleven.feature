@double_eleven
Feature: 雙十一優惠
  同一種商品每買 10 件，則該 10 件同種商品的價格總和會享有 20% 的折扣

  Scenario: 雙十一優惠 - 購買 12 件相同商品
    Given 一位用戶購買 12 件相同商品
    And 雙十一優惠：同一種商品每買 10 件，則該 10 件同種商品的價格總和會享有 20% 的折扣
    When 用戶下訂單
      | productName | category | quantity | unitPrice |
      | 襪子          | apparel  | 12       | 100       |
    Then 總訂單的價格應為 1000 元
      | originalAmount | discount | totalAmount |
      | 1200           | 200      | 1000        |

  Scenario: 雙十一優惠 - 購買 27 件相同商品
    Given 雙十一優惠 - 購買 27 件相同商品
    And 雙十一優惠：同一種商品每買 10 件，則該 10 件同種商品的價格總和會享有 20% 的折扣
    When 用戶下訂單
      | productName | category | quantity | unitPrice |
      | 襪子          | apparel  | 27       | 100       |
    Then 總訂單的價格應為 2300 元
      | originalAmount | discount | totalAmount |
      | 2700           | 400      | 2300        |

  Scenario: 雙十一優惠 - 購買 10 件不同商品
    Given 雙十一優惠 - 購買 10 件相同商品
    And 雙十一優惠：同一種商品每買 10 件，則該 10 件同種商品的價格總和會享有 20% 的折扣
    When 用戶購買商品 A, B, C, D, E, F, G, H, I, J 各一件（總共十件商品），每一件價格皆為 100 元
    Then 總訂單的價格應為 1000 元
      | originalAmount | discount | totalAmount |
      | 1000           | 0        | 1000        |
