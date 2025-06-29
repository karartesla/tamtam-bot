const { TamTamBotAPI } = require('tamtam-bot-api');
const bot = new TamTamBotAPI({
  token: process.env.TOKEN,
  polling: { interval: 3000 }
});

bot.on('message', (ctx) => {
  if (ctx.body.text?.toLowerCase() === 'مرحبا') {
    ctx.reply('أهلاً بك! 👋');
  }
});

console.log('✅ البوت يعمل!');
