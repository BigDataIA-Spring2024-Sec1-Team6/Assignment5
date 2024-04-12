# Assignment5 

## Problem Statement
In the context of finance professional development, there's a need to enhance knowledge retrieval and question-answer capabilities using Models as a Service APIs. This involves curating information from multiple sources and determining the best approach for operationalizing the results within an enterprise environment.

## Project Goals
1. **Create Knowledge Summaries**: Leverage OpenAI’s GPT to generate detailed summaries based on the learning objectives and content from finance professional development resources.
2. **Generate Knowledge Base (Q/A)**: Develop a comprehensive question and answer database from topic summaries to enhance learning and retention for financial analysts.
3. **Vector Database Integration**: Utilize Pinecone to create a vector database that efficiently finds and retrieves relevant questions and answers, improving query responses.
4. **Operationalize Knowledge Retrieval**: Use the generated summaries and Q/A database to validate the operational feasibility of the model within an enterprise setting.
5. **Develop Multi-Page Streamlit Application**: Build a user-friendly, multi-page Streamlit application that allows users to interact with the knowledge summaries and Q/A database.
6. **Documentation and Version Control**: Ensure thorough documentation of the project and processes, managed via a professional GitHub repository.
7. **Security and Privacy Measures**: Implement appropriate security settings for APIs and data storage, ensuring the protection of sensitive information.

  ## Technologies Used

![Pinecone](https://img.shields.io/badge/Pinecone-13AA52?style=for-the-badge&logo=pinecone&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)


## Data Sources
- Data will be scraped from the **CFA Institute’s website**, webscraping using BeautifulSoup to get a csv file with the 4 assigned documents.

## Pre-requisites

1. **Scraping and Data Extraction**: Proficiency in extracting data from websites, particularly from complex financial documents, using tools like Beautiful Soup or Scrapy.
2. **Machine Learning and NLP with OpenAI**: Familiarity with machine learning techniques and natural language processing, especially using OpenAI's GPT for generating text and summarization.
3. **Pinecone Vector Database Usage**: Understanding of vector databases, particularly Pinecone, to handle embeddings and perform semantic search and retrieval.
4. **Streamlit for Interactive Dashboards**: Experience in building interactive web applications using Streamlit to display data and insights dynamically.
5. **API Integration and Development**: Skills in developing and integrating APIs to connect backend services with frontend applications, possibly using frameworks like FastAPI.
6. **Data Handling with Python**: Strong Python programming skills, especially for data manipulation, processing, and analysis.
7. **GitHub for Version Control**: Proficiency in using GitHub for source control, including pushing updates, pulling requests, and managing branches.

## Learning Outcomes
1. **Advanced Data Scraping Techniques**: Gain expertise in scraping and structuring data from complex web sources, focusing on financial educational content.
2. **Text Summarization with AI**: Develop skills in applying AI models, particularly OpenAI's GPT, to create accurate and concise content summaries from extensive financial documents.
3. **Question and Answer Database Creation**: Learn to design and populate a question-answer database to facilitate learning and query answering, enhancing understanding of financial topics.
4. **Vector Database Implementation**: Acquire knowledge in setting up and utilizing vector databases like Pinecone for semantic searching and data retrieval.
5. **Interactive Application Development**: Master the development of multi-page, interactive web applications using Streamlit, enhancing user engagement and content accessibility.
6. **API Design and Integration**: Understand how to build robust APIs that connect various components of an application, facilitating seamless data flow and functionality.
7. **Operational Decision-Making**: Learn to evaluate and choose the best operational approaches for integrating AI and database technologies in real-world enterprise scenarios.
8. **Professional Documentation and Reporting**: Improve abilities in creating detailed, professional documentation and reports to support project development, implementation, and evaluation.

## References
- https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/pinecone/Using_Pinecone_for_embeddings_search.ipynb
- https://docs.pinecone.io/examples/notebooks
- https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/pinecone/Gen_QA.ipynb
- https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/pinecone/GPT4_Retrieval_Augmentation.ipynb


This outline should provide a comprehensive framework for the assignment, detailing all necessary aspects for successful completion and evaluation.

## Team Information and Contribution

WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENT'S WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

| Name               | Contribution %   | Contributions                                             |
|--------------------|------------------|-----------------------------------------------------------|
| Osborne Lopes      | 30%            | Documentaion (50%) , Use Case 3 (50%)                     |
| Akshita Pathania   | 40%            | Pinecone (50%), Use Case 1, OpenAI (50%)                  |
| Smithi Parthiban   | 40%            | Pinecone (50%) , Use Case 2, OpenAI (50%)                 |
| Manimanya Reddy    | 30%            | Arch Diagram, Documentation (50%),Use Case 3 (50%)        |
 


CodeLabs Document: https://codelabs-preview.appspot.com/?file_id=1G9JvGRC8y_qDn36QhqQY8fIfYreahONuV6Cloe24e_8#4

Architecture Diagram:
<img width="563" alt="Screenshot 2024-04-12 at 4 25 53 PM" src="https://github.com/BigDataIA-Spring2024-Sec1-Team6/Assignment5/assets/114605149/b47b9f62-75bc-44ee-8866-51fdb273cf88">






