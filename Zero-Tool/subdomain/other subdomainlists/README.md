# Popular-Site-Subdomains
A list of subdomains for some of the most popular sites on the internet. Made as a result of [this tweet]
(https://twitter.com/soaj1664ashar/status/777182478075326464). "Sometimes simple things are ignored".

# Why?
There are plenty of reasons why people sometimes want a list of subdomains for a website. Whether you're just curious what type of stuff
the company are working on or you want to check for security vulnerabilities, a list of subdomains can really come in handy. Not so long back
someone figured out that he could get in to [anybody's Facebook account](http://www.anandpraka.sh/2016/03/how-i-could-have-hacked-your-facebook.html) 
due to a vulnerability that was only there on their very old subdomains.

# Contribute
The idea behind this is to let everyone contribute and get a fairly big list of subdomains of all the most popular sites on the internet.

Before opening a pull request, please make sure that:

* Each domain has its own .txt file, eg. Facebook.com.txt, Facebook.co.uk.txt
* There are no duplicates in the list
* The list is in alphabetical order, [you could use this site to do that](http://alphabetizer.flap.tv/)
* http:// or https:// is not in any of the subdomains (as well as no trailing slashes at the end of the domain)

If you're not sure how you can help out, [this site can find subdomains ](https://pentest-tools.com/information-gathering/find-subdomains-of-domain) for you but it also includes the IP addresses which we don't really want. What I do is open open the list in Notepad which has subdomains like:

Facebook.com  127.0.0.1

m.Facebook.com 127.0.0.2

Next, to get rid of everything other than just the subdomain do a regex find and replace. Find "[ \t].*" and replace it with "\1"
