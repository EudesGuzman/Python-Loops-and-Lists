parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
total_slots=0
available_slots =0
occupied_slots =0
parkingStatus={}
def get_parking_lot(parking):
    global total_slots,available_slots ,occupied_slots 
    for i in parking:    
        total_slots += (i.count(1)+i.count(2))
        occupied_slots += i.count(1)
        available_slots += i.count(2)
    parkingStatus.update({"total_slots":total_slots, "available_slots":available_slots ,"occupied_slots":occupied_slots })
    return parkingStatus     
print(get_parking_lot(parking_state))