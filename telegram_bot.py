from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final ='7888384366:AAFnkIHfb6y0-m4qGuY6kIfOXffL_ufn8F0'
Bot_USERNAME: Final ='@faceDGod_bot'

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yo! Thanks for chatting. Im the faceDGod bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yo! Type something so I can help you out!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yo! TThis is a custom command.')

#Handle Responses

