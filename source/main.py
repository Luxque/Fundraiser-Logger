import scraper, output


if __name__ == '__main__':
    id = input("Enter the Project ID: ")
    data = scraper.getProgress(id)
    output.printData(data)