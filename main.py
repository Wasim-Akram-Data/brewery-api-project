import requests
import pandas as pd

def fetch_breweries(state, brewery_type):

    url = f"https://api.openbrewerydb.org/v1/breweries?by_state=texas"

    try:
        print("\nFetching brewery data...\n")

        response = requests.get(url)

        response.raise_for_status()

        breweries = response.json()

        filtered_data = []

        for brewery in breweries:

            b_type = brewery.get("brewery_type", "N/A")

            if b_type.lower() == brewery_type.lower():

                brewery_info = {
                    "Name": brewery.get("name", "N/A"),
                    "Type": b_type,
                    "City": brewery.get("city", "N/A"),
                    "State": brewery.get("state", "N/A"),
                    "Website": brewery.get("website_url", "N/A")
                }

                filtered_data.append(brewery_info)

        if not filtered_data:
            print("No matching breweries found.")
            return

        # Display Data
        print(f"Total Breweries Found: {len(filtered_data)}\n")

        for brewery in filtered_data:

            print(f"Name    : {brewery['Name']}")
            print(f"Type    : {brewery['Type']}")
            print(f"City    : {brewery['City']}")
            print(f"Website : {brewery['Website']}")

            print("-" * 50)

        # Create DataFrame
        df = pd.DataFrame(filtered_data)

        # Save CSV
        file_name = f"{state}_breweries.csv"

        df.to_csv(file_name, index=False)

        print(f"\nCSV File Saved Successfully: {file_name}")

    except requests.exceptions.RequestException as e:
        print("API Request Failed")
        print(e)

    except Exception as e:
        print("Something went wrong")
        print(e)

# User Inputs
state = input("Enter US state name: ")
brewery_type = input("Enter brewery type (micro, nano, brewpub): ")

# Function Call
fetch_breweries(state, brewery_type)
