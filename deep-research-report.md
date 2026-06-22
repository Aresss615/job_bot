# Free-only job search system for Jc

## Files I still need

Please upload your current resume PDF first. If you have an editable source file, send that too, because tailoring is much faster and more accurate from a DOCX, Google Doc export, or plain-text resume than from a PDF alone. If you have them, also include your latest transcript, a short list of your best projects with links, and any previous cover letters or application answers you have already used. I proceeded with the research and built the system below without those files, but real resume tailoring should start from your actual resume rather than assumptions.

## Best free strategy in plain English

Your best free strategy is not “apply everywhere.” It is a narrow, approval-first pipeline built around a few sources that actually fit your situation: OnlineJobs.ph for Filipino-only remote work; LinkedIn, Kalibrr, JobStreet, and Indeed Philippines for legitimate remote, part-time, internship, and entry-level roles; We Work Remotely and Remote OK for public remote leads you can collect safely through official RSS/API feeds; Wellfound only for startup roles that explicitly say global or “anywhere”; Mindrift only as a selective side option because it is project-based, not employment, and many current technical openings skew specialized or senior. OnlineJobs.ph is explicitly for Filipino workers and includes salaried full-time and part-time remote jobs, LinkedIn offers a free basic account and job search, Kalibrr markets free profiles plus remote and fresh-grad listings, JobStreet has work-from-home and fresh-graduate filters, Indeed Philippines has remote and entry-level listings, We Work Remotely publishes a public RSS feed, Remote OK exposes a public JSON API, and Mindrift’s general geographic restrictions do not currently list the Philippines, although project-level eligibility can still vary. citeturn0search0turn22search5turn31search16turn17search1turn1search5turn32search13turn20search14turn0search17turn0search8turn25search0turn24view0turn5view0turn4view0

The workflow should stay semi-automated, not fully automated. Safe automation is only for collecting public leads into a spreadsheet from official feeds or public pages that clearly allow it. Application submission, messaging, and account actions should stay manual unless a platform explicitly supports the exact automation you want. LinkedIn, Indeed, and Wellfound all prohibit or restrict scraping/bot behavior, Indeed specifically prohibits automating Indeed Apply outside official tooling, and We Work Remotely says API-exposed data is okay while scraping, copying, saving, or storing site data outside the API is prohibited. Mindrift also says some projects may restrict automation, generative AI tools, or third-party assistance. citeturn14view1turn16view0turn11view0turn25search2turn5view0

For your profile specifically, the winning angle is **junior backend + automation + practical business systems**, not “strong frontend engineer.” You already have credible experience in Django, PHP, MySQL, APIs, backend/QA/Jira work, and internal systems development. That means the highest-value searches are backend/Python/PHP/API/automation jobs with junior, internship, freelancer, contract, part-time, or remote wording. It does **not** mean chasing React-heavy product roles that expect a polished frontend specialist. Current live platform language also supports this positioning: OnlineJobs.ph is showing automation and AI automation roles, We Work Remotely has dedicated back-end programming categories, Remote OK uses tags like web dev, testing, API, and part time, and Mindrift currently lists roles such as full-stack developer, messaging bot developer, and senior data scraping engineer. citeturn22search9turn22search10turn25search3turn24view0turn4view1

One important exclusion: DataAnnotation remains **excluded for now**. Its official site says it works with contractors worldwide and even lists Tagalog among supported languages, but during this research I could not verify a Philippines-specific onboarding or eligibility page from official DataAnnotation sources. Because you explicitly said to exclude it unless Philippines eligibility is verified, I am keeping it out of the recommended MVP stack. citeturn7search0turn7search1turn7search2

## Platform comparison

The table below is ranked for **your** exact use case: free-only, Philippines-eligible, honest positioning, and approval-first applications. In the platform name column, the citations are the clickable official links.

