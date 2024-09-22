def __main__():
    def defangIPaddr(address: str) -> str:
        return address.replace(".", "[.]")

    print(defangIPaddr("192.168.1.1")) # "192[.]168[.]1[.]1"

if __name__ == "__main__":
    __main__()