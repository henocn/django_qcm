# from django.shortcuts import render
# from django.http import HttpResponse
# from main.henoc import verifierNombre, appreciation
# from main.models import Qcm, Branche


# def accueil(request):
# 	if request.method == "POST":
# 		branche = request.POST.get("branche")
# 		if branche == "toutes":
# 			qcms = list(Qcm.objects.all())
# 		else:
# 			qcms = list(Qcm.objects.filter(branche__nom=branche))
# 	else:
# 		qcms = list(Qcm.objects.all())

# 	qcms = verifierNombre(qcms)
# 	branches = Branche.objects.all()

# 	return render(request, "main/index.html", {"QCM":qcms,"branches":branches})

# def corriger(request):

# 	if request.method == 'POST':
# 		qcm_reponses = {}
# 		for qcm in Qcm.objects.all():
# 			qcm_id = str(qcm.id)
# 			select = request.POST.get(qcm_id)
# 			if select and qcm.reponse()[0] != select:
# 				qcm_reponses[qcm_id] = select

# 		note = 20
# 		qcms = []
# 		for id, reponse in qcm_reponses.items():
# 			qcms.append(Qcm.objects.get(id=id))
# 			note -= 2.25

# 		appr = appreciation(note)
# 		return render(request, "main/correction.html", {"note": note, "appr":appr, "QCM": qcms})
# 	else:
# 		return HttpResponse("Méthode non autorisée")

###########################################################################

from rest_framework.viewsets import ReadOnlyModelViewSet
from main.serializers import DomaineSerializer, BrancheSerializer, QcmSerializer
from main.models import Domaine, Branche, Qcm
from main.henoc import verifierNombre


class DomaineViewset(ReadOnlyModelViewSet):
	serializer_class = DomaineSerializer

	def get_queryset(self):
		return Domaine.objects.all()

class BrancheViewset(ReadOnlyModelViewSet):
	serializer_class = BrancheSerializer

	def get_queryset(self):
		return Branche.objects.all()

class QcmViewset(ReadOnlyModelViewSet):
	serializer_class = QcmSerializer 

	def get_queryset(self):
		qcms = Qcm.objects.all()
		branche = self.request.GET.get("branche")
		if branche is not None:	
			qcms = qcms.filter(branche__nom=branche)
		qcms = verifierNombre(list(qcms))
		return qcms