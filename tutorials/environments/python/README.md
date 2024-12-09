# Python

## Python Interpreter

You have the flexibility to install the Python interpreter of your choice. However, we highly recommend installing Miniconda, especially for Windows users, to preempt any potential compatibility issues that may arise during our daily work.

Moreover, Miniconda provides a convenient solution for managing multiple Python versions, facilitating efficient project development.


# Aproach 1: Miniconda Installation

## Download the installer

1. Visit the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html).
2. Choose the latest available versions of both Python 3 and Miniconda from the installers.
3. Download the installer suitable for your operating system (Windows, macOS, or Linux).

### Windows

1. Double-click the downloaded `.exe` file.
2. Follow the installation wizard instructions.
3. Select "Install for just me".
4. Choose the installation directory (the default is usually fine).
5. Allow the installer to add Miniconda to your system **PATH** environment variable (recommended for easy command-line usage).

### macOS and Linux

1. Open a terminal.
2. Navigate to the directory where you downloaded the installer.
3. Run the installer: `bash Miniconda3-latest-MacOSX-x86_64.sh` (replace with the actual filename).
4. Follow the installation prompts, and press `Enter` to accept the license agreement.
5. Choose the installation directory (the default is usually fine).
6. Allow the installer to add Miniconda to your system **PATH** environment variable (recommended for easy command-line usage).
7. To make the changes take effect, close and then re-open your terminal window.


### Test Your Installation

1. In your terminal window or Anaconda Prompt, ensurethat you have the conda base environment activated. You can confirm this by checking if `(base)` appears at the beginning of the path in the terminal, as shown below:

   ```
   (base) dpalacioj@COL-LT-241007D:/mnt/c/Users/david.palacio/Documents/projects/onboarding$
   ```

2. Run the command `conda list`. If Miniconda has been installed correctly, a list of installed packages will be displayed.

```
(job-profiler-model) dpalacioj@COL-LT-241007D:/mnt/c/Users/david.palacio/Documents/projects/onboarding$ conda list
# packages in environment at /home/dpalacioj/miniconda3/envs/job-profiler-model:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main
_openmp_mutex             5.1                       1_gnu
aiohappyeyeballs          2.4.3                    pypi_0    pypi
aiohttp                   3.11.7                   pypi_0    pypi
aiosignal                 1.3.1                    pypi_0    pypi
async-timeout             5.0.1                    pypi_0    pypi
attrs                     24.2.0                   pypi_0    pypi
ca-certificates           2024.9.24            h06a4308_0
certifi                   2024.8.30                pypi_0    pypi
charset-normalizer        3.4.0                    pypi_0    pypi
filelock                  3.16.1                   pypi_0    pypi
frozenlist                1.5.0                    pypi_0    pypi
fsspec                    2024.10.0                pypi_0    pypi
greenlet                  3.1.1                    pypi_0    pypi
huggingface-hub           0.26.2                   pypi_0    pypi
```

### Create, Activate and Use Your First Python Environment

1. Open your terminal window with conda base activated or Anaconda Prompt and open this folder (named python). As for example:

```
(base) dpalacioj@COL-LT-241007D:/mnt/c/Users/david.palacio$ cd Documents/projects
```
2.  Create a new environment named "test_env" that contains Python3.10:
```
conda create --name test_env python=3.10
```
3. Activate your environmet
```
conda activate test_env
```
4. Install numpy:
```
pip install numpy
```
5. Verify installation of numpy:
```
pip list
```
After that you must see numpy listed as an installed package.

6. Install all the packages listed on the file `test_requirements.txt`
```
pip install -r test_requirements.txt
```

After that you must see all the packages on such a file listed as an installed package.


# Approach 2: Setting Up a Development Environment with `.venv` from Scratch

This guide will take you step-by-step through setting up a Python environment on your computer using `.venv`. It’s designed for a brand-new computer and beginners who want to work on Python projects.
---

## **Step 1: Download and Install Python**

1. **Download Python:**
   - Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Download the latest stable version of Python for your operating system (Windows, macOS, or Linux).

