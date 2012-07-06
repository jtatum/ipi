Feature: Parse filenames
    Given various filenames,
    ipi should correctly parse out the package and version numbers

    Scenario: Simple filename
        Given the filename BeautifulSoup-3.2.1.tar.gz
        When I parse the filename
        Then the package is BeautifulSoup
        And the version is 3.2.1

    Scenario: Dashed packagename
        Given the filename package-a-1.0.tar.gz
        When I parse the filename
        Then the package is package-a
        And the version is 1.0
