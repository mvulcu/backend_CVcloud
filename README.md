# Google Cloud Platform (GCP) Resume Challenge

Welcome to my GCP Resume Challenge project! This is a serverless resume, showcasing my skills and experiences in cloud technologies, particularly within the Google Cloud Platform. Here, I'll take you through what I did, how I did it, and why I made certain decisions both in terms of what to do and how to execute it.

## Overview

This project involves the creation of a serverless, dynamic resume hosted on GCP. It's not just a static display of my professional journey, but also a testament to my skills in cloud architecture, serverless technologies, and modern web development practices.

## What I Did

1. **Created a Static Web Resume**:
   - Designed and developed a resume in HTML/CSS, showcasing my professional background.
   - Integrated JavaScript to add interactive elements like a visitor counter.

2. **Implemented Serverless Backend**:
   - Used Google Cloud Functions to handle backend processes such as retrieving and updating the visitor count.

3. **Data Storage with Firestore**:
   - Chose Google Cloud's Firestore for storing and managing the visitor count data.

4. **Infrastructure as Code**:
   - Utilized Terraform for defining and deploying all the cloud infrastructure in a codified and version-controlled manner.

5. **CI/CD Pipeline**:
   - Configured GitHub and Google Cloud Build for continuous integration and deployment, ensuring updates and changes are automatically and safely deployed to production.

## How I Did It

### Frontend Development

- **HTML/CSS**: Crafted a clean, responsive design to present my resume.
- **JavaScript**: Wrote a script for dynamically displaying the visitor count.

### Backend and Cloud Functions

- **Python**: Chose Python for Cloud Functions due to its simplicity and efficiency.
- **Firestore Integration**: Used Google Cloud Client Libraries in Python for interacting with Firestore.

### Terraform for IaC

- Defined the entire cloud infrastructure needed for this project in Terraform, including Cloud Functions, Firestore, and necessary permissions.

### CI/CD Setup

- Integrated GitHub with Google Cloud Build to automate the testing and deployment process.

## Why I Did It

### Technology Choices

- **GCP and Serverless**: Opted for GCP to showcase my expertise in this cloud platform and serverless to demonstrate the ability to build scalable, efficient applications.
- **Terraform**: Chose IaC for its ability to manage infrastructure in a reproducible way, making the deployment process transparent and efficient.
- **Python**: Selected for backend logic due to its wide acceptance and ease of use in cloud environments.

### Design and Implementation Decisions

- **Static Site with Dynamic Elements**: This approach balances simplicity with interactivity, ensuring the site is easy to host and manage while still being engaging.
- **Firestore for Real-Time Data**: Enables real-time visitor count updates, showcasing real-time data handling capabilities.

## Conclusion

This project is more than a digital resume; it's a reflection of my skills in cloud-based development and my understanding of modern web technologies. It demonstrates my ability to leverage GCP's serverless architecture to build a scalable, responsive web application.

Feel free to explore the site and see how the visitor count changes with each visit, which is a small yet powerful demonstration of real-time data processing and serverless backend capabilities.

---

Thank you for taking the time to explore my GCP Resume Challenge project!
