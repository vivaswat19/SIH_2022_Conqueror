from Backend import *
class connector:
    def __init__(self):
        self.t1=False
        self.t2=False
        self.t3=False
        self.t4=False
        self.t5=False
        self.t6=False
        self.K=2.5
        self.Ss=1e-05   
        self.Sy=0.15
        self.b=7
        self.bc=3
        self.Kc=0.05
        self.Ssc=0.0001
        self.filePath="./transducer.csv"
        self.aquifer=None
        self.well=None
        self.data=None
        self.r = 0.076
        self.q = -27.255
    def getValues(self):
        return self.aquifer.S,self.aquifer.T

    def setValues(self): 
        output_file = open('aquifer.txt','w')
        output_file.writelines(['K', '\t', str(self.K),'\n'])
        output_file.writelines(['Ss', '\t', str(self.Ss), '\n'])
        output_file.writelines(['Sy', '\t', str(self.Sy), '\n'])
        output_file.writelines(['b', '\t', str(self.b), '\n'])
        output_file.writelines(['bc', '\t', str(self.bc), '\n'])        
        output_file.writelines(['Kc', '\t', str(self.Kc), '\n'])        
        output_file.writelines(['Ssc', '\t', str(self.Ssc), '\n'])
        output_file.close()

        output_file = open('well.txt','w')
        output_file.writelines(['r', '\t', str(self.r),'\n'])
        output_file.writelines(['Q', '\t', str(self.q), '\n'])
        output_file.close()



        self.data=DataSet(self.filePath)
        self.model = MLModel(self.data.s,self.data.t, self.K, self.Sy, self.b, self.r, self.q);
        self.well=Well(self.data.t.min(), self.data.t.max())
        self.data.setTr2Array(self.well.r)
        self.aquifer=Aquifer()

        # set up test objects using current parameter values
        self.theis = Theis(self.aquifer, self.well)
        self.hantush = Hantush(self.aquifer, self.well)
        self.shortStor = ShortStorage(self.aquifer, self.well)    
        self.numericWaterTable = MOL(self.aquifer, self.well)    

    def mlgraph(self):
        ans = self.model.Drawdown()
        return self.data.t,ans

    def graph1(self):
        #drawdown-time graph
        xValues=[]
        yValues=[]
        xValues.append(self.data.t)
        yValues.append(self.data.s)
        if self.t1:
            xValues.append(self.well.tArray)
            yValues.append(self.theis.Drawdown(0,0))
        if self.t2:
            xValues.append(self.well.tArray)
            yValues.append(self.numericWaterTable.Drawdown(1))
        if self.t3:
            xValues.append(self.well.tArray)
            yValues.append(self.hantush.Drawdown(0))
        if self.t4:
            xValues.append(self.well.tArray)
            yValues.append(self.shortStor.Drawdown(0))
        if self.t5:
            xValues.append(self.well.tArray)
            yValues.append(self.theis.Drawdown(1,0))
        if self.t6:
            xValues.append(self.well.tArray)
            yValues.append(self.numericWaterTable.Drawdown(0))

        return xValues,yValues

    def graph2(self):

        #composite graph
        xValues=[]
        yValues=[]
        if self.t1:
            xValues.append(self.well.tr2Array)
            yValues.append(self.theis.Drawdown(0,2))
        if self.t2:
            xValues.append(self.well.tr2Array)
            yValues.append(self.numericWaterTable.Drawdown(1))
        if self.t3:
            xValues.append(self.well.tr2Array)
            yValues.append(self.hantush.Drawdown(1))
        if self.t4:
            xValues.append(self.well.tr2Array)
            yValues.append(self.shortStor.Drawdown(1))
        if self.t5:
            xValues.append(self.well.tr2Array)
            yValues.append(self.theis.Drawdown(1,2))
        if self.t6:
            xValues.append(self.well.tr2Array)
            yValues.append(self.numericWaterTable.Drawdown(0))

        return xValues,yValues

    def graph3(self):
        #Drawdown - Distance Graph
        xValues=[]
        yValues=[]
        if self.t1:
            xValues.append(self.well.rArray)
            yValues.append(self.theis.Drawdown(0,1))
        if self.t2:
            xValues.append(self.well.rArray)
            yValues.append(self.numericWaterTable.Drawdown(1))
        if self.t3:
            xValues.append(self.well.rArray)
            yValues.append(self.hantush.Drawdown(2))
        if self.t4:
            xValues.append(self.well.rArray)
            yValues.append(self.shortStor.Drawdown(2))
        if self.t5:
            xValues.append(self.well.rArray)
            yValues.append(self.theis.Drawdown(1,1))
        if self.t6:
            xValues.append(self.well.rArray)
            yValues.append(self.numericWaterTable.Drawdown(0))

        return xValues,yValues
