URL=http:/localhost:8080


# Create users
curl -XPUT -d fn=Girum -d ln=Ibssa $URL/users/123 # Create Girum
curl -XPUT -d fn=Nati -d ln=Tessema $URL/users/456 # Create Nati
curl -XPUT -d fn=Samora -d ln=Deng $URL/users/789 # Create Samora

# Add new broadcast
curl -XPOST -d body="If a chicken had lips could it whistle?" $URL/users/123/messages
curl -XPOST -d body="Who's going to win the NBA playoffs?" $URL/users/123/messages 
curl -XPOST -d body="My parents broke up." $URL/users/123/messages
curl -XPOST -d body="Tell me a joke!" $URL/users/123/messages


# Create new proposal
curl -XPUT -d des="basketball?" -d loc="the court by my place" -d time="28 Apr 2014 08:59:47 GMT" -d int=456 -d int=789 -d conf=456 $URL/users/123/proposal # Set Girum's proposal
curl -XPUT -d des="pop a molly" -d loc="my house" -d time="28 Apr 2014 08:59:47 GMT" -d int=123 -d int=789 -d conf=123 $URL/users/456/proposal # Set Nati's proposal

curl -XDELETE $URL/users/456/proposal
curl -XPUT -d des="pop a molly" -d loc="my house" -d time="28 Apr 2014 08:59:47 GMT" -d int=123 -d int=789 -d conf=123 $URL/users/456/proposal # Set Nati's proposal