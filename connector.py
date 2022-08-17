from Backend import *
class connector:
    def __init__(self):
        self.t1=False
        self.t2=False
        self.t3=False
        self.t4=False
        self.t5=False
        self.t6=False
        self.K=0
        self.Ss=0
        self.Sy=0
        self.b=0
        self.bc=0
        self.Kc=0
        self.Ssc=0
        self.filePath=""
        self.aquifer=None
        self.well=None
        self.data=None
    def getValues(self):
        return self.aquifer.S,self.aquifer.T
    def setValues(self,dict):
        self.t1=dict['T1']
        self.t2=dict['T2']
        self.t3=dict['T3']
        self.t4=dict['T4']
        self.t5=dict['T5']
        self.t6=dict['T6']
        self.K=dict['K']
        self.Ss=dict['Ss']
        self.Sy=dict['Sy']
        self.b=dict['b']
        self.bc=dict['bc']
        self.Kc=dict['Kc']
        self.Ssc=dict['Ssc']
        self.filepath= None
        self.theis = None
        self.hantush = None
        self.shortStor =   None
        self.numericWaterTable = None 
        self.filePath=dict['filepath']    

        output_file = open('aquifer.txt','w')
        output_file.writelines(['K', '\t', str(self.K),'\n'])
        output_file.writelines(['Ss', '\t', str(self.Ss), '\n'])
        output_file.writelines(['Sy', '\t', str(self.Sy), '\n'])
        output_file.writelines(['b', '\t', str(self.b), '\n'])
        output_file.writelines(['bc', '\t', str(self.bc), '\n'])        
        output_file.writelines(['Kc', '\t', str(self.Kc), '\n'])        
        output_file.writelines(['Ssc', '\t', str(self.Ssc), '\n'])
        output_file.close()

        self.data=self.DataSet()
        self.well=self.Well(self.data.t.min(), self.data.t.max(),self.filePath)
        self.data.setTr2Array(self.well.r)
        self.aquifer=self.Aquifer()
        

        # set up test objects using current parameter values
        self.theis = self.Theis(self.aquifer, self.well)
        self.hantush = self.Hantush(self.aquifer, self.well)
        self.shortStor = self.ShortStorage(self.aquifer, self.well)    
        self.numericWaterTable = self.MOL(self.aquifer, self.well)    


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

        xValues.append(self.data.tr2)
        yValues.append(self.data.s)
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