| Platform | Best use for you | Philippines eligibility | Free-only fit | Automation safety | Recommendation |
|---|---|---:|---:|---|---|
| **OnlineJobs.ph** citeturn0search0turn22search5turn0search9 | Best source for Filipino-only remote work, including part-time salaried work and OLJ-style automation/dev support roles | **Yes, officially Filipino-only** | **Yes** | **Manual only** for searching/applying; use the built-in employer search to vet legitimacy | **Highest priority** |
| **LinkedIn Jobs** citeturn0search4turn31search16turn31search6turn0search13turn14view1 | Mid-to-high quality remote roles, networking, recruiter visibility, company pages, referral paths | **Yes**, but each job may have country limits | **Yes** with optional Premium upsell | **Manual only**; bots/scraping are prohibited | **Highest priority** |
| **Kalibrr** citeturn17search1turn17search3turn1search5turn1search17 | Strong local source for fresh grads, internships, junior jobs, work-from-home filters | **Yes** | **Yes** | **Manual only**; treat as no-public-API/manual workflow | **Highest priority** |
| **JobStreet** citeturn32search0turn32search13turn20search14turn20search16turn20search22 | Strong PH volume, especially fresh graduate, WFH, and contract/temp filters | **Yes** | **Yes** for job seekers | **Manual only** | **High priority** |
| **Indeed Philippines** citeturn0search17turn0search8turn0search14turn15search5turn16view0 | Broad aggregator for remote, part-time, and entry-level searches | **Yes**, but job-level restrictions vary | **Yes** | **Manual only**; Indeed Apply automation outside official tooling is prohibited | **High priority** |
| **We Work Remotely** citeturn25search1turn25search0turn25search2turn25search3turn25search8 | High-signal remote lead source for engineering roles, especially backend | **Mixed**; many roles are global, many are country-restricted | **Yes** for browsing/searching | **Safe only via official RSS/API-style access**; do **not** scrape or auto-apply | **High priority for lead collection, not direct automation** |
| **Remote OK** citeturn23search0turn23search2turn24view0 | Good remote lead feed for keywords like API, part time, web dev, testing | **Mixed**, but has Philippines-specific remote filtering pages | **Yes** for core use, with premium upsells on some pages | **Safe for lead collection via official public API**; do not auto-apply | **High priority for lead collection** |
| **Wellfound** citeturn8search3turn8search13turn8search1turn11view0turn8search16 | Startup roles with some salary/equity visibility; useful only when listings clearly allow remote/global candidates | **Mixed**; many startup jobs are US-only or region-limited | **Yes** | **Manual only**; scraping/automated harvesting is prohibited | **Selective use only** |
| **Mindrift** citeturn4view0turn5view0turn4view1 | Side-income AI training/evaluation work, not classic employment | **Generally yes**, since PH is not listed as restricted, but project-level rules vary | **Yes** | **Manual only**; some projects may ban automation or gen-AI assistance | **Selective use only** |
| **GitHub plus direct outreach** citeturn26search4turn26search0turn26search1turn26search2 | Not a job board, but one of your best credibility channels for inbound proof, repo links, and contribution-led networking | **Yes** | **Yes** | Safe to automate only on your own files/repos/site, not on third-party job platforms | **High support channel** |
| **Contra** citeturn27search0turn27search13turn27search7turn27search16 | Legit freelance alternative with free profile and free applications | **Unverified for PH-specific screening**, but globally oriented | **Yes** | **Manual only** unless the platform itself supports a feature | **Selective use only** |
| **PhilJobNet** citeturn1search10 | Official DOLE-backed local job portal; good as a legitimacy anchor and fallback source | **Yes** | **Yes** | **Manual only** | **Secondary backup source** |
| **Upwork** citeturn29search7turn27search5turn27search8 | Massive marketplace, but proposal volume and Connects make it a poor free-only fit right now | **Yes**, generally | **Weak fit** because the free tier is constrained by Connects and upsells | **Manual only** | **Low priority / mostly skip** |
| **Freelancer.com** citeturn29search11turn30search2turn30search9 | Free sign-up, but bidding limits depend on membership plans and upgrades | **Yes**, generally | **Weak fit** because bids and visibility are heavily membership-driven | **Manual only** | **Low priority / mostly skip** |
| **DataAnnotation** citeturn7search0turn7search1turn7search2 | Would be interesting for AI work, but your rule was explicit | **Unverified for PH-specific onboarding during this research** | **Yes** in principle | Manual only | **Exclude until PH eligibility is verified from an official source** |

