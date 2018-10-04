""" Sandbox Data Structure api
"""
from core_schema_viewer_app.components.sandbox_data_structure.models import SandboxDataStructure
from core_schema_viewer_app.utils.parser import generate_form
from datetime import datetime


def get_by_id(sandbox_data_structure_id):
    """ Return the sandbox data structure with the given id

    Args:
        sandbox_data_structure_id:

    Returns:

    """
    return SandboxDataStructure.get_by_id(sandbox_data_structure_id)


def upsert(sandbox_data_structure):
    """ Save or update the Sandbox Data Structure

    Args:
        sandbox_data_structure:

    Returns:

    """
    return sandbox_data_structure.save()


def create_and_save(template, user_id):
    """ Create and save Sandbox Data Structure

    Args:
        template:

    Returns:

    """
    # generate the root element
    root_element = generate_form(template.content)
    unique_name =  str(datetime.now()) + template.display_name
    # create sandbox data structure
    sandbox_data_structure = SandboxDataStructure(user=str(user_id),
                                                  template=template,
                                                  name=unique_name,
                                                  data_structure_element_root=root_element)

    # save the data structure
    return upsert(sandbox_data_structure)
