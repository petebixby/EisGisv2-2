DATABASES = {
    'default-2': {
        'dbname': 'dfgis',
        'host': 'virtualizedva.c4mbzih6i7ca.us-east-1.rds.amazonaws.com',
        'port':'5432',        
        #'ENGINE': 'django.db.backends.postgresql',
        'user': 'wn_user',
        #'password': 'haoisdfu098#jj'
        'password': ''
    },
    'default-1': {
        'dbname': 'eisgeo',
        'host': 'eisgis.c4mbzih6i7ca.us-east-1.rds.amazonaws.com',
        'port':'5432',        
        #'ENGINE': 'django.db.backends.postgresql',
        'user': 'eisgis_user',
        #'password': 'haoisdfu098#jj'
        'password': ''
    },
    'default': {
        'dbname': 'eisgeo',
        'host': 'localhost',
        'port':'5432',        
        'user': 'postgres',
        'password': ''
    },
    
}
