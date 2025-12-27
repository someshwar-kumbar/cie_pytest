from vehical import vehical_info
def test_vhical_info(pid,bname,price,yop):
    output=(
        "pid=1234\n"
        "bname=bmw\n"
        "price=15000000\n"
        "yop=2025"
    )
    assert vehical_info(1234,"bmw",15000000,2025)==output
