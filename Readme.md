[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JNZip13Q)
## Overview

In this lab, you will deploy your Flask application to Render and verify that it works as a public web service.

You will practice:

1. Preparing a Flask app for cloud deployment
2. Configuring a Render Web Service from a GitHub repository
3. Managing production environment variables securely
4. Verifying the deployed application through a public URL

The goal is to move your project from local development to a live deployment that can be accessed through the web.

---

## Quick Setup

1. Make sure your application runs locally before deploying.
2. Push your latest code to GitHub.
3. Create a Render account at https://render.com if you do not already have one.

---

## Task 1: Prepare the App for Deployment

Before deploying, make sure your project is ready to run in a hosted environment.

### Requirements

1. Your app must expose the Flask application as `app` in `app.py`
2. Dependencies must be listed in `requirements.txt`
3. Use environment variables for secrets and configuration
4. Use a production server such as `gunicorn` instead of Flask's development server

### Recommended start command

```bash
gunicorn app:app
```

### Notes

- If `gunicorn` is not already in `requirements.txt`, add it before deploying.
- Do not hardcode secrets into your source code.
- Keep `.env` files and credential files out of GitHub.

---

## Task 2: Create a Render Web Service

Deploy the application from your GitHub repository using Render.

### Steps

1. Log in to Render.
2. Click **New +** and choose **Web Service**.
3. Connect your GitHub repository.
4. Select the branch you want to deploy.
5. Configure the service using settings similar to the following:

```text
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

6. Create the service and wait for the initial deploy to complete.

### Tips

- If Render asks for a Python version, use Python 3.11.
- Read the deploy logs carefully if the build or startup fails.
- A successful deployment should end with a public `.onrender.com` URL.

---

## Task 3: Configure Environment Variables Securely

Your deployed app will not have access to your local `.env` file, so required values must be added in Render.

### Environment variables for this project

Based on `config.py`, your app may require:

```text
FLASK_SECRET_KEY
FIREBASE_WEB_API_KEY
SENSOR_API_KEY
FIREBASE_SERVICE_ACCOUNT
```

### Requirements

1. Add required environment variables in the Render dashboard.
2. Do not commit real secrets to GitHub.
3. If your Firebase Admin SDK needs a JSON key file, use a secure file-based approach supported by Render and point `FIREBASE_SERVICE_ACCOUNT` to that file path.

### Important

- Never paste secrets into source files.
- Never rely on your local `.env` file in production.
- If a deployment fails because of missing configuration, fix the environment variables and redeploy.

---

## Task 4: Verify the Deployment

After Render finishes deploying, confirm that the live application works.

### Verification steps

1. Open the public Render URL in your browser.
2. Confirm the application loads successfully.
3. Test at least one meaningful flow, such as:
   - loading the dashboard
   - signing in
   - opening a profile page
   - calling one API route
4. Inspect the Render logs and confirm the app starts without immediate crashes.

### Success indicators

- The service builds successfully.
- The app starts successfully on Render.
- The public URL responds correctly.
- At least one real application flow works in the deployed environment.

---

## Deliverables

Submit the following:

```text
GitHub repository URL
Public Render deployment URL
Updated requirements.txt (if needed for deployment)
```

Deployment proof:

- Screenshot of the successful Render deployment logs
- Screenshot of the deployed application running in the browser
- Short note listing the environment variable names you configured in Render

---

## Success Criteria

1. The application is deployed publicly on Render.
2. The deployed service starts without startup errors.
3. Required secrets and configuration are set through Render, not hardcoded in the repo.
4. The public URL is accessible and at least one application flow works.
5. Submission includes deployment proof.

---

## Rubric

Each criterion is scored out of 5 points.

### 1. Deployment Configuration - /5

- Level 5 (5): Render service is configured correctly with the proper build command, start command, and working deployment.
- Level 4 (4): Deployment works with minor configuration issues or small inefficiencies.
- Level 3 (3): Deployment is partially correct but required instructor help or repeated fixes.
- Level 2 (2): Deployment is incomplete or unstable.
- Level 1 (1): No functional deployment configuration.

### 2. Environment Variable Management - /5

- Level 5 (5): All required environment variables are configured correctly and secrets are handled securely.
- Level 4 (4): Most variables are configured correctly with minor issues.
- Level 3 (3): Some configuration works, but important variables are missing or unclear.
- Level 2 (2): Secrets/configuration are poorly managed or only partially working.
- Level 1 (1): Environment configuration is missing or insecure.

### 3. Deployment Verification - /5

- Level 5 (5): Public URL works and at least one meaningful application flow is verified successfully.
- Level 4 (4): Deployment works with minor verification gaps.
- Level 3 (3): App is reachable but testing is minimal or incomplete.
- Level 2 (2): App deployment exists but does not function correctly.
- Level 1 (1): No meaningful verification provided.

### 4. Documentation and Proof - /5

- Level 5 (5): Clear screenshots and deployment evidence are included with all required artifacts.
- Level 4 (4): Most proof artifacts are included with minor omissions.
- Level 3 (3): Some proof is included, but important evidence is missing.
- Level 2 (2): Limited proof is provided.
- Level 1 (1): Little or no proof of deployment.

**Total Score: /20**
