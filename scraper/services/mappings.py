
# Mapping for 'players' table
# Corresponds to 'stats' (standard) table in Fbref
PLAYER_MAPPING = {
    'Player': 'name',
    'Nation': 'nation',
    'Pos': 'position',
    'Age': 'age',
    'MP': 'matches_played',
    'Starts': 'starts',
    'Min': 'minutes_played',
    '90s': 'nineties',
    'Gls': 'goals',
    'Ast': 'assists',
    'G+A': 'goals_plus_assists',
    'G-PK': 'non_penalty_goals', # This is actually G-PK in Fbref, which is non-penalty goals
    'PK': 'penalties_made',
    'PKatt': 'penalties_attempted',
    'CrdY': 'yellow_cards',
    'CrdR': 'red_cards',
    'xG': 'xg',
    'npxG': 'npxg',
    'xAG': 'xag',
    'npxG+xAG': 'npxg_plus_xag',
    'PrgC': 'progressive_carries',
    'PrgP': 'progressive_passes',
    'PrgR': 'progressive_passes_received',
    
    # Per 90 stats
    'Gls per 90': 'goals_per_90',
    'Ast per 90': 'assists_per_90',
    'G+A per 90': 'g_plus_a_per_90',
    'G-PK per 90': 'g_minus_pk_per_90',
    'xG per 90': 'xg_per_90',
    'xAG per 90': 'xag_per_90',
    'xG+xAG': 'xg_plus_xag_per_90',
    'npxG per 90': 'npxg_per_90',
    'npxG+xAG per 90': 'npxg_plus_xag_per_90',
    
    # Custom/Extra fields
    'stats_Squad': 'team' 
}

# Mapping for 'stats_shooting' table
SHOOTING_MAPPING = {
    'Gls': 'goals',
    'Sh': 'shots',
    'SoT': 'shots_on_target',
    'SoT%': 'sot_percent',
    'Sh/90': 'shots_per_90',
    'SoT/90': 'sot_per_90',
    'G/Sh': 'goals_per_shot',
    'G/SoT': 'goals_per_sot',
    'Dist': 'avg_dist',
    'FK': 'free_kicks',
    'PK': 'pk_made',
    'PKatt': 'pk_att',
    'xG': 'xg',
    'npxG': 'npxg',
    'npxG/Sh': 'npxg_per_shot',
    'G-xG': 'g_minus_xg',
    'np:G-xG': 'npg_minus_npxg'
}

# Mapping for 'stats_goalkeeping' table
GOALKEEPER_MAPPING = {
    'GA': 'goals_against',
    'PKga': 'pk_allowed',
    'FK': 'free_kicks', 
    'CK': 'corner_kicks',
    'OG': 'own_goals',
    'PSxG': 'psxg',
    'PSxG/SoT': 'psxg_per_sot',
    'PSxG+/-': 'psxg_plus_minus',
    '/90': 'psxg_per_90', 
    'Cmp': 'launched_completed',
    'Att': 'launched_attempted',
    'Cmp%': 'launched_pct',
    
    'PasAtt': 'passes_attempted', 
    'Thr': 'throws_attempted',
    'Launch%': 'launch_pct',
    'AvgLen': 'avg_length',
    
    'GK_Att': 'goal_kicks_attempted',
    'GK_Launch%': 'goal_kicks_pct',
    'GK_AvgLen': 'goal_kicks_avg_length',
    
    'Opp': 'crosses_faced',
    'Stp': 'crosses_stopped',
    'Stp%': 'crosses_stopped_pct',
    
    '#OPA': 'sweeper_actions',
    '#OPA/90': 'sweeper_per_90',
    'AvgDist': 'sweeper_avg_dist'
}

# Mapping for 'stats_passing' table
PASSING_MAPPING = {
    'Cmp': 'completed',
    'Att': 'attempted',
    'Cmp%': 'completion_pct',
    'TotDist': 'total_distance',
    'PrgDist': 'progressive_distance',
    'Short_Cmp': 'short_completed',
    'Short_Att': 'short_attempted',
    'Short_Cmp%': 'short_pct',
    'Med_Cmp': 'medium_completed',
    'Med_Att': 'medium_attempted',
    'Med_Cmp%': 'medium_pct',
    'Long_Cmp': 'long_completed',
    'Long_Att': 'long_attempted',
    'Long_Cmp%': 'long_pct',
    'Ast': 'assists',
    'xAG': 'xag', 
    'xA': 'expected_assists',
    'A-xAG': 'a_minus_xag',
    'KP': 'key_passes',
    '1/3': 'final_third',
    'PPA': 'pen_area',
    'CrsPA': 'cross_pen_area',
    'PrgP': 'progressive_passes'
}

