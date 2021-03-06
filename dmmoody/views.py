from django.shortcuts import render, render_to_response
import json
import urllib2

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    codeschool = urllib2.urlopen('https://www.codeschool.com/users/dmmoody.json')
    codeschool_data = json.load(codeschool)

    treehouse = urllib2.urlopen('http://teamtreehouse.com/duanemoody.json')
    treehouse_data = json.load(treehouse)
    badge_count = 0
    points = treehouse_data['points']['total']
    course_dict = {}
    activity_date = []
    for i in treehouse_data['badges']:
        badge_count += 1
        activity_date.append(i['earned_date'])
        if i['courses']:
            if i['courses'][0]['title'] in course_dict:
                course_dict[i['courses'][0]['title']].append([i['courses'][1]['title'], i['icon_url']])
            else:
                course_dict[i['courses'][0]['title']] = [[i['courses'][1]['title'], i['icon_url']]]
    activity_date = json.dumps(activity_date)
    return render_to_response('about.html', {'treehouse_data': treehouse_data,
                                             'course_dict': course_dict,
                                             'points': points,
                                             'badge_count': badge_count,
                                             'activity_date': activity_date,
                                             'codeschool_data': codeschool_data})

def projects(request):
    github = urllib2.urlopen('https://api.github.com/users/dmmoody/repos')
    github_data = json.load(github)
    return render_to_response('projects.html', {'github_data': github_data})