A simple ranking for your MVP is: **daily** use OnlineJobs.ph, LinkedIn, Kalibrr, JobStreet, and Indeed PH; **3–4 times per week** scan We Work Remotely RSS, Remote OK API output, Wellfound, and GitHub/network leads; **selectively** check Mindrift and Contra; **mostly skip** Upwork and Freelancer.com because their free economics are weak for a student-level approval-first workflow; **exclude** DataAnnotation until Philippines eligibility is officially confirmed. citeturn0search0turn31search16turn17search1turn32search0turn0search17turn25search0turn24view0turn11view0turn27search13turn27search5turn30search2turn7search1

## Search keywords and scoring rubric

Use search terms that match both your real strengths and the language platforms are currently using. Right now, the most realistic clusters for you are backend, Python, Django, PHP, API integration, automation, junior software roles, tech support with development overlap, and selective AI-training/evaluation terms. This is grounded in current platform language: OnlineJobs.ph is listing automation and AI automation roles including “Future AI Automation Specialist Wanted (Student/Fresh Grad),” We Work Remotely has dedicated remote back-end programming pages, Remote OK uses tags such as API, testing, web dev, and part time, and Mindrift’s task descriptions explicitly mention prompt writing, evaluating AI-generated responses, and creating training data. citeturn22search9turn22search10turn25search3turn24view0turn4view0

Use these keyword bundles:

```text
Core backend bundle
"backend developer"
"backend engineer"
"python developer"
"django developer"
"php developer"
"api developer"
"api integration"
"rest api"
"mysql developer"
"junior software engineer"
"junior developer"
"software engineer intern"
"system developer"
```

```text
Automation bundle
"automation developer"
"automation specialist"
"workflow automation"
"ai automation"
"n8n"
"zapier"         # only if the job is otherwise free-to-apply and skill-aligned
"technical support developer"
"technical support engineer"
"internal tools developer"
"business systems developer"
```

```text
Remote and flexibility modifiers
"remote"
"work from home"
"part time"
"contract"
"project based"
"freelance"
"entry level"
"fresh graduate"
"internship"
"student"
```

```text
Selective AI and data bundle
"ai trainer"
"prompt evaluator"
"prompt engineering"
"ai training"
"data annotation"
"response evaluator"
"content reviewer"
"search quality"
```

```text
Use cautiously or usually avoid
"react developer"
"frontend engineer"
"next.js developer"
"senior full-stack engineer"
"lead developer"
"principal engineer"
```

A strong search pattern is to combine one term from the first bundle, one from the second, and one modifier. Examples:

```text
"python developer" remote part time
"django developer" junior remote
"php developer" contract work from home
"api integration" freelance remote
"automation specialist" student fresh graduate
"technical support engineer" php mysql remote
"backend developer" internship philippines remote
```

Use this **job-fit scoring rubric** from 0 to 100. It is designed to stop you from wasting time on glamorous but unrealistic roles.

