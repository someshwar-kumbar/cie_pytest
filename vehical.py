def vehical_info(pid, bname, price, yop):
    result = (
        f"pid:{pid}"
        f"bname:{bname}"
        f"price:{price}"
        f"yop:{yop}"
    )
    return result
if __name__ == "__main__":
    print(vehical_info(1234,"bmw",15000000,2025))
