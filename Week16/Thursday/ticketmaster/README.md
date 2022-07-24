# Ticketmaster

The Google Maps API challenge made making requests to a 3rd Party API very easy. All we needed to do was copy and paste. We mentioned that it would actually be much more difficult to actually make requests in real life and this challenge is for that.

Typically, when you make a request to a 3rd Party API, you read through the documentation, make a [Request](https://realpython.com/python-requests/) (you'll need that link later), and get a [Response](https://realpython.com/python-requests/#the-response). Once you parse through the response, you can use that data to achieve your application goals.

This challenge is going to be rather nebulous and that's by design. Most software engineering features are going to come as a laundry list of wants from your client. It is up to you to figure out how it works and implement it.

In this application, I want to be able to come to a home page, enter the name of my favorite musical artist and get a list of where their next 5 concerts will be on a map. Good luck.

## Release 0
You don't need a schema for this because you're not saving anything. First, spend some time drawing out how the flow of data will go. What happens first? What happens with data? Where are requests/responses happening in the flow of data?

## Release 1
Create your form and capture the search query.

## Release 2
Look up the available endpoints on [Ticketmaster's Free API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/). Which ones do you need to figure out the next 5 concerts of the artist in question? You'll be making lots of requests and getting lots of responses. Ticketmaster gives you 5000 free calls per day.

## Release 3
Parse the data that comes back. It's going to be a huge bunch of nested JSON. You need to find the next 5 concert venues and capture their addresses in date order

## Release 4
Now that you have the name of the venues and their addresses, map them via Google Maps. 
