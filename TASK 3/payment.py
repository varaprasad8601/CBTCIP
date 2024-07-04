#CREATE PAYMENT RECEPIT
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_receipt(transaction_id, date, customer_name, items, total_amount, receipt_filename):
    c = canvas.Canvas(receipt_filename, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 20)
    c.drawString(2 * inch, height - inch, "Payment Receipt")
    c.setFont("Helvetica", 12)
    c.drawString(0.5 * inch, height - 1.5 * inch, f"Transaction ID: {transaction_id}")
    c.drawString(0.5 * inch, height - 2 * inch, f"Date: {date}")
    c.drawString(0.5 * inch, height - 2.5 * inch, f"Customer Name: {customer_name}")
    c.drawString(0.5 * inch, height - 3 * inch, "Item")
    c.drawString(3.5 * inch, height - 3 * inch, "Price")
    c.line(0.5 * inch, height - 3.1 * inch, 5.5 * inch, height - 3.1 * inch)
    c.line(0.5 * inch, height - 2.8 * inch, 5.5 * inch, height - 2.8 * inch)
    y = height - 3.5 * inch
    for item, price in items:
        c.drawString(0.5 * inch, y, item)
        c.drawString(3.5 * inch, y, f"RS.  {price:.2f}")
        y -= 0.5 * inch
        c.line(0.5 * inch, y + 0.3 * inch, 5.5 * inch, y + 0.3 * inch)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.5 * inch, y, f"Total Amount: RS. {total_amount:.2f}")
    c.showPage()
    c.save()
transaction_id = "varaprasad@862001"
date = "2024-06-18"
customer_name = "VARA PRASAD"
items = [("chapathi", 50.00), ("parota", 45.50), ("panipuri", 50.75)]
total_amount = sum(price for item, price in items)
receipt_filename = "paymentreceipt.pdf"

create_receipt(transaction_id, date, customer_name, items, total_amount, receipt_filename)
