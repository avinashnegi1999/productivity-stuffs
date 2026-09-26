**Python-backend product companies in India: 157 companies across 8 files. Links checked 2026-09-26.**
Fintech 23 · E-commerce 15 · SaaS 34 · Edtech 10 · Healthtech 12 · Consumer apps 18 · Devtools/Infra 18 · Big tech 27

## Files
[fintech.md](fintech.md) · [ecommerce.md](ecommerce.md) · [saas.md](saas.md) · [edtech.md](edtech.md) · [healthtech.md](healthtech.md) · [consumer-apps.md](consumer-apps.md) · [devtools-infra.md](devtools-infra.md) · [big-tech-india.md](big-tech-india.md)

## How each column was filled

| Column | Method |
|---|---|
| **Inclusion** | Product company with Indian engineering, **and** at least one source showing Python used for backend work. The source is an official engineering blog, the company's GitHub, an official careers or ATS posting, or a posting the company wrote on a job board (Instahyre, Cutshort, LinkedIn, an investor job board). Postings that list Python only as one of 4 or more interchangeable languages, with no Python framework named, were **not** accepted. |
| **HQ** | AmbitionBox company profile, with manual fixes. This is the global HQ; big-tech rows are included for their India centres. |
| **Python Stack** | Frameworks named in the evidence source(s). "Python (framework Unverified)" means Python is confirmed but no framework was named. "— listed with Go/Java" means the posting also lists other backend languages. |
| **Fresher Hiring** | **Yes** = AmbitionBox has fresher (0 yr) SDE salary reports for the company, or an open posting targets SDE-1, new grads or 0–2 years. **Unclear** = no such evidence found. No company is marked **No**: I found no source that confirms an experienced-only policy, so treat Unclear companies with mostly senior postings as likely experienced-only. |
| **Fresher CTC** | AmbitionBox fresher (0 yrs experience) data for the company's SDE-type job title with the most reports. Shown as the min–max of reported **total CTC**, and only if at least 5 data points exist. Otherwise N/A. Not estimated. |
| **SDE-1 CTC** | AmbitionBox range for an SDE-1 job title (SDE1, SDE I, Software Engineer 1…). If no such title exists, the main SDE title's 1–3 yr experience range is used. Needs at least 5 data points. |
| **Salary Source** | Link to the AmbitionBox salary page, plus the month of AmbitionBox's last update and the number of data points (fresher n, SDE-1 n). |
| **Interview Rounds** | AmbitionBox's aggregated round pattern for the company's main SDE title, where it has at least 5 interviews. Otherwise my summary of at least 3 SDE interview reports on AmbitionBox, preferring fresher reports. Otherwise "Unverified". **OA** = online coding test, **Tech** = technical/DSA interview, **LLD/Design** = design round, **HM** = hiring-manager round, **HR** = HR round. |
| **Apply Link** | **(Live)** = a Python backend or SDE posting that was open on 2026-09-26, pulled from the company's own job system (Greenhouse, Lever, Ashby, Workday, Workable, or its careers site). Otherwise **(Careers)** = the official careers page or ATS board. No aggregator links. |
| **Verification Source** | The single URL used to accept the company. |

## Caveats
- **Python in coding rounds:** there is no public per-company policy. The online-test platforms these companies use (HackerRank, HackerEarth, CodeSignal, Codility) all support Python, and no listed company is known to ban it. Still, confirm with the recruiter.
- **2027 graduates:** campus drives for the 2027 batch are not published per company. Fresher Hiring = Yes means the company demonstrably hires freshers, not that it has a 2027 drive open.
- **Small samples:** check the `n` in Salary Source before relying on a salary. Ranges are min–max of self-reported offers, so one outlier can widen them.
- **Postings expire:** "(Live)" links, and verification links that point to postings, can close. Instahyre pages usually stay readable after a job closes.
- **Bot-blocked links:** a few links (Medium-hosted blogs such as lambda.blinkit.com, tech.bigbasket.com, medium.com/healthify-tech, and rubrik.com) return 403 to scripts but open normally in a browser.
- **Missing salary data:** some newer startups have no AmbitionBox data. Their salaries are shown as N/A rather than guessed.

## Checked and excluded (no verifiable Python backend)
Notable exclusions with reasons:
- **CRED:** backend postings list Python only among 5 accepted languages; Java/Go are primary.
- **Myntra, Walmart Global Tech:** Java backend.
- **Zomato:** PHP/Go/Java.
- **Freshworks:** Ruby on Rails/Java.
- **Dream11, Games24x7:** Java.
- **Truecaller:** Scala/Kotlin.
- **Testbook:** Go.
- **Nanonets:** Go APIs; Python for ML only.
- **Razorpay, Paytm, Zeta, Juspay:** current backend postings are PHP/Go/Java/Haskell with no Python-backend source.
- **Atomicwork:** its only Python evidence closed on the check date.

About 280 other candidates were dropped because no Python-backend source could be found.
