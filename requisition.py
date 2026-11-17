# BACT7501 Assessment 2 - Software Development Project
# Requisition System


class Requisition:
    """A class to implement the functionality of the staff requisition system.

    Each Requisition object represents one requisition submitted by a staff
    member. Data that is shared by every requisition (the ID counter and the
    list of all requisitions) is kept as class variables.
    """

    # Class variables - shared by all requisition objects
    next_requisition_id = 10001   # unique requisition ID counter
    all_requisitions = []         # every requisition that has been created

    def __init__(self, date, staff_id, staff_name):
        """Initialise the shared data of a requisition."""
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.next_requisition_id
        Requisition.next_requisition_id += 1
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"
        Requisition.all_requisitions.append(self)

    def requisitions_details(self, items):
        """Add a requisition.

        Accepts a list of requisition items with the cost of each item,
        e.g. [("Printer paper", 120), ("Toner cartridge", 180)], stores the
        items and returns the total cost of the requisition.
        """
        self.items = items
        total = 0
        for item_name, cost in items:
            total = total + cost
        self.total = total
        return self.total

    def approve_requisition(self):
        """Decide automatically whether the requisition is approved.

        A requisition with a total of less than $500 is approved straight
        away and is given an approval reference number made from the staff
        ID and the last three digits of the requisition ID (e.g. FN19001).
        A requisition of $500 or more stays Pending until a manager
        responds to it.
        """
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )
        else:
            self.status = "Pending"
        return self.status

    def respond_to_requisition(self, manager_response):
        """Record a manager's response to a pending requisition.

        The manager can mark a pending requisition as "Approved" or
        "Not approved"; the status (and the approval reference number, if
        it is approved) is updated. Requisitions that are not pending are
        not changed.
        """
        if self.status == "Pending":
            if manager_response == "Approved":
                self.status = "Approved"
                self.approval_reference = (
                    self.staff_id + str(self.requisition_id)[-3:]
                )
            elif manager_response == "Not approved":
                self.status = "Not approved"
        return self.status

    def display_requisition(self):
        """Print the information of this requisition."""
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + str(self.total))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print()

    @classmethod
    def display_all_requisitions(cls):
        """Print the information of all the requisition objects."""
        for req in cls.all_requisitions:
            req.display_requisition()

    @classmethod
    def requisition_statistics(cls):
        """Print the requisition statistics.

        Counts how many requisitions have been submitted in total and how
        many are approved, pending and not approved.
        """
        submitted = len(cls.all_requisitions)
        approved = 0
        pending = 0
        not_approved = 0
        for req in cls.all_requisitions:
            if req.status == "Approved":
                approved += 1
            elif req.status == "Pending":
                pending += 1
            elif req.status == "Not approved":
                not_approved += 1
        print("Displaying the Requisition Statistics")
        print()
        print("The total number of requisitions submitted:", submitted)
        print()
        print("The total number of approved requisitions:", approved)
        print()
        print("The total number of pending requisitions:", pending)
        print()
        print("The total number of not approved requisitions:", not_approved)
        print()
