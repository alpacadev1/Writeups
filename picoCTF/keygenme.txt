username_trial = "PRITCHARD"                                                                                                                                           bUsername_trial = b"PRITCHARD"                                                                                                                                                                                                                                                                                                                key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"               
key_part_dynamic1_trial = "xxxxxxxx"                                                                                                                 key_part_static2_trial = "}"  


 if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:                                                                                                           return False                                                                                                                                                             else:                                                                                                                                                                i += 1 

here just take the index [4,5,3,6,2,7,1,8] from the hashed username (sha256 online hash) and substitute in place of the "x" 
