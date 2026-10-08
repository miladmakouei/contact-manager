# Contact Manager

A simple Python contact management system that allows users to add, search, display, and delete contacts.

## توضیح فارسی


برنامه می‌تواند:

 مخاطب جدید اضافه کند
 لیست مخاطبین را نمایش دهد
 مخاطب را بر اساس نام یا شماره پیدا کند
 مخاطب را حذف کند
 اطلاعات را داخل فایل ذخیره کند
 اطلاعات ذخیره‌شده را هنگام اجرای مجدد برنامه بخواند
 از ثبت شماره تلفن تکراری جلوگیری کند
خطاهای ورودی و اجرای برنامه را مدیریت کند

این پروژه برای تمرین Python و نزدیک شدن به ساخت برنامه‌های کاربردی در مسیر **AI Automation** ساخته شده است.

## Features

* Add new contacts
* Display all contacts
* Search contacts by name or phone number
* Delete contacts
* Save contacts to a text file
* Load contacts when the program starts
* Prevent duplicate phone numbers
* Handle errors safely
* Interactive command-line menu

## Concepts Used

This project uses Python concepts learned throughout the learning path:

* Variables
* Strings and f-strings
* `input()`
* Type conversion
* `if / elif / else`
* `while`
* `for`
* Lists
* Dictionaries
* `break`
* `continue`
* Functions
* `return`
* `try / except`
* File handling
* Sets

## Project Structure

```text
contact-manager/
├── main.py
├── contacts.txt
├── README.md
└── .gitignore
```

> `contacts.txt` is created automatically when the first contact is added.

## How to Run

Make sure Python is installed.

Run the following command:

```bash
python3 main.py
```

## Example

```text
========== CONTACT MANAGER ==========
1. Show contacts
2. Add contact
3. Search contact
4. Delete contact
5. Exit
=====================================
Choose an option:
```

## Data Storage

Contacts are stored in a simple text file using the following format:

```text
Name|Phone|Email
```

Example:

```text
Ali|09120000000|ali@gmail.com
Sara|09350000000|sara@gmail.com
```

## Purpose

This project is part of my Python learning path toward **AI Automation**.

The goal is to build practical Python projects and gradually move toward working with APIs, data processing, automation tools, and AI integrations.