| Category | Weight | How to score it honestly |
|---|---:|---|
| Geography and schedule fit | 20 | 20 if Philippines-compatible and timezone workable; 10 if unclear; 0 if country-restricted |
| Skill truthfulness | 20 | 20 if mostly Python/Django/PHP/MySQL/API/automation; 10 if mixed; 0 if React-heavy or senior frontend |
| Seniority realism | 15 | 15 if internship, junior, assistant, associate, trainee, or clearly trainable; 5 if mid-level but stretchable; 0 if senior/lead/principal |
| Role alignment | 15 | 15 if backend, API, automation, internal tools, QA-adjacent, technical support with coding; 5 if generic full-stack; 0 if pure frontend/product design |
| Flexibility | 10 | 10 if freelance, part-time, contract, project-based, or async-friendly; 5 if full-time remote only; 0 if onsite |
| Application safety and legitimacy | 10 | 10 if company site, reputable board, clear JD, no weird fees/tests; 5 if some uncertainty; 0 if scam signals appear |
| Portfolio leverage | 5 | 5 if you can show proof from GitHub/site/internship work; 0 if you have nothing relevant to point to |
| Compensation clarity | 5 | 5 if budget/range/payment method is clear; 0 if vague or suspicious |

Interpret the score this way:

| Score band | Action |
|---|---|
| 85–100 | Strong target. Prepare materials and ask for approval |
| 70–84 | Good target. Apply only if tailored well and risks are manageable |
| 55–69 | Borderline. Only continue if you need pipeline volume that day |
| Below 55 | Skip |

## Tracking schema and the approval-first workflow

Your tracker should be simple enough to maintain manually, but structured enough to support filtering, scoring, and later automation. A Google Sheet is the easiest MVP. If you prefer local-first, use the exact same columns in CSV.

| Column name | Purpose |
|---|---|
| `date_found` | When the lead entered your tracker |
| `platform` | LinkedIn, OLJ, Kalibrr, etc. |
| `job_title` | Raw title from posting |
| `company` | Employer name |
| `job_link` | Source link |
| `company_site` | Official company careers/homepage if found |
| `country_limit` | Philippines / Global / US-only / Unclear |
| `work_type` | Full-time / Part-time / Contract / Freelance / Internship |
| `remote_type` | Remote / Hybrid / Onsite |
| `timezone_overlap` | Good / Moderate / Bad |
| `salary_or_rate` | Exact range or text from posting |
| `tech_stack_keywords` | Python, Django, PHP, MySQL, API, etc. |
| `fit_score` | 0–100 using the rubric above |
| `fit_reason` | One-sentence explanation |
| `risks_or_mismatch` | React-heavy, seniority stretch, unclear geography, etc. |
| `status` | New / Reviewed / Shortlisted / Packet Ready / Awaiting Approval / Approved to Submit / Submitted / Rejected / Closed |
| `resume_version` | Filename or resume variant used |
| `cover_letter_version` | Filename or doc link |
| `app_answers_version` | Filename or doc link |
| `approval_packet_link` | Local path or doc link |
| `submission_method` | Easy Apply / Company site / Email / OLJ platform |
| `submit_button_note` | Exact button or final action that would submit |
| `approved_by_you` | Yes / No |
| `date_submitted` | Only fill after manual submission |
| `follow_up_date` | Planned follow-up date |
| `result` | Interview / No reply / Rejected / Offer |

The workflow should look like this:

| Step | What you do | Output |
|---|---|---|
| Find leads | Search core boards manually; import leads only from official feeds where allowed | New rows in tracker |
| Hard filter | Remove country-restricted, senior, React-heavy, scammy, or unclear jobs | Cleaner short list |
| Score | Apply the 0–100 rubric | Ranked list |
| Verify legitimacy | Check company website, board reputation, and scam signals; on OnlineJobs.ph, use Employer Search; on Indeed, remember the platform explicitly says it cannot guarantee employer identity and that job seekers must verify legitimacy | Safer shortlist |
| Tailor | Prepare targeted resume changes, cover letter, and likely application answers | Approval packet |
| Stop before submission | Present the exact package to you with link, fit, risks, edits, final text, and what button would submit | Awaiting approval |
| Submit manually | Only after you approve that exact application | Submitted record |
| Log and follow up | Record date, version used, and next action | Repeatable pipeline |

That **approval packet** should always contain exactly these fields before any submission:

