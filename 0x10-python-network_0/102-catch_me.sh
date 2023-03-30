#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me with You got me! reply.
curl -sL -X PUT -H "Orign: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
