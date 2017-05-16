import os
import sys

'''
data_table = [
    [0, 0, 1, 0, 4, 6, 8, 0, 0],
    [5, 3, 0, 1, 2, 0, 0, 0, 0],
    [4, 6, 0, 8, 0, 0, 0, 0, 2],
    [0, 0, 3, 0, 1, 0, 6, 2, 0],
    [0, 2, 0, 0, 8, 4, 7, 0, 0],
    [1, 0, 7, 6, 9, 0, 0, 4, 0],
    [0, 8, 0, 0, 6, 0, 4, 9, 3],
    [3, 0, 0, 0, 0, 8, 0, 1, 6],
    [0, 0, 2, 4, 0, 9, 0, 0, 7]
    ]
'''
'''
data_table = [
    [0, 3, 8, 5, 2, 9, 4, 7, 1],
    [0, 0, 0, 0, 0, 0, 6, 3, 8],
    [4, 7, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 6, 7],
    [1, 4, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 4, 9],
    [3, 0, 0, 2, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 3, 0, 6],
    [7, 8, 4, 6, 3, 5, 0, 0, 0]
    ]
'''
data_table = [
    [0, 0, 3, 1, 0, 0, 6, 4, 0],
    [0, 4, 0, 0, 8, 3, 0, 0, 0],
    [1, 0, 0, 0, 4, 2, 0, 0, 0],
    [0, 6, 4, 2, 0, 0, 0, 0, 5],
    [3, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 3, 1, 5, 0, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 7, 6],
    [0, 0, 6, 0, 0, 0, 8, 3, 0],
    [0, 0, 0, 5, 7, 0, 4, 0, 0]
    ]

def INDEX(x):
    assert x > 0 and x < 10
    return x-1


def is_valid(x):
    if x>0 and x<10:
        return True
    else:
        return False

class point:
    row = 0
    vol = 0
    group = 0

    def set_position(x,y):
        self.row = y
        self.vol = x

class node:
    value = 0
    mark_values = []
    mark_count = 9

    row = 0
    vol = 0
    group = 0

    def __init__(self, x, y):
        self.mark_values = [True, True, True, True, True, True, True, True, True]
        self.set_position(x, y)
        '''        
        if (x == 1 and y == 7):
            self.show_position()
            self.show_avaliable()
        '''

    def set_position(self, x, y):
        self.row = y
        self.vol = x

        self.group = ((y-1)/3)*3+(x-1)/3+1

    def show_position(self):
        print self.row, self.vol, self.group

    def set_value(self, val):
        self.value = val
        
        if val != 0:
            self.mark_count = 0
            for i in range(1,10):
                self.mark_values[INDEX(i)] = False 

    def mark_invalid(self, val):
        if self.value != 0 or self.mark_values[INDEX(val)] == False:
            return

        #print "marking node(%d, %d) with val %d" % (self.row, self.vol, val)

        self.mark_values[INDEX(val)] = False
        self.mark_count -= 1
        if self.mark_count == 1:
            for i in range (1, 10):
                if self.mark_values[INDEX(i)] == True:
                    print "fill node (%d, %d) with value %d" % (self.row, self.vol, i)
                    self.set_value(i)
                    nt.mark_invalid(self.row, self.vol, self.group, i)
        elif self.mark_count < 1:
            print "no avaliable value for node (%d, %d), failed" % (self.row, self.vol)
            return -1

    def show_avaliable(self):
        values = []
        #print self.mark_values
        for i in range(1, 10):
            if self.mark_values[INDEX(i)] == True:
                values.append(i)

        print values

    def is_avaliable(self, value):
        return self.mark_values[INDEX(value)]



