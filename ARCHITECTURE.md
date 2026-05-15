# SUN-flower Architecture

## Why this exists

People do not have two free hours to “learn.”
They have tabs open.
They have commutes.
They have messy mornings.
They have a life.

SUN-flower turns that chaos into a daily SUN-rise.

It takes what you care about, reads the internet, picks what matters, and sends you 3 short audio courses before your day really starts.

---

## What it does

User gives us 5 interests.

Every morning, SUN-flower:
1. reads the internet
2. finds what is moving in those interests
3. removes overlap
4. picks 3 sharp angles
5. writes clean SUN prompts
6. generates 3 short audio courses
7. pushes them to Spotify
8. waits for the next day

That is the whole game.

---

## Flow

User interests
    ↓
fresh topics
    ↓
score + filter + dedupe
    ↓
build 3 learning angles
    ↓
SUN-generation
    ↓
poll until ready
    ↓
download audio
    ↓
push to Spotify
    ↓
daily brief ready

---

## Core modules

### 1. Fetcher
Pulls the raw signal.

It reads:
- RSS feeds
- news
- Hacker News
- Reddit
- other public sources

It does not try to be smart.
It just brings in what is happening.

Output:
- title
- source
- url
- timestamp
- short summary

---

### 2. Ranking layer
This is where the system starts thinking.

It decides:
- what matches the user
- what is fresh
- what is credible
- what is repeated noise

ML:
- TF-IDF
- cosine similarity
- weighted scoring

This layer makes sure the brief is not random.

---

### 3. Prompt builder
This is not string stuffing.

This layer turns topics into clear SUN-prompts that feel like:
- “what changed today”
- “why this matters”
- “what to remember”
- “what to listen to next”

The output should sound like a real person teaching, not a machine performing.

---

### 4. SUN-client
This sends the prompt into SUN and handles the wait.

It:
- creates the audio request
- polls status
- retries safely
- downloads the final MP3 when ready

No drama. Just reliable execution.

---

### 5. Spotify client
This takes the audio and puts it where the user already listens.

It:
- uploads episodes
- keeps them private
- organizes them by day
- makes the delivery feel effortless

---

### 6. Scheduler
This runs the whole thing every morning 7:00 am

The job is simple:
- wake up
- generate
- deliver
- repeat

---

