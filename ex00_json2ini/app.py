
import configparser
config = configparser.ConfigParser()
config['data'] ={'structure': [
    {
      "firstname" : "Jim",
      "age" : 32
    },
    {
      "firstname" : "Juvet",
      "age" : 34
    },
    {
      "firstname" : "Dylane",
      "age" : 23
    },
    {
      "firstname" : "Jean",
      "age" : 18
    }
  ]

  }
with open('data.ini', 'w') as configfile:
    config.write(configfile)











      
		