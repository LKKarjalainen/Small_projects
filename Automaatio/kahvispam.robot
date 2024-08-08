*** Settings ***
Documentation	Kahvi.cafe button spammer
Library		SeleniumLibrary
Library    	.venv/lib/python3.11/site-packages/robot/libraries/Collections.py


*** Variables ***
${web_site} =    	https:/kattila.cafe/
${id} =    		    painike


*** Keywords ***
Press the button
    FOR  ${i}    IN RANGE    1    10
        Click Button	painike
    END


*** Test Cases ***
Spam
    # Start a browser and navigate to the website.
    Open Browser    ${web_site}    Chrome
    
    ${halukkaat}    Get Text    id:halukkaat
    Log To Console    ${halukkaat}

    ${numero}    Evaluate    "${halukkaat}".split(":")[1].split(" ")[1]
    Log To Console    ${numero}

    IF    ${numero} != 10
       Press the button
    ELSE
        Log To Console    "Nyt on hyvä mieli, kun kaverin hieno painike ei ole hyödyllinen"
    END

    # Teardown
    Close Browser
