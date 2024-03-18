class PageElement:
    def __init__(self, element: dict):
        self.name = element.get("name")
        self.id = element.get("id")
        self.xpath = element.get("xpath")
