# 🤖 Lumie-Bot

**Lumie** is a simple Python bot that automatically posts motivational quotes to a **Facebook Page** using the Facebook Graph API. It supports both local testing and scheduled automated posting using **GitHub Actions**.

> 💡 Perfect for personal projects, daily quote pages, or automation practice.
> ⚠️ For personal learning and testing purposes only.

---

### ⚠️ Sensitive Information Warning

> 🔐 This project uses **environment variables** to manage sensitive data like access tokens and Page IDs.
> These tokens allow access to your Facebook Page through the Meta Graph API.

#### 🚫 DO NOT:

* Commit your real `.env` file to version control
* Share your **access tokens**, **Page IDs**, or **Meta App secrets** publicly
* Push changes that include hardcoded credentials inside `.py` files

#### ✅ Always:

* Add `.env` to your `.gitignore` file (already done in this project)
* Use `os.getenv()` in your code to access environment variables
* Use `.env.example` to show users what config values they need
* Set secrets in **GitHub Actions → Settings → Secrets** for automated workflows

---

> ⚠️ Leaking tokens can give others full access to your Page — always treat access tokens like **passwords**.

---

## ⚙️ Environment Setup (.env)

Create a `.env` file in the root directory with the following:

```env
LUMIE_PAGE_ID=your_facebook_page_id
LUMIE_PAGE_ACCESS_TOKEN=your_facebook_page_access_token
````

* `LUMIE_PAGE_ID`: Your Facebook **Page ID**
* `LUMIE_PAGE_ACCESS_TOKEN`: A **long-lived Page Access Token** with `pages_manage_posts` permission

> 🔐 **Never commit your `.env` file**. It should already be listed in `.gitignore`.

---

### 📌 Notes

* This bot **only works with Facebook Pages**, not personal profiles or Groups
* Your Page must be:

  * ✅ **Published**
  * ✅ **Free of country or age restrictions**
  * ✅ **Created using** [facebook.com/pages/create](https://facebook.com/pages/create)
* If posts appear but are **only visible to Page admins**, the most likely causes are:

  * ❌ The Page is **unpublished**
  * ❌ The Meta App is in **Development mode**
  * ❌ The Page was created incorrectly as a personal profile
    
* **Issue I Encountered**:
    > “The script worked and successfully posted to my Page, but I couldn’t see the post from my personal account that wasn’t tied to the Page.
    > In the post it said:
    > *'Only people who manage this Page can see this.'*
    > I wasn’t sure how to troubleshoot the Meta App permissions, switch the app to Live mode, or check if the access token visibility was limited.”

This issue is common when:
* The **Facebook Page is unpublished**
* The **Meta App** used is still in **Development Mode**
* The **access token** lacks proper scopes or is tied to a test user/dev only
* The Page was created as a **profile or not properly set up**

---

## 📜 Features

* ✅ Posts random motivational quotes from a local `quotes.txt` file
* ✅ Formats quotes with date and hashtags
* ✅ Posts directly to your Facebook Page via the Graph API
* ✅ Supports scheduled daily posting using **GitHub Actions**

---

## 🚀 Quick Start (Local Testing)

### 1. Install dependencies

```bash
pip install python-dotenv requests
```

### 2. Add your quotes

Create a file called `quotes.txt` in the root folder. Each quote should be on a separate line.

```
Be yourself; everyone else is already taken.
Do something today that your future self will thank you for.
The only limit is your mind.
```

### 3. Run the bot

```bash
python lumieBot.py
```

If everything is set up correctly, it will post a random quote to your Facebook Page.

---

## ⏰ Scheduled Posting with GitHub Actions

LumieBot is set to post quotes **3 times a day** using GitHub Actions.

### 📅 Posting Schedule (Philippine Time, PHT)

| Time         | UTC Equivalent | Purpose       |
| ------------ | -------------- | ------------- |
| 7:00 AM PHT  | 11:00 PM UTC   | Morning boost |
| 12:00 PM PHT | 4:00 AM UTC    | Midday post   |
| 6:00 PM PHT  | 10:00 AM UTC   | Evening wrap  |

### ✅ GitHub Secrets Required

Add the following secrets in your repo under **Settings → Secrets and variables → Actions**:

* `LUMIE_PAGE_ID`
* `LUMIE_PAGE_ACCESS_TOKEN`

GitHub Actions will inject these into the bot during runtime.

---

## 🗂️ Project Structure

```
lumie-Bot/
│
├── quotes.txt          # Your list of quotes (one per line)
├── lumieBot.py         # Main Python script
├── .env                # (Ignored) Local environment config
├── .gitignore          # Ignores .env, cache, editor files
└── .github/workflows/
    └── lumiebot.yml    # GitHub Actions workflow
```

---

## 📌 Notes

* This only works with **Facebook Pages** (not profiles or groups)
* Your Page must be **published** and publicly visible
* Ensure your access token is valid and has the correct permissions
* Facebook sometimes delays post visibility — give it a few seconds

---

## 🛡️ Disclaimer

This tool is intended for **educational or personal use** only. Use responsibly and in accordance with [Meta’s Platform Terms](https://developers.facebook.com/terms).

---

## 💬 Credits

Built with ❤️ by [MelDev](https://github.com/MvPorcalla)

