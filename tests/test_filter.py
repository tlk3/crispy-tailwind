from django.template import Context, Template
from django.test import SimpleTestCase

from .forms import SampleForm


class CrispyFilterTests(SimpleTestCase):
    maxDiff = None

    def test_crispy_filter(self):
        template = Template(
            """
            {% load tailwind_filters %}
            {{ form|crispy }}
            """
        )
        form = SampleForm()
        c = Context({"form": form})
        html = template.render(c)

        self.assertHTMLEqual(
            html,
            """<div id="div_id_is_company" class=" mb-3">
            <label for="id_is_company" class="block text-gray-700 text-sm font-bold mb-2">company</label>
            <input type="checkbox" name="is_company" class="checkboxinput " id="id_is_company"> </div>

            <div id="div_id_email" class=" mb-3">
            <label for="id_email" class="block text-gray-700 text-sm font-bold mb-2">email<span class="asteriskField">
            *</span> </label>
            <input type="text" name="email" maxlength="30" class="textinput textInput inputtext tailwind-text"
            required id="id_email">
            <small id="hint_id_email" class="text-gray-600">Insert your email</small> </div>

            <div id="div_id_password1" class=" mb-3">
            <label for="id_password1" class="block text-gray-700 text-sm font-bold mb-2">password
            <span class="asteriskField">*</span>
            </label>
            <input type="password" name="password1" maxlength="30" class="textinput textInput "
            required id="id_password1"> </div>

            <div id="div_id_password2" class=" mb-3">
            <label for="id_password2" class="block text-gray-700 text-sm font-bold mb-2">
            re-enter password<span class="asteriskField">*</span> </label>
            <input type="password" name="password2" maxlength="30" class="textinput textInput "
            required id="id_password2"> </div>

            <div id="div_id_first_name" class=" mb-3">
            <label for="id_first_name" class="block text-gray-700 text-sm font-bold mb-2">
            first name<span class="asteriskField">*</span> </label>
            <input type="text" name="first_name" maxlength="5" class="textinput textInput inputtext tailwind-text"
            required id="id_first_name"> </div>

            <div id="div_id_last_name" class=" mb-3">
            <label for="id_last_name" class="block text-gray-700 text-sm font-bold mb-2">
            last name<span class="asteriskField">*</span> </label>
            <input type="text" name="last_name" maxlength="5" class="textinput textInput inputtext tailwind-text"
            required id="id_last_name"> </div>

            <div id="div_id_datetime_field" class=" mb-3">
            <label for="id_datetime_field_0" class="block text-gray-700 text-sm font-bold mb-2">
            date time<span class="asteriskField">*</span> </label>
            <input type="text" name="datetime_field_0" class="dateinput " required id="id_datetime_field_0">
            <input type="text" name="datetime_field_1" class="timeinput " required id="id_datetime_field_1">
            </div>

            <div id="div_id_tos_accepted" class=" mb-3">
            <label for="id_tos_accepted" class="block text-gray-700 text-sm font-bold mb-2">
            terms of service<span class="asteriskField">*</span> </label>
            <div class=" mb-3">
            <div class="relative">
            <select class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" name="tos_accepted">
            <option value="accepted">Accepted</option>
            <option value="not_accepted">Not accepted</option>
            </select><div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
            <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"></path>
            </svg>
            </div> </div></div></div>
            """,
        )
