# Applications of Pyramid
   Pyramid - is a general, open source, web application development framework built in python. It is backed by the enterprise knowledge Management System KARL (a George Soros project).
   
   
    Companies which use Pyramid framework are:
             •	AdRoll
             •	BraveWords
             •	Easy Blog Networks
             •	DiscNW
             •	LinkPeek
             •	ITCase
             •	NiteoWeb

    Why Pyramid is used:
             •	It is lightweight web framework for Python applications
             •	As your application grows, Pyramid offers many features that make writing complex software take less effort.
             •	Pyramid works in all supported versions of Python.

    Pyramid is used for
             •	get a basic web application up and running quickly
             •	creating the entire framework layout in a single file if you would like
             •	start small and finish big
             
    Simple Hello World Program:
             from pyramid.config import Configurator
             from pyramid.response import Response

             def hello_world(request):
             return Response('Hello World!')

             if __name__ == '__main__':
                 with Configurator() as config:
                     config.add_route('hello', '/')
                     config.add_view(hello_world, route_name='hello')
                     app = config.make_wsgi_app()
             server = make_server('0.0.0.0', 6543, app)
             server.serve_forever()
    
    
   
