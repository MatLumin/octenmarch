
from typing import * 





def mash(data:Dict[str,Any])->str:
    output:str = str()
    for k, v in data.items():
        output += str(v)
    return output



if __name__ == "__main__":
    print(mash({"hello":1, "world":False, "ohno":"wat??"}))