from models import TASK_ACTION, TASK_WAITING

ONBOARDING_TEMPLATE = {
    "tasks": [
        {
            "process_name": "BGV",
            "task_name": "Initiate BGV",
            "task_type": TASK_ACTION
        },
        {
            "process_name": "BGV",
            "task_name": "BGV Cleared",
            "task_type": TASK_WAITING
        },

        {
            "process_name": "Compliance",
            "task_name": "Assign Compliance Training",
            "task_type": TASK_ACTION
        },
        {
            "process_name": "Compliance",
            "task_name": "Compliance Completed",
            "task_type": TASK_WAITING
        },

        {
            "process_name": "Network ID",
            "task_name": "Raise Network ID Request",
            "task_type": TASK_ACTION
        },
        {
            "process_name": "Network ID",
            "task_name": "Client Approval Received",
            "task_type": TASK_WAITING
        },
        {
            "process_name": "Network ID",
            "task_name": "Network ID Credentials Received",
            "task_type": TASK_WAITING
        },

        {
            "process_name": "Migration",
            "task_name": "Ask User For Laptop Details",
            "task_type": TASK_ACTION
        },
        {
            "process_name": "Migration",
            "task_name": "Details Received",
            "task_type": TASK_WAITING
        },
        {
            "process_name": "Migration",
            "task_name": "Send Details To ITH For Approval",
            "task_type": TASK_ACTION
        },
        {
            "process_name": "Migration",
            "task_name": "Approval Received",
            "task_type": TASK_WAITING
        },
        {
            "process_name": "Migration",
            "task_name": "Send Details To System Team For Removal",
            "task_type": TASK_ACTION
        },
        {
            "process_name": "Migration",
            "task_name": "Device Removed From Company Intune",
            "task_type": TASK_WAITING
        },
        {
            "process_name": "Migration",
            "task_name": "Send Details To Client Team",
            "task_type": TASK_ACTION
        },
        {
            "process_name": "Migration",
            "task_name": "Device Added To Client Intune",
            "task_type": TASK_WAITING
        },
        {
            "process_name": "Migration",
            "task_name": "Ask User To Complete Setup",
            "task_type": TASK_ACTION
        },
        {
            "process_name": "Migration",
            "task_name": "User Setup Completed",
            "task_type": TASK_WAITING
        }
    ],

    "dependencies": [
        ("BGV Cleared", "Initiate BGV"),

    ("Compliance Completed", "Assign Compliance Training"),

    ("Raise Network ID Request", "BGV Cleared"),
    ("Raise Network ID Request", "Compliance Completed"),

    ("Client Approval Received", "Raise Network ID Request"),

    ("Network ID Credentials Received",
    "Client Approval Received"),

    ("Ask User For Laptop Details",
    "Network ID Credentials Received"),

    ("Details Received",
    "Ask User For Laptop Details"),

    ("Send Details To ITH For Approval",
    "Details Received"),

    ("Approval Received",
    "Send Details To ITH For Approval"),

    ("Send Details To System Team For Removal",
    "Approval Received"),

    ("Device Removed From Company Intune",
    "Send Details To System Team For Removal"),

    ("Send Details To Client Team",
    "Device Removed From Company Intune"),

    ("Device Added To Client Intune",
    "Send Details To Client Team"),

    ("Ask User To Complete Setup",
    "Device Added To Client Intune"),

    ("User Setup Completed",
    "Ask User To Complete Setup")
    ]
}

OFFBOARDING_TEMPLATE = {
    "tasks": [
        {
            "process_name": "Offboarding",
            "task_name": "Request Device Removal",
            "task_type": TASK_ACTION
        },

        {
            "process_name": "Offboarding",
            "task_name": "Device Removed From Client Intune",
            "task_type": TASK_WAITING
        },

        {
            "process_name": "Offboarding",
            "task_name": "Request Network ID Deactivation",
            "task_type": TASK_ACTION
        },

        {
            "process_name": "Offboarding",
            "task_name": "Network ID Deactivated",
            "task_type": TASK_WAITING
        },

        {
            "process_name": "Offboarding",
            "task_name": "Request Device Enrollment",
            "task_type": TASK_ACTION
        },

        {
            "process_name": "Offboarding",
            "task_name": "Device Added To Company Intune",
            "task_type": TASK_WAITING
        }
    ],

    "dependencies": [

        ("Device Removed From Client Intune",
         "Request Device Removal"),

        ("Request Network ID Deactivation",
         "Device Removed From Client Intune"),

        ("Network ID Deactivated",
         "Request Network ID Deactivation"),

        ("Request Device Enrollment",
         "Network ID Deactivated"),

        ("Device Added To Company Intune",
         "Request Device Enrollment")
    ]
}