import json
class Request:
    def __init__(self, request_text):
      self.parse_request(request_text.recv(1024).decode('utf-8').split('\r\n'))

    def parse_request(self, request_as_list):
      if request_as_list[0].split(' ')[0] == 'POST':
        post_content = json.loads(request_as_list[10])
        self.parsed_request = {
          'method': request_as_list[0].split(' ')[0],
          'uri': request_as_list[0].split(' ')[1],
          'author': post_content['author'],
          'title': post_content['title'],
          'content': post_content['content']
        }
      else :
        self.parsed_request = {
          'method': request_as_list[0].split(' ')[0],
          'uri': request_as_list[0].split(' ')[1]
        }
