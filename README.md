# SalsaApp

In this project we will create annotations/labels for cuban salsa videos. Salsa is a couple dance where movement patterns appear in counting of 4 steps.
The elementary unit of movement (word) is assigned to one of these steps, while figures (sentences) correspond to a sequential arrangement of one or more 4 steps counting. 

Information of the dancing couple in the videos can be simplied by capturing the key points with Openpose. 

Supervised learning: learn to match skeleton with "labels", which model?
 * Features are: coordinates of joints of 2 persons
 * Labels are: label at "1 step counting" or/and label "4 steps counting"

Semi-supervised

With this structure of words and sentences the problem could be tackled with NLP tools. Learning the embedding of a sentence. 

We expect 2 main outputs:

1. Given a video: obtain the annotations at different levels (words or sentences)
1. Given a seed movement: generate words or sentences that can continue the dance in autonomus way

## Tasks having to do with the project building
  
  1. Git repo.
   * Create repo
   * Create branches
   * Procedure for git use 
   * Git and Collab connection
   * Git and google drive

## Theory to check
  1. Openpose model and limitations. Can be improved for a dance couple?
  2. 
  
## Tasks 
### Preprocessing
1. Creating skleton files (JSON):
2. Processing JSON:
* Assing ID for the FO and LE 
* Track the ID of each person (Maybe object detection)
* 

### Training model XXX





## Milestones
