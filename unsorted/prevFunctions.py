"""
? Bu fonksiyon Screen class'ına aitti.
def CreateGUI(self):
    # ? Create a frame for positioning the elements
         # Bu frameleri kullanmak için yukarıdaki grid (self.grid() )fonksiyonunu çağırmamız gerekiyor.
        upperFrame = LabelFrame(self,text="Control Unit", width=490, height=175, bd=2)
        upperFrame.grid(row=0, column=0, columnspan=3,rowspan = 3)

        #Button positioning and labeling 

        #Get Model Button and label
        # TODO: Keras kullanılarak eğitilen modelin import edilme ve kullanıma hazır hale gelme işlemi olacak
        getModelButton = Button(upperFrame ,text="Get Model")
        getModelButton.grid(row=1,column=0)
        # TODO: Bu yazılar model yüklendikten sonra çıkacak ve başarılı başarısız diye değişebilecek
        modelLabel = Label(upperFrame,text="Success")
        modelLabel.grid(row=2,column=0)

        #Get Test Values
        # TODO: Burada yolu girilen test verilerinin sisteme dahil edilme durumu bulunuyor
        getTestValuesButton = Button(upperFrame,text="Get Test File")
        getTestValuesButton.grid(row=1,column=1)
        # TODO: Bu yazılar model yüklendikten sonra çıkacak ve başarılı başarısız diye değişebilecek
        testLabel = Label(upperFrame,text="Success")
        testLabel.grid(row=2,column=1)
        

        #Run 
        # TODO: Bu kısımda ise test verilerini hazırladığımız model üzerinde çalıştırılacak ve elde edilen veriler alt kısımda gözükecek olan grafikte gösterilecek
        runButton = Button(upperFrame,text="RUN")
        runButton.grid(row=3,column=0) """


""" 
## ! Adding with panelWindow
        upperPanel = PanedWindow(borderwidth=3,height=65,orient=HORIZONTAL)
        upperPanel.pack(fill=BOTH)

        # ! Test function
        def changecolor():
            modelLabel.config(bg="green")

        #Get Model Button and label
        modelPanel = PanedWindow(height=50,orient=VERTICAL)
        upperPanel.add(modelPanel)
        # TODO: Keras kullanılarak eğitilen modelin import edilme ve kullanıma hazır hale gelme işlemi olacak
        getModelButton = Button(modelPanel ,text="Get Model",command=changecolor)
        modelPanel.add(getModelButton)
        modelPanel.paneconfig(getModelButton,minsize=25,padx=3,pady=3)
        # TODO: Bu yazılar model yüklendikten sonra çıkacak ve başarılı başarısız diye değişebilecek
        modelLabel = Label(modelPanel,text="Success")
        modelPanel.add(modelLabel)
        modelPanel.paneconfig(modelLabel,minsize=24)


        #Get Test Values
        testPanel = PanedWindow(height=50,orient=VERTICAL)
        upperPanel.add(testPanel)
        # TODO: Burada yolu girilen test verilerinin sisteme dahil edilme durumu bulunuyor
        getTestValuesButton = Button(testPanel,text="Get Test File")
        testPanel.add(getTestValuesButton)
        testPanel.paneconfig(getTestValuesButton,minsize=25,padx=3,pady=3)
        # TODO: Bu yazılar model yüklendikten sonra çıkacak ve başarılı başarısız diye değişebilecek
        testLabel = Label(testPanel,text="Success")
        testPanel.add(testLabel)
        testPanel.paneconfig(testLabel,minsize=24)
        

        #Run 
        # TODO: Bu kısımda ise test verilerini hazırladığımız model üzerinde çalıştırılacak ve elde edilen veriler alt kısımda gözükecek olan grafikte gösterilecek
        runButton = Button(upperPanel,text="RUN")
        upperPanel.add(runButton) """