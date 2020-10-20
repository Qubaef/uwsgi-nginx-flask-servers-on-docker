from .models import ChatTableModel

class ChatService:
    def __init__(self):
        self.model = ChatTableModel()

    # create new element from fiven params
    def create(self, params):
        return self.model.create(params)

    # delete element by id
    def delete(self, item_id):
        return self.model.delete(item_id)

    # get list of all elements
    def list(self):
        response = self.model.list_items()
        return response