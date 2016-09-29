from system.core.model import Model
class Game(Model):
	def __init__(self):
		super(Game, self).__init__()

	def add_game(self, latlong):
		query = 'INSERT INTO games ( starting_point_lat, starting_point_long, created_at, updated_at ) VALUES ( :starting_point_lat, :starting_point_long, NOW(), NOW() )'
		data = { 'stating_point_lat': = latlong['lat'], 'starting_point_long': = latlong['long'] }
		return self.db.query_db( query, data )