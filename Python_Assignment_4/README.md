## Banking System

This Jupyter Notebook delves into the world of object-oriented programming (OOP) by designing a banking system in Python. We'll explore concepts like:

* **Abstract Base Class:** Defining `BankAccount` as an abstract class to represent core account functionalities (deposit, withdraw, balance inquiry).
* **Inheritance Hierarchy:** Creating subclasses (`SavingsAccount`, `CheckingAccount`, `CreditCardAccount`) that inherit from `BankAccount` and specialize in specific account types.
* **Polymorphism:** Overriding methods like `withdraw` in subclasses to implement account-specific withdrawal behavior (checking overdraft limits, credit limits).
* **Abstraction:** Hiding internal logic for cleaner code and a user-friendly experience.

**Banking System Structure:**

1. **`BankAccount` Class:**
    * Attributes: Account number, account holder name, account balance.
    * Methods: Deposit, withdraw (checks balance), get balance, display account details.
2. **`SavingsAccount` Class:**
    * Inherits from `BankAccount`.
    * Adds an `interest_rate` attribute.
    * Method: `add_interest` (increases balance based on interest rate & time).
3. **`CheckingAccount` Class:**
    * Inherits from `BankAccount`.
    * Adds an `overdraft_limit` attribute.
    * Overridden `withdraw` method (checks both balance and overdraft limit).
4. **`CreditCardAccount` Class:**
    * Inherits from `BankAccount`.
    * Adds a `credit_limit` attribute.
    * Methods: `make_purchase` (deducts from credit limit if possible), `make_payment` (increases both balance and credit limit).

**Exploring the System:**

The code demonstrates creating instances of each account type and utilizing their methods to:

* Deposit and withdraw funds.
* Add interest to a savings account.
* Utilize overdraft in a checking account (within defined limits).
* Make purchases and payments with a credit card account.

**Learning Outcomes:**

* Grasp the power of OOP in modeling real-world entities like bank accounts.
* Implement inheritance and polymorphism for flexible and reusable code.
* Utilize abstraction to separate internal logic from user interaction.

**Ready to Dive In?**

1. **Save this file as `Banking_System.ipynb`.**
2. **Launch Jupyter Notebook** and navigate to the directory containing this file.
3. **Run the notebook cells sequentially** to embark on your banking system adventure!
