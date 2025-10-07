# GitHub Push Instructions

Follow these steps to push your code to GitHub:

## 1. Create a New Repository on GitHub

1. Go to https://github.com/new
2. Name your repository (e.g., "caprae-capital-intern-challenge")
3. Keep it public or private as you prefer
4. Do NOT initialize with a README
5. Click "Create repository"

## 2. Push Your Code to GitHub

After creating the repository, run these commands in your terminal:

```bash
cd c:\Users\diwak\lead-enrich-streamlit
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git branch -M main
git push -u origin main
```

Replace YOUR_USERNAME with your GitHub username and YOUR_REPOSITORY_NAME with the name you gave your repository.

## 3. Alternative: If You Already Have a Repository

If you already have a repository you want to use:

```bash
cd c:\Users\diwak\lead-enrich-streamlit
git remote add origin https://github.com/YOUR_USERNAME/YOUR_EXISTING_REPOSITORY.git
git branch -M main
git push -u origin main
```

## 4. Verify the Push

After pushing, you should be able to see your code at:
https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME

The following files have been committed and are ready to push:
- app.py (Main application)
- requirements.txt (Dependencies)
- README.md (Project documentation)
- report.md (Implementation report)
- business_understanding.md (Business questions answers)
- video_script.md (Demo video script)
- .gitignore (Git ignore file)