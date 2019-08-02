import os
import re


class writecompositionXML():

    """
    Class managing the writing of a composition model xml file with all gathered data with pycrop2ml' user interface.

    Parameters : \n
        - data : {
                    'Path': '',
                    'Model type': 'unit',
                    'Model name': '',
                    'Authors': '',
                    'Institution': '',
                    'Reference': '',
                    'Abstract': '',
                    'Old name':'' IF iscreate=False
                   }
        
        - listmodel : []

        - listlink : [
                       {
                        'Link type': '',
                        'Target': '',
                        'Source': ''
                       }
                     ]
        
        - iscreate : bool
    """


    def __init__(self, data, listmodel, listlink, iscreate=True):

        self._datas = data
        self._listmodel = listmodel
        self._listlink = listlink
        self._iscreate = iscreate



    def write(self):

        """
        Writes the xml file with the new data set
        """
      
        try:
            fw = open('{}{}{}.{}.xml'.format(self._datas['Path'], os.path.sep, self._datas['Model type'], self._datas['Model name']), "w", encoding='utf8')

        except IOError as ioerr:
            raise Exception('File {} could not be opened in write mode. {}'.format(self._datas['Path'], ioerr))

        else:
            split = os.path.split(self._datas['Path'])[0]

            fw.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE ModelComposition PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelComposition.dtd">')
            fw.write('<ModelComposition name="{0}" id="{1}.{0}" version="001" timestep ="1">'.format(self._datas['Model name'], os.path.split(split)[-1]))
            fw.write('\n\t<Description>\n\t\t<Title>{}</Title>\n\t\t<Authors>{}</Authors>\n\t\t<Institution>{}</Institution>\n\t\t<Reference>{}</Reference>\n\t\t<Abstract>{}</Abstract>'.format(self._datas['Model name'], self._datas['Authors'], self._datas['Institution'], self._datas['Reference'], self._datas['Abstract']))
            fw.write('\n\t</Description>\n\n\t<Composition>')

            for i in self._listmodel:
                fw.write('\n\t\t<Model name="{0}" id="{1}.{0}" filename="{2}" />'.format(re.search(r'\.(.*?)\.xml', i).group(1), self._datas['Model name'], i))

            fw.write("\n\n\t\t<Links>")
            
            for j in self._listlink:
                fw.write('\n\t\t\t<{} target="{}" source="{}" />'.format(j['Link type'], j['Target'], j['Source']))
                       
            fw.write('\n\t\t</Links>\n\t</Composition>\n</ModelComposition>')
            fw.close()
        

            if not self._iscreate and self._datas['Model name'] != self._datas['Old name']:
                os.remove('{}{}composition.{}.xml'.format(self._datas['Path'], os.path.sep, self._datas['Old name']))