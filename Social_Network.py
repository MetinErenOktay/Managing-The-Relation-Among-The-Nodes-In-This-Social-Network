import sys
import os

dict = {}
with open(sys.argv[1], "r+", encoding="utf-8") as f1, open(sys.argv[2],"r+", encoding="utf-8") as f2, open("output.txt", "w", encoding="utf-8") as output:
    output.write("Welcome to Assignment 3\n")
    output.write("-------------------------------\n")
    #converts content of smn.txt to a dictionary
    for elements in f1:
        username, friends = elements.split(":")
        dict[username] = friends[:].split()



    #converts content of commands.txt to a list
    command_list = []
    for line in f2:
        stripped_line = line.strip()  # slices content of txt file line by line
        line_list = stripped_line.split(' ')  # slices content of the line by tab spaces
        command_list.append(line_list)


    #functions that changes dict
    for i in range(len(command_list)):
        if command_list[i][0] == 'ANU':
            if command_list[i][1] in dict.keys():
                output.write(f"ERROR: Wrong input type! for 'ANU'! -- This user already exists!!\n")
            else:
                dict = {**dict, **{f"{command_list[i][1]}": []}}
                output.write(f"User '{command_list[i][1]}' has been added to the social network successfully\n")
        elif command_list[i][0] == 'DEU':
            #to delete this user from key part of the dictionary
            if command_list[i][1] in dict.keys() :
                del dict[command_list[i][1]]
                # to delete this user from value part of the dictionary
                for j in range(len(dict)):
                    if command_list[i][1] in list(dict.values())[j]:
                        list(dict.values())[j].remove(f"{command_list[i][1]}")
                output.write(f"User '{command_list[i][1]}' and his/her all relations have been deleted successfully\n")
            else:
                output.write(f"ERROR: Wrong input type! for 'DEU'!--There is no user named '{command_list[i][1]}'!!\n")
        elif command_list[i][0] == 'ANF':
            # if one of or both of the nodes don't exist
            if command_list[i][1] not in dict.keys():
                if command_list[i][2] not in dict.keys():
                    output.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{command_list[i][1]}' and '{command_list[i][2]}' found!\n")
                else:
                    output.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{command_list[i][1]}' found!\n")
            elif command_list[i][2] not in dict.keys():
                output.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{command_list[i][2]}' found!\n")
            # if both nodes already exist
            elif command_list[i][1] in dict.keys():
                # if there is a relation between the nodes

                if command_list[i][2] in dict[command_list[i][1]]:
                    output.write(f"ERROR: A relation between '{command_list[i][1]}' and '{command_list[i][2]}' already exists!!\n")
                # if there is no relation between the nodes
                else:
                    dict[f"{command_list[i][1]}"].append(f"{command_list[i][2]}")
                    output.write(f"Relation between '{command_list[i][1]}' and '{command_list[i][2]}' has been added successfully\n")
        elif command_list[i][0] == 'DEF':
            # if one of or both of the nodes don't exist
            if command_list[i][1] not in dict.keys():
                if command_list[i][2] not in dict.keys():
                    output.write(
                        f"ERROR: Wrong input type! for 'DEF'! -- No user named '{command_list[i][1]}' and '{command_list[i][2]}' found!\n")
                else:
                    output.write(
                        f"ERROR: Wrong input type! for 'DEF'! -- No user named '{command_list[i][1]}' found!\n")
            elif command_list[i][2] not in dict.keys():
                output.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{command_list[i][2]}' found!\n")
            # if both nodes already exist
            elif command_list[i][1] in dict.keys():
                # if there is a relation between the nodes
                if command_list[i][2] in dict[f"{command_list[i][1]}"]:
                    dict[f"{command_list[i][1]}"].remove(f"{command_list[i][2]}")
                    output.write(f"Relation between '{command_list[i][1]}' and '{command_list[i][2]}' has been deleted successfully\n")
                # if there is no relation between the nodes
                else:
                    output.write(f"ERROR: No relation between '{command_list[i][1]}' and '{command_list[i][2]}' found!!\n")
        elif command_list[i][0] == 'CF':
            if command_list[i][1] not in dict.keys():
                output.write(f"ERROR: Wrong input type! for 'CF'! -- No user named '{command_list[i][1]}' found!\n")
            else:
                friendcount=len(dict[f"{command_list[i][1]}"])
                output.write(f"User '{command_list[i][1]}' has {friendcount} friends\n")
        elif command_list[i][0] == 'FPF':
            if command_list[i][1] not in dict.keys():
                output.write(f"ERROR: Wrong input type! for 'FPF'! -- No user named '{command_list[i][1]}' found!\n")
            elif int(command_list[i][2])<1 or int(command_list[i][2])>3:
                output.write(f"Error: Maximum distance is out of range\n")
            else:
                distance=int(command_list[i][2])
                poss_fr_list=[]
                #adds direct friends to the list
                poss_fr_list.extend(dict[f"{command_list[i][1]}"])
                distance -= 1
                # adds friends of friends to the list
                if distance > 0:
                    for k in range(len(poss_fr_list)):
                        poss_fr_list.extend(dict[f"{poss_fr_list[k]}"])
                    #to avoid duplication into the list
                    poss_fr_list=list(set(poss_fr_list))
                    poss_fr_list.sort()
                    #to remove main user from the user's friends list
                    if command_list[i][1] in poss_fr_list:
                        poss_fr_list.remove(f"{command_list[i][1]}")
                    distance -= 1
                    ## adds friends of friends of friends to the list
                    if distance>0:
                        for l in range(len(poss_fr_list)):
                            poss_fr_list.extend(dict[f"{poss_fr_list[l]}"])

                        poss_fr_list = list(set(poss_fr_list))
                        poss_fr_list.sort()
                        # to remove main user from the user's friends list
                        if command_list[i][1] in poss_fr_list:
                            poss_fr_list.remove(f"{command_list[i][1]}")

                #next to lines writes "these possible friends:{...} instead of [...]"
                str_fpf=str(poss_fr_list)
                set_fpp=str_fpf.replace("[","{").replace("]","}")
                output.write(f"User '{command_list[i][1]}' has {len(poss_fr_list)} possible friends when maximum distance is {command_list[i][2]}\n")
                output.write(f"These possible friends:{set_fpp}\n")
        elif command_list[i][0] == 'SF':
            if command_list[i][1] not in dict.keys():
                output.write(f"ERROR: Wrong input type! for 'SF'! -- No user named '{command_list[i][1]}' found!\n")
            elif int(command_list[i][2])<2 or int(command_list[i][2])>3:
                output.write(f"Error: Mutually Degree cannot be less than 1 or greater than 4\n")
            else:
                ex = []
                fr_of_friends_list = []
                mf_3 = []
                mf_2 = []
                for frs in dict[command_list[i][1]]:      #ex = friends of friend list
                    ex.append(dict[frs])
                for a in range(len(ex)):                  #fr_of_friends_list = all element in a single line
                    for b in ex[a]:
                        fr_of_friends_list.append(b)
                for name in fr_of_friends_list:
                    if fr_of_friends_list.count(name) == 2:
                        if name != command_list[i][1]:    #fr_of_friends_list stores elements that duplicates 2 or 3 times (uexcept user)
                            mf_2.append(name)
                    elif fr_of_friends_list.count(name) == 3:
                        if name != command_list[i][1]:
                            mf_3.append((name))

                mf_2, mf_3 = sorted(list(set(mf_2))), sorted(list(set(mf_3)))  #deletes duplicating elements
                mf_total = sorted(mf_2 + mf_3)

                output.write(f"Suggestion List for '{command_list[i][1]}' (when MD is {command_list[i][2]}):\n")
                if int(command_list[i][2]) == 2:
                    for x in range(len(mf_2)):
                        output.write(f"'{command_list[i][1]}' has 2 mutual friends with '{mf_2[x]}'\n")
                    for x in range(len(mf_3)):
                        output.write(f"'{command_list[i][1]}' has 3 mutual friends with '{mf_3[x]}'\n")
                    m_f_d_2 = "'"+"', '".join(mf_total)+"'"          #writes elements into quotes
                    output.write(f"The suggested friends for '{command_list[i][1]}': {m_f_d_2}\n")
                elif int(command_list[i][2]) == 3:
                    for x in range(len(mf_3)):
                        output.write(f"'{command_list[i][1]}' has 3 mutual friends with '{mf_3[x]}'\n")
                    m_f_d_3 = "'"+"', '".join(mf_3)+"'"
                    output.write(f"The suggested friends for '{command_list[i][1]}': {m_f_d_3}\n")





