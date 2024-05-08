#dictionary
dict_of_cloud = {
    "AWS":"Amazon Web Services",
    "GCP": "Google Cloud Platform",
    "Azure": "Microsft Azure"
}


print(dict_of_cloud.get('vmware',"Not found" ))

dict_of_cloud.update({"DG":"Digital Ocean"})

print(dict_of_cloud)