```text
Job link:
Company:
Platform:
Fit score:
Why it fits:
Risks / mismatch:
Tailored resume changes:
Tailored cover letter:
Application answers:
Exact final text to submit:
What button or action would submit it:
Status: Awaiting your approval
```

This approach is safer than high-volume automation for two reasons. First, multiple platforms explicitly restrict bot behavior or application automation. Second, legitimacy still has to be checked by a human: Indeed says it does not guarantee employer identity and that job seekers must verify job offers, and OnlineJobs.ph offers built-in employer search specifically to help workers inspect potential employers. citeturn16view0turn0search9

## Truthful tailoring kit

### Resume tailoring rules that preserve truth

Your resume should sell **evidence**, not confidence theater.

| Rule | Do this | Do not do this |
|---|---|---|
| Positioning | Lead with backend, APIs, automation, internal tools, and business systems | Lead with React/frontend unless the job is clearly backend-first |
| Titles | Keep official titles if you had them; if you need clarity, use a truthful clarifier like “Software Engineer Intern” or “System Developer and Technical Support” | Invent stronger titles like “Full-Stack Engineer” or “AI Engineer” if that was not the real role |
| Skills | List Python, Django, PHP, MySQL, REST APIs, automation, Git/GitHub, Jira, basic HTML/CSS/JS | Claim expert JavaScript or strong React ability |
| Bullet writing | Use verbs like “built,” “maintained,” “tested,” “documented,” “supported,” “integrated,” “automated,” “debugged” | Use inflated verbs like “architected enterprise platform” unless that is actually defensible |
| Metrics | Use only metrics you can explain or document, like number of modules, users, reports, bug fixes, response time improvements, or ticket volume | Make up percentages, scale claims, or performance wins |
| AI usage | It is fine to mention AI tools as productivity support when relevant, especially for automation or prompt work | Hide behind AI to imply skills you cannot explain in an interview |
| Education | Keep “BS Computer Engineering, expected 2027” visible; for internships and junior roles this helps | Downplay student status when the role is junior/intern-friendly |
| Project selection | Prioritize projects that show backend logic, CRUD systems, data handling, integrations, QA, or business operations | Prioritize decorative frontend projects that do not reflect your real strengths |
| Full-stack jobs | Apply only when the backend/database/API side is central and frontend demands are modest | Apply to roles whose core stack is React/Next/TypeScript-heavy |
| Honesty test | Every line must survive the question: “Can I explain exactly what I did here?” | Use any claim you could not defend live |

A strong summary line for your current reality would look like this:

```text
Backend-leaning Computer Engineering student with hands-on internship and business-system experience in Django, PHP, MySQL, REST APIs, QA, and workflow automation. Comfortable building internal tools and data-driven web systems, with practical experience supporting production work through Git, Jira, and AI-assisted development workflows.
```

That summary is honest because it emphasizes backend, systems work, and AI-assisted workflow support without pretending you are an expert frontend specialist.

### Reusable cover letter template

```text
Subject: Application for [Job Title] — Jc Delos Santos

Dear [Hiring Manager Name or Hiring Team],

I am applying for the [Job Title] role at [Company]. I am a 3rd-year BS Computer Engineering student at Mariano Marcos State University and currently work as a Software Engineer Intern at Komunidad Global, where I support backend and QA-related work using Django, MySQL, Jira, and related tools. I have also built PHP/MySQL systems for retail operations, including POS and inventory workflows.

What makes this role a strong fit for me is the overlap with my practical experience in [backend development / APIs / automation / internal tools / technical support with coding]. I am most effective in roles where I can help build or improve real operational systems, work with data and business logic, and support reliable delivery without exaggerating my level of experience.

In my recent work, I have contributed to:
- [Tailored bullet tied to Job Requirement 1]
- [Tailored bullet tied to Job Requirement 2]
- [Tailored bullet tied to Job Requirement 3]

I am especially interested in this opportunity because [specific reason tied to company, product, mission, or stack]. I would value the chance to contribute as a junior but dependable builder who is honest about my strengths, coachable where needed, and focused on delivering useful work.

You can view my work here:
GitHub: github.com/Aresss615
LinkedIn: linkedin.com/in/johnchrisley
Website: johnchrisley.dev

Thank you for your time and consideration.

Sincerely,
John Chrisley E. Delos Santos
Preferred name: Jc
Email: johnchrisley4@gmail.com
Phone: 0947 893 8873
Location: Philippines
```

