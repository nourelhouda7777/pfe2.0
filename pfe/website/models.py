from py2neo import Graph, Node,Relationship

graph = Graph("http://localhost:7475", auth=("neo4jjj", "optimal-student-collect-road-peace-738"),name="neo4j")
# graph  = Graph("http://localhost:____", auth = ("neo4j", "password"), name="neo4j")
class doctor:
    def __init__(self,nom):
      self.nom = nom
    def find(key, values):
      label = "doctor"
      property_key = key
      property_value = values
      node = graph.nodes.match(label, **{property_key: property_value}).first()
      if node:
         return True
      else:
         return False
    
class patient:
        def find(key, values):
          label = "patient"
          property_key = key
          property_value = values
          node = graph.nodes.match(label, **{property_key: property_value}).first()
          if node:
            return True
          else:
            return False
        def create(n,p,d,f,g):
          label = "patient"
          a= Node(label,nom=n,foction=f,sex="sex",numero="0000000",email="email.patient@gmail.com",prenom=p,adress="Béjaïa",date_naiss=d,groupage=g)
          node = graph.create(a)
          if graph.exists(a):
              return True
          else:
              return False
# <elementId>: 4:626af745-1916-485b-8e02-e671b188de43:14
# <id>: 14
# adress: Béjaïa
# date_naiss:  3/2/1988
# email: yasmina.touati@email.com
# foction:  Infirmière
# groupage: O-
# nom: Yasmina
# numero: 05678901
# prenom: Touati
# sex: F