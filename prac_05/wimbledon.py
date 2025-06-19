"""
wimbledon
Estimate: 35 minutes
Actual:   minutes
"""



def read_wimbledon_file(file):
    """read the file and extract the champion and country """
    data=[]
    with open(filename,"r",encoding="utf-8-sig") as file:
        for line in file:
            parts=line.strip().split(",")
            champion=parts[2]
            country=parts[1]
            data.append([champion,country])
    return data