### Reusable prompts

Use these prompts **after** you upload your current resume, so the outputs can be grounded in the real document.

**Job-post analyzer**

```text
Act as a strict job-fit analyst for me.

My profile:
- Name: John Chrisley E. Delos Santos, preferred name Jc
- Location: Philippines
- 3rd-year BS Computer Engineering student, expected 2027
- Current work: Software Engineer Intern at Komunidad Global
- Other work: System Developer and Technical Support at J & J Grocery
- Stronger areas: Python, Django, PHP, MySQL, REST APIs, automation, AI tools, prompt engineering, Git/GitHub, Jira, basic HTML/CSS/JS
- Important constraint: do not position me as a strong React/frontend developer
- I build mostly with AI assistance, so do not overclaim independent senior-level expertise

Analyze this job post and return:
1. one-sentence summary
2. hard requirements
3. soft requirements
4. hidden risks or mismatch
5. whether it is likely Philippines-eligible
6. whether the seniority is realistic
7. which parts of my background are actually relevant
8. what evidence I would need to show
9. score it from 0 to 100 using this rubric:
   - geography and schedule fit 20
   - skill truthfulness 20
   - seniority realism 15
   - role alignment 15
   - flexibility 10
   - application safety and legitimacy 10
   - portfolio leverage 5
   - compensation clarity 5
10. final recommendation: apply / apply if tailored / skip

Job post:
[PASTE JOB POST]
```

**Resume tailoring prompt**

```text
Tailor my resume for the job below, but preserve strict truthfulness.

Rules:
- Do not add fake tools, years, titles, or achievements
- Do not over-position me as a React/frontend developer
- Prefer backend, APIs, automation, PHP, Django, MySQL, QA, Jira, internal tools, and practical business systems
- Keep student status honest
- Use bullets that I could defend in an interview
- If something is missing, mark it as a gap instead of inventing it

Return:
1. tailored professional summary
2. top skills section reordered for this job
3. revised bullets for Komunidad Global
4. revised bullets for J & J Grocery
5. suggested project bullets to add
6. items to remove or downplay
7. biggest remaining gaps
8. final ATS keyword checklist

Job:
[PASTE JOB POST]

Current resume text:
[PASTE RESUME TEXT]
```

**Cover letter prompt**

```text
Write a brief, credible cover letter for this job.

Requirements:
- sound junior but capable
- no fake confidence
- emphasize practical backend/API/automation experience
- mention I am a BS Computer Engineering student expected 2027
- mention Komunidad Global internship and J & J Grocery systems work
- avoid claiming strong React/frontend expertise
- keep it specific to the company and role
- 220 to 320 words
- plain English
- no hype, no clichés, no fake passion

Job post:
[PASTE JOB POST]

Tailored resume notes:
[PASTE TAILORED RESUME NOTES]
```

**Application-answer prompt**

```text
Help me answer application questions honestly and strategically.

Rules:
- answers must match my actual profile
- do not invent years of experience
- do not claim expert React/frontend ability
- if the question asks for a tool I only know at a basic level, say so clearly but positively
- make answers concise, professional, and human

My profile:
[PASTE RESUME TEXT OR PROFILE]

Job post:
[PASTE JOB POST]

Questions:
[PASTE APPLICATION QUESTIONS]

Return:
1. best final answer for each question
2. risk note if any answer is borderline
3. shorter backup version if character limits are tight
```

**Honesty and safety checker**