2. **Install Python:**
   - During installation, make sure to select the option **"Add Python to PATH"** so Python can be accessed from the terminal.
   - Proceed with the default installation options.

3. **Verify the installation:**
   - Open your terminal or command prompt.
   - Run the following command:
     ```bash
     python --version
     ```
     You should see something like `Python 3.x.x`.

---

## **Step 2: Set Up a Virtual Environment with `.venv`**

A virtual environment isolates your project’s dependencies, avoiding conflicts with other projects on your machine.

1. **Create a folder for your project:**
   - In the terminal, navigate to the location where you want to store your project and create a folder:
     ```bash
     mkdir my_project
     cd my_project
     ```

2. **Create the virtual environment:**
   - Use the following command to create a virtual environment inside your project folder:
     ```bash
     python -m venv .venv
     ```

3. **Activate the virtual environment:**
   - Depending on your operating system, run:
     - **Windows:**
       ```bash
       .venv\Scripts\activate
       ```
     - **macOS/Linux:**
       ```bash
       source .venv/bin/activate
       ```

   - Once activated, you will see the virtual environment name at the beginning of your terminal line, like this:
     ```bash
     (.venv) C:\my_project>
     ```

4. **Update `pip` and basic tools:**
   - After activating the environment, update the default tools:
     ```bash
     pip install --upgrade pip setuptools wheel
     ```

---

## **Step 3: Install Project Dependencies**

1. **Create a `requirements.txt` file (optional):**
   - If your project requires specific packages, create a file called `requirements.txt` and list the packages there. Example:
     ```
     numpy==1.23.5
     pandas==1.5.3
     ```

2. **Install packages from `requirements.txt`:**
   - Use the following command:
     ```bash
     pip install -r requirements.txt
     ```

3. **Manually install packages:**
   - If you need to install a specific package, use:
     ```bash
     pip install <package_name>
     ```

---


## **Step 4: Deactivate the Virtual Environment**

- When you finish working, deactivate the environment by running:
    ```bash
  deactivate
    ```

## **Step 5: Reactivate the Virtual Environment in the Future**

- To work on you project again, navigate to the project folder and activate the virtual environment:

     - **Windows:**
       ```bash
       .venv\Scripts\activate
       ```
     - **macOS/Linux:**
       ```bash
       source .venv/bin/activate
       ```

## Troubleshooting Common Issues

### Python is not recognized:
1. Ensure you selected the "Add Python to PATH" option during the installation.

2. Verify Python is in your system’s PATH by running the following command:

    - On Windows:
        ```bash
        where python
        ```
    - On macOS/Linux:
        ```bash
        which python
        ```

If you encounter problems running scripts, ensure the files have execution permissions by running:
        ```bash
        chmod +x .venv/bin/activate
        ```

## .venv Summary

![Common Commands Reference for venv](/images/CommonCommandsReference-venv.png)


After that you must see all the packages on such a file listed as an installed package.

## VS Code Extensions

Our preferred IDE is Visual Studio Code (VS Code). To enable Python development effectively, we recommend installing specific extensions:


