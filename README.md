<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">API Test Automation</h3>

  <p align="center">
    Test automation framework for rest APIS.
    <br />
  </p>
</div>


## About The Project
The purpose of this project is to showcase on how to create a test automation framwork to be used in testing api and generate a readable report.

### Built With

* Python 
* Pytest
* Allure for report creation.

## Getting Started

These are the steps to follow when you want to run the project locally.

### Prerequisites

Items required be installed before you can start running the test.
These are instructions for a user with a mac device.
* Python
  ```sh
  brew install python
  ```
* Allure
```sh
  brew install allure
  ```

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/Moukatech/API_Automation
   ```
2. Change directory to the cloned project:
   ```sh
    cd API_Automation
    ```
4. Install pipenv to create a virtual enviroments and activate it:
   ```sh
   pip install pipenv
   pipenv shell 
   ```
4. Install required packages from the `requirement.txt` file:
   ```sh
   pip install -r requirements.txt
   ```
5. To run the test run:
   ```sh
   pytest --alluredir=allure_report/ tests/  
   ```
6. To be able to view the test results:
   ```sh
    allure serve allure_report/ 
    ```

 ## Example of how the final report should look like
 [![Allure report Screen Shot][Report_Screenshot]]
 
 
 
 
 
 
 [Report_Screenshot]: images/Report_Screenshot.png