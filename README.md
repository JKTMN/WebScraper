# Web Scraper 

- webcrawler.py: This project contains a web scraper & crawler which takes a link from the user and collects all email addresses on the page and stores them in a json file.
The crawler will then alter the URL of the website to navigate through pagination.
It is currently hard coded to stop after 35 pages.

- findCourses.py: This project scrapes through the Bournemouth University Website and completes 1 of 4 tasks:
-  1 Scrapes and returns every course provided by Bournemouth University.
-  2 Scrapes and returns every academic department at Bournemouth University
-  3 Scrapes and returns all of the courses tied to a pre determined academic department
-  4 Scrapes and returns all of the courses tied to an academic department which the user can input


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

This project requires a few external dependencies which can be installed using the follow commands:
- **pip install selenium**
- **pip install beautifulsoup4**
- **pip install validate_email**

## Usage

- findCourses.py: Uncomment the function you would like to run and run the python file, if you are running the pre determined department, make sure to change the department to your use

- webCrawler.py: Create a json file called **"emailADdresses.json"** Run the python file and enter the target URL. If you would like to change the amount of pages it searches through. Change **"if self.pagesOpened >= 35:"** (located on **line 33**, within the **click_next_page()** function) to your desired amount.

## Contributing

You are welcome to make changes however you see fit, however ensure your **output json file** is **included** within **".gitignore"**

## License

This project is licensed under the [MIT License](LICENSE) - see [LICENSE](LICENSE) file for details.
