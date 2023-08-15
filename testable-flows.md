(Add your list of flows here)

# Acceptance Criteria

| Acceptance criteria ID | Acceptance Criteria Description                                                                                                                                                                                                                                                                                                              |
|:----------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           1            | The UI consists of a header, a search form and a search result section                                                                                                                                                                                                                                                                       |
|           2            | The header displays the title of the app                                                                                                                                                                                                                                                                                                     |
|           3            | The search form accepts a text input as a search term. Search is activated by clicking the "Go" button, or by pressing the "Enter" key                                                                                                                                                                                                       |
|           4            | For each repo found, the search result section displays a row with basic info about that repo: name and description. Clicking on the repo name takes the user to the repo's URL. In case of a missing value, – is displayed                                                                                                                  |
|           5            | The user sees feedback about the result of the search action. Either a success or error message are shown above the search field at the completion of a search action, for a short amount of time. If the error is due to a user not found on Github, a specific error message is displayed. Otherwise, a generic error message is displayed |


# **Test cases**

| TC ID | AC ID         | TITLE                                   | PC               | DATA                      | STEPS                                                                                                                                                                               | EXPECTED                                                                                                                                                                                                                                       | ACTUAL | AUTO | STATUS |
|:-----:|---------------|-----------------------------------------|------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|--------|
|   1   | AC1, AC2      | Verify UI initial state                 | User on website  | N/A                       | Navigate to initial page                                                                                                                                                            | 1. Page should have:<br/>1.1 A header<br/>1.2 A search form<br/>1.3 A search result section<br/>2.The content of the header should be equal to the page title<br/>3. On the results section, there should be a text "No repos" being displayed |        |      |        |
|   2   | AC3           | Verify search input trigger behavior    | User on website  | usernames: gbl3, testname | 1. Click on the search input to get focus<br/>2. Type the first username<br/>3. Press enter<br/>4. Refresh the page<br/>5. Type the second username<br/>6. Click on the "Go" button | 1. After steps 3, search should be triggered.<br/>2. After step 4, results from previous search should be cleared.<br/>3. After step 6, search should be triggered.                                                                            |        |      |        |
|   3   | AC3, AC4, AC5 | Try to search using an invalid username | User on website  | username: @@@             |                                                                                                                                                                                     |                                                                                                                                                                                                                                                |        |      |        |
|   4   |               |                                         |                  |                           |                                                                                                                                                                                     |                                                                                                                                                                                                                                                |        |      |        |
|   5   |               |                                         |                  |                           |                                                                                                                                                                                     |                                                                                                                                                                                                                                                |        |      |        |




tc id,  
ac,  
title,  
pre conditions,  
data,  
steps,  
expected result,   
actual result,  
automated or not,  
exec status