class node_group:
    nodes = []
    is_resolved = False
    need_check_value = []
    parent = None

    def __init__(self, input_nodes, parent=None):
        self.nodes = input_nodes
        self.parent = parent

    def show_values(self):
        values = []
        for i in range(0, 9):
            values.append(self.nodes[i].value)
        print values

    def mark_invalid(self):
        for i in range(0, 9):
            mark = self.nodes[i].value
            if mark != 0:
                for j in range(0, 9):
                    if j != i:
                        self.nodes[j].mark_invalid(mark)
                        #n = self.nodes[j]
                        #print "marking node (%d,%d) with value %d" % (n.row, n.vol, mark)
        self.check_resolved()

    def mark_invalid_except(self, mode, id, value):
        for i in range(0, 9):
            if (mode == "row" and self.nodes[i].row != id):
                print "mark_invalid_except", self.nodes[i].row, self.nodes[i].vol, value
                self.nodes[i].mark_invalid(value)
            elif (mode == "vol" and self.nodes[i].vol != id):
                print "mark_invalid_except", self.nodes[i].row, self.nodes[i].vol, value
                self.nodes[i].mark_invalid(value)
            elif (mode == "group" and self.nodes[i].group != id):
                print "mark_invalid_except", self.nodes[i].row, self.nodes[i].vol, value
                self.nodes[i].mark_invalid(value)
                        
    def check_resolved(self):
        for i in range(0, 9):
            if self.nodes[i].value == 0:
                self.is_resolved = False
                return
        self.is_resolved = True
        self.parent.check_resolved()


    def get_need_check_values(self):
        self.need_check_values = []
        for i in range(0, 9):
            #print self.nodes[i].mark_values
            for j in range(1, 10):
                if self.nodes[i].mark_values[INDEX(j)] == True:
                    if j not in self.need_check_values:
                        self.need_check_values.append(j)
                        print self.need_check_values
        
        print "need_check_values result"
        print self.need_check_values

    def get_small_group(self, mode=""):
        small_groups = []

        for i in range(0,3):
            small_nodes = []
            for j in range(0,3):
                if mode == "row":
                    index = i*3+j
                elif mode == "vol":
                    index = i+j*3
                else:
                    index = i*3+j
                small_nodes.append(self.nodes[index])
            small_groups.append(node_small_group(small_nodes))

        return small_groups

    def find_in_small_groups(self, values, grps):
        ret_vals = []
        result = [True, True, True]

        #print "in find_in_small_groups", values, grps

        for i in values:
            print "now checking", i
            count = 0
            for j in range(0, 3):
                c = grps[j].find_value(i)
                result[j] = (c > 0)
                count += c
            print result, count

            if count == 1:
                for j in range(0,9):
                    if self.nodes[j].is_avaliable(i):
                        print "fill node",self.nodes[j].row, self.nodes[j].vol,"with value",i
                        self.nodes[j].set_value(i)
                        self.parent.mark_invalid(self.nodes[j].row, self.nodes[j].vol, self.nodes[j].group, i)

            if result.count(True) == 1:
                print i, "only in small grp", result.index(True)
                #print mode
                #print "need send cmd to small grp", grps[result.index(True)].nodes[0]
                ret_vals.append([i, grps[result.index(True)].nodes[0]])

        return ret_vals
            
        
    def check_cross(self, mode):
        if mode == "group":
            ret_vals= [[], []]
            
            rows = self.get_small_group("row")
            
            row_ret = self.find_in_small_groups(self.need_check_values, rows)

            for d in row_ret:
                ret_vals[0].append([d[0], d[1].row])

            vols = self.get_small_group("vol")

            vol_ret = self.find_in_small_groups(self.need_check_values, vols)

            for d in vol_ret:
                ret_vals[1].append([d[0], d[1].vol])

            return ret_vals
            
        else:
            ret_val = []
            small_grps = self.get_small_group()
            
            grp_ret = self.find_in_small_groups(self.need_check_values, small_grps)

            for d in grp_ret:
                ret_val.append([d[0], d[1].group])

            return ret_val

     
            
class node_small_group(node_group):
    def find_value(self, value):
        count = 0
        for i in range(0,3):
            print "now checking node", self.nodes[i].row, self.nodes[i].vol
            #print self.nodes[i].mark_values
            if self.nodes[i].mark_values[value-1] == True:
                count += 1
        print count
        return count
        
                    

