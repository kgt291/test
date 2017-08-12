import random

from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy
from nltk.corpus import names

def extract_features(word, N=2):
    last_n_letters = word[-N:]
    return {'features': last_n_letters.lower()}

if __name__=='__main__':
    male_list = [(name, 'male') for name in names.words('male.txt')]
    female_list = [(name, 'female') for name in names.words('female.txt')]
    data = (male_list+female_list)

    random.seed(5)

    random.shuffle(data)

    input_names= ['Alexander', 'Danielle', 'David', 'Cheryl']

    num_train= int(0.8*len(data))

    for i in range(1, 6):
        print('\nNumber of end letters:', i)
        features = [(extract_features(n, i), gender) for (n, gender) in data]
        train_data, test_data = features[:num_train], features[num_train:]
        classifier = NaiveBayesClassifier.train(train_data)
        accuracy = round(100*nltk_accuracy(classifier, test_data), 2)
        print('Accuracy = ' + str(accuracy) + '%')

        for name in input_names:
          print(name, '==>', classifier.classify(extract_features(name, i)))
        
