*** Settings ***
Library    Browser
Library    lib/python3.10/site-packages/robot/libraries/Collections.py

*** Variables ***
${web_site} =    https:/freegogpcgames.com/
${class_name} =    entry-title

*** Test Cases ***
Get Text List of Elements with Class
    # Start a browser and navigate to the website.
    New Browser    chromium    headless=${True}
    New Context
    New Page    ${web_site}

    # Get all elements with a certain class.
    ${elements}    Get Elements    css=.${class_name}

    # Get the text of the element and add it to a list.
    ${text_list} =     Create List
    FOR    ${element}    IN    @{elements}
        ${text}    Get Text    ${element}
        Append To List    ${text_list}    ${text}
    END

    # For changing line before list of text.
    Log To Console    ''

    # Log the text from the list.
    FOR    ${text}    IN    @{text_list}
        Log To Console    ${text}
    END

    # Teardown
    Close Browser