```text
Audit this application package before submission.

Check for:
1. fake or inflated claims
2. unsupported metrics
3. mismatch with my real skills
4. country or schedule restrictions
5. suspicious employer or unclear application flow
6. whether the role is too React/frontend-heavy
7. whether the final text sounds human and credible
8. final verdict: safe to submit / revise first / do not submit

My profile:
[PASTE RESUME TEXT]

Job:
[PASTE JOB POST]

Resume draft:
[PASTE DRAFT]

Cover letter draft:
[PASTE DRAFT]

Application answers:
[PASTE DRAFT]
```

## Launch plan and free local MVP

### Seven-day manual launch plan

| Day | What to do | Output by the end of the day |
|---|---|---|
| **Day one** | Upload your current resume PDF and source file. Create one Google Sheet using the schema above. Create folders named `resume`, `cover_letters`, `answers`, and `approval_packets`. | Baseline system ready |
| **Day two** | Set up saved searches on LinkedIn, Indeed PH, JobStreet, Kalibrr, and OLJ using the keyword bundles above. Turn on email alerts where available. | Repeatable lead inflow |
| **Day three** | Build your first 30-lead sheet: 10 from OLJ, 5 from LinkedIn, 5 from Indeed PH, 5 from JobStreet/Kalibrr, 5 from WWR/RemoteOK/Wellfound. Score every lead. | Ranked backlog |
| **Day four** | Shortlist the top 8–10 leads. Verify company legitimacy, location fit, and stack fit. Skip anything React-heavy, senior, vague, or suspicious. | Safe shortlist |
| **Day five** | Create three truthful resume variants: `backend-python`, `php-systems`, and `automation-support`. Draft one reusable cover letter base. | Tailoring assets |
| **Day six** | Prepare full approval packets for the top 3 jobs only. Each packet must include the exact final text and the exact action that would submit it. | Ready-for-approval applications |
| **Day seven** | Review the packets with me or by your own final checklist, then manually submit only the ones you explicitly approve. Log every submission and set follow-up dates. | Live pipeline |

### No-code MVP first

The no-code version is the one I recommend you launch first. It uses:

- Google Sheets for lead tracking
- Gmail labels and saved searches/email alerts
- Manual browsing on OLJ, LinkedIn, Kalibrr, JobStreet, and Indeed
- Official public feeds only for We Work Remotely and Remote OK
- Local folders for versioned resumes, letters, answers, and approval packets

That setup is enough to run a serious job hunt without paying for tools and without violating platform rules. The reason it works is that you only automate the **collection of public leads** where official feeds exist, while keeping **review, tailoring, and submission** human-controlled. That matches the official restrictions on LinkedIn, Indeed, Wellfound, We Work Remotely, and Mindrift. citeturn14view1turn16view0turn11view0turn25search2turn5view0

### Free local Python MVP design

After the no-code version is running, you can add a small local Python script that pulls leads from **Remote OK’s official API** and **We Work Remotely’s public RSS feed** into a CSV. Do **not** expand this into auto-apply or scraping for restricted job boards. Remote OK explicitly exposes a public API, and We Work Remotely explicitly offers a public RSS feed while prohibiting scraping outside its API/feed rules. citeturn24view0turn25search0turn25search2

Use this folder layout:

```text
job-hunt/
  data/
    leads_raw.csv
    leads_scored.csv
  templates/
    approval_packet.md
  scripts/
    fetch_leads.py
  resume/
  cover_letters/
  answers/
```

Setup commands:

```bash
python -m venv .venv
```

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install requests feedparser pandas python-dateutil
```

```bash
# macOS / Linux
source .venv/bin/activate
pip install requests feedparser pandas python-dateutil
```

A minimal lead collector:

```python
# scripts/fetch_leads.py
from __future__ import annotations

import csv
import re
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import pandas as pd
import requests

