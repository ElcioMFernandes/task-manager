# Bibliotecas nativas
import os
import throw

# Bibliotecas externas
try:
    import dotenv 
    import pymongo

    try:
        dotenv.load_dotenv()

    except Exception as e:
        throw.error(code="0002", additional_message=e)

except Exception as e:
    throw.error(code="0001", additional_message=e)

class Mongo:
    def __init__(self) -> None:
        try: 
            self.__URI = str(os.getenv('URI_MONGO')) # Definindo a URI do banco de dados
            self.__client = pymongo.MongoClient(self.__URI) # Criação do cliente MongoDB
            self.__db = self.__client[str(os.getenv('BASE_NAME'))] # Acesso a um banco de dados específico
            self.__collection = self.__db['COLL_NAME'] # Acesso a uma coleção específica dentro do banco de dados

        except Exception as e:
            throw.error(code="0003", additional_message=e)

    def __close_client(self):
        self.__client.close() # Fechar a conexão

# Inserção de Documentos

# insert_one(document): Insere um único documento na coleção.
    def insert_one(self, data): #
        self.__collection.insert_one(data)

# insert_many(documents): Insere múltiplos documentos na coleção.

# Leitura de Documentos

# find(filter, projection): Retorna um cursor para os documentos que correspondem ao filtro. Se nenhum filtro for fornecido, retorna todos os documentos.
# find_one(filter, projection): Retorna um único documento que corresponde ao filtro. Se nenhum filtro for fornecido, retorna o primeiro documento na coleção.
# find_one_and_replace(filter, replacement): Substitui um único documento que corresponde ao filtro e retorna o documento antigo.
# find_one_and_update(filter, update): Atualiza um único documento que corresponde ao filtro e retorna o documento antigo.
# find_one_and_delete(filter): Deleta um único documento que corresponde ao filtro e retorna o documento deletado.

# Atualização de Documentos

# update_one(filter, update): Atualiza um único documento que corresponde ao filtro.
# update_many(filter, update): Atualiza múltiplos documentos que correspondem ao filtro.

# Remoção de Documentos

# delete_one(filter): Deleta um único documento que corresponde ao filtro.
# delete_many(filter): Deleta múltiplos documentos que correspondem ao filtro.

# Contagem e Agregação

# count_documents(filter): Retorna a contagem de documentos que correspondem ao filtro.
# estimated_document_count(): Retorna uma estimativa da contagem de documentos na coleção.
# aggregate(pipeline): Realiza operações de agregação na coleção.

# Indexação

# create_index(keys, **kwargs): Cria um índice na coleção.
# create_indexes(indexes): Cria múltiplos índices na coleção.
# list_indexes(): Lista todos os índices da coleção.
# drop_index(index_or_name): Remove um índice da coleção.
# drop_indexes(): Remove todos os índices da coleção.

# Outros Métodos Úteis

# distinct(key, filter): Retorna uma lista de valores distintos para um campo especificado.
# bulk_write(requests): Realiza operações de escrita em lote.
# rename(new_name): Renomeia a coleção.
# drop(): Remove a coleção do banco de dados.