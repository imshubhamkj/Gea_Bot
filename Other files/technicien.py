
import json
d = {
    
1:{

  "day" : "monday",
  "end_time" : 6,
  "pin" : 122102,
  "start_time" : 2,
  "technician" : "Shubham Kumar"

  },
2:{

  "day" : "wednesday",
  "end_time" : 6,
  "pin" : 122102,
  "start_time" : 2,
  "technician" : "Shubham Kumar"

  },

3:{

  "day" : "sunday",
  "end_time" : 12,
  "pin" : 122102,
  "start_time" : 8,
  "technician" : "Shubham Kumar"

  },

4:{

  "day" : "monday",
  "end_time" : 6,
  "pin" : 632014,
  "start_time" : 2,
  "technician" : "Harsh Kumar"

  },

5:{

  "day" : "friday",
  "end_time" : 4,
  "pin" : 632014,
  "start_time" : 12,
  "technician" : "Harsh Kumar"

  },

6:{

  "day" : "saturday",
  "end_time" : 12,
  "pin" : 632014,
  "start_time" : 8,
  "technician" : "Harsh Kumar"

  },

7:{

  "day" : "thursday",
  "end_time" : 6,
  "pin" : 560037,
  "start_time" : 2,
  "technician" : "Harshit Kulshreshtha"

  },

8:{

  "day" : "saturday",
  "end_time" : 12,
  "pin" : 560037,
  "start_time" : 8,
  "technician" : "Harshit Kulshreshtha"

  },

9:{

  "day" : "sunday",
  "end_time" : 12,
  "pin" : 560037,
  "start_time" : 8,
  "technician" : "Harshit Kulshreshtha"

  },

10:{

  "day" : "monday",
  "end_time" : 6,
  "pin" : 122006,
  "start_time" : 2,
  "technician" : "Yash Tandon"

  },

11:{

  "day" : "thursday",
  "end_time" : 7,
  "pin" : 122006,
  "start_time" : 3,
  "technician" : "Yash Tandon"

  },

12:{

  "day" : "sunday",
  "end_time" : 12,
  "pin" : 122006,
  "start_time" : 8,
  "technician" : "Yash Tandon"

  },

13:{

  "day" : "tuesday",
  "end_time" : 6,
  "pin" : 122001,
  "start_time" : 2,
  "technician" : "Chand Nawab"

  },

14:{

  "day" : "friday",
  "end_time" : 6,
  "pin" : 122001,
  "start_time" : 2,
  "technician" : "Chand Nawab"

  },

15:{

  "day" : "sunday",
  "end_time" : 4,
  "pin" : 122001,
  "start_time" : 12,
  "technician" : "Chand Nawab"

  }



}

with open('gea_technicien_data.json', 'w') as outfile:
    json.dump(d, outfile)