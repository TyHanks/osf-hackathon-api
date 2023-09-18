import requests

class ExampleRequest:

    #-INFO- ::FUNCTION:: Example function for getting all data from file/api
    def get_data(self):
        response = requests.get('http://localhost:8080/api')
        return print("GET Response:", response.status_code, response.json())

    #-INFO- ::FUNCTION:: Example function for posting data to data.json file/api
    def post_data(self):
        data_to_post = {"type": "post", "title": "Post title one", "author": "john doe", "body": "body text one random post text"}
        response = requests.post('http://localhost:8080/api', json = data_to_post)
        return print("POST Response:", response.status_code, response.json())

    #-INFO- ::FUNCTION:: Example function for deleteing data from data.json file/api
    def delete_data(self):
        key_to_delete = 1
        response = requests.delete(f'http://localhost:8080/api/{key_to_delete}')
        return print("DELETE Response:", response.status_code, response.json())

#-!- Uncomment example below that you would like to test
#-INFO- data.json empty by default I would start with post other wise you will recieve {}   
test = ExampleRequest()

#-DATA- GET request example {} by default
#test.get_data()

#-DATA- POST request example can be modified for Posts or Comments based on needs
#test.post_data()

#-DATA- DELETE request uses key 1 by default can be modified to delete other keys in function
#test.delete_data()
