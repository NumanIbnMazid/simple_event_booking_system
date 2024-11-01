# Event Booking System

## User Credentials

### Admin User

Email: admin@admin.com
Password: admin

### Regular User

Email: user1@user.com
Password: password@123

### VIP User
Email: user_vip@user.com
Password: password@123


## API Documentation

The Project is using swagger for API Documentation.
Please Navigate to:
- http://127.0.0.1:8000/swagger/
- http://127.0.0.1:8000/redoc/


API Schema:

```json
{
   "swagger":"2.0",
   "info":{
      "title":"`Event Booking System` Backend API",
      "description":"API Documentation for `Event Booking System`",
      "termsOfService":"https://www.google.com/policies/terms/",
      "contact":{
         "email":"numanibnmazid@gmail.com"
      },
      "license":{
         "name":"BSD License"
      },
      "version":"v1"
   },
   "host":"127.0.0.1:8000",
   "schemes":[
      "http"
   ],
   "basePath":"/api",
   "consumes":[
      "application/json"
   ],
   "produces":[
      "application/json"
   ],
   "securityDefinitions":{
      "Bearer":{
         "type":"apiKey",
         "name":"Authorization",
         "in":"header"
      }
   },
   "security":[
      {
         "Bearer":[
            
         ]
      }
   ],
   "paths":{
      "/auth/login/":{
         "post":{
            "operationId":"auth_login_create",
            "description":"",
            "parameters":[
               {
                  "name":"data",
                  "in":"body",
                  "required":true,
                  "schema":{
                     "$ref":"#/definitions/CustomAuthToken"
                  }
               }
            ],
            "responses":{
               "201":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/CustomAuthToken"
                  }
               }
            },
            "tags":[
               "auth"
            ]
         },
         "parameters":[
            
         ]
      },
      "/auth/logout/":{
         "post":{
            "operationId":"auth_logout_create",
            "description":"",
            "parameters":[
               
            ],
            "responses":{
               "201":{
                  "description":""
               }
            },
            "tags":[
               "auth"
            ]
         },
         "parameters":[
            
         ]
      },
      "/auth/logoutall/":{
         "post":{
            "operationId":"auth_logoutall_create",
            "description":"Log the user out of all sessions\nI.E. deletes all auth tokens for the user",
            "parameters":[
               
            ],
            "responses":{
               "201":{
                  "description":""
               }
            },
            "tags":[
               "auth"
            ]
         },
         "parameters":[
            
         ]
      },
      "/bookings/":{
         "get":{
            "operationId":"bookings_list",
            "description":"A viewset for creating and retrieving bookings.",
            "parameters":[
               
            ],
            "responses":{
               "200":{
                  "description":"",
                  "schema":{
                     "type":"array",
                     "items":{
                        "$ref":"#/definitions/Booking"
                     }
                  }
               }
            },
            "tags":[
               "bookings"
            ]
         },
         "post":{
            "operationId":"bookings_create",
            "description":"A viewset for creating and retrieving bookings.",
            "parameters":[
               {
                  "name":"data",
                  "in":"body",
                  "required":true,
                  "schema":{
                     "$ref":"#/definitions/Booking"
                  }
               }
            ],
            "responses":{
               "201":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/Booking"
                  }
               }
            },
            "tags":[
               "bookings"
            ]
         },
         "parameters":[
            
         ]
      },
      "/bookings/{id}/":{
         "get":{
            "operationId":"bookings_read",
            "description":"A viewset for creating and retrieving bookings.",
            "parameters":[
               
            ],
            "responses":{
               "200":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/Booking"
                  }
               }
            },
            "tags":[
               "bookings"
            ]
         },
         "put":{
            "operationId":"bookings_update",
            "description":"A viewset for creating and retrieving bookings.",
            "parameters":[
               {
                  "name":"data",
                  "in":"body",
                  "required":true,
                  "schema":{
                     "$ref":"#/definitions/Booking"
                  }
               }
            ],
            "responses":{
               "200":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/Booking"
                  }
               }
            },
            "tags":[
               "bookings"
            ]
         },
         "patch":{
            "operationId":"bookings_partial_update",
            "description":"A viewset for creating and retrieving bookings.",
            "parameters":[
               {
                  "name":"data",
                  "in":"body",
                  "required":true,
                  "schema":{
                     "$ref":"#/definitions/Booking"
                  }
               }
            ],
            "responses":{
               "200":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/Booking"
                  }
               }
            },
            "tags":[
               "bookings"
            ]
         },
         "delete":{
            "operationId":"bookings_delete",
            "description":"A viewset for creating and retrieving bookings.",
            "parameters":[
               
            ],
            "responses":{
               "204":{
                  "description":""
               }
            },
            "tags":[
               "bookings"
            ]
         },
         "parameters":[
            {
               "name":"id",
               "in":"path",
               "description":"A unique integer value identifying this booking.",
               "required":true,
               "type":"integer"
            }
         ]
      },
      "/events/":{
         "get":{
            "operationId":"events_list",
            "description":"ViewSet for managing events. Only admins can create and modify events.",
            "parameters":[
               
            ],
            "responses":{
               "200":{
                  "description":"",
                  "schema":{
                     "type":"array",
                     "items":{
                        "$ref":"#/definitions/Event"
                     }
                  }
               }
            },
            "tags":[
               "events"
            ]
         },
         "post":{
            "operationId":"events_create",
            "description":"ViewSet for managing events. Only admins can create and modify events.",
            "parameters":[
               {
                  "name":"data",
                  "in":"body",
                  "required":true,
                  "schema":{
                     "$ref":"#/definitions/Event"
                  }
               }
            ],
            "responses":{
               "201":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/Event"
                  }
               }
            },
            "tags":[
               "events"
            ]
         },
         "parameters":[
            
         ]
      },
      "/events/{id}/":{
         "get":{
            "operationId":"events_read",
            "description":"ViewSet for managing events. Only admins can create and modify events.",
            "parameters":[
               
            ],
            "responses":{
               "200":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/Event"
                  }
               }
            },
            "tags":[
               "events"
            ]
         },
         "put":{
            "operationId":"events_update",
            "description":"ViewSet for managing events. Only admins can create and modify events.",
            "parameters":[
               {
                  "name":"data",
                  "in":"body",
                  "required":true,
                  "schema":{
                     "$ref":"#/definitions/Event"
                  }
               }
            ],
            "responses":{
               "200":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/Event"
                  }
               }
            },
            "tags":[
               "events"
            ]
         },
         "patch":{
            "operationId":"events_partial_update",
            "description":"ViewSet for managing events. Only admins can create and modify events.",
            "parameters":[
               {
                  "name":"data",
                  "in":"body",
                  "required":true,
                  "schema":{
                     "$ref":"#/definitions/Event"
                  }
               }
            ],
            "responses":{
               "200":{
                  "description":"",
                  "schema":{
                     "$ref":"#/definitions/Event"
                  }
               }
            },
            "tags":[
               "events"
            ]
         },
         "delete":{
            "operationId":"events_delete",
            "description":"ViewSet for managing events. Only admins can create and modify events.",
            "parameters":[
               
            ],
            "responses":{
               "204":{
                  "description":""
               }
            },
            "tags":[
               "events"
            ]
         },
         "parameters":[
            {
               "name":"id",
               "in":"path",
               "description":"A unique integer value identifying this event.",
               "required":true,
               "type":"integer"
            }
         ]
      }
   },
   "definitions":{
      "CustomAuthToken":{
         "required":[
            "email",
            "password"
         ],
         "type":"object",
         "properties":{
            "email":{
               "title":"Email",
               "type":"string",
               "format":"email",
               "minLength":1
            },
            "password":{
               "title":"Password",
               "type":"string",
               "minLength":1
            }
         }
      },
      "Booking":{
         "required":[
            "user",
            "event",
            "ticket_type",
            "quantity"
         ],
         "type":"object",
         "properties":{
            "id":{
               "title":"ID",
               "type":"integer",
               "readOnly":true
            },
            "user":{
               "title":"User",
               "type":"integer"
            },
            "event":{
               "title":"Event",
               "type":"integer"
            },
            "ticket_type":{
               "title":"Ticket Type",
               "type":"string",
               "enum":[
                  "Regular",
                  "VIP"
               ]
            },
            "quantity":{
               "title":"Ticket Quantity",
               "type":"integer",
               "maximum":9223372036854775807,
               "minimum":0
            },
            "total_price":{
               "title":"Total Price",
               "type":"string",
               "format":"decimal",
               "readOnly":true
            },
            "booked_at":{
               "title":"Booked At",
               "type":"string",
               "format":"date-time",
               "readOnly":true
            }
         }
      },
      "Event":{
         "required":[
            "name",
            "date",
            "location",
            "total_regular_tickets",
            "total_vip_tickets",
            "available_regular_tickets",
            "available_vip_tickets",
            "regular_ticket_price",
            "vip_ticket_price",
            "early_bird_price",
            "early_bird_deadline"
         ],
         "type":"object",
         "properties":{
            "id":{
               "title":"ID",
               "type":"integer",
               "readOnly":true
            },
            "name":{
               "title":"Event Name",
               "type":"string",
               "maxLength":255,
               "minLength":1
            },
            "date":{
               "title":"Event Date",
               "type":"string",
               "format":"date"
            },
            "location":{
               "title":"Location",
               "type":"string",
               "maxLength":255,
               "minLength":1
            },
            "description":{
               "title":"Description",
               "type":"string",
               "x-nullable":true
            },
            "total_regular_tickets":{
               "title":"Total Regular Tickets",
               "type":"integer",
               "maximum":9223372036854775807,
               "minimum":0
            },
            "total_vip_tickets":{
               "title":"Total VIP Tickets",
               "type":"integer",
               "maximum":9223372036854775807,
               "minimum":0
            },
            "available_regular_tickets":{
               "title":"Available Regular Tickets",
               "type":"integer",
               "maximum":9223372036854775807,
               "minimum":0
            },
            "available_vip_tickets":{
               "title":"Available VIP Tickets",
               "type":"integer",
               "maximum":9223372036854775807,
               "minimum":0
            },
            "regular_ticket_price":{
               "title":"Regular ticket price",
               "type":"number",
               "format":"decimal"
            },
            "vip_ticket_price":{
               "title":"Vip ticket price",
               "type":"number",
               "format":"decimal"
            },
            "early_bird_price":{
               "title":"Early bird price",
               "type":"number",
               "format":"decimal"
            },
            "early_bird_deadline":{
               "title":"Early Bird Deadline",
               "type":"string",
               "format":"date-time"
            }
         }
      }
   }
}
```
