# AGRakClient-Runner

Select Language: [English](#english_lang_toofan) | [فارسی](#persian_lang_toofan)

<a id="english_lang_toofan"></a>

**AGRakClient-Runner** is a Python-based tool designed to manage multiple accounts for the SA-MP (San Andreas Multiplayer) server **Arsacia Game** by interacting with the **AGRakClient** executable. This runner automates the process of launching and managing connections for multiple accounts simultaneously.

## Features
- Multi-account management
- Simplified setup and execution
- Seamless integration with **AGRakClient**

## Requirements
To use AGRakClient-Runner, ensure the following prerequisites are met:

1. **Python** is installed on your system (Python 3.7 or later is recommended).
2. The `AGRakClient.exe` file is present in the same directory as this runner.
3. A properly configured `Runner.xml` file is available in the directory.

## How to Use
### Step 1: Prepare the Environment
1. Clone or download the AGRakClient-Runner repository.
2. Ensure that `AGRakClient.exe` (available in the AGRakClient repository) is in the same directory as the runner script.
3. Create a `Runner.xml` file with the following content:

   ```xml
   <users>
       <user username="Your account 1 username" password="Your account 1 password" />
       <user username="Your account 2 username" password="Your account 2 password" />
       .
       .
       .
   </users>
   ```

   - Replace `Your account 1 username` and `Your account 1 password` with your actual credentials for the first account.
   - Repeat this for additional accounts.

### Step 2: Install Dependencies
AGRakClient-Runner may require additional Python libraries. Install them using:

```bash
pip install -r requirements.txt
```

(Note: The repository includes a `requirements.txt` file if libraries are necessary.)

### Step 3: Run the Script
Execute the runner script by running:

```bash
python Runner.py
```

The script will:
- Read the credentials from `Runner.xml`.
- Launch **AGRakClient.exe** for each account listed.

## Donations
If you find AGRakClient-Runner helpful and would like to support its development, consider making a donation:  
[Support AGRakClient-Runner](https://reymit.ir/dawshtoofan)

Thank you for using AGRakClient-Runner!

---

<a id="persian_lang_toofan"></a>

# اجراکننده AGRakClient

**AGRakClient-Runner** یک ابزار مبتنی بر پایتون است که برای مدیریت چندین حساب کاربری در سرور SA-MP (بازی چندنفره San Andreas Multiplayer) **Arsacia Game** طراحی شده است. این ابزار فرآیند راه‌اندازی و مدیریت اتصال به چندین حساب را به صورت همزمان خودکار می‌کند.

## ویژگی‌ها
- مدیریت چندین حساب کاربری
- راه‌اندازی و اجرای ساده
- ادغام یکپارچه با **AGRakClient**

## پیش‌نیازها
برای استفاده از AGRakClient-Runner، موارد زیر باید فراهم باشد:

1. **پایتون** روی سیستم شما نصب باشد (نسخه 3.7 یا بالاتر توصیه می‌شود).
2. فایل `AGRakClient.exe` در همان دایرکتوری که این ابزار قرار دارد موجود باشد.
3. یک فایل پیکربندی به نام `Runner.xml` در دایرکتوری موجود باشد.

## راهنمای استفاده
### مرحله 1: آماده‌سازی محیط
1. مخزن AGRakClient-Runner را کلون یا دانلود کنید.
2. اطمینان حاصل کنید که `AGRakClient.exe` (موجود در مخزن AGRakClient) در همان دایرکتوری که اسکریپت اجراکننده قرار دارد موجود است.
3. یک فایل `Runner.xml` با محتوای زیر ایجاد کنید:

   ```xml
   <users>
       <user username="نام کاربری حساب اول شما" password="رمز عبور حساب اول شما" />
       <user username="نام کاربری حساب دوم شما" password="رمز عبور حساب دوم شما" />
       .
       .
       .
   </users>
   ```

   - `نام کاربری حساب اول شما` و `رمز عبور حساب اول شما` را با اطلاعات حساب اول خود جایگزین کنید.
   - این کار را برای حساب‌های اضافی تکرار کنید.

### مرحله 2: نصب وابستگی‌ها
ممکن است AGRakClient-Runner نیاز به کتابخانه‌های اضافی پایتون داشته باشد. آنها را با دستور زیر نصب کنید:

```bash
pip install -r requirements.txt
```

(توجه: مخزن شامل فایل `requirements.txt` است در صورت نیاز به کتابخانه‌ها.)

### مرحله 3: اجرای اسکریپت
اسکریپت اجراکننده را با دستور زیر اجرا کنید:

```bash
python Runner.py
```

اسکریپت:
- اطلاعات ورود را از فایل `Runner.xml` می‌خواند.
- **AGRakClient.exe** را برای هر حساب فهرست شده راه‌اندازی می‌کند.

## حمایت مالی
اگر AGRakClient-Runner برای شما مفید بود و مایل به حمایت از توسعه آن هستید، می‌توانید از طریق لینک زیر کمک کنید:  
[حمایت از AGRakClient-Runner](https://reymit.ir/dawshtoofan)

از استفاده شما از AGRakClient-Runner متشکریم!

