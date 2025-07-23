# from django.shortcuts import render
# import pickle
# import os
# import pandas as pd
# # Create your views here.



# def predict_survival(request):
#     if request.method == 'POST':
#         model_filename = 'lr_pile.pkl'
#         model_path = os.path.join(os.path.dirname(__file__), 'models', model_filename)
#         # Load the trained model from the pickle file
#         with open(model_path, 'rb') as model_file:
#             model = pickle.load(model_file)

#         # Get user input from the form
#         ticket = int(request.POST.get('pclass'))
#         sex = request.POST.get('sex')
#         age = float(request.POST.get('age'))
#         sibsp = int(request.POST.get('sibsp'))
#         parch = int(request.POST.get('parch'))
#         fare = float(request.POST.get('fare'))
#         embarked = request.POST.get('embarked')

#         test_data = pd.DataFrame({
#                     'Sex': [sex],
#                     'Age': [age],
#                     'SibSp': [sibsp],
#                     'Parch': [parch],
#                     "Ticket":[ticket],
#                     'Fare': [fare],
#                     'Embarked': [embarked]
#                 })

#         # Make prediction
#         prediction = model.predict(test_data)[0]

#         # Render the result
#         return render(request, 'prediction_result.html', {'prediction': prediction})

#     # If the form is not submitted, render the empty form
#     return render(request, 'predict_survival.html', {'prediction': None})

from django.shortcuts import render
import pickle
import os
import pandas as pd # type: ignore

def predict_discount(request):
    if request.method == 'POST':
        model_filename = 'lr_pile.pkl'  # Change this to the name of your pickle file
        model_path = os.path.join(os.path.dirname(__file__), 'models', model_filename)
        
        # Load the trained model from the pickle file
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)

        # Get user input from the form
        # You need to update this part based on your form fields
        rating = float(request.POST.get('rating'))
        aggregate_rating = float(request.POST.get('aggregate_rating'))
        price = float(request.POST.get('price'))
        best_prices = float(request.POST.get('best_prices'))
        location_frequency_encoded = float(request.POST.get('location_frequency_encoded'))

        test_data = pd.DataFrame({
            'Rating': [rating],
            'Price': [price],
            'Best Prices': [best_prices],
            'Location_Frequency_Encoded': [location_frequency_encoded],
        })

        # Make prediction
        prediction = model.predict(test_data)[0]

        # Render the result
        return render(request, 'prediction_result.html', {'prediction': prediction})

    # If the form is not submitted, render the empty form
    return render(request, 'predict_discount.html', {'prediction': None})
