import os
from ipaddress import IPv4Network
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


@pytest.fixture(scope='module')
def ranges(json_file):
    return parse_ipv4_service_ranges(json_file)


def test_raises(ranges):
    with pytest.raises(ValueError) as excinfo:
        get_aws_service_range(ranges, '256.256.256.256')
    assert "maximum recursion" in str(excinfo.value)


def test_get_aws_service_range(ranges):
    assert [] == get_aws_service_range('67.10.12.2', ranges)
    assert [[ServiceIPRange(service='AMAZON', region='ap-east-1',
                            cidr=IPv4Network('54.240.17.0/24')),
             ServiceIPRange(service='EC2', region='ap-east-1',
                            cidr=IPv4Network('54.240.17.0/24'))]] == (
               get_aws_service_range('54.240.17.255', ranges))

    network = "IPv4Network('54.240.17.0/24')"
    service = "AMAZON"
    region = "ap-east-1"
    exp_out = f"{network} is allocated to the {service} " \
              f"service in the {region} region"
    assert exp_out == str(get_aws_service_range('54.240.17.255', ranges)[0])
