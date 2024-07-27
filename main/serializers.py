
from rest_framework import serializers
from main.models import Domaine, Branche, Qcm


class QcmSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qcm
		fields = ['branche', 'question', 'propositions']

class BrancheSerializer(serializers.ModelSerializer):
	qcms = QcmSerializer(many=True)
	class Meta:
		model = Branche
		fields = ["nom", "domaine", "qcms"]


class DomaineSerializer(serializers.ModelSerializer):
	branches = BrancheSerializer(many=True)
	class Meta:
		model = Domaine
		fields = ['nom', 'branches']

