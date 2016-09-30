from system.core.model import Model
class Pin(Model):
	def __init__(self):
		super(Pin, self).__init__()

	def add_pin(self, game_info):
		query = 'INSERT INTO pin ( latitude, longitude, game_id, created_at, updated_at ) VALUES ( :latitude, :longitude, :game_id, NOW(), NOW() )'
		data = { 'latitude': game_info['latitude'], 'longitude': game_info['longitude'], 'game_id': game_info['game_id'] }
		return self.db.query_db( query, data )

	def get_game_by_id(self, game_id):
		query = 'SELECT * FROM pins JOIN games ON games.id = pins.game_id WHERE games.id = :games.id'
		data = { 'games.id': game_id }
		return self.db.query_db( query, data )