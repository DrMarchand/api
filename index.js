require("dotenv").config();

const express = require("express");
const { Client, GatewayIntentBits, REST, Routes, SlashCommandBuilder } = require("discord.js");

const app = express();
const PORT = process.env.PORT || 8787;

app.get("/health", (_req, res) => {
  res.json({
    ok: true,
    service: "echo-discord-bot",
    app: "Atlas",
    mode: "audit-only",
    time: new Date().toISOString()
  });
});

const client = new Client({
  intents: [GatewayIntentBits.Guilds]
});

const commands = [
  new SlashCommandBuilder()
    .setName("nfe_status")
    .setDescription("Show NFE Echo bot status.")
].map(c => c.toJSON());

async function registerCommands() {
  const rest = new REST({ version: "10" }).setToken(process.env.DISCORD_TOKEN);

  await rest.put(
    Routes.applicationGuildCommands(
      process.env.DISCORD_CLIENT_ID,
      process.env.DISCORD_GUILD_ID
    ),
    { body: commands }
  );

  console.log("Slash commands registered.");
}

client.once("ready", () => {
  console.log(`Echo online as ${client.user.tag}`);
});

client.on("interactionCreate", async interaction => {
  if (!interaction.isChatInputCommand()) return;

  if (interaction.commandName === "nfe_status") {
    await interaction.reply({
      content: "⚙︎ Echo online. Atlas mode: audit-only. High-risk actions blocked.",
      ephemeral: true
    });
  }
});

async function main() {
  app.listen(PORT, () => {
    console.log(`Health server listening on http://localhost:${PORT}/health`);
  });

  if (!process.env.DISCORD_TOKEN || !process.env.DISCORD_CLIENT_ID || !process.env.DISCORD_GUILD_ID) {
    console.warn("Discord env vars missing. Health server only.");
    return;
  }

  await registerCommands();
  await client.login(process.env.DISCORD_TOKEN);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
