import json
import csv
import requests
import collections

def main():
    output_path = "outputs"
    output_file = "mds_results.json"
    mds_results = query_mds()
    #clean_mds_results = transform_mds_dict(mds_results)

    # Export to JSON
    with open(f"{output_path}/{output_file}", "w") as stream:
        json.dump(mds_results,indent=2,fp=stream)

def query_mds():

    # Request Details (hardcoded for now)
    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
        }
    base_url = "https://gen3.biodatacatalyst.nhlbi.nih.gov/mds"
    endpoint = "metadata"  
    guid_type = "discovery_metadata"
    return_data = "true"
    limit = 2000

    request_url = f"{base_url}/{endpoint}?_guid_type={guid_type}&limit={limit}&data={return_data}"
    
    # Request Object:
    req = requests.request(method = "GET",
                        url = request_url,
                        headers = headers)
        
    # What happens when we fail
    if req.status_code is not 200:
        print("Issue with API call. Contact Gen3")

    results_obj = req.json()
        
    return(results_obj)

def transform_mds_dict(mds_result):
    # Do some transformations
    return(mds_results)

if __name__ == "__main__":
    main()