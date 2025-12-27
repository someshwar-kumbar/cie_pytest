import pytest
from vehical import vehical_info
def test_vhical_info():
    output=(
        "pid=1234"
        "bname=bmw"
        "price=15000000"
        "yop=2025"
    )
    assert vehical_info(1234,"bmw",15000000,2025)==output
