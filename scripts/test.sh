URL=http://localhost:8080


# Create users
echo "PUT User"
curl -XPUT -d fn=Girum -d ln=Ibssa $URL/users/123 # Create Girum
echo "PUT User"
curl -XPUT -d fn=Nati -d ln=Tessema $URL/users/456 # Create Nati
echo "PUT User"
curl -XPUT -d fn=Samora -d ln=Deng $URL/users/789 # Create Samora

# Add new messages.
echo "POST Message"
curl -XPOST -d body="If a chicken had lips could it whistle?" $URL/users/123/messages
echo ''
echo ''

echo "POST Message"
curl -XPOST -d body="Who's going to win the NBA playoffs?" $URL/users/123/messages 
echo ''
echo ''

echo "POST Message"
curl -XPOST -d body="My parents broke up." $URL/users/123/messages
echo ''
echo ''

# # Don't curl this one in, since we have its old Key hard-coded into the Responses curl request below.
# curl -XPOST -d body="Tell me a joke!" $URL/users/123/messages
# echo ''
# echo ''


# Get some users.
echo "GET User"
curl -XGET $URL/users/123
echo ''
echo ''

# curl -XGET $URL/users/123/messages
# echo ''
# echo ''


echo "GET User"
curl -XGET $URL/users/456
echo ''
echo ''

# curl -XGET $URL/users/456/messages
# echo ''
# echo ''

echo "GET User"
curl -XGET $URL/users/789
echo ''
echo ''

# curl -XGET $URL/users/789/messages
# echo ''
# echo ''


# Use a hard-coded Key to post a new Response
echo "POST Response"
curl -XPOST -d body="My penis~" -d author="456" $URL/users/123/messages/6245226045767680/responses
echo ''
echo ''







# # Create new proposal
# curl -XPUT -d des="basketball?" -d loc="the court by my place" -d time="28 Apr 2014 08:59:47 GMT" -d int=456 -d int=789 -d conf=456 $URL/users/123/proposal # Set Girum's proposal
# curl -XPUT -d des="pop a molly" -d loc="my house" -d time="28 Apr 2014 08:59:47 GMT" -d int=123 -d int=789 -d conf=123 $URL/users/456/proposal # Set Nati's proposal

# curl -XDELETE $URL/users/456/proposal
# curl -XPUT -d des="pop a molly" -d loc="my house" -d time="28 Apr 2014 08:59:47 GMT" -d int=123 -d int=789 -d conf=123 $URL/users/456/proposal # Set Nati's proposal