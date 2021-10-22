import math


def int_list(list):
    new_list = []
    for i in list:
        line = []
        line.append(int(i[0]))
        line.append(int(i[1]))
        new_list.append(line)
    return new_list

def dist(point_1,point_2):
        return round(math.sqrt((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2),2)    

#state az hogy melyik szamu csucson vagyunk
#a koordinatakat a csucs szamaval tudjuk indexelni ekkor megkapjuk a koordinatakat
#a celokon vegig kell majd iteralni hogy mindent osszehasonlitsunk
#elekbol tudjuk a parsagot kinyerni

class Node:
    def __init__(self,state,cost_to_node,cost_to_end):
        #state a csucs azonositoja a grafban
        self.state = state
        #cost to node hogy mennyi az eddigi uton ide eljutni ez a parent node koltsege plusz a parent node es a node kozotti dzakaszhossz
        #cost_to_node = parent.cost_to_node + distance(node,parent_node)
        self.cost_to_node = cost_to_node
        #ez a heurisztika alapjan kiszamolt koltseg cost_to_end = distance(node,end)
        self.cost_to_end = cost_to_end


class Frontier:
    def __init__(self):
        self.nodes = []

    def addNode(self,node):
        self.nodes.append(node)

    def empty(self):
        return len(self.nodes) == 0
    
    def contains_state(self,state):
        return any(node.state == state for node in self.nodes )
    
    #legoptimalisabbat kell kivalasztani
    def removeNode(self):
        if self.empty():
            return None
        else:
            self.nodes = sorted(self.nodes,key=lambda node: node.cost_to_node + node.cost_to_end,reverse=True)
            node = self.nodes[-1]
            self.nodes = self.nodes[:-1]
            return node
    


        


class Palya:

    def __init__(self):
        self.csucsok = []
        self.elek = []
        self.celok = []

    def neighbour(self,state):
        neighbouring_states = []
        for el in self.elek:
            if el[0] == state:
                neighbouring_states.append(el[1])
            elif el[1] == state:
                neighbouring_states.append(el[0])
        return neighbouring_states

    

    def solve(self):
        for megoldandok in self.celok:
            start_state = megoldandok[0]
            end_state = megoldandok[1]
            frontier = Frontier()

            #koordinatakat kell megtalalni nem a nodeokat irni erre egy fuggvenyt
            start_node = Node(state=start_state,cost_to_node=0,cost_to_end=dist(self.csucsok[start_state],self.csucsok[end_state]))
            frontier.addNode(start_node)

            self.explored = set()

            while True:
                if frontier.empty():
                    break

                node = frontier.removeNode()

                if node.state == end_state:
                    print(node.cost_to_node,end="\t")
                    break

                self.explored.add(node.state)

                for neighbouring_state in self.neighbour(node.state):
                    if neighbouring_state not in self.explored and not frontier.contains_state(neighbouring_state):
                        costtoend = dist(self.csucsok[end_state],self.csucsok[neighbouring_state])
                        costtonode = node.cost_to_node + dist(self.csucsok[node.state],self.csucsok[neighbouring_state])
                        child_node = Node(neighbouring_state,cost_to_node=costtonode,cost_to_end=costtoend)
                        frontier.addNode(child_node)
                        

    def beolvas(self):
        utszam = int(input())
        csucsszam = int(input())
        elszam = int(input())

        input()

        for i in range(utszam):
            line = input()
            self.celok.append(line.split('\t'))


        input()

        for i in range(csucsszam):
            line = input()
            self.csucsok.append(line.split('\t'))


        input()

        for i in range(elszam):
            line = input()
            self.elek.append(line.split('\t'))

        self.celok = int_list(self.celok)
        self.csucsok = int_list(self.csucsok)
        self.elek = int_list(self.elek)

        


palya = Palya()
palya.beolvas()
palya.solve()

