import unittest
import requests
import json
import time

class TestStringMethods(unittest.TestCase):
    
    def test_del_not_real(self):
        s = requests.session()
        data = {"key": "sfs"}
        data = json.dumps(data)
        req = s.delete(cur_adr + '/delete', data = data)
        self.assertEqual(json.loads(req.text)["status"], 'Not Found')
    
    def test_bad_put(self):
        s = requests.session()
        data = {
            "key": "test"
            }
        data = json.dumps(data)
        req = s.put(cur_adr + '/put', data = data)
        self.assertEqual(req.status_code, 404)
    
    def test_good_put(self):
        s = requests.session()
        data = {
            "key": "test",
            "message": "1"
        }
        data = json.dumps(data)
        req = s.put(cur_adr + '/put', data = data)
        self.assertEqual(json.loads(req.text)["status"], 'Create')
            
    def test_del_real(self):
        s = requests.session()
        data = {"key": "test"}
        data = json.dumps(data)
        req = s.delete(cur_adr + '/delete', data = data)
        self.assertEqual(json.loads(req.text)["status"], 'OK')

    # Выше добавил тесты более простых случаев...Не вижу смысла избавляться от старых тестов, которые ниже, плюс два из трех тестов выше тестируют "плохие" случаи
    
    def test_put_and_get(self):
        s = requests.session()
        data = {
            "key": "sfs",
            "message": "1"
                }
        data = json.dumps(data)
        req = s.put(cur_adr + '/put', data = data)
        data = {"key": "sfs"}
        data = json.dumps(data)
        req1 = s.get(cur_adr + '/get', data = data)
        self.assertEqual(json.loads(req1.text)["message"], '1')

    def test_put_del(self):
        s = requests.session()
        data = {
            "key": "sfs",
            "message": "1"
            }
        data = json.dumps(data)
        req = s.put(cur_adr + '/put', data = data)
        data = {"key": "sfs"}
        data = json.dumps(data)
        req1 = s.delete(cur_adr + '/delete', data = data)
        self.assertEqual(json.loads(req1.text)['status'], 'OK')

if __name__ == '__main__':
    time.sleep(3)
#    f = open('ip.txt') #беру ip внутри контейнера
#    host_ip = f.read()
    cur_adr = 'http://172.25.0.3:65430/'
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