DATA_DIR = Path("../data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

REMOTEOK_API = "https://remoteok.com/api"
WWR_RSS = "https://weworkremotely.com/remote-jobs.rss"

KEYWORDS = [
    "backend", "python", "django", "php", "api", "automation",
    "technical support", "intern", "junior", "part time", "contract"
]

NEGATIVE_KEYWORDS = [
    "react", "frontend", "front-end", "senior", "staff", "principal", "lead"
]


def text_matches(text: str) -> tuple[bool, int]:
    lower = text.lower()
    if any(bad in lower for bad in NEGATIVE_KEYWORDS):
        return False, 0
    score = sum(1 for kw in KEYWORDS if kw in lower)
    return score > 0, score


def fetch_remoteok() -> list[dict]:
    resp = requests.get(REMOTEOK_API, headers={"User-Agent": "jc-job-hunt/1.0"}, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    rows: list[dict] = []
    for item in data[1:]:  # first object contains API legal text
        title = item.get("position", "") or ""
        company = item.get("company", "") or ""
        desc = item.get("description", "") or ""
        tags = " ".join(item.get("tags", []) or [])
        url = item.get("url", "") or ""
        combined = f"{title} {company} {tags} {desc}"

        ok, kw_score = text_matches(combined)
        if not ok:
            continue

        rows.append({
            "date_found": datetime.now(timezone.utc).isoformat(),
            "platform": "RemoteOK",
            "job_title": title,
            "company": company,
            "job_link": url,
            "work_type": "Unknown",
            "remote_type": "Remote",
            "salary_or_rate": f"{item.get('salary_min', '')}-{item.get('salary_max', '')}",
            "tech_stack_keywords": tags,
            "keyword_score": kw_score,
        })
    return rows


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "")


def fetch_wwr() -> list[dict]:
    feed = feedparser.parse(WWR_RSS)
    rows: list[dict] = []

    for entry in feed.entries:
        title = getattr(entry, "title", "") or ""
        link = getattr(entry, "link", "") or ""
        summary = strip_html(getattr(entry, "summary", "") or "")
        combined = f"{title} {summary}"

        ok, kw_score = text_matches(combined)
        if not ok:
            continue

        rows.append({
            "date_found": datetime.now(timezone.utc).isoformat(),
            "platform": "WeWorkRemotely",
            "job_title": title,
            "company": "",
            "job_link": link,
            "work_type": "Unknown",
            "remote_type": "Remote",
            "salary_or_rate": "",
            "tech_stack_keywords": "",
            "keyword_score": kw_score,
        })
    return rows


def main() -> None:
    rows = fetch_remoteok() + fetch_wwr()
    df = pd.DataFrame(rows)

    if df.empty:
        print("No matching leads found.")
        return

    df["fit_score"] = (
        df["keyword_score"] * 10
    ).clip(upper=60)

    # Manual-review defaults
    df["country_limit"] = "Unclear"
    df["timezone_overlap"] = "Unclear"
    df["risks_or_mismatch"] = ""
    df["status"] = "New"

    out = DATA_DIR / "leads_raw.csv"
    df.to_csv(out, index=False, quoting=csv.QUOTE_MINIMAL)
    print(f"Saved {len(df)} leads to {out.resolve()}")


if __name__ == "__main__":
    main()
```

Run it like this:

```bash
cd scripts
python fetch_leads.py
```

That script is intentionally limited. It is useful because it gives you a **daily lead inbox** from official public sources, but it still forces you to do the important parts manually: reading the posting, checking country restrictions, verifying legitimacy, tailoring truthfully, and stopping before submission until you approve the exact package.

For your first real MVP, keep it even simpler than the script above:

1. manually track OLJ, LinkedIn, Kalibrr, JobStreet, and Indeed  
2. let Python help only with Remote OK and We Work Remotely lead intake  
3. score everything in Sheets  
4. generate approval packets in Markdown or Google Docs  
5. never submit anything until the packet says **Awaiting your approval** and you explicitly approve that exact application