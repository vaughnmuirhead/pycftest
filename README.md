# pycftest
A package to assist with writing unit tests for Google Cloud Functions written in python.

## Disclaimer
At the moment, this is a very simple class I wrote to get me through an immediate issue I couldn't solve with a quick Google search. If this helps you I'm happy but use your own judgement in using this one.

## Contributing
If you find this useful or not useful enough and wish to contribute please do!

## Usage
Simply import this class and call the GetRequest method with a python dict containing your Cloud Function request payload.

The returned request object should be accepted as input for your cloud function.

See this in action below.

## Including in requirements.txt
You can add this package to your requirements.txt using the following syntax:

`git+git://github.com/vaughnmuirhead/pycftest@v0.4#egg=pycftest`


## Simple unit test example

```
import unittest
from pycftest import CFtest as cft
import main


class TestMain(unittest.TestCase):

    def test_hello_world(self):
        payload = {}
        request = cft.GetRequest(payload)
        response = main.hello_world(request)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
```
