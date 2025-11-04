# 🕌 Association Management System – SOLID Project (Python)

## 📘 Project Overview
This project implements a **management system for a youth Qur'anic association**, designed with **Object-Oriented Programming (OOP)** principles and following the **SOLID** guidelines.  

It manages:
- Members (students, teachers)
- Events (trips, meetings, competitions)
- Subscriptions and donations  
- Data persistence through repositories and storage classes.

---

## 🧩 Applied SOLID Principles

### 1️⃣ **Single Responsibility Principle (SRP)**
**Definition:**  
Each class should have one and only one reason to change.

**Applied in:**  
- `Member` → stores only member data (name, email, etc.).  
- `MemberRepository` → handles saving and loading members to/from storage.  
- `Subscription` → handles payment logic only.  
- `EventManager` (if implemented) → manages event-related operations separately.

**Problem solved:**  
Previously, some classes mixed data and logic (e.g., a `Member` saving itself to a file).  
By splitting responsibilities, the system became **easier to test**, **extend**, and **maintain**.

---

### 2️⃣ **Open/Closed Principle (OCP)**
**Definition:**  
Classes should be **open for extension** but **closed for modification**.

**Applied in:**  
- `Event` extended by `Trip`, `Meeting`, and `Competition`.  
- `Subscription` extended by `MonthlySubscription` and `AnnualSubscription`.  

**Problem solved:**  
Instead of rewriting the main logic for every new event or subscription type,  
we can **add new subclasses** without changing the existing ones — avoiding code duplication and regression.

---

### 3️⃣ **Liskov Substitution Principle (LSP)**
**Definition:**  
Subclasses should be replaceable by their parent classes without altering program behavior.

**Applied in:**  
- `Trip`, `Meeting`, `Competition` can all replace `Event` in any context.  
- `Student` and `Teacher` can both replace `Member`.

**Problem solved:**  
Ensures polymorphism works correctly — functions expecting an `Event` can safely receive any subclass, making the system **flexible and robust**.

---

### 4️⃣ **Interface Segregation Principle (ISP)**
**Definition:**  
Clients should not depend on interfaces they don’t use.  
In other words, split large interfaces into smaller, specific ones.

**Applied in:**  
- `Payable` → implemented by `Subscription` and `Donation` (defines `process_payment()` only).  
- `Organizable` → implemented by `Event` and its subclasses (defines `schedule()`).  
- `Registrable` → implemented by `Member` (defines `register_member()`).

**Problem solved:**  
Avoided creating one giant “god” interface with too many methods.  
Each class only implements what it actually needs, keeping the design **clean and decoupled**.

---

### 5️⃣ **Dependency Inversion Principle (DIP)**
**Definition:**  
High-level modules should not depend on low-level modules; both should depend on abstractions.

**Applied in:**  
- `MemberRepository` depends on an abstract `Storage` interface (e.g., `JSONStorage`, `CSVStorage`).  
- The main program (`main.py`) uses dependency injection to provide the chosen storage system.

**Problem solved:**  
Allows switching from one storage type (e.g., JSON) to another (e.g., database)  
without changing the core application logic — making the system **scalable and adaptable**.

---

## 🧱 Project Structure

