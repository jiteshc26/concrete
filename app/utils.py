import pickle
import json
import numpy as np

class prediction():
    def __init__(self):
        pass

    def load_raw(self):
        with open(r"artifacts/concrete.pkl","rb") as model_file:
            self.model=pickle.load(model_file)

        with open(r"artifacts/column_names.json","r") as col_file:
            self.column_names=json.load(col_file)    

    def predict_strength(self,data):
        self.load_raw()
        self.data=data

        user_input=np.zeros(len(self.column_names["Column Names"]))

        Cement=data["html_cement"]
        Blast_Furnace_Slag=data["html_bfs"]
        Fly_Ash=data["html_fly"]
        Water=data["html_water"]
        Superplasticizer=data["html_sp"]
        Coarse_Aggregate=data["html_ca"]
        Fine_Aggregate=data["html_fa"]
        Age=data["html_age"]

        user_input[0]=Cement
        user_input[1]=Blast_Furnace_Slag
        user_input[2]=Fly_Ash
        user_input[3]=Water
        user_input[4]=Superplasticizer
        user_input[5]=Coarse_Aggregate
        user_input[6]=Fine_Aggregate
        user_input[7]=Age

        print(f"{user_input=}")
        compressive_strength=self.model.predict([user_input])

        return (f"Predicted Compressive Strength in Mpa = {compressive_strength}")
    
if __name__ == "__main__":
    pred_obj=prediction()
    pred_obj.load_raw

        
