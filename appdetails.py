from flask import Flask,render_template,url_for
from aylienapiclient import textapi
from flask_bootstrap import Bootstrap
import os
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
Bootstrap(app)
def grahicsreview(review_string):
    if "graphics" in review_string :
        return 1
    return 0
def controlreview(review_string):
    if review_string.find("battery") != -1:
        return 1
    return 0
def powerreview(review_string):
    if review_string.find("power") != -1:
        return 1
    return 0
def userfriendly(review_string):
    if review_string.find("user friendly") != -1:
        return 1
    return 0
def crashreview(review_string):
    if review_string.find("crash") != -1:
        return 1
    return 0
def adsreview(review_string):
    if review_string.find("ads") != -1:
        return 1
    return 0
def advertisedreview(review_string):
    if review_string.find("advertise") != -1:
        return 1
    return 0
@app.route('/')
def hello_world():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fb.png')
    file =open("/home/zaoad/PycharmProjects/untitled2/a.txt")
    client = textapi.Client("402c4f5d", "c4ce28551be5a50a9299d5badb825287")
    file_string=str(file.read())
    file_string=file_string.split('.')
    positive_sentiment=0.0
    negative_sentiment=0.0
    positive_review_number=0
    negative_review_number=0
    graphics_upvote=0
    graphics_downvote=0
    control_upvote=0
    control_downvote=0
    power_consume_upvote=0
    power_consume_downvote=0
    userfriendly_upvote=0
    userfriendly_downvote=0
    advertise_upvote=0
    advertise_downvote=0
    crash_upvote=0
    crash_downvote=0
    i=0
    while i<len(file_string):
        reviewstring=file_string[i]
        sentiment=client.Sentiment({'text': file_string[i]})
        positive=0
        negative=0
        if(str(sentiment['polarity'])=='negative'):
            negative=1
            print (str(sentiment['text'])+' is ' +'negative')
            negative_sentiment+=float(str(sentiment['polarity_confidence']))
            s="{0:.2f}".format(negative_sentiment)
            negative_sentiment=float(s)
            negative_review_number+=1
        elif (str(sentiment['polarity']) == 'positive'):
            positive=1
            print(str(sentiment['text']) + ' is ' + 'positive')
            positive_sentiment += float(str(sentiment['polarity_confidence']))
            s = "{0:.2f}".format(positive_sentiment)
            positive_sentiment = float(s)
            positive_review_number += 1
        if(grahicsreview(reviewstring)):
            if(positive==1):
                graphics_upvote+=1
            elif(negative==1):
                graphics_downvote+=1
        if(controlreview(reviewstring)):
            if(positive==1):
                control_upvote+=1
            elif(negative==1):
                control_downvote+=1
        if(powerreview(reviewstring)):
            if(positive==1):
                power_consume_downvote+=1
            elif(negative==1):
                power_consume_upvote+=1
        if(crashreview(reviewstring)):
            if(positive==1):
                crash_downvote+=1
            elif(negative==1):
                crash_upvote+=1
        if(userfriendly(reviewstring)):
            if(positive==1):
                userfriendly_upvote+=1
            if(negative==1):
                userfriendly_downvote+=1
        if(adsreview(reviewstring)):
            if(positive==1):
                advertise_downvote+=1
            elif(negative==1):
                advertise_upvote+=1
        if(advertisedreview(reviewstring)):
            if(positive==1):
                advertise_downvote+=1
            elif(negative==1):
                advertise_upvote+=1
        i=i+1
    if(negative_review_number==0):
        negative_review_number=1
    if(positive_review_number==0):
        positive_review_number=1
    total=positive_review_number+negative_review_number
    average_negative_sentiment=negative_sentiment/negative_review_number
    average_positive_sentiment=positive_sentiment/positive_review_number
    average_positive_sentiment=average_positive_sentiment*positive_review_number/total
    average_negative_sentiment=average_negative_sentiment*negative_review_number/total
   # return 'positive review : '+str(average_positive_sentiment)+'\n'+'negative review : '+str(average_negative_sentiment)
    return render_template(
        'appdetailspage.html', positive_senti=average_positive_sentiment,negative_senti=average_negative_sentiment,user_image = full_filename,graphicsupvote=graphics_upvote,graphicsdownvote=graphics_downvote,controlupvote=control_upvote,controldownvote=control_downvote,
        powerconsumeupvote=power_consume_upvote,powerconsumedownvote=power_consume_downvote,crashupvote=crash_upvote,crashdownvote=crash_downvote,userfriendlyupvote=userfriendly_upvote,userfriendlydownvote=userfriendly_downvote,advertiseupvote=advertise_upvote,advertisedownvote=advertise_downvote
    )
if __name__ == '__main__':

    app.run()
