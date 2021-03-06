  
from django.contrib.auth.models import User
from rest_framework import serializers
from User.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from User.models import User
from Registeration.models import Student
class UserDetailSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ['username']
		

	


class CustomUserSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'password2','name']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = User(
					email=self.validated_data['email'],
					username=self.validated_data['username'],
					name = self.validated_data['name']
				)
		student = Student(
			studentID = self.validated_data['username'],
			name = self.validated_data['name']
		)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()
		student.save()

		return account

