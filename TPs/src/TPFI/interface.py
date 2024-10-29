import uuid
from corporate_data import CorporateData


class Interface:
    def __init__(self, config_data):
        self.session_id = config_data.get("session_id", str(uuid.uuid4()))
        self.cpu_id = config_data.get("cpu_id", str(uuid.getnode()))
        self.id = config_data.get("id", "UADER-FCyT-IS2")
        self.corporate_data = CorporateData()

    def get_data(self):
        try:
            data_response = self.corporate_data.getData(
                self.session_id, self.cpu_id, self.id
            )
            return data_response
        except Exception as e:
            return {"error": f"Error al obtener datos: {str(e)}"}

    def get_cuit(self):
        try:
            cuit_response = self.corporate_data.getCUIT(
                self.session_id, self.cpu_id, self.id
            )
            return cuit_response
        except Exception as e:
            return {"error": f"Error al obtener CUIT: {str(e)}"}

    def get_seq_id(self):
        try:
            seq_id_response = self.corporate_data.getSeqID(
                self.session_id, self.cpu_id, self.id
            )
            return seq_id_response
        except Exception as e:
            return {"error": f"Error al obtener Seq ID: {str(e)}"}

    def list_corporate_data(self):
        try:
            data_list = self.corporate_data.listCorporateData(self.id)
            return data_list
        except Exception as e:
            return {"error": f"Error al listar datos corporativos: {str(e)}"}

    def list_corporate_log(self):
        try:
            log_list = self.corporate_data.listCorporateLog(self.cpu_id)
            return log_list
        except Exception as e:
            return {"error": f"Error al listar logs corporativos: {str(e)}"}