class node_table:
    table = []
    is_resolved = False
    rows = []
    vols = []
    grps = []

    def __init__(self, input_table):
        for i in range(0, 9):
            line = []
            for j in range(0, 9):
                n = node(j+1,i+1)
                if input_table[i][j] != 0:
                    n.set_value(input_table[i][j])
                line.append(n)
                
            self.table.append(line)

        for i in range(1,10):
            self.rows.append(node_group(self.get_row(i), self))

        for i in range(1,10):
            self.vols.append(node_group(self.get_vol(i), self))


        for i in range(1,10):
            self.grps.append(node_group(self.get_group(i), self))        
        

    def get_node(self, row, vol):
        return self.table[INDEX(row)][INDEX(vol)]

    def show_values(self):
        for line in self.table:
            line_data = []
            for n in line:
                line_data.append(n.value)
            print line_data
        print

    def get_row(self, row_num):
        #print "geting row", row_num
        return self.table[row_num - 1]

    def get_vol(self, vol_num):
        v = []
        for row in range(0, 9):
            v.append(self.table[row][vol_num - 1])
        return v

    def get_group(self, group_num):
        g = []
        for i in range(0, 9):
            for j in range(0, 9):
                n = self.table[i][j]
                if n.group == group_num:
                    g.append(n)
        return g

    def mark_invalid(self, row, vol, group, value):
        print "nt marking", row, vol, group, value
        for i in range(0,9):
            for j in range(0,9):
                n = self.table[i][j]
                if n.row == row or n.vol == vol or n.group == group:
                    n.mark_invalid(value)

    def check_resolved(self):
        for i in range(0, 9):
            if self.rows[i].is_resolved == False:
                self.is_resolved = False
                return 


        print "Sudoku Resolved!!!"
        self.is_resolved = True

            
    

'''
for row in range(1,10):
    for vol in range(1,10):
        n = node(vol,row)
        n.show_position()
'''
'''
n = node(1,1)
for i in range(1, 10):
    n.mark_invalid(i)
    if n.value != 0:
        print "get value", n.value
    n.show_avaliable()
'''

nt = node_table(data_table)
print "original table:"
nt.show_values()
print "start-----"

'''
print "group test"
g = node_group(nt.get_group(3))
g.show_values()
g.mark_invalid()
g.show_values()    
'''
#n = nt.get_node(7,1)
#print "node position %d, %d, value=%d, mark_count=%d" % (n.row, n.vol, n.value, n.mark_count)
#n.show_avaliable()
'''
rows = []
for i in range(1,10):
    rows.append(node_group(nt.get_row(i), nt))

vols = []
for i in range(1,10):
    vols.append(node_group(nt.get_vol(i), nt))


grps = []
for i in range(1,10):
    grps.append(node_group(nt.get_group(i), nt))
'''
rows = nt.rows
vols = nt.vols
grps = nt.grps
'''
print "parent"
print grps[7].parent
grps[7].parent.show_values()
'''


for round in range(1,10):
    print "round", round
    all_resolved = True
    for i in range(0,9):
        rows[i].mark_invalid()
        vols[i].mark_invalid()
        grps[i].mark_invalid()

        if rows[i].is_resolved == False:
            print "row", i+1, "is not resolved"
            all_resolved = False
    
    nt.show_values()
    #print all_resolved
    if all_resolved == True:
        print "Resolved!!!"
        break
    else:
        print "Need another round"

for i in range(1,10):
    for j in range(1,10):
        n = nt.get_node(i, j)
        if n.value == 0:
            print "node(",i,",",j,") mark="
            n.show_avaliable()

print "stage 1 end, stage 2 start"


