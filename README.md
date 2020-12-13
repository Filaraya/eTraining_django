# eTraining


![GitHub repo size](https://img.shields.io/github/repo-size/Filaraya/eTraining)
![GitHub contributors](https://img.shields.io/github/contributors/Filaraya/eTraining)
![GitHub stars](https://img.shields.io/github/stars/Filaraya/eTraining?style=social)
![GitHub forks](https://img.shields.io/github/forks/Filaraya/eTraining?style=social)


eTraining is a web application that allows the employees to do attend companies capacity building via online.

eTraining web application has features to Create, Read, Update and Delete (CRUD) materials like text, image, video and Files. The Admin (the company owner) manages all the CRUD operations in the web application. The user (employee or consultant) can create an account and able to attend the virtual training and materials.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* create virtualenv and install requirements 
```
python3
pip install -r requirements.txt 
```
## Installing eTraining

Create database tables, user for admin panel and run project.
```
python manage.py makemigrations
python manage.py migrate`
python manage.py createsuperuser`
python manage.py runserver
```
## Contributing to eTraining
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
To contribute to <project_name>, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@FilmonAraya](https://github.com/Filaraya) 📖

You might want to consider using something like the [All Contributors](https://github.com/all-contributors/all-contributors) specification and its [emoji key](https://allcontributors.org/docs/en/emoji-key).

## Contact

If you want to contact me you can reach me at <faraya1@live.maryville.edu>.

## License

This project uses the following license: [<license_name>](<link>).
