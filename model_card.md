# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

The recommender takes genre, accoustic, energy, and mood of song to generate song recommendations based on User profile with these attributes. This is mainly for classroom exploration since in the real world the dataset would be much bigger. An assumption made here is that the Userprofiles are defined well and are not empty. 

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

The features used here are genre, mood, energy, and acoustic. The user preference also considers these attributes. The model compares user preference with the song atributes, and aggregates a total score based on matching characteristics. I tinkered with the weights for each attribute. 

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

There are 18 songs. A wide array of moods and genre are represented here, inlcuding moody, sad, jazz, etc. 
## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---
The model works well with recommending the top 2 songs, but seems to struggle in the other songs. It predicts high energy songs well. 

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---
A song with the right genre but terrible energy/mood will often outscore a perfect-energy song from the wrong genre. This will affect niche genre preferences like classical. 


## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

I tested the following profiles:         
"High-Energy Pop":   high_energy_pop,
        "Chill Lofi":        chill_lofi,
        "Deep Intense Rock": deep_intense_rock
I looked at the top suggestion to see if the song corresponds to the user profile. What surprised me was when doubiling the score for energy and halfing the score for energy, I got the same score and the same song recommendations. 

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

Will look to tinker with niche genre profiles to see how the model performs. I can try assigning equal weights to each attribute for a balanced song recommendation list. Increase size and representation of dataset.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I got get a sense of how recommender systems work, like giving higher weightage for certain attributes like Genre. The difference between collaborating- filtering and individualized filtering. It is interesting to see how songs are associated with a wide array of meta data to be used for recommendation systems. The AI helped me to understand the implementations of the functions. I just wonder how music recommendation apps store all this data and cater to every single user. Just trying to visualize their infrastructre. 