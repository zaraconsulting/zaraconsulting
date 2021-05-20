from flask import current_app as app

@app.context_processor
def make_context():
    context = {
        'COMPANY_NAME': app.config.get('COMPANY_NAME'),
        'COMPANY_PHONE': app.config.get('COMPANY_PHONE')
    }
    return context