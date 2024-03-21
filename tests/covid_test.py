import requests
from assertpy import assert_that
from lxml import etree


def test_covid_cases_have_crossed_a_million():
    response = requests.get('http://127.0.0.1:3000/api/v1/summary/latest')
    response_xml = response.text

    xml_tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
    total_cases = xml_tree.xpath("//data/summary/total_cases")[0].text
    assert_that(int(total_cases)).is_greater_than(1000000)