1.Python (mandatory):  The Python extension, developed and maintained by Microsoft, is essential for executing Python code in VS Code. It will automatically install the [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension, enriching your coding experience with rich type information and enhancing code-writing efficiency.


1. The following are optional extensions that you can install to make easier your experience while working with python. Furthermore,It could enhance the quality of your python developments.
   - [autoDocstring - Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring): It will help you to create automatically the docstring snippet including the datatype of your parameters and output function through pep484 type hints, default values, and var names.
   - [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8): It is a powerful linter that will help you to follow a code style guide, like [PEP8](https://peps.python.org/pep-0008/), and when you do not follow any of this guidelines, it will be shown on the PROBLEMS tab of the VS Code terminal.

   - [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter): This extension will help you to automatically format your code according some code style guideline.

   - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter): It provides Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.

## Quick Exercise

The ptyhon script ```test_installation.py``` was created with a lot of style code issues. Then, the challenge for you, if you decide to accept it is:

1. Create a copy of the file  ```test_installation.py``` and rename it with ```test_installation_namually_edited.py```.
2. Make all the necessary changes to this file until you do not have any problem at the ```PROBLEMS``` tab related to this file.
3. If you installed the black extension, format the file ```test_installation.py``` using such extension. To use this extension follow the next steps:
   1.  Open the file  ```test_installation.py```
   2.  Right click -> Format Document With
   3.  Select Black Formatter
   4.  Optional: If you want you can configure `Black` as your default Formatter so that the next time you require to format a file with Black, only have to do: `Right click -> Format Document`.
   5.  It is possible that after have formatted your file with Black remain some code style issues. In that case, make all the necessary changes to this file until you do not have any problem at the ```PROBLEMS``` tab related to this file.


# Python Refresher

As each newly hired AI Engineer comes from diverse backgrounds and job experiences, there is a possibility that you may seek to enhance your skills and familiarize yourself with Python and/or programming concepts and tools commonly utilized in this role. This endeavor would undoubtedly improve the quality of your work. Therefore, I have meticulously curated a list of valuable links that offer concise and efficient resources for each topic, enabling you to accelerate your learning process.

Please feel at liberty to bypass topics in which you possess ample experience, or delve into more comprehensive tutorials, documents, and articles to attain a deeper understanding of any subject you desire to master. Your autonomy in selecting the most suitable learning path is encouraged to foster your professional growth and expertise.

## General Python

### Basic
1. Write Best Functions in Python: As functions is at the core of any python program and whether you write great or bad functions can be the difference between a success or a failed project, we encurage you to check you are comfortable with all the concepts revisted in the following tutorial splitted into seven parts.

   1. [Do you know all your functions terminology well?](https://thepythoncodingbook.com/2022/11/05/intermediate-python-functions-series-1/)
   2. [Choosing whether to use positional or keyword arguments when calling a function](https://thepythoncodingbook.com/2022/11/11/positional-arguments-and-keyword-arguments-in-python/)
   3. [Using optional arguments by including default values when defining a function](https://thepythoncodingbook.com/2022/11/23/optional-arguments-with-default-values-in-python-functions/)
   4. [Using any number of optional positional and keyword arguments: `*args` and `**kwargs`](https://thepythoncodingbook.com/2022/11/30/what-are-args-and-kwargs-in-python/)
   5. [Using positional-only arguments and keyword-only arguments: the “rogue” forward slash / or asterisk * in function signatures](https://thepythoncodingbook.com/2022/12/11/positional-only-and-keyword-only-arguments-in-python/)
   6. [Type hinting in functions](https://thepythoncodingbook.com/2022/12/27/type-hints-in-python-functions/)
   7. [Best practices when defining and using functions](https://thepythoncodingbook.com/2023/01/18/best-practices-in-python-functions/)
2. **Challenge**: Create some simple functions, around $5$, applying all the concepts of the above series of articles.
3. Write a README.MD describing crearly your solution.

### Intermediate
1. **Object Oriented Programming (OOP)**
   1. [Python Classes: The Power of Object-Oriented Programming](https://realpython.com/python-classes/): It is an article to learn all the basics of OOP in Python as well as part of some OOP intermediate concepts. 
   2. [Getters and Setters: Manage Attributes in Python](https://realpython.com/python-getter-setter/): Getters and Setters are methods of a (python)class commonly used in every python program that allow you to access and mutate private attributes while maintaining encapsulation. 
   3. [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/):  They  are two important concepts in object oriented programming that model the relationship between two classes. Also they are the building blocks of object oriented design, and they help programmers to write reusable code. In AI it appears in a natural way when you want to create your custom objects based on Base classes of popular libraries like Tensorflow or Scikit-Learn.
   4. [Implementing an Interface in Python
](https://realpython.com/python-interface/): Interfaces play an important role in software engineering. As an application grows, updates and changes to the code base become more difficult to manage. In this tutorial, you’ll see how you can use a Python interface to help determine what class you should use to tackle the current problem.


2. **Unit Testing**: Unit testing is a method for testing software that looks at the smallest testable pieces of code, called units, which are tested for correct operation. By doing unit testing, we can verify that each part of the code, including helper functions that may not be exposed to the user, works correctly and as intended. 
   1. [A Beginner’s Guide to Unit Tests in Python (2023)
 ](https://www.dataquest.io/blog/unit-tests-python/): A first lecture about what unit tests are, how to write them and why it is important to have unit test in our programs.
   2. [A Gentle Introduction to Unit Testing in Python
](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/): This tutorial is created by *Machine Learning Mastery* and contains both general python functions and data related functions.
   3. [Effective Python Testing With Pytest
](https://realpython.com/pytest-python-testing/): This is a guide that will you to leverage of the powerful features that [Pytest](https://docs.pytest.org/en/7.4.x/) has to offer.
   4. [Testing Machine Learning Systems: Unit Tests
](https://medium.com/pykes-technical-notes/testing-machine-learning-systems-unit-tests-38696264ee04)
1. **Challenge**: Now it is time to put in practice what you should know at this point.
   1. Choose any dataset that you want in order to train either a regression or a classification model.
   2. Use the [base classes](https://scikit-learn.org/stable/modules/classes.html#base-classes) of Scikit-Learn to create custom preprocessing classes that you want to apply to your dataset.
   3.  Use the [base classes](https://scikit-learn.org/stable/modules/classes.html#base-classes) of Scikit-Learn to create custom models classes.
   4.  Create unit test by using the [Pytest](https://docs.pytest.org/en/7.4.x/) library foe each of the classes and fuctions that you have written.
   5.  Run all the test and make sure all of them have passed sucessfully.
   6.  Preprocess the data and train the model using your custom classes you have created.
   7.  **HINT:** Ask your self which are the mandatory methods that a preprocessing and/or an estimator (model) class must have?. Look at the source code of some preprocessing and estimator concrete classes of scikit-learn and see how they are created.
   8.  Write a README.MD describing crearly your solution.
### Advanced

1. Decorators
   1. [Primer on Python Decorators:](https://realpython.com/primer-on-python-decorators/)
2. [Pydantic:](https://www.youtube.com/watch?v=Vj-iU-8_xLs) It stands as the preeminent data validation library in the Python ecosystem, revered for its widespread adoption and versatile capabilities. Its significance becomes profoundly evident when embarking on the creation of your custom REST API utilizing FastAPI, as the latter was meticulously constructed on top of Pydantic. Embracing Pydantic empowers developers to ensure data integrity, streamline validation processes, and foster robustness in their API development endeavors.
3. **Web Development:** AS a *AI Engineer* your expertise may lean more towards AI and machine learning, rather than traditional software development. Consequently, when tasked with creating backend and/or frontend APIs to serve your AI models, you might encounter challenges.  Fortunately, there exists a couple of tools that came to help you out create end-to-end *AI* applications in a easy but professional manner.
By the way, FAST API was created, and still mantained, by the Colombian Software Engineer, [Sebastian Ramirez](https://linkedin.com/in/tiangolo). Furthermore, FastAPI has became in one the most popular Web-Frameworks around the world, according to the [2023 Developer Survey](https://survey.stackoverflow.co/2023/#section-admired-and-desired-web-frameworks-and-technologies) by Stack Overflow.

   1. [Fast API: Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
   2. [Streamlit:](https://docs.streamlit.io/library/get-started/create-an-app) Create your first frontend app by using the simplicity if streamlit. It will be helpful to present demos and results without having to create complext and time consuming JS programs, and the most important, using only your python knowlegde.
1. **Challenge:** Use this [article](https://rihab-feki.medium.com/deploying-machine-learning-models-with-streamlit-fastapi-and-docker-bb16bbf8eb91) as an step-by-step guide to create an end-to-end ML application with your own models and datasets. The app created must acomplish the following goals.
   1. Implement all the functionalities the guide already has but adapt it to your needs.
   2. Test every function that you have created.
   3. Add at least three more features different than implemented already by the guide.
   4. Write a README.MD documenting crearly each part of your solution.
   5. Create a diagram of the arquitecture of the solution.