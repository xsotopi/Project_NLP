# DETECTION OF NEGATIONS AND UNCERTAINTIES IN DISCHARGED MEDICAL TEXTS
This project aims to explore and effectively detect the expressions of negations and uncertainties within medical discharge summaries. In the medical field, understanding such nuances is essential to accurate diagnosis, prognosis, and ultimately patient care. This project aims to provide an effective, automated solution that can facilitate and expedite this process, reducing the scope for human error and increasing the speed of healthcare service provision.
<p align="center">
  <img width="500" alt="image" src="https://github.com/NilBiescas/Project_NLP/assets/98542048/628ac09c-27c8-48a8-9acd-e48f0b79c061">
</p>


## Overview:
This project explores two distinct approaches for the detection of these linguistic phenomena: a rule-based method and a machine learning method. The rule-based method relies on pre-established sets of patterns and rules, while the machine learning method takes advantage of the CRFSuite, a Conditional Random Field (CRF) algorithm known for its applicability in the field of Natural Language Processing.

To get started with the project, you need to have Python installed on your machine along with certain other prerequisites. Detailed instructions for setup and execution are provided below:
### Prerequesites:
Clone the project repository to your local machine. Use the following command in your terminal:
```
[https://github.com/DCC-UAB/dlnn-project_ia-group_1.git](https://github.com/NilBiescas/Project_NLP.git)
```
Next, install the CRFSuite algorithm, which is the backbone of the machine learning approach of this project. Use the pip command to install it from the following repository:
```
pip install git+https://github.com/MeMartijn/updated-sklearn-crfsuite
```
After successful installation of the required software, you are ready to proceed with the code execution.

### Executing the Program:
To experiment with the approaches provided, run either the RuleBased_approach.py or the Machine_approach.py file. The decision between these approaches depends on your specific use-case or interest in one method over the other.

This project opens up possibilities for improving and expediting patient care by harnessing the power of machine learning and rule-based detection. We hope it proves to be beneficial in your research or application.
