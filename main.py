# BACT7501 Assessment 2 - Requisition System
# Final test program: submits requisitions in different scenarios,
# displays them, shows the statistics, then records the manager's
# responses to the pending requisitions and displays everything again.

from requisition import Requisition

# ---- Submit requisitions -------------------------------------------------

# 1. Total $450 (less than $500) - approved automatically
req1 = Requisition("03/04/2024", "FN19", "John Paul")
req1.requisitions_details([
    ("Printer paper", 120),
    ("Toner cartridge", 180),
    ("Stationery set", 150),
])
req1.approve_requisition()

# 2. Total $1000 ($500 or more) - stays pending for a manager
req2 = Requisition("05/04/2024", "FN20", "Tracy Brown")
req2.requisitions_details([
    ("Laptop", 850),
    ("Laptop bag", 150),
])
req2.approve_requisition()

# 3. Total $3500 ($500 or more) - stays pending for a manager
req3 = Requisition("07/05/2024", "FN15", "Emma Wellington")
req3.requisitions_details([
    ("Office desks (x5)", 2000),
    ("Office chairs (x5)", 1500),
])
req3.approve_requisition()

# 4. Total $490 (less than $500) - approved automatically
req4 = Requisition("03/05/2024", "FN02", "Catlin White")
req4.requisitions_details([
    ("Whiteboard", 220),
    ("Markers and erasers", 90),
    ("Notice board", 180),
])
req4.approve_requisition()

# 5. Total $750 ($500 or more) - stays pending for a manager
req5 = Requisition("10/05/2024", "FN25", "David Smith")
req5.requisitions_details([
    ("Projector", 750),
])
req5.approve_requisition()

# 6. Total $120 (less than $500) - approved automatically
req6 = Requisition("12/05/2024", "FN30", "Sarah Lee")
req6.requisitions_details([
    ("USB drives (x4)", 80),
    ("HDMI cable", 40),
])
req6.approve_requisition()

# ---- Display all requisitions and the statistics -------------------------

print("========== ALL REQUISITIONS ==========")
print()
Requisition.display_all_requisitions()
Requisition.requisition_statistics()

# ---- Manager responds to the pending requisitions (totals over $499) -----

req2.respond_to_requisition("Approved")       # $1000 - manager approves
req3.respond_to_requisition("Not approved")   # $3500 - manager does not approve
# req5 ($750) is left as Pending - the manager has not responded yet

# ---- Display everything again after the responses ------------------------

print("========== AFTER MANAGER RESPONSES ==========")
print()
Requisition.display_all_requisitions()
Requisition.requisition_statistics()