'''
for i in range(0,9):
    print "checking grp", i+1
    grps[i].get_need_check_values()
    grps[i].check_cross("group")
'''
for i in range(0,9):
    print "checking row", i+1
    rows[i].get_need_check_values()
    result = rows[i].check_cross("row")
    print result
    for j in range(0, len(result)):
        grps[result[j][1]-1].mark_invalid_except("row", i+1, result[j][0])
        grps[result[j][1]-1].mark_invalid()
    
    nt.show_values()
    print "checking vol", i+1
    vols[i].get_need_check_values()
    result = vols[i].check_cross("vol")
    print result
    for j in range(0, len(result)):
        grps[result[j][1]-1].mark_invalid_except("vol", i+1, result[j][0])
        grps[result[j][1]-1].mark_invalid()

    nt.show_values()
    print "checking group", i+1
    grps[i].get_need_check_values()
    result = grps[i].check_cross("group")
    print result
    for j in range(0, len(result[0])):
        rows[result[0][j][1]-1].mark_invalid_except("group", i+1, result[0][j][0])
        rows[result[0][j][1]-1].mark_invalid()
    for j in range(0, len(result[1])):
        vols[result[1][j][1]-1].mark_invalid_except("group", i+1, result[1][j][0])
        vols[result[1][j][1]-1].mark_invalid()
    nt.show_values()

    if nt.is_resolved == True:
        break
nt.show_values()

print "stage 2 end, stage 3 start"
for round in range(1,10):
    print "round", round
    all_resolved = True
    for i in range(0,9):
        rows[i].mark_invalid()
        vols[i].mark_invalid()
        grps[i].mark_invalid()

        if rows[i].is_resolved == False:
            print "row", i+1, "is not resolved"
            all_resolved = False
    
    nt.show_values()
    #print all_resolved
    if all_resolved == True:
        print "Resolved!!!"
        break
    else:
        print "Need another round"

for i in range(1,10):
    for j in range(1,10):
        n = nt.get_node(i, j)
        if n.value == 0:
            print "node(",i,",",j,") mark="
            n.show_avaliable()

print "stage 3 end, stage 4 start"


'''
for i in range(0,9):
    print "checking grp", i+1
    grps[i].get_need_check_values()
    grps[i].check_cross("group")
'''
for i in range(0,9):
    print "checking row", i+1
    rows[i].get_need_check_values()
    result = rows[i].check_cross("row")
    print result
    for j in range(0, len(result)):
        grps[result[j][1]-1].mark_invalid_except("row", i+1, result[j][0])
        grps[result[j][1]-1].mark_invalid()
    
    nt.show_values()
    print "checking vol", i+1
    vols[i].get_need_check_values()
    result = vols[i].check_cross("vol")
    print result
    for j in range(0, len(result)):
        grps[result[j][1]-1].mark_invalid_except("vol", i+1, result[j][0])
        grps[result[j][1]-1].mark_invalid()

    nt.show_values()
    print "checking group", i+1
    grps[i].get_need_check_values()
    result = grps[i].check_cross("group")
    print result
    for j in range(0, len(result[0])):
        rows[result[0][j][1]-1].mark_invalid_except("group", i+1, result[0][j][0])
        rows[result[0][j][1]-1].mark_invalid()
    for j in range(0, len(result[1])):
        vols[result[1][j][1]-1].mark_invalid_except("group", i+1, result[1][j][0])
        vols[result[1][j][1]-1].mark_invalid()
    nt.show_values()
    if nt.is_resolved == True:
        break
nt.show_values()

'''
for i in range(0,9):
    print "checking vol", i+1
    vols[i].get_need_check_values()
    vols[i].check_cross("vol")
'''

'''
nt.show_values()
n.show_avaliable()




for i in range(0,9):
    print "debug mark vol %d" %(i+1)
    vols[i].mark_invalid()
    nt.show_values()
    print "node position %d, %d, value=%d" % (n.row, n.vol, n.value)
    n.show_avaliable()
'''
'''
nt.show_values()


print "round 2"
for i in range(0,9):
    rows[i].mark_invalid()
    vols[i].mark_invalid()
    grps[i].mark_invalid()
nt.show_values()

print "round 3"
for i in range(0,9):
    rows[i].mark_invalid()
    vols[i].mark_invalid()
    grps[i].mark_invalid()
nt.show_values()

'''

