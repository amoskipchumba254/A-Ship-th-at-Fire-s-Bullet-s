class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initializing statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # number of ships at the start of the game.
        self.ships_left = 3
        
        # start game in an inactive state.
        self.game_active = False
        
        # start Alien Invasion in an active state.
        self.game_active = True
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit