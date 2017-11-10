import json
import uuid
import urllib
import datetime
import re 
import requests # for setting cookies

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.contrib import auth
#from django.forms.util import ErrorList
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

#import requests

from charlievannorman.util import *
def simple_page(template):
	def handler(request):
		return renderWithNav(request, template)
	return handler

def file_a(request):
	return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")
def file_b(request):
	return HttpResponse("v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA.myqbUoOfbuYMTb3HuxVonYYuwHgoAV2835bCeWTwqkY")

def home(request):
	obj = {}
	obj['developer'] = []
#	obj['developer'].append({
#		"title" : "Jet ZT",
#		"link" : "http://tiny.jetzt",
#		"year" : "2017",
##		"subtitle" : "A prototype of a 3D flying game with missiles",
#		"description" : "A prototype of a 3D flying game. Press Shift to move forwards, and use the mouse to navigate and fire. This one-level demo consists of a ship, cannon and missile capabilities, and moving targets. You can crash on the ",
#		"images" : [	
#			{"video" : { "source": "https://player.vimeo.com/video/230824116", "image" : "" }},
#			{"img":"archer2.png"},
#			{"img":"archer1.png"}
#		],	
#	})
	obj['developer'].append({
		"title" : "Magic Hands VR",
		"link" : "",
		"year" : "2017",
		"subtitle" : "An action game for Vive/Oculus + LeapMotion",
		"description" : "Use your hands to cast spells and open portals to other worlds.",
		"images" : [	
			{"video" : { "source": "https://player.vimeo.com/video/241614660", "image" : "" }},
			{"img":"magichands1.png"},
			{"img":"magichands2.png"}
		],	
	})
	obj['developer'].append({
		"title" : "Space Archer VR",
		"link" : "",
		"year" : "2017",
		"subtitle" : "An action game for Vive/Oculus",
		"description" : "Fly around in 3D space and shoot drones and space-men with your bow and arrow.",
		"images" : [	
			{"video" : { "source": "https://player.vimeo.com/video/230824116", "image" : "" }},
			{"img":"archer2.png"},
			{"img":"archer1.png"}
		],	
	})
	obj['developer'].append({
		"title" : "Fitness Cube VR",
		"link" : "",
		"year" : "2017",
		"subtitle" : "An exercise game for Vive/Oculus",
		"description" : "Cubes fly at you, and you smash them with your fists! Duck and dodge to prevent losing health.",
		"images" : [
			{"video" : { "source": "https://player.vimeo.com/video/230823053", "img" : "fitness2.png" }},
			{"img":"fitness1.png"},
		],	
	})
	obj['developer'].append({
		"title" : "Coffee Command ARKit",
		"link" : "",
		"year" : "2017",
		"subtitle" : "A passive multiplayer base control game",
		"description" : "Your phone becomes a ship which can attack bases and drones at your favorite coffee shop in a 3-D shooter style game. Once you clear the area, you can build your own turrets to deter other players and control the area, and mine resources from areas you control to become more powerful.",
		"images" : [
			{"img":"coffeecommand1.png"},
			{"img":"coffeecommand2.png"},
			{"img":"coffeecommand3.png"},
		],	
	})
	obj['developer'].append({
		"title" : "Mouse Brain Explorer VR",
		"link" : "https://3scan.com",
		"year" : "2015",
		"position" : "Contractor",
		"subtitle" : "Fly through a real mouse brain",
		"description" : "Using a cubic centimeter of a mouse brain imaged with 3Scan's equipment, I made a virtual reality tour through the vasculature and a mini-game to destroy blood clots. This was on exhibit during the Exploratorium's science week in 2015.",
		"images" : [{
			"video" : { "source": "https://player.vimeo.com/video/117482417", "img" : "3scan_1.jpg" }
			
		}],	
	})	

	
	obj['startups'] = []
	obj['startups'].append({
		"title" : "Radian Studios",
		"link" : "http://radian.ai",
		"year" : "2017",
		"position" : "Consultant & Apprentice",
#		"subtitle" : "A WebGL based math sandbox",
		"description" : "Consulting and contracting services for VR and AR applications, including executive strategy, b2b sales and partnerships, and full stack development. Our favorite b2b opportunities: hazardous environment simulations, medical device training, corporate innovation sprints, corporate HR training, immersive patient therapy, and aptitude assessments.",
		"responsibilities" : 
		[
#				"Business development",
#				"Project management",
#				"3D Interaction Design",
		],
		"images" : [
			{ "img" : "radian_logo.png", "class" : "contain square", "link" : "http://radian.ai"},
		],	
		})
	obj['startups'].append({
		"title" : "Super Math World",
		"link" : "https://supermathworld.com",
		"year" : "2016 - 2017",
		"position" : "Founder, CTO",
#		"subtitle" : "A WebGL based math sandbox",
		"description" : "A math sandbox video game for grades 2 - 8 which allows users to edit, create, and share game content from directly inside the application, natively in a web browser.",
		"responsibilities" : 
		[
				"Unity c# framework architecture",
				"Game design & programming",
				"Web backend (python, django, MySQL, AWS)",
		],
		"images" : [
			{ "img" : "smw.png", "class" : "contain", "link" : "Https://supermathworld.com" },
			{ "video" : { "source": "https://player.vimeo.com/video/219464062", "img" : "smw_1.jpg" }},
			{ "img" : "smw_2.jpg"},
			{ "img" : "smw_4.jpg"},
#			{ "img" : "smw_3.jpg"}
		],	
		})
	obj['startups'].append({
		"title" : "Mathbreakers",
		"link" : "https://mathbreakers.com",
		"year" : "2013 - 2015",
		"position" : "Co-Founder",
		"subtitle" : "A math puzzle platformer for grades 2 - 8",
		"description" : "We partnered with some of the biggest names in math education, including Dan Meyer and Jo Boaler, to discover the intersection between 3-D action gaming and elementary mathematics. The result was a truly immersive, stress free math game that kids love to play.",
		"responsibilities" : 
		[
			"Game design & programming",
			"Strategic partnerships",
		],
		"images" : [
			{ "img" : "mb.png", "class" : "contain", "link" : "https://mathbreakers.com/" },
			{ "video" : { "source": "https://player.vimeo.com/video/73754523", "img" : "mb_1.jpg" }},
			{ "img" : "mb_2.jpg"},
#			{ "img" : "mb_3.jpg"},
			{ "img" : "mb_4.jpg"}
		],	
		})

	obj['startups'].append({
		"title" : "Fractal Games",
		"link" : "https://fractalgames.com (old)",
		"year" : "2010 - 2011",
		"position" : "Founder",
		"subtitle" : "An iOS game development studio.",
		"description" : "We produced two games, 'Santa\'s Last Stand' and 'Bank Defense' for iOS." ,
		"responsibilities" : 
		[
			"Game design & programming",
			"Hired and managed art team",
		],
		"images" : [	
			{"img": "fg.png","class":"contain"},
			{"img" : "bd1.png"},
			{"img" : "bd2.png"},
			{"img" : "bd3.png"},
			{"img" : "sls1.png"},
			{"img" : "sls2.png"}
			],	
		})
	obj['startups'].append({
		"title" : "Startup Grid (Hactus)",
		"link" : "https://startupgrid.net",
		"year" : "2012",
		"position" : "Founder",
		"description" : "One of my first solo projects, a search-and-filter website for exploring the startup landscape and searching for new opportunities. The startup data is scraped from CrunchBase. The original vision was to provide startups a go-to resource for funding, incubators, and other opportunities.",
		"images" : [{"img":'startupgrid.png', "link":"http://startupgrid.net"}],	
		})
	obj['startups'].append({
		"title" : "Code Hero",
		"link" : "https://codehero.org",
		"year" : "2011",
		"position" : "Contractor",
		"description" : "I led production of the first 3D version of Code Hero, in which you learn programming by editing the world around you in real time using a javascript laser.",
	"images" : [
			{"img":"codehero.png"},
		],	

	})	

	obj['social'] = [
		{ "name" : "github.com/zannorman", "link" : "https://github.com/zannorman" },
		{ "name" : "linkedin.com/in/zannorman", "link" : "https://www.linkedin.com/in/zannorman" },
		{ "name" : "facebook.com/zannorman", "link" : "https://www.facebook.com/zannorman" },
		{ "name" : "twitter.com/@supermathworld", "link" : "https://twitter.com/@supermathworld" },
		{ "name" : "angel.co/supermathworld", "link" : "https://angel.co/supermathworld" },
	]

	return renderWithNav(request,'home.html', obj)

def file_a(request):
	return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
	return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")	



