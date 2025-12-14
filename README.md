## Perion - Automation Home Test ##

This project contains UI automation test and manual test cases.
The tests are written in Python using Behave (BDD) and Selenium WebDriver, and follow the Page Object Model (POM).

## Instructions ## 
1. Clone the repository:
     * bash `git clone https://github.com/GaliGit2/Perion-HomeTest.git`
2. Install dependencies (Local Run):
     * pip install -r requirements.txt
3. Run tests locally (visible browser)
     * behave -f pretty
4. Run tests headless (Local)
     * $env:HEADLESS="true"
       behave -f pretty 
5. Build and run with Docker (headless by default)
     * docker build -t behave-tests . 
       docker run --rm behave-tests
6. Run Docker and save screenshots
     * docker run --rm `
       -v ${PWD}\screenshots:/app/screenshots `
       behave-tests
7. Generate HTML report
     * docker run --rm `
       -v ${PWD}\reports:/app/reports `
       behave-tests behave -f behave_html_formatter:HTMLFormatter -o reports/report.html
8. Notes
     * Locked-out user negative login scenario is covered as part of the Login feature.
     * Step definitions are located under features/steps/ as required by Behave conventions.
     * Checkout with empty is not preventing by the system 
       The negative test validates that no items exist in the checkout summary, rather than expecting a UI block.
