from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from doctorSearch.models import doctor
def doctorMain(request):
        if request.method == 'POST':
            name = request.POST.get('name')  
            area = request.POST.get('area')
            specialty = request.POST.get('specialty')
            rscore = request.POST.get('reviewscore') 
            nTrue = False
            if name != "":
                nTrue = True
            
            sTrue = False
            if specialty != "":
                sTrue = True
            aTrue = False
            if area != "":
                aTrue = True
            rTrue = False
            if rscore != "":
                rTrue = True

            #loop checks everything in database and returns corresponding
         
            if nTrue:
                if sTrue and rTrue and aTrue:
                    
                    mainDoc = doctor.objects.filter(name=name,area=area,specialty=specialty,reviewScore__gte=rscore)
                    similarDoc =  doctor.objects.filter(area=area, specialty=specialty, reviewScore__gte=rscore)
           
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif sTrue and aTrue:
                    mainDoc = doctor.objects.filter(name=name,area=area,specialty=specialty)
                    similarDoc =  doctor.objects.filter(area=area, specialty=specialty )
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
            
                elif sTrue and rTrue :
                    mainDoc = doctor.objects.filter(name=name,specialty=specialty,reviewScore__gte=rscore)
                    similarDoc =  doctor.objects.filter(specialty=specialty, reviewScore__gte=rscore)
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif aTrue and rTrue:
                    mainDoc = doctor.objects.filter(name=name,area=area,reviewScore__gte=rscore)
                    similarDoc =  doctor.objects.filter(area=area, reviewScore__gte=rscore)
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif aTrue:
                    mainDoc = doctor.objects.filter(name=name, area=area)
                    similarDoc =  doctor.objects.filter(area=area)
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif sTrue:
                    mainDoc = doctor.objects.filter(name=name, specialty=specialty)
                    similarDoc =  doctor.objects.filter(specialty=specialty)
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif rTrue:
                    mainDoc = doctor.objects.filter(name=name, reviewScore__gte=rscore).order_by('-reviewScore').values()
                    
                    similarDoc =  doctor.objects.filter(reviewScore__gte=rscore).order_by('-reviewScore').values()
                 
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                else:
                    mainDoc = doctor.objects.filter(name=name)
                    similarDoc = None
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
            else:
                if sTrue and rTrue and aTrue:
                    mainDoc = doctor.objects.filter(area=area,specialty=specialty,reviewScore__gte=rscore)
                    similarDoc =  doctor.objects.filter(area=area)
               
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif sTrue and aTrue:
                    mainDoc = doctor.objects.filter(area=area,specialty=specialty)
                    similarDoc =  doctor.objects.filter(area=area )
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif sTrue and rTrue :
                    mainDoc = doctor.objects.filter(specialty,reviewScore__gte=rscore)
                    similarDoc =  doctor.objects.filter(reviewScore__gte=rscore)
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif aTrue and rTrue:
                    mainDoc = doctor.objects.filter(area=area,reviewScore__gte=rscore)
                    similarDoc =  doctor.objects.filter( reviewScore__gte=rscore)
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif aTrue:
                    mainDoc = doctor.objects.filter( area=area)
                    similarDoc =  None
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif sTrue:
                    mainDoc = doctor.objects.filter( specialty=specialty)
                    similarDoc =  None
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                elif rTrue:
                    mainDoc = doctor.objects.filter( reviewScore__gte=rscore).order_by('-reviewScore').values()
                   
                    similarDoc =  None
                    return render(request, 'results.html', {'a' :area, 'n': name, 's':specialty, 'r' :rscore, 'test' :mainDoc, "sim":similarDoc})
                else:
                    mainDoc = None
                    similarDoc = None
        return render(request, 'mainPage.html')
