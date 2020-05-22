#Author: Ori Weiss
#Version: 1.0

from FeatureExtraction import *
from Tools import *
from LabelledData import *
from Classify import *
import sys

#Accept in image path argument
if(len(sys.argv) < 2):
    print("Error: Please include image path in argument")
    exit()
if(len(sys.argv)> 2):
    print("Error: Only one argument allowed")
    exit()
imagePath = str(sys.argv[1])

#Prepare the image for analysis
plt.figure("Original Image")
try:
    plt.imshow(cv2.imread(imagePath))
except:
    print("Error: Image path is not valid")
    exit()
result, num_features = image_prep(imagePath)
plt.figure("Prepped Image")
plt.imshow(result)


#Extract the area and perimeter for each cell
areaArray, perimArray= extract_area_perim(result, num_features)

#Remove empty first elements
areaArray.pop(0)
perimArray.pop(0)


#Get the circularity for each cell
circularityArray = extract_circularity(areaArray, perimArray)

#Get the relative area and perimeter of each cell
relativeAreaArray, relativePerimArray = convert_to_relative(areaArray, perimArray)


#displayAllImages(result, num_features) NEEDS FIXING

#Get preloaded data
sickleData = getSickleData()
healthyData = getHealthyData()

#Combine the two training data arrays into one array
combinedHealthySickle = sickleData
for i in range(len(healthyData)):
    combinedHealthySickle.append(healthyData[i])

#Classify each cell
classified = KNNClassifier(combinedHealthySickle,
                           [1] * 12 + [0] * 40,
                           convertTo3D(relativeAreaArray, relativePerimArray, circularityArray),
                           3)


#Create a 3D plot
fig = plt.figure("Classified Graph")
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Area')
ax.set_ylabel('Perimeter')
ax.set_zlabel('Circularity')

#Count the number of sickle cells & plot them in red
numSickleCells = 0
for i in range(len(classified)-1, -1, -1):
    if classified[i] == 1:
        numSickleCells += 1
        ax.scatter(relativeAreaArray.pop(i), relativePerimArray.pop(i), circularityArray.pop(i), c="red")

#plot the rest of the healthy cells
ax.scatter(relativeAreaArray, relativePerimArray, circularityArray)

#Place an image of the sickle cells
displaySickleImage(result, classified)

#PrintStatistics
print("Total Cells: ", num_features)
print("Sickle Cells: ", numSickleCells)
print("Healthy Cells: ", num_features-numSickleCells)
print("Percent Sickle: ", (numSickleCells/num_features)*100, "%")
print("Percent Healthy: ", ((num_features-numSickleCells)/num_features)*100, "%")


#Display All images
plt.show()




