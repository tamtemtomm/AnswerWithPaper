import os, json
from Reader import ReadPDF

# @title <p> Make a journal dataset class
class JournalDataset:
  def __init__(self, filepath='./dataset/raw', export_json=None, verbose=True, **kwargs):
    self.reader = ReadPDF() 
    self.data = []
    self.text_data = []
    self.label_to_int = {'AI' : 0,
                        'Mechatronics' : 1,
                        'Robotics' : 2}
    self.export_json = export_json
    if self.export_json is not None:
      os.makedirs(export_json, exist_ok=True)

    self.verbose = verbose

  def run(self):

    if self.verbose : 
      print(f'Initializing dataset')

    for label in os.listdir('label'):

        if self.verbose : 
          print(f'Processing {label} documents...')

        for i, document_name in enumerate(os.listdir(os.path.join('label', label))):

          if self.verbose : 
            print(f'({i + 1}) {document_name}')

          document = os.path.join('label', label, document_name)
          results = self.reader.read(document)

          # Make data object and append it to data
          result = {
              'filename': document_name.split('.')[0],
              'label': self.label_to_int[label],
              'text': results,
          }
          self.data.append(result)

          # # Join the text and append it to text_data
          self.text_data.append(' '.join(result for result in results))
        
        if self.verbose : 
          print(f'------------------------------------------------------------------')

  def export(self):
    ## Save result to json
    data_object = json.dumps(self.data, indent=4)
    with open(os.path.join(self.export_json, "data.json"), "w") as outfile:
        outfile.write(data_object)
      
    text_object = json.dumps(self.text_data, indent=4)
    with open(os.path.join(self.export_json, "text.json"), "w") as outfile:
        outfile.write(text_object)

  def generate(self):
      
      self.run()

      if self.export_json is not None:
        self.export()
      
      return self.data, self.text_data