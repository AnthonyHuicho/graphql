from ariadne import QueryType, make_executable_schema, gql
from ariadne.asgi import GraphQL
import uvicorn


type_defs = gql("""
    type Query {
        hello: String
        nombre: String
        alumno(id: ID!): Alumno
    }

    type Alumno {
        id: ID!
        nombre: String!
        edad: Int!
    }
""")


query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hola, mundo !"

@query.field("nombre")
def resolve_nombre(_, info):
    return "Mi nombre es Pedrito ramirez"

@query.field("alumno")
def resolve_alumno(_, info, id):
    return {
        "id": id,
        "nombre": "Alan chavez",
        "edad": 19
    }

schema = make_executable_schema(type_defs, query)

app = GraphQL(schema, debug=True)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
