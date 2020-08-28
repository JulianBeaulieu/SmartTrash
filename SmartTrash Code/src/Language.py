class Language:
    language = "English"

    def getLanguage(self):
        self.loadLanguage()
        return(self.language)

    def setLanguage(self, newLanguage):
        if(self.languageIsSupported(newLanguage)):
            self.saveLanguage(newLanguage)


    #Helper Methods
    def languageIsSupported(self, newLanguage):
        supportedLanguages = ['English', 'German', 'Arabic', 'Spanish', 'Chinese']
        return(newLanguage in supportedLanguages)

    def loadLanguage(self):
        file = open("language.txt", "wb+")
        tmp = file.read()

        if(self.languageIsSupported(tmp)):
            self.language = tmp

        print(tmp)
        print(self.language)

        file.close()

    def saveLanguage(self, newLanguage):
        file = open("language.txt", "wb+")
        file.write(newLanguage)
        file.close()
