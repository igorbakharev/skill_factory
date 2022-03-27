# Project 1. Guess a number from 1 to 100 in less than 20 attempts

<a id='Content'></a>
## Content
[1. Project description](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Project-description)

[2. Quality assessment](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Quality-assessment)

[3. Personal goals](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Personal-goals)

[4. Method description](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Method-description)

[5. Results](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Results)

[6. Conclusions](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Conclusions)

[7. Code reproducibility](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Code-reproducibility)

<a id='Project-description'></a>
## 1. Project description
The goal is to find an integer guessed by the computer using less than 20 attempts.
* The computer guesses an integer from 1 to 100 to be found.
* The algorithm takes into account information if the random number is less than or greater than the required number.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Content)

<a id='Quality-assessment'></a>
## 2. Quality assessment
The results are evaluated by the average number of attempts per 1000 repetitions. The goal is to get the minimum number of attempts.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Content)

<a id='Personal-goals'></a>
## 3. Personal goals
* Create a nice Python code
* Learning the IDE
* Exploring GitHub

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Content)

<a id='Method-description'></a>
## 4. Method description
The median of the range of integers from 1 to 100 is 50. This should be the first guess. If we're less than that number, our next guess will be 25. Keep guessing halfway and we'll get the correct number in less than 8 attempts.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Content)

<a id='Results'></a>
## 5. Results
Using the *score_game* function from the Skill Factory PYTHON-8 unit, which takes 1000 iterations to evaluate the performance of the modified *random_predict* function, it was found that the updated algorithm needs an average of **5 attempts** to find the guessed number that is lower than 20.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Content)

<a id='Conclusions'></a>
## 6. Conclusions
The use of a mathematical "half-cut" algorithm with the information that the random number is greater or less than the one guessed has reduced the number of attempts from 101 to 5 in average.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Content)

<a id='Code-reproducibility'></a>
## 7. Code reproducibility
To be sure that the code can be anytime reproduced, the libraries versions are fixed in the *requirements.txt* file. To transfer these versions to another computer, use the **pip install -r requirements.txt** command.

:arrow_up:[Back to content](https://github.com/igorbakharev/skill_factory/tree/main/project_1/README.md#Content)