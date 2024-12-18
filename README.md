# Retrieval Augmented Generation (RAG) System for Nordic Travel Queries

| Authors               | Student ID           
|-----------------------|-------------------
| Loh Jianyang John     | 1006360
| Min Hui Liew          | 100XXXX
| Vannara Lim           | 1006088

This project is designed to be ran on Google Colab.

## Notebooks and short explanations

Each notebook contains <u>details</u> to use and run it.

Key things to take note in the notebooks have headings such as 
- User Action Required

that can be found at different sections of the notebook

<br/>

| Notebook                                                     | Description                                             
|--------------------------------------------------------------|---------------------------------------------------------
| Retrieval_Evaluation_Setup.ipynb                             | Prepares Retrieval Evaluation Dataset         
| retriever_evaluation.py                                      | Retrieval Experiment helper functions                       
| Retrieval_Experiment_1.ipynb                                 | Retrieval Experiment for Ensemble Retriever                        
| Retrieval_Experiment_2.ipynb                                 | Retrieval Experiment for Reranked Retriever and Base Retriever           
| Retrieval_Experiment_Results.ipynb                           | Consolidated Retrieval Experiment Results
| Generation_Evaluation_Setup.ipynb                            | Prepares RAG System Evaluation Dataset     
| Generation_Experiment_docs_feed_X_parent_chunk_size_Y.ipynb  | RAG System Experiment for X number of chunks and Y parent chunk size        
| Generation.ipynb                                             | Sample code for running RAG System
| Generation_Similarity.ipynb                                  | Calculate cross-encoder similarity between RAG System response and GPT Web response      
| citation.ipynb                                               | Citation playground code

## Files and short explanations

Files that were used in this project and could be uploaded to GitHub can be found under ```/data```

| File                                                         | Description                                             
|--------------------------------------------------------------|---------------------------------------------------------
| finland_articles.csv                                         | Web scraped data for Finland       
| iceland_articles.csv                                         | Web scraped data for Iceland                        
| sweden_articles.csv                                          | Web scraped data for Sweden                           