# MyApp/views.py
from django.shortcuts import render
import os
from django.conf import settings
from .Backend.predictor import predict_tumor  # use this new file

def home_view(request) :
    return render(request, 'upload.html')

from django.http import HttpResponse

def tumor_detection_view(request):
    if request.method == "POST" and request.FILES.get('image'):
        print("POST received")
        image = request.FILES['image']
        image_name = image.name
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        print("Image path:", image_path)

        with open(image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        result = predict_tumor(image_path)

        tumor = "The MRI analysis indicates the presence of abnormalities that are consistent with signs of a brain tumor. While this result does not confirm a specific diagnosis, it strongly suggests that further clinical evaluation is necessary. We recommend consulting a qualified neurologist or neuro-oncologist at the earliest opportunity. Early detection plays a vital role in determining the most effective treatment options and improving patient outcomes. Please ensure that you follow up with a medical professional for detailed imaging review, possible biopsy, and an individualized treatment plan. Remember, medical advances have significantly improved the chances of recovery and long-term management. You are not alone — timely action is your strongest ally."
        no_tumor = "Based on the analysis of your MRI image, no signs of a brain tumor have been identified. Your scan appears within normal limits, and there is no indication of any mass or abnormal growth in the brain. This is a positive outcome and suggests that there is no current evidence of tumor-related complications. However, it is always important to monitor your neurological health and consult your physician if you experience any new or unusual symptoms. Routine medical checkups and preventive care are essential to maintaining your overall well-being. Stay healthy, and thank you for using our brain tumor detection service."

        print("Prediction result:", result)

        res = tumor if result=="Tumor" else no_tumor

        return render(request, 'result.html', {
            'image_url': settings.MEDIA_URL + image_name,
            'result': result,
            "description" : res,
        })

    print("GET request or no image")
    return render(request, 'upload.html')
