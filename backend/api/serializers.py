from rest_framework import serializers
from .models import User, Competition, Score

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'email', 'password', 'account_type')

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('id', 'name', 'description', 'units', 'frequency','type_of_competition', 'end_date', 'host_id', 'completed')

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'competition_id', 'user_id', 'score', 'last_updated')