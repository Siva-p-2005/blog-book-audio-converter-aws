# blog-book-audio-converter-aws
# Blog / Book Audio Converter using AWS Polly

## 👨‍🎓 Name
Siva

## ☁️ Project Type
AWS Serverless Project

---

## 📌 Project Overview
The Blog/Book Audio Converter project converts written content such as blogs, articles, newsletters, or book excerpts into natural-sounding speech.  
It uses AWS managed services to automatically convert uploaded text files into audio files, improving accessibility and content engagement.

---

## 🎯 Key Features
- Accessibility for visually impaired users
- Audio-based learning support
- Increased content engagement
- Hands-free content consumption (commute, workouts, multitasking)

---

## 🧰 Tools & Technologies
- Amazon S3 – Stores input text files and output audio files
- AWS Lambda – Serverless backend processing
- Amazon Polly – Text-to-Speech conversion
- AWS IAM – Secure permissions and roles
- Python 3.8 – Lambda runtime

---

## 🏗️ Architecture
Text File Upload (Source S3 Bucket)  
→ S3 Event Notification  
→ AWS Lambda Function  
→ Amazon Polly (Text-to-Speech)  
→ Audio File Stored in Destination S3 Bucket

---

## ⚙️ Step-by-Step Implementation

### Step 1: AWS Account Setup
Create an AWS account and configure credentials.

### Step 2: Create S3 Buckets
- Source Bucket: `amc-polly-source-bucket`
- Destination Bucket: `amc-polly-destination-bucket`

### Step 3: IAM Policy Creation
Create a policy allowing:
- S3 read/write access
- Polly speech synthesis access
- CloudWatch logs access

### Step 4: Create IAM Role
- Role Name: `amc-polly-lambda-role`
- Attach IAM policy and AWSLambdaBasicExecutionRole

### Step 5: Create Lambda Function
- Function Name: `TextToSpeechFunction`
- Runtime: Python 3.8
- Configure environment variables for bucket names

### Step 6: Configure S3 Event Notification
Trigger the Lambda function when a `.txt` file is uploaded to the source bucket.

### Step 7: Lambda Function Logic
- Read text file from S3
- Convert text to MP3 using Amazon Polly
- Upload MP3 file to destination S3 bucket

### Step 8: Testing
- Upload a sample `.txt` file
- Verify MP3 output in destination bucket
- Check CloudWatch logs for execution status

---

## ✅ Advantages
- Fully automated serverless solution
- No server maintenance required
- Scalable and cost-effective
- Improves accessibility and user experience

---

## 🏁 Conclusion
This project demonstrates how AWS services such as S3, Lambda, and Polly can be integrated to build an automated text-to-speech system. It provides an efficient and scalable solution for converting written content into audio format.
