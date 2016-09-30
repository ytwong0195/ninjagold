from system.core.model import Model
class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def add_user(self, info):
		query = 'INSERT INTO users ( name, email, created_at, updated_at ) VALUES ( :name, :email, NOW(), NOW() )'
		data = { 'name': info['name'], 'email': info['email'] }
		return self.db.query_db( query, data )

	def get_user(self, user_email):
		query = 'SELECT * FROM users WHERE email = :email'
		data = { 'email': user_email }
		return self.db.query_db( query, data )
