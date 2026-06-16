from datetime import date

from database import get_connection

from workflow_templates import (
    ONBOARDING_TEMPLATE,
    OFFBOARDING_TEMPLATE
)

from models import (
    STATUS_ACTIVE,
    STATUS_INACTIVE
)

def get_template(process_type):
    if process_type == "Onboarding":
        return ONBOARDING_TEMPLATE

    return OFFBOARDING_TEMPLATE

def create_resource(
    name,
    email,
    process_type):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO resources(
        name,
        email,
        process_type,
        created_date
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        name,
        email,
        process_type,
        str(date.today())
    )
    )
    resource_id = cursor.lastrowid

    template = get_template(process_type)

    task_id_map = {}

    for task in template["tasks"]:
        status = STATUS_INACTIVE
        cursor.execute(
        """
        INSERT INTO tasks(
            resource_id,
            process_name,
            task_name,
            task_type,
            status
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            resource_id,
            task["process_name"],
            task["task_name"],
            task["task_type"],
            status
        )
    )
    
    task_id_map[
        task["task_name"]
    ] = cursor.lastrowid


    for task_name, dependency_name in template["dependencies"]:
        cursor.execute(
        """
        INSERT INTO task_dependencies(
            task_id,
            depends_on_task_id
        )
        VALUES (?, ?)
        """,
        (
            task_id_map[task_name],
            task_id_map[dependency_name]
        )
    )
        
    for task_name, task_id in task_id_map.items():
        cursor.execute(
        """
        SELECT COUNT(*)
        FROM task_dependencies
        WHERE task_id = ?
        """,
        (task_id,)
    )
    dependency_count = cursor.fetchone()[0]

    if dependency_count == 0:
        cursor.execute(
        """
        UPDATE tasks
        SET status = ?
        WHERE id = ?
        """,
        (
            STATUS_ACTIVE,
            task_id
        )
    )
    
    conn.commit()
    conn.close()

    return resource_id
