# This script runs a word counter on every post and comment
# in every subreddit in the list for the last year

from subprocess import call

subreddits = [
	"berkeley",
	"stanford",
	"rit",
	"ucla",
	"uiuc",
	"virginiatech",
	"rpi",
	"uwaterloo",
	"rutgers",
	"aggies",
	"gatech",
	"mit",
	"jhu",
	"stjohnscollege",
	"msu",
	"ucsd",
	"uva",
	"uofmn",
	"ucf",
	"uoft",
	"fsu",
	"calpoly",
	"ucsantabarbara",
	"emersoncollege",
	"njtech",
	"hampshirecollege"
]

for sub in subreddits:
	call(['word_freqs', '-p', 'year', 'collegeAnalysis', '/r/' + sub])
