import unittest
import sys
import requests
import json
import os
import mysql.connector as mysql

HOST = os.environ["HVAC_HOST"]
TOKEN = os.environ["HVAC_TOKEN"]
TICKETS = os.environ["HVAC_TICKETS"]

class TestStringMethods(unittest.TestCase):

    def test_simulator_up(self):
        r = requests.get(f"{HOST}/api/health")
        self.assertEqual("All system operational Commander !", r.text)
    
    def test_turn_off_unit(self):
        r = requests.get(f"{HOST}/api/HVAC/{TOKEN}/TurnOffHvac")
        res_payload_dict = r.json()
        self.assertEqual("Turning off Hvac", res_payload_dict['Response'])

    def test_turn_on_AC(self):
        r = requests.get(f"{HOST}/api/HVAC/{TOKEN}/TurnOnAc/{TICKETS}")
        res_payload_dict = r.json()
        self.assertEqual(f"Activating AC for {TICKETS} ticks", res_payload_dict['Response'])
    
    def test_turn_on_Heater(self):
        r = requests.get(f"{HOST}/api/HVAC/{TOKEN}/TurnOnHeater/{TICKETS}")
        res_payload_dict = r.json()
        self.assertEqual(f"Activating Heater for {TICKETS} ticks", res_payload_dict['Response'])
    
    
if __name__ == '__main__':
    unittest.main()
