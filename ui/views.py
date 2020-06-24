from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
import os
import pickle 

model_path_pkl = os.path.join(os.getcwd(), 'pt_models', 'random_forest_clf_naive.pickle')
model_path_joblib = os.path.join(os.getcwd(), 'pt_models', 'random_forest_clf_naive.sav')


def predict_rating(request):
    if request.method == 'POST':
        review = request.POST['review']

        # from sklearn.externals import joblib
        # model = joblib.load(model_path_joblib)
        if not review.strip():
            return HttpResponseRedirect("/")

        with open(model_path_pkl, 'rb') as f:
            model = pickle.load(f)
        rating = model.predict([review])[0]
        return render(request, 'ui/show.html', {'review': review, 'value': rating})
        # return HttpResponse(f"Rating predicted for your Review is: {str(rating)}")

    elif request.method == 'GET':
        return render(request, 'ui/front.html', {})
