import unittest
from flask_testing import TestCase
from app import app, db
from app.models import Todo


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config['DEBUG'] = True
        app.config['TESTING'] = True 
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Todo(text='Test', status=False))
        db.session.add(Todo(text='Test1', status=True))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the root page loads correctly
    def test_root_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'Add a new todo item:', response.data)

    # Ensure that Todo entries load correctly
    def test_existing_todo(self):

        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(
            b'Test</td>\n                    <td><a style="color: red;" href="/complete/1">pending', 
            response.data
        )

    # this testcase doenst work due to the way it is configured
    # Ensure that Todos are added correctly
    def test_adding_todo(self):
        response = self.client.post(
            '/add',
            data=Todo(text='Test2', status=True),
            follow_redirects=True
        )
        self.assertIn(b'Test2', response.data)

    # Ensure changing status to done works 
    def test_todo_done(self):
        id=Todo.query.filter_by(text='Test').first().id
        response = self.client.get(
            f'/complete/{id}',
            follow_redirects=True
        )
        self.assertIn(
            bytes(f'Test</td>\n                    <td><a href="/incomplete/{id}">done','ASCII'), 
            response.data
        )

    # Ensure changing status to pending works 
    def test_todo_pending(self):
        id=Todo.query.filter_by(text='Test1').first().id
        response = self.client.get(
            f'/incomplete/{id}',
            follow_redirects=True
        )
        self.assertIn(
            bytes(f'Test1</td>\n                    <td><a style="color: red;" href="/complete/{id}">pending','ASCII'), 
            response.data
        )

if __name__ == '__main__':
    unittest.main()
