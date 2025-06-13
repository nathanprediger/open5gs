import pymongo
from bson import ObjectId
from bson import Int64

# Conexão com o servidor do MongoDB. Alterar a porta específica do serviço do MongoDB
client = pymongo.MongoClient("mongodb://localhost:63145/")

# Acessa a base de dados e seleciona a coleção
db = client["open5gs"]
collection = db["subscribers"]

# Define uma lista de documentos a ser passada para a base de dados posteriormente
documentos = []

# Define o valor inicial para o imsi
valor_inicial = "999700000000000"

# Define a quantidade de UEs que queira cadastrar
qtd_UE = 5000

# Cria os documentos 
for num_UE in range(qtd_UE):
    documento = {
    "imsi" : str(int(valor_inicial) + num_UE),
    "subscribed_rau_tau_timer" : int(12),
    "network_access_mode" : int(2),
    "subscriber_status" : int(0),
    "access_restriction_data" : int(32),
    "slice" : [
        {
            "sst" : int(1),
            "sd" : "000001",
            "default_indicator" : True,
            "session" : [
                {
                    "name" : "default",
                    "type" : int(3),
                    "pcc_rule" : [

                    ],
                    "ambr" : {
                        "uplink" : {
                            "value" : int(1),
                            "unit" : int(3)
                        },
                        "downlink" : {
                            "value" : int(1),
                            "unit" : int(3)
                        }
                    },
                    "qos" : {
                        "index" : int(9),
                        "arp" : {
                            "priority_level" : int(8),
                            "pre_emption_capability" : int(1),
                            "pre_emption_vulnerability" : int(1)
                        }
                    }
                }
            ]
        }
    ],
    "ambr" : {
        "uplink" : {
            "value" : int(1),
            "unit" : int(3)
        },
        "downlink" : {
            "value" : int(1),
            "unit" : int(3)
        }
    },
    "security" : {
        "k" : "465B5CE8B199B49FAA5F0A2EE238A6BC",
        "amf" : "8000",
        "op" : None,
        "opc" : "E8ED289DEBA952E4283B54E88E6183CA",
        "sqn" : int(32)
    },
    "msisdn": [],
    "schema_version" : int(1)
}
    documentos.append(documento)

# Insere todos os documentos na coleção
resultado = collection.insert_many(documentos)
