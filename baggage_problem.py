#!/usr/bin/python

import sys


def initial_baggage_order(a):
    bag_list = ['B', 'A']*a
    bag_bin = ["_"]*2*a
    bag_bin.extend(bag_list) 
    return bag_bin

def target_baggage_order(a):
    bag_bin_final = ['A']*a
    bag_bin_final.extend(['B']*a)
    return bag_bin_final

def ordering(lst, from_pos, to_pos, a):
    if from_pos + 2 == 0:
        lst[from_pos:], lst[to_pos:to_pos+2] = lst[to_pos:to_pos+2], lst[from_pos:]
    else:
        lst[from_pos:from_pos+2], lst[to_pos:to_pos+2] = lst[to_pos:to_pos+2], lst[from_pos:from_pos+2]
    
    if from_pos < 0:
        frm_pos = 2*a + from_pos + 1
    else:
        frm_pos = from_pos - 2*a + 1
    if to_pos < 0:
        too_pos = 2*a + to_pos + 1
    else:
        too_pos = to_pos - 2*a + 1
    print "%d to %d" %(frm_pos, too_pos)
    print


def controller(lst, a):
    while True:
        ini_pos = lst.index('B')
	from_pos = None
	to_pos = None
        B_pos = ini_pos + 2
        A_pos = -3
	
	if a % 2 == 0:
            rng1 = a/2
            rng2 = a - rng1
        else:
            rng1 = a/2 + 1
            rng2 = a - rng1
	for i in range(rng1):
	    if i == 0:
                from_pos = A_pos
                to_pos = ini_pos - 2
		ordering(lst, from_pos, to_pos, a)
                if a < 6:
                    A_pos -= 2
                else:
                    A_pos -= 4
	    elif (i % 2 != 0):
                to_pos = from_pos
	        from_pos = B_pos
	        ordering(lst, from_pos, to_pos, a)
                if i == rng1 - 3 and (a % 2 != 0):
                    B_pos += 2
                else:
                    B_pos += 4
	    elif (i % 2 == 0):
		to_pos = from_pos
                from_pos = A_pos
		ordering(lst, from_pos, to_pos, a)
                if i == rng1 - 3 and (a % 2 != 0):
                    A_pos -= 2
                else:
                    A_pos -= 4

        tmp = ini_pos/2 + ini_pos
        a_pos = lst[tmp:].index('A')+tmp
        b_pos = lst.index('B')
        for i in range(rng2):
            if i == 0:
                to_pos = from_pos 
		from_pos = b_pos
		ordering(lst, from_pos, to_pos, a)
                b_pos += 4
            elif (i % 2 != 0):
                to_pos = from_pos
                from_pos = a_pos
		ordering(lst, from_pos, to_pos, a)
                a_pos += 4
            elif (i % 2 == 0):
                to_pos = from_pos
                from_pos = b_pos
		ordering(lst, from_pos, to_pos, a)
                b_pos += 4
                    
        else:
            break                
	        
            

if __name__ == "__main__":
    no_of_bags = int(sys.argv[1])
    print "Input : %d" %no_of_bags
    lst = initial_baggage_order(no_of_bags)
    final_lst = target_baggage_order(no_of_bags)
    print "output"
    print "-----------"
    controller(lst, no_of_bags)
    index = lst.index('A')
    new_lst = lst[index:]
    for count in range(2*no_of_bags):
        if new_lst[count] == final_lst[count]:
            flag = True 
        else:
            flag = False
            break
    print "-------------------------"
    if flag == True:
        print "TEST CASE PASSED"
    else:
        print  "TEST CASE FAILED"
