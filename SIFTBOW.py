
import cv2
import numpy as np
import os
sift = sift = cv2.xfeatures2d.SIFT_create()
image_paths = []
path = "training"

image_pathtest = []
pathtest = "test"

#lister nos classes ici
training_names = os.listdir(path)
test_names = os.listdir(pathtest)
training_paths = []
test_paths = []
names_path = []
names_testpath = []
#Obtenir la liste de toutes les images
for p in training_names:
    training_paths1 = os.listdir("training/"+p)
    for j in training_paths1:
        training_paths.append("training/"+p+"/"+j)
        names_path.append(p)
                              
for p in test_names:
    test_paths.append("test/"+p)
    names_testpath.append(p)



#sift = cv2.xfeatures2d.SIFT_create()
print (names_path)
print (names_testpath)


descriptors_unclustered = []

dictionarySize = 3
#appel du kmeans
BOW = cv2.BOWKMeansTrainer(dictionarySize)

for p in training_paths:
    image = cv2.imread(p)
    gray = cv2.cvtColor(image, cv2.IMREAD_GRAYSCALE)
    kp, dsc= sift.detectAndCompute(gray, None)
    BOW.add(dsc)

#Création du dictionnaire des mots
dictionary = BOW.cluster()


FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or rentre dans le dictionnaire vide
flann = cv2.FlannBasedMatcher(index_params,search_params)
sift2 = cv2.xfeatures2d.SIFT_create()
bowDiction = cv2.BOWImgDescriptorExtractor(sift2, cv2.BFMatcher(cv2.NORM_L2))
bowDiction.setVocabulary(dictionary)
print ("bow dictionary", np.shape(dictionary))


#retourner les descripteurs de l'image au path
def feature_extract(pth):
    im = cv2.imread(pth, 1)
    gray = cv2.cvtColor(im,  cv2.IMREAD_GRAYSCALE)
    return bowDiction.compute(gray, sift.detect(gray))

train_desc = []
train_labels = []
i = 0
for p in training_paths:
    train_desc.extend(feature_extract(p))
    if names_path[i]=='obj1':
        train_labels.append(1)
    if names_path[i]=='obj2':
        train_labels.append(2)
    if names_path[i]=='obj3':
        train_labels.append(3)
 
    i = i+1

print ("svm items", len(train_desc), len(train_desc[0]))
count=0
svm = cv2.ml.SVM_create()

svm.train(np.array(train_desc),cv2.ml.ROW_SAMPLE, np.array(train_labels))
i=0
j=0

confusion = np.zeros((3,3))
def classify(pth):
    feature = feature_extract(pth)
    p = svm.predict(feature)
    #train_labels[count]
    #print("TotoTest",p)
    confusion[train_labels[count]-1,int(p[1][0][0])-1] = confusion[train_labels[count]-1,int(p[1][0][0])-1] +1
   
    
#partie des tests sur le dossiers test
for p in test_paths:
    classify(p)
    count+=1

def normalizeRows(M):
  som=0
  row_sums = M.sum(axis=1)
  som = M / row_sums
  return som
    
confusion = normalizeRows(confusion)

confusion = confusion.transpose()
    
print (confusion)
