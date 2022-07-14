from demo.documents import CarDocument
def run():
    s = CarDocument.search().filter("term", color="测")
    print(s.to_queryset())
    s = CarDocument.search().filter("match", color="测试")
    print(s.to_queryset())
    s = CarDocument.search().query("match", description="测试")
    for hit in s:
        print(
            "Car name : {}, description {}".format(hit.name, hit.description)
        )