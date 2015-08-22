# -*- coding: utf-8 -*-
##############################################################################
# Web Task Color
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "project_task_agenda_colouring",
    'summary': """
        Add colors to tasks in the agenda view of project tasks.
        """,
    'description': """
        With this module you can add custom colours to project tasks with a colour picker.
    """,
    'author': "Adil Houmadi, Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'project',
	'calendar',
	'web_calendar',
        'web_widget_color'
    ],
    'data': [
        'views/project_task_views.xml',
        'views/project_task_assets.xml',
    ],
    "installable": True,
}
