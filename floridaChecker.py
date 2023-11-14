# import selenium and itertools
from colorama import init, Fore
init(autoreset=True)

from itertools import product
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# license plate length to check for
plateLength = 2
# all possible license plate combinations
textFile = open(r'2_digit_license_list.txt', 'w')
li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', \
      'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
twoDigitCombs = ([''.join(comb) for comb in product(li, repeat=plateLength)])

validPlates =[]
DRIVER_PATH = "PATH-TO-CHROME-DRIVER"
options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get('https://services.flhsmv.gov/MVCheckPersonalPlate/')
# Get user info
count = 0
while count <= (35**plateLength):

    plate1 = twoDigitCombs[(0 + count)]
    plate2 = twoDigitCombs[(1 + count)]
    plate3 = twoDigitCombs[(2 + count)]
    plate4 = twoDigitCombs[(3 + count)]
    plate5 = twoDigitCombs[(4 + count)]
    count += 5

    # set webdriver path

    # find the 5 text input fields on flhsmv.gov

    rowOne = driver.find_element("id", "MainContent_txtInputRowOne")
    rowTwo = driver.find_element("id", "MainContent_txtInputRowTwo")
    rowThree = driver.find_element("id", "MainContent_txtInputRowThree")
    rowFour = driver.find_element("id", "MainContent_txtInputRowFour")
    rowFive = driver.find_element("id", "MainContent_txtInputRowFive")

    # enter in user data to 5 text fields
    rowOne.send_keys(plate1)
    rowTwo.send_keys(plate2)
    rowThree.send_keys(plate3)
    rowFour.send_keys(plate4)
    rowFive.send_keys(plate5)

    submitButton = driver.find_element("id", "MainContent_btnSubmit")
    driver.execute_script("arguments[0].click();", submitButton)

    # get the result of search for each plate
    rowOneResult = driver.find_elements("id", "MainContent_lblOutPutRowOne")
    rowTwoResult = driver.find_elements("id", "MainContent_lblOutPutRowTwo")
    rowThreeResult = driver.find_elements("id", "MainContent_lblOutputRowThree")
    rowFourResult = driver.find_elements("id", "MainContent_lblOutputRowFour")
    rowFiveResult = driver.find_elements("id", "MainContent_lblOutputRowFive")


    for element in rowOneResult:
        if element.text == "AVAILABLE":
            print(Fore.GREEN + plate1 + ": " + element.text,)
            validPlates.append(plate1)
        else:
            print(Fore.RED + plate1 + ": " + element.text)
    for element in rowTwoResult:
        if element.text == "AVAILABLE":
            print(Fore.GREEN + plate2 + ": " + element.text)
            validPlates.append(plate2)
        else:
            print(Fore.RED + plate2 + ": " + element.text)
    for element in rowThreeResult:
        if element.text == "AVAILABLE":
            print(Fore.GREEN + plate3 + ": " + element.text)
            validPlates.append(plate3)
        else:
            print(Fore.RED + plate3 + ": " + element.text)
    for element in rowFourResult:
        if element.text == "AVAILABLE":
            print(Fore.GREEN + plate4 + ": " + element.text)
            validPlates.append(plate4)
        else:
            print(Fore.RED + plate4 + ": " + element.text)
    for element in rowFiveResult:
        if element.text == "AVAILABLE":
            print(Fore.GREEN + plate5 + ": " + element.text)
            validPlates.append(plate5)
        else:
            print(Fore.RED + plate5 + ": " + element.text)

    clearButton = driver.find_element("id", "MainContent_btnClear")
    driver.execute_script("arguments[0].click();", clearButton)

    print("\nValid Plates Found: " + str(len(validPlates)))

print(validPlates)
textFile.write(str(validPlates))



