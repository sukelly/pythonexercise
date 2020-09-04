# Dependencies:

1. Python3

# Run program using cli 

1. `$ git clone https://github.com/sukelly/pythonexercise.git`
2. `$ cd pythonexercise`
3. `$ python3 main.py --items <json_file> --cart <cart_items>`

parameters: 
 - cart_items: string
 - json_file: path to .json file
 
# Run all tests

1. `$ python3 test_module.py`

Note: Examples included in instruction are included in test_module.py

# Usage
## json_file schema:
```
[
    {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "cost": {"type": "number"},
            "discount": {
                "type": "object",
                "properties": {
                    "quantity": {"type": "number"},
                    "cost": {"type": "number"}
                },
                "required": ["quantity", "cost"]
            }
        "required": ["id", "name", "cost"]
    }
]
```

See samples/groceryItems.json for an example

# Example run:

```
$ python3 main.py --items samples/groceryItems.json --cart "ABCD"
```
