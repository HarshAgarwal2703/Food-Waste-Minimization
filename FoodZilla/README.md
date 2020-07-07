# Parsec 2020
Reducing food waste

## Setup
If you have miniconda3 and it says conda not found
    
    export PATH="/Users/username/miniconda3/bin:$PATH" 

Create virtual environment (only need to do once)
    
    conda update conda
    
    conda create -n venv_name python=3.6

To activate virtual environment (do every time before running)
    
    source activate venv_name
    
    pip install -r requirements.txt

Run server
    
    python3 manage.py runserver

That way, it's in a separate virtual environment

## Problem Statement

The Grapes of Wrath is a novel by John Steinbeck about the hardships farmers had to endure during the Dust Bowl and Great Depression. At one point, the Californian farmers put their crops in a giant mountain in the field and refuse to give the crops away. Instead,  they light the food on fire because they cannot sell it. The choice between burning the crops and donating them to those in need is one that many modern people face everyday. Restaurants, when reaching the end of their raw material’s lifespan, often throw away their materials without considering the alternative or mitigating procedures. A pressing social issue we don’t talk about often is that 63 million tons of food (165 billion dollars worth) is wasted annually and  40% of that waste comes from restaurants throwing away unused raw materials (ReFED). Often, restaurants order more food than they need in anticipation of demand from customers. However, without solid numerical backing, the estimates taken by restaurants owners are often grossly overshot.  In essence, restaurants are “burning” their food instead of connecting with those who need it. Our product, Bona, is a software as a service that alleviates this problem. First, restaurants will save money by using Machine Learning to predict demand and waste from the past. We use data logged and seasonality prediction from previous months to predict both the demand and the wastage in the upcoming months. Using computer vision and object recognition techniques, we keep track of how much food is unused at the end of inventory periods. We then advise the restaurant owner to order an adjusted value. Second, the platform gives people who need food the most and restaurants a way to connect when their inventory reflects the wastage. When restaurants have excess food, it will post on the website where anyone can reach out to the restaurant to pick up the food at an agreed upon location. Our solution reduces food waste two-fold, by using Machine Learning techniques to intelligently predict future orders, and in the case of wastage, provide a much needed platform for restaurant owners to distribute their food. 

## Architecture Outline

Bona is composed of several moving parts. First, we use Computer Vision and object detection using Yolo and OpenCV to keep track of the remaining inventory of raw materials. For example, our camera will track how many apples are remaining at the end of the week when they go bad. Then, the system will update our database of timestamps with the wastage amount. Next, we require input from the restaurant owner about their inventory orders. By gathering this data, we can apply Machine Learning using the Facebook Prophet API to predict both the inventory order in the coming month, and the wastage in the coming month. Using these predictions, we can advise the owner on how much they should order to minimize their food wastage for the coming month. Once the owner orders their new inventory, they will add the number back into the database, thereby completing the loop and allowing our Machine Learning to better learn and predict future demand and wastage. This feature is extremely important in giving owners a gauge of how much yield protection they should use. 
Second, there are always unpredictable times when restaurant demand will be low. This will cause unexpected wastage. Bona provides a social platform for owners to connect to those in need who reach out and meet with the owners. This way, even if there is unexpected wastage, it will not be thrown out by the owners. 

## Usage
The restaurant owner can use our service by going to our website and first entering how much inventory they ordered for a specific product that month. In the background, the system will be taking snapshots of how much inventory there is and updating the database. As a result, when the restaurant owner requests to know how much inventory they should order next term, the model is already trained and will output a more accurate answer. Furthermore, if the restaurant has excess food, they can post on the site for people in need to be notified about. The platform provides a way for the restaurant to connect with those who need food the most. The benefit of the system is that it is automated, and only requires the initial inventory input. The model will train itself and blackbox the Machine Learning and output useful information. 

## Future expansion
We bounded our solution to apples. However, Bona is a general purpose inventory controller. We can expand it to any generic raw material such as oranges, onions, carrots, etc. As a result, we simply need more infrastructure to support monitoring the various inventory. By adding more cameras, we can control the inventory and retrain our model constantly. This would result in even more accurate predictions. As restaurants spend more time on Bona, they will drive down their error in ordering and reduce their waste. Currently, we have our website focusing on a single restaurant. However, it is a simple matter to increase the network into a marketplace for an arbitrary number of restaurants. This way, in any given locale, people in need will have access to various points of food. We simply need more restaurants to join the marketplace with the incentive that they will both save money and reduce food waste. This is a win-win situation for both restaurants and those in need. By applying Machine Learning methods in both Object Detection and seasonality prediction, Bona hopes to fill a hole in the restaurant business and fill the hungry stomachs of those in need. 

