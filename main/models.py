from django.db import models
import random

from main.henoc import presence


class Domaine(models.Model):
	nom = models.CharField(max_length=64)

	def __str__(self):
		return self.nom


class Branche(models.Model):
	nom = models.CharField(max_length=64)
	domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name='branches')

	def __str__(self):
		return self.nom


class Qcm(models.Model):
	branche = models.ForeignKey(Branche, on_delete=models.CASCADE, related_name='qcms')
	question = models.TextField()
	propositions = models.JSONField()

	def __str__(self):
		return self.question

	def reponse (self):
		propositions = list(self.propositions.items())
		for proposition in propositions:
			if proposition[1] == "vrai" or proposition[1] == "Vrai":
				return proposition


	def generate(self):
		propositions = random.sample(list(self.propositions.items()), 4)

		if not presence(propositions):
			propositions[random.choice([0,1,2,3])] = self.reponse()

		propositions = dict(propositions)

		return propositions
