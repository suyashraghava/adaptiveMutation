import  random ;
import  copy;
import collections;

citiesData          =    open('citiesData','w')
cityWithDistance    =    [[0 for i in range(26)] for j in range(26)]
cityNumberCoding    =    {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
CityNumberCoding    =    dict((v,k) for k,v in cityNumberCoding.iteritems())
population          =    []
value               =    []
currentChromosome   =    [[0 for i in range(26)] for j in range(21)] 
generation          =    0
score               =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mutatedChromosome   =    []
mutatedGenes        =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
populationForTesting=    []
x=[]
y=[]
z=[]

def setCities():         # function to create 26 cities and allots them with randomly generated distances and writes it to a text file 
    import random ;
    strData=[]
    for i in range(0,26):
                for j in range(0,26):
                        if i==j:
                                cityWithDistance[i][j]=0
                                
                        elif i>j:
                                    cityWithDistance[i][j]=cityWithDistance[j][i]
                        elif j>i:
                                    cityWithDistance[i][j]=random.randrange(1,1000)
                        strData.append(str(cityWithDistance[i][j]))
                citiesData.write(str(strData[len(strData)-26:]))
                citiesData.write('\n')
    
def chromosomeGenerator():     # function to generate binary chromosome 
    number=[]
    chromosome=[]
    flag = 0
    
    while (flag == 0):
        randomNumber=random.randint(1,26)
        if (randomNumber in number ):
            pass 
        else :
            chromosome.append(CityNumberCoding[randomNumber])
            number.append(randomNumber)
        if (len(number)==26):
                flag=1
    return chromosome

def chromosomeDecoder(passedChromosome):   #function to decode the binary chromosome
    
    i=1
    
    totalDistance=0
    while(i<26):
        start                   =  cityNumberCoding[passedChromosome[i-1]]
        destination             =  cityNumberCoding[passedChromosome[i]]
        distanceBetweenCities   =  cityWithDistance[start-1][destination-1]
        totalDistance           =  distanceBetweenCities+totalDistance
        i=i+1
    return totalDistance

def populationGenerator():    # generates a random population 
    
    for p in range(0,1000):
        population.append(chromosomeGenerator())

    global  populationForTesting
    

    
def selection():         # this function is used to select chromosome for crossover 
    populationSize=len(population)
    for i in range (0,populationSize):
        value.append(chromosomeDecoder(population[i]))
    for i in range  (0,populationSize):
        for  j in range(0,populationSize-1):
            if (value[j] < value[j+1] ):
                temp= value[j+1]
                value[j+1]=value[j]
                value[j]=temp

                tempChromosome=population[j+1] 
                population[j+1]=population[j]
                population[j] =tempChromosome
    cutOff=abs(0*populationSize/100)
    
    del  value[0:cutOff]
    del  population[0:cutOff]
    populationSize=len(population)
    print value[populationSize-1],'\t',value[0],'value'
    if(generation>19 and generationForTesting==20):
        y.append(value[populationSize-1])
    if (generationForTesting<20):
        z.append(value[populationSize-1])



def orderedCrossover():     # this function performs ordered crossover 
    


    g=0
    populationSize=len(population)
    i=populationSize-1
    oldPopulationSize=len(population)
    
    del value[0:populationSize]
    while (i>0):
        
        firstParent    = population[i]
        secondParent   = population[i-1] 
        
        lowerCutoffFirstParent    = random.randrange(0,26)
        lowerCutOffSecdondParent  = random.randrange(0,26)
        upperCutoffFirstParent    = random.randrange(lowerCutoffFirstParent,27)
        upperCuttOffSecondParent  = random.randrange(lowerCutOffSecdondParent,27)
        
        dnaFirstParent = firstParent[lowerCutOffSecdondParent:upperCuttOffSecondParent]
        dnaSecondParent= secondParent[upperCutoffFirstParent:upperCutoffFirstParent]
        
        j = 0
        p = 0

        while (j<len(dnaFirstParent)-1):
            t=0
            while (t<26):
                if (dnaFirstParent[j] == secondParent[t]):
                    del secondParent[t]
                    secondParent.append(dnaFirstParent[j])
                t = t+1
            j = j+1
        while (p<len(dnaSecondParent)-1):
            l=0
            while (l<26):
                if (dnaSecondParent[p] == firstParent[l]):
                    del firstParent[l]
                    firstParent.append(dnaSecondParent[p])
                l = l+1
            p = p+1
        
        population.append(firstParent)
        population.append(secondParent)
        i=i-2
        firstParent=[]
        secondParent=[]
     
    del population[0:oldPopulationSize]

#........................................................................// FOR TESTING //......................................................................................
def setPopulationForTesting ():

    populationForTesting = copy.deepcopy(population)                      # just copies the current population for testing 

def setBackThePopulation():
    
    population = copy.deepcopy(populationForTesting)


    


def updatePattern ():     # this is a the core function which is used to detect a pattern among high performing chromosome to create healthier chromosome  
    populationSize   =  len(population)
    dummy                     = population[populationSize-1]

    stringOfcurrentHealthyChromosome=''.join(str(e) for e in dummy)
    
    start=0
    for i in range (0,26):
        currentChromosome[generation][i]=stringOfcurrentHealthyChromosome[i]


    if (generation==20):
        A=B=C=D=E=F=G=H=I=J=K=L=M=N=O=P=Q=R=S=T=U=V=W=X=Y=Z=0
        for j in range(0,26):
            for i in range(0,20):

                if (currentChromosome[i][j]==CityNumberCoding[1]):
                    A=A+1
                    score[0]=A
                elif(currentChromosome[i][j]==CityNumberCoding[2]):
                    B=B+1
                    score[1]=B 
                elif(currentChromosome[i][j]==CityNumberCoding[3]):
                    C=C+1
                    score[2]=C

                elif(currentChromosome[i][j]==CityNumberCoding[4]):
                    D=D+1
                    score[3]=D

                elif(currentChromosome[i][j]==CityNumberCoding[5]):
                    E=E+1
                    score[4]=E

                elif(currentChromosome[i][j]==CityNumberCoding[6]):
                    F=F+1
                    score[5]=F

                elif(currentChromosome[i][j]==CityNumberCoding[7]):
                    G=G+1
                    score[6]=G
                elif(currentChromosome[i][j]==CityNumberCoding[8]):
                    H=H+1
                    score[7]=H

                elif(currentChromosome[i][j]==CityNumberCoding[9]):
                    I=I+1
                    score[8]=I

                elif(currentChromosome[i][j]==CityNumberCoding[10]):
                    J=J+1
                    score[9]=J

                elif(currentChromosome[i][j]==CityNumberCoding[11]):
                    K=K+1
                    score[10]=K

                elif(currentChromosome[i][j]==CityNumberCoding[12]):
                    L=L+1
                    score[11]=L

                elif(currentChromosome[i][j]==CityNumberCoding[13]):
                    M=M+1
                    score[12]=M

                elif(currentChromosome[i][j]==CityNumberCoding[14]):
                    N=N+1
                    score[13]=N

                elif(currentChromosome[i][j]==CityNumberCoding[15]):
                    O=O+1
                    score[14]=O

                elif(currentChromosome[i][j]==CityNumberCoding[16]):
                    P=P+1
                    score[15]=P

                elif(currentChromosome[i][j]==CityNumberCoding[17]):
                    Q=Q+1
                    score[16]=Q
                elif(currentChromosome[i][j]==CityNumberCoding[18]):
                    R=R+1
                    score[17]=R

                elif(currentChromosome[i][j]==CityNumberCoding[19]):
                    S=S+1
                    score[18]=S

                elif(currentChromosome[i][j]==CityNumberCoding[20]):
                    T=T+1
                    score[19]=T

                elif(currentChromosome[i][j]==CityNumberCoding[21]):
                    U=U+1
                    score[20]=U

                elif(currentChromosome[i][j]==CityNumberCoding[22]):
                    V= V+1
                    score[21]=V

                elif(currentChromosome[i][j]==CityNumberCoding[23]):
                    W=W+1
                    score[22]=W

                elif(currentChromosome[i][j]==CityNumberCoding[24]):
                    X=X+1
                    score[23]=X

                elif(currentChromosome[i][j]==CityNumberCoding[25]):
                    Y=Y+1
                    score[24]=Y

                elif(currentChromosome[i][j]==CityNumberCoding[26]):
                    Z=Z+1
                    score[25]=Z
            
            mutatedChromosome.append(CityNumberCoding[score.index(max(score))+1])

def traditionalMutation():   # this function is used to perform traditional swap mutation 
    populationSize=len(population)
    cutOff=abs(80*populationSize/100)
    print cutOff
    for i in range(0,cutOff):
        temp=population[i][18]
        population[i][18]=population[j][4]
        population[i][4]=temp





def mutation():        # this function performs mutation to change the current part of the population according to detected pattern  
    indexOfGene=[]
    repeatCounter=firstElementCounter =0
    breaker= 0
    for j in range(0,24):
         
        for i in range (0,24):
            
            if (mutatedChromosome[j]==mutatedChromosome[i]):
                    repeatCounter =repeatCounter + 1
        if (repeatCounter>firstElementCounter):
            firstElementCounter=repeatCounter
            mutatedGenes[j]=mutatedChromosome[j]
            indexOfGene.append(j)
            repeatCounter=0
        
        if (j>0 and j%8==0):
            firstElementCounter=0
    #print indexOfGene   
    populationSize=len(population)
    cutOff=abs(50*populationSize/100)
    print cutOff
    for i in range(0,cutOff):
        j=0
        stub = []
        stub=population[i]
        while (j<3):
            
            stub.remove(mutatedGenes[indexOfGene[j]])
            stub[indexOfGene[j]] 
            stub.insert(indexOfGene[j],mutatedGenes[indexOfGene[j]])
            

            #population[i][indexOfGene[j]]=mutatedGenes[indexOfGene[j]]
            j =j+1
        population[i]=stub    


populationForTesting=    []
setCities()
populationGenerator()
generationForTesting = 100
#........................................................// Running the final algorithm //........................................................................................

def showFigure():  # this function creates a plot comparing the mutation with regular mutation 
    import matplotlib.pyplot as plot 
    for i in range(0,20):
        x.append(i)
    plot.figure(figsize=(7,7),dpi=300)
    #plot.axis('equal')
    plot.xlabel('$Generation$')
    plot.ylabel('$Fitness Value$')
    plot.plot(x, z, label=r'$Adaptive$', color='red')
    plot.plot(x, y, ':', label=r'$Traditional$')
    plot.legend(loc='upper right')
    #plot.plot(x,y)
    #plot.plot(x,z)
    plot.savefig("tsp.png")


while (generation<41):
    
    selection()
    
    if (generation<21):
        updatePattern()
    
    orderedCrossover()
    
    if (generation == 20):
        
        
        setPopulationForTesting()
        
    
    #For testing it on the original population 
    
    if (generation == 20):
        
        print '\n.......Now smart mutation................\n' 
        generationForTesting = 0

        while (generationForTesting <20):
            
            if (generationForTesting==0):
                mutation()
            
            selection()
            orderedCrossover()
            generationForTesting=generationForTesting+1
    
    if (generation==20):
        setBackThePopulation()
        print '\n......Break point for mutation to occur traditionally ..........\n'
        traditionalMutation()
        
    generation=generation+1
showFigure()
# ........................................................// Algorithm complete // ................................................................................








