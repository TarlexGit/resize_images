from django.shortcuts import render
from .models import Image_model
from django.views.generic.base import TemplateView
from django.http import Http404, HttpResponseRedirect, request 
from .forms import AddImageForm 

from PIL import Image 
from io import BytesIO
from django.core.files.base import ContentFile
import requests


class GetImages(TemplateView):  
    template_name = 'index.html' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Image_model.objects.all()
        return context
   
def add_image(request):  
    if request.method == 'POST': 
        form = AddImageForm(request.POST, request.FILES) 
        if form.is_valid():
            instance = form.save(commit=False)
            image_file = form.cleaned_data['image_file']
            url = form.cleaned_data['url']

            if url and image_file:
                return HttpResponseRedirect('/images/both/')

            elif not url and not image_file:
                return HttpResponseRedirect('/images/both/')

            elif url: 
                response = requests.get(url)
                url_img = Image.open(BytesIO(response.content))    
                thumb_io = BytesIO()

                # convert for good save 
                # circumventing the error "cannot write mode RGBA as JPEG"
                rgb_im = url_img.convert('RGB')

                rgb_im.save(thumb_io, "JPEG", quality=60)

                img_name_from_url = url.split('/')[-1]

                instance.image_file.save(img_name_from_url, ContentFile(thumb_io.getvalue()), save=False)
                instance.save()
            elif image_file:
                form.save() 
            last = Image_model.objects.last()
            get_last = last.get_absolute_url()
            return HttpResponseRedirect(get_last) 
    else:
        form = AddImageForm() 
    return render(request, 'add_form.html', {'form': form})

def except_both(request):
    return render(request, template_name='both.html')
   

from .services import resize_both
class ImageDetail(TemplateView):    
    template_name = 'detail_page.html'

    def get_context_data(request, pk):
        try:
            image_id=Image_model.objects.get(pk=pk)
        except Image_model.DoesNotExist:
            raise Http404("Image does not exist")
        context={'image':image_id,} 
        return context

    def post(self, request, pk):
        if request.method == 'POST': 
            width = None
            height = None
            form = request.POST 

            obj = Image_model.objects.get(pk=pk)
      
            img_open = str(obj.image_file) 

            if form['width'] != "":
                try:
                    width = int(form['width'])
                except:
                    return HttpResponseRedirect('/images/both/')
                
            if form['height'] != "":
                try:
                    height = int(form['height'])
                except:
                    return HttpResponseRedirect('/images/both/')
            try:
                print('ресайзим')
                resize_both(img_file=img_open, width=width, height=height)
                print('закончили')
            except: 
                return HttpResponseRedirect('/images/both/')
            
            last = Image_model.objects.last()
            get_last = last.get_absolute_url()
            return HttpResponseRedirect(get_last)  
 