# Mapping for 'stats_passing_types' table
PASS_TYPES_MAPPING = {
    'Att': 'attempted',
    'Live': 'live',
    'Dead': 'dead',
    'FK': 'free_kicks',
    'TB': 'through_balls',
    'Sw': 'switches',
    'Crs': 'crosses',
    'TI': 'throw_ins',
    'CK': 'corners',
    'In': 'in_corners',
    'Out': 'out_corners',
    'Str': 'straight_corners',
    'Cmp': 'completed',
    'Off': 'offsides',
    'Blocks': 'blocked'
}

# Mapping for 'stats_gca' table
GCA_MAPPING = {
    'SCA': 'sca',
    'SCA90': 'sca_per_90',
    'SCA_PassLive': 'sca_live',
    'SCA_PassDead': 'sca_dead',
    'SCA_TO': 'sca_takeon',
    'SCA_Sh': 'sca_shot',
    'SCA_Fld': 'sca_fouled',
    'SCA_Def': 'sca_defense',
    'GCA': 'gca',
    'GCA90': 'gca_per_90',
    'GCA_PassLive': 'gca_live',
    'GCA_PassDead': 'gca_dead',
    'GCA_TO': 'gca_takeon',
    'GCA_Sh': 'gca_shot',
    'GCA_Fld': 'gca_fouled',
    'GCA_Def': 'gca_defense'
}

# Mapping for 'stats_defense' table
DEFENSE_MAPPING = {
    'Tkl': 'tackles',
    'TklW': 'tackles_won',
    'Def 3rd': 'tackles_def_3rd',
    'Mid 3rd': 'tackles_mid_3rd',
    'Att 3rd': 'tackles_att_3rd',
    'Tkl_Drib': 'dribblers_tackled', 
    'Att_Drib': 'dribbles_challenged',
    'Tkl%': 'dribbles_tackled_pct',
    'Lost': 'challenges_lost',
    'Blocks': 'blocks',
    'Sh': 'blocked_shots',
    'Pass': 'blocked_passes',
    'Int': 'interceptions',
    'Tkl+Int': 'tackles_interceptions',
    'Clr': 'clearances',
    'Err': 'errors'
}

# Mapping for 'stats_possession' table
POSSESSION_MAPPING = {
    'Touches': 'touches',
    'Def Pen': 'touches_def_pen', 
    'Def 3rd': 'touches_def_3rd',
    'Mid 3rd': 'touches_mid_3rd',
    'Att 3rd': 'touches_att_3rd',
    'Att Pen': 'touches_att_pen',
    'Live': 'touches_live',
    'Att': 'takeons_attempted',
    'Succ': 'takeons_won',
    'Succ%': 'takeons_won_pct',
    'Tkld': 'takeons_tackled',
    'Tkld%': 'takeons_tackled_pct',
    'Carries': 'carries',
    'TotDist': 'carries_dist',
    'PrgDist': 'carries_prog_dist',
    'PrgC': 'progressive_carries',
    '1/3': 'carries_final_third',
    'CPA': 'carries_pen_area',
    'Mis': 'miscontrols',
    'Dis': 'dispossessed',
    'Rec': 'passes_received',
    'PrgR': 'prog_passes_received'
}

# Configuration combining Stat Name (from scraper loop) -> (Table Name, Column Mapping)
STAT_TO_DB_CONFIG = {
    'stats': ('players', PLAYER_MAPPING),
    'shooting': ('stats_shooting', SHOOTING_MAPPING),
    'keepers': ('stats_goalkeeping', GOALKEEPER_MAPPING),
    'keepersadv': ('stats_goalkeeping', GOALKEEPER_MAPPING),
    'passing': ('stats_passing', PASSING_MAPPING),
    'passing_types': ('stats_passing_types', PASS_TYPES_MAPPING),
    'gca': ('stats_gca', GCA_MAPPING),
    'defense': ('stats_defense', DEFENSE_MAPPING),
    'possession': ('stats_possession', POSSESSION_MAPPING)
}
