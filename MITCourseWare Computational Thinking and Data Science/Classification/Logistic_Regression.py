# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/lecture-slides-and-files/MIT6_0002F16_lec13.pdf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


def readFile(fileName):
    cardiacData = open(fileName, 'r')
    gender_str, age, class_travel, survived, name = [], [], [], [], []
    gender = []
    for l in cardiacData:
        l = l.split(',')
        class_travel.append(int(l[0]))
        age.append(float(l[1]))
        gender_str.append(str(l[2]))
        survived.append(int(l[3]))
        name.append(str(l[4]))


    for i in range(len(gender_str)):
        if gender_str[i] == "M":
            gender.append(1)
        else:
            gender.append(0)

    return gender, age, class_travel, survived, name


gender, age, class_travel, survived, name = readFile('TitanicPassengers.txt')

feature_list, survived_list = [], []
for i in range(len(gender)):
    feature_list.append([gender[i], age[i], class_travel[i]])
    survived_list.append([survived[i]])

X_train, X_test, Y_train, Y_test = train_test_split(feature_list, survived_list, test_size=0.2, random_state=1)
model = LogisticRegression()
model.fit(X_train, Y_train)
print "Logistic regression used: \n" + str(model)

prediction = model.predict(X_test)
print "Accuracy is: \t" + str(model.score(X_test, Y_test))

conf_mat = confusion_matrix(Y_test, prediction)
print "Confusion matrix \n" + str(conf_mat)
