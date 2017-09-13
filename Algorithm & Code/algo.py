import json;

fci_file = open("FCI_Data.json").read()
fci_data = json.loads(fci_file)

disaster_file = open("Disaster_Data.json").read()
disaster_data = json.loads(disaster_file)

rainfall_file = open("Rainfall_Data.json").read()
rainfall_data = json.loads(rainfall_file)



current_stock = fci_data[0]["current_total_stock"]

base_emergency_stock = 0.15 * current_stock

avrg_em_stock = fci_data[0]["avrg_grain_emergency_stock"]

last_yr_em_stock = fci_data[0]["last_yr_grain_emergency_stock"]

avg_stock = (avrg_em_stock + last_yr_em_stock) / 2;

if(base_emergency_stock < last_yr_em_stock):
	base_emergency_stock = last_yr_em_stock + ( 5 * current_stock / 100 )
	

if(base_emergency_stock >= last_yr_em_stock):
	base_emergency_stock = avrg_em_stock


dis_prob = disaster_data[0]["Probability"]
dis_severity = disaster_data[0]["Severity"]

if(dis_prob > 0.5):
	base_emergency_stock = last_yr_em_stock + ( 5 * ( dis_severity * current_stock / 100 ))


rainfall_prob = rainfall_data[0]["Probability"]
rainfall_scale = rainfall_data[0]["Scale"]

if(rainfall_prob > 0.5):
	if (not(rainfall_scale > 3.5 and rainfall_scale < 8.9)) :    
	   base_emergency_stock = last_yr_em_stock + (5 * (rainfall_scale * current_stock / 100 ))

gov_stock = fci_data[0]["grain_used_by_gov"]

current_stock = current_stock - gov_stock

export = current_stock - base_emergency_stock

print ("grains to be exported")
print (export)
