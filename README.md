<br />
<div align="center">
  <a href="https://github.com/Moukatech/API_Automation">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">API Test Automation</h3>

  <p align="center">
    Test automation framework for REST APIS.
    <br />
  </p>
</div>


## About The Project
The purpose of this project is to showcase how to create a test automation framwork to be used in testing REST APIs and generate a readable report.

### Built With:

* Python.
* Pytest.
* Allure reporting template.

## Getting Started

These are the steps to follow when you want to run the project locally.

### Prerequisites

Items required to be installed before you can start running the tests.
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
4. Install pipenv to create a virtual enviroment and activate it:
   ```sh
   pip install pipenv
   pipenv shell 
   ```
4. Install the required packages from the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```
5. To run the tests:
   ```sh
   pytest --alluredir=allure_report/ tests/  
   ```
6. To be able to view the test results:
   ```sh
    allure serve allure_report/ 
   ```

 ## Example of how the final report should look like.
 ![Allure report Screen Shot][Report_Screenshot]
 
 ## Contact
 Lewis Mocha - lewismocha@gmail.com
 
 
 
 
 [Report_Screenshot]: images/Report_Screenshot.png
