# Group-IB Threat Intelligence — Integrations (API Integration)

> **Nguồn:** `TI_Integrations.pdf` (483 trang) — chuyển sang Markdown ngày 2026-11-03.
> **Lưu ý:** 79 trang trong PDF là ảnh chụp màn hình/sơ đồ (trang 1–5, 23–36, 38–56, 58–76, 78–96, 361, 399, 471) nên không trích xuất được chữ — nội dung các trang đó không có trong file này. Một số bảng bị vỡ cột do trích xuất tự động từ PDF.

---

Content
       Integrations

       Starting Guide _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 5

       Initial Steps _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 5

       Steps to Get Started _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 5

       URLs and IP Addresses for Access _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 5

       API key generation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 5

       IP access list _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 7

       Test API Configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 9

       Request _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 9

       Response _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 9

       Troubleshooting _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 10

       Troubleshooting and Error Codes _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 12

       HTTP Response Codes _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 12

       Important Points to Avoid Errors _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 12

       API Limitations _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 15

       Quantity Requests Limitations _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 15

       Records limits _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 15

       IP Access List _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 17

       POC and Partner Access Limitations _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 18

       API Ticket Creation Guide _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 19

       Navigate to the Service Desk _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 19

       Click “Create Request” _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 19

       Choose category and fill out the form _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 20

       API and Integration Support _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 21

       Integration development request _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 96

       Collections Overview _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 98

       Threats and Actors _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 98

       Malware _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 98

       Darkweb _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 99

       Compromises _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 99

       Banking _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 100

       Suspicious Indicators _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 100

       Not presented in the interface _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 101

       Utility & Analysis Endpoints _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 102

       Legend _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 103

       Collections Details - Utilities _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 105

       User Granted Collections _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 105

       Sequence List _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 109

       Search _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 113

       IMC API _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 118

Content


       Collections Details - Feeds _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 134

       Threats and Actors - APT Threat Actors _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 134

       Threats and Actors - APT Threat Reports _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 145

       Threats and Actors - HI Threat Actors _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 157

       Threats and Actors - HI Threat Reports _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 167

       Threats and Actors - Open Threats _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 179

       Threats and Actors - Analyst Reports _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 188

       IOC Primary _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 195

       IOC Common _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 206

       Malware - C2 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 212

       Malware - Config _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 218

       Malware - Reports _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 224

       Malware - Suricata _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 231

       Malware - Yara _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 237

       Malware - Vulnerability _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 242

       Malware - Phishing Kit _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 250

       Darkweb - Discord _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 257

       Darkweb - Telegram _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 261

       Darkweb - Shops _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 269

       Darkweb - Forums _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 274

       Compromises - Account _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 280

       Compromises - Git Repository _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 290

       Compromises - Public Leak _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 294

       Compromises - Breached DB _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 302

       Banking - Cards _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 309

       Banking - Masked cards _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 314

       Banking - SPD _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 319

       Suspicious indicators - Deface _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 327

       Suspicious indicators - DDoS _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 334

       Suspicious indicators - Open Proxies IP _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 343

       Suspicious indicators - Phishing _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 348

       Suspicious indicators - Scanning IP _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 361

       Suspicious indicators - Socks Proxy IP _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 366

       Suspicious indicators - TOR IP _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 371

       Suspicious indicators - VPN IP _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 376

       Collections Details - Analysis _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 382

       Domain Whois _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 382

       IP Whois _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 388

       IP Scoring _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 395

       Domain Scoring _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 399

       Deprecated Collections _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 403

       Overview _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 403

       Collections: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 403

Content


       Reference: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 403

       Custom and native integrations _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 404

       List of integrations _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 404

       Explanatory notes _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 406

       Google SecOps _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 407

       Overview _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 407

       Installation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 407

       Configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 408

       Step 1. App configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 408

       Step 2. Connectors configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 409

       Step 3. Alerts configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 412

       Usage _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 413

       Data filtering _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 417

       Troubleshooting _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 417

       Common errors _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 418

       Download logs _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 418

       Common errors solution _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 418

       LogRhythm _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 420

       Installation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 420

       Configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 420

       Run the script _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 420

       Automation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 421

       Configuration script steps _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 421

       Troubleshooting _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 421

       MISP _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 422

       Installation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 422

       Configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 422

       Troubleshooting _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 425

       FAQ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 425

       ThreatConnect _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 426

       Installation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 426

       Configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 427

       Step 1. Add new Job _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 427

       Step 2. Collections configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 428

       Usage _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 430

       Data filtering _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 433

       Troubleshooting _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 440

       Enable Debug Logging _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 440

       Log Collection _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 440

       Testing API Connectivity via cURL _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 441

       Common Errors and Solutions _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 441

       Data Input Error Code (HTTP) in TC _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 442

       ArcSight SIEM Connector _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 443

Content


       ArcSight SIEM Connector _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 443

       Requirements _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 443

       Configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 443

       Deploy _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 444

       ArcSight FlexConnector Setup _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 444

       Working with the Integration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 445

       Available Collections _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 446

       Troubleshooting _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 448

       Custom API tools _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 453

       TI Data Export Utility _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 453

       Glossary _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 454

       Introduction _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 455

       Use Cases _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 456

       Installation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 457

       Running the Utility _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 458

       CLI Menu Structure Overview _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 459

       Data Export Utility Options _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 459

       Tips and Best Practices _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 466

       TI Python library _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 467

       ciaops _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 467

       License _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 467

       Installation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 467

       Usage _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 467

       Parsing _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 470

       Records limits _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 470

       Troubleshooting _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 470

       TI Postman configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 471

       Prerequisites _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 471

       Installation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 471

       Configuration _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 471

       Usage _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 471

       Example Requests _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 472

       Additional Notes _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 473

       Developer Guide _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 474

       Common Dev info _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 474

       API Logic Explanation _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 479

       API logic _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 479

       Sequence Update logic _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 480

       Search logic _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 481

Starting  Guide
       Initial Steps
       API is a powerful interface designed to seamlessly integrate Group-IB Threat Intelligence with your internal security and anti-fraud systems. It operates
       using the RESTful protocol, with all data returned in JSON format for easy parsing and integration.


       Steps to Get Started

          · IP Access List Provide your public IP addresses, and we’ll add them to the API access list.

          · Generate API Key Log in to your account, navigate to your profile, and generate an API_KEY. Be sure to save this key, as it will be required for
               API access. For API authorization, use your email and the generated API key instead of your portal password.

          · Start Using API Tools Once the previous steps are completed, you can test your API connection by following the steps outlined in the Test API
               Configuration article. Then, begin utilizing the API with tools such as Custom TI Data Export, Postman, and other integration utilities.
       Developing your own integration? Before you start building, review the ciaops Python library and the TI Postman collection. The ciaops library handles
       authentication, pagination, and rate limiting for you, and the Postman collection lets you explore the endpoints interactively - both are the
       recommended starting points for any custom integration.


       URLs and IP Addresses for Access

       To ensure the API and web interface function properly (this list is applicable for both API and web-interface), add the following URLs and IP addresses
       to your internal security access list:


       URLs:


          · tap.group-ib.com - Base domain for web portal and API access

          · sso.group-ib.com - Required for web portal


       IP-addresses


          · 148.251.50.14

          · 144.76.117.21

          · 138.201.56.157

          · 88.99.105.142

          · 94.130.70.148

          · 88.99.167.51


       API key generation

       To generate the API_KEY follow these steps:

· Navigate to Group-IB Threat Intelligence

          · Click your name in the upper-right corner and select Profile


          · Go to Security and Access -> Personal token


          · Click GENERATE TOKEN

· Enter your password, then click Save button to save API KEY and exit the settings.


       NOTE: Don’t forget to save all changes during API key generation!


       IP access list

       You can add your external IP addresses through your profile settings. Follow the steps below:


          · Navigate to Group-IB Threat Intelligence

          · Click your name in the upper-right corner, select Profile.

          · Go to Security and Access -> IP white list.

          · Click the Edit button and enter your trusted IP address.


          · Before entering another IP, click the “Create ‘X.X.X.X.’” line. Repeat this process for each IP address you want to add.

· Click Save to confirm and apply the changes, adding all IP addresses to your access list.


       NOTE: If you need to add a large number of IP addresses, or configure an access list for an entire company or cloud system, please create a ticket
       through the Service Desk for assistance.

Test API Configuration
       Request

       Once you’ve configured the API, you can verify that everything is working correctly by using the following curl request in your terminal:


       curl -u login:api_key https://tap.group-ib.com/api/v2/user/granted_collections


       Alternatively, you can verify everything in Postman as shown in the screenshot below: Request: GET
       https://tap.group-ib.com/api/v2/user/granted_collections


       For the password field enter the API key you have generated. This key is required for successful authentication.


       If you haven’t generated an API key yet, please refer to the Initial Steps article for step-by-step instructions on how to create one.


       Response

This request will help ensure that your API setup is functioning as expected. If you receive a successful response, your API is correctly configured.


       Troubleshooting

       Make sure you follow all the steps in the Initial Steps. If you receive an error response (e.g., 401 Unauthorized or 403 Forbidden), ensure that:


          · Your login and API key are correct.

               · Your IP address is whitelisted in the access list.

               · You are using the correct API endpoint.

               · The Authorization header is properly formatted.

Then refer to the Troubleshooting and error codes article for further details.

Troubleshooting and Error Codes
       HTTP Response Codes

          · 400: Bad Request A bad request usually stems from incorrect request formatting. Check the error details in the response JSON and adjust the
               request accordingly.

          · 401: Unauthorized This code indicates a failed authentication attempt. Make sure you’re using Basic Authentication with the correct username
               and API key. Verify that these credentials are accurate and included in the request header.

          · 403: Forbidden Access issues, such as IP restrictions or invalid API keys, can cause this error. Confirm that your IP address is allowed, the API
               key is valid, and you have permission to access the requested feed. Check your settings or contact Group-IB support if necessary.

          · 404: Not Found The requested resource does not exist on the server. Double-check that the URL is correct and that the resource is available.

          · 429: Too Many Requests This response means you’ve exceeded the allowable request rate. Reduce your request frequency or adjust the limit
               parameter to stay within the acceptable range.

          · 500: Internal Server Error This error indicates a server-side problem while processing your request. Wait and try again later.

          · 504: Gateway Timeout or Timeout The request took too long to process. Try reducing the limit parameter when making API requests to
               decrease the load and avoid timeouts.


       Note: If these response codes don’t resolve your issue or if further troubleshooting is needed, you can reach out to our support team via the Service
       Desk for additional assistance. For detailed steps on how to create a Service Desk ticket, please refer to API Ticket Creation Guide.


       Important Points to Avoid Errors

          · Avoid Using DF and DT Parameters with seqUpdate In the updated endpoint /updated, do not use the DF (date from) and DT (date to)
               parameters along with the seqUpdate parameter. This is because the seqUpdate already acts as a timestamp for filtering data, and including
               DF and DT will introduce conflicting date filters. For example, avoid using the endpoint in this format:
               /api/v2/ioc/common/updated?sequpdate=15995952916289&df=2024-01-01&dt=2024-09-09 Using both date filters (DF/DT) alongside
               seqUpdate will result in errors, and while the API might return a response, the data will be inaccurate and inconsistent with the expected
               results as shown in the screenshot below: The screenshot below illustrates the proper configuration for sending a GET request using
               Postman:

The following screenshot highlights a common mistake that should be avoided:


          · Do Not Use Your Account Password as the API Key Ensure that you do not mistakenly use your account password as the API key. API keys are
               designed to authenticate your requests securely, and using your password could not only cause errors but also expose your credentials to
               unauthorized access, compromising account security.

API Limitations
       Quantity Requests Limitations

       Due to technical constraints, the API has several request rate limitations:


       You are allowed 1 request per 1 second per company per feed per route. This means you can only poll a specific feed from one account. For instance,
       while you cannot poll the feed at /api/v2/hi/threat/updated more frequently than once per 1 second, you can simultaneously poll different feeds such
       as /api/v2/ioc/primary/updated and /api/v2/hi/threat/updated


       Records limits

       Default limit is 100 records per request. Due to different size of feeds there are different limits for getting data:


                                       Feed                                                                            Limit


                            osi/vulnerability/updated                                                                   500


                            osi/public_leak/updated                                                                     100


                           osi/git_repository/updated                                                                   100


                    compromised/account_group/updated                                                                   500


                      compromised/breacheddb/updated                                                                    100


                   compromised/bank_card_group/updated                                                                  500


                      compromised/masked_card/updated                                                                   500


                          compromised/spd/updated                                                                       500


                         compromised/access/updated                                                                     500


                      compromised/messenger/updated                                                                     100


                        compromised/discord/updated                                                                     100


                           darkweb/forums/updated                                                                       100

Feed                  Limit


                              hi/threat/updated            10


                           hi/threat_actor/updated        100


                           hi/open_threats/updated        100


                             apt/threat/updated            10


                          apt/threat_actor/updated        100


                       suspicious_ip/tor_node/updated     100


                      suspicious_ip/open_proxy/updated    5000


                      suspicious_ip/socks_proxy/updated   5000


                          suspicious_ip/vpn/updated       100


                        suspicious_ip/scanner/updated     5000


                           malware/config/updated         100


                          malware/malware/updated         100


                            malware/cnc/updated           1000


                            malware/yara/updated          5000


                         malware/signature/updated        5000


                             ioc/primary/updated          2500


                            ioc/common/updated            5000


                            attacks/ddos/updated          5000


                         attacks/phishing_kit/updated     1000

Feed                                                                            Limit


                        attacks/phishing_group/updated                                                                 1000


                             attacks/deface/updated                                                                    100


       IP Access List

       The API is only accessible from trusted IP addresses. During validation, we check the following IP lists:


       1. User’s IP List You can set up your own allowed IP list by navigating to your Profile page -> Security and Access -> Allowed IP list.


       2. Company’s IP List You can find the IP assets of your company on the Company page -> Assets -> (IP v4 addresses | IP v6 addresses) Note: The
       Company’s IP list is fixed. If you need to add new IP addresses to your assets, please submit a request via the Service Desk.


       3. Global IP addresses list These IP addresses belong to vendors with whom we have integrations. If you use one of these vendors, their IPs are
       already in our access list. Here is the list of these IPs:


                          Vendor                                                                      IP Address(es)


                          Anomali                             54.208.4.186, 105.184.118.114, 194.46.126.6, 197.101.51.179, 197.101.53.127, 216.38.139.26,

                                                           34.227.3.92, 34.231.7.29, 35.168.197.59, 35.172.241.145, 35.173.107.231, 50.1.114.34, 50.1.114.40,

                                                         52.23.133.33, 52.34.112.37, 52.37.145.253, 52.73.15.50, 54.147.241.218, 54.87.172.249, 54.87.192.13,

                                                        81.128.219.20, 94.204.8.39, 3.225.1.124, 52.24.86.178, 52.37.145.25, 52.158.28.64/28, 20.50.68.128/29,

                                                                                             51.144.56.96/28, 40.113.178.32/29


                         EclecticIQ                                                            34.247.181.230, 3.75.187.123


                       Splunk Cloud                           34.225.9.69, 52.70.128.234, 3.225.120.176, 34.231.205.169, 122.179.137.12, 122.169.101.20,

                                                                    34.193.4.124, 52.21.139.207, 103.108.207.48/28, 122.179.137.12/32, 122.169.101.20/32


                      ThreatConnect                                                                   54.159.242.168

Vendor                                                                    IP Address(es)


                    Microsoft Sentinel                 40.68.209.23, 40.68.222.65, 20.193.17.32, 20.197.219.106, 20.48.128.36, 20.199.186.58, 40.80.86.109,

                                                       52.158.170.36, 20.52.212.85, 52.251.70.29, 20.74.12.78, 20.194.150.139, 20.194.17.254, 51.13.75.153,

                                                             102.133.139.160, 20.197.113.87, 40.123.207.43, 51.11.168.197, 20.71.8.176, 40.64.106.65


                        Cortex XSOAR                        35.244.250.18, 35.227.237.180, 34.120.31.199, 34.120.87.77, 35.241.28.254, 34.117.211.129,

                                                      34.120.229.65, 34.98.68.183, 35.186.207.80, 34.111.6.153, 34.117.240.208, 34.160.28.41, 35.190.0.180,

                                                      34.111.134.57, 34.111.129.144, 35.222.81.194, 34.90.67.58, 35.203.82.121, 34.89.56.78, 34.84.125.129,

                                                             34.87.83.144, 35.189.18.208, 34.107.57.23, 35.200.158.164, 34.65.248.119, 34.116.216.55,

                                                              35.234.8.249, 34.18.46.240, 34.155.222.152, 34.165.156.139, 35.222.81.194, 34.90.67.58,

                                                      35.203.82.121, 34.89.56.78, 34.84.125.129, 34.87.83.144, 35.189.18.208, 34.107.57.23, 35.200.158.164,

                                                            34.65.248.119, 34.116.216.55, 35.234.8.249, 34.18.46.240, 34.155.222.152, 34.165.156.139,

                                                        35.225.156.101, 34.69.88.119, 34.147.67.188, 34.90.16.31, 35.203.57.162, 35.203.90.79, 34.142.3.42,

                                                             34.142.44.136, 34.146.60.215, 34.84.93.160, 35.240.144.192, 35.240.255.15, 35.244.73.76,

                                                        35.201.22.63, 34.107.83.197, 34.159.53.97, 34.93.118.113, 35.244.5.205, 34.65.233.60, 34.65.222.25,

                                                              34.116.223.119, 34.118.92.214, 104.199.223.229, 34.81.38.132, 34.18.39.0, 34.18.32.96,

                                                                             34.155.197.131, 34.155.5.100, 34.165.33.165, 34.165.27.131


                    Filigran, OpenCTI                         5.135.76.0/27 141.95.234.96/28 164.132.148.32/27 135.148.64.32/27 51.89.91.160/27


                          Liberty91                                                                  35.210.22.235


       If you are missing your vendor IP, please inform us via Service Desk.


       POC and Partner Access Limitations

       For users with a Proof of Concept (POC) license or a trial, feed consumption is limited to data from the last 30 days. This same 30-day data access
       restriction also applies to partner accounts. Ensure that your use cases align with these limitations to effectively leverage the available data within the
       set timeframe.

API Ticket Creation Guide
       This guide will walk you through the steps required to create a ticket in the service desk system. Follow these instructions to ensure proper reporting
       and tracking of issues.


       Disclaimer#1: When creating an API support ticket, it is crucial to select the correct category and provide all necessary information and data required
       for issue resolution. Failure to do so may result in your inquiry not being addressed. Choosing the wrong category or omitting essential details can
       delay or prevent effective troubleshooting and support.


       Disclaimer#2: Coins are not charged for requests related to integrations.


       Navigate to the Service Desk

          · From the TI Portal Dashboard, locate and click on the Service Desk tab in the left-side panel.


       Click “Create Request”

          · In the Service Desk section, click on the Create Request button to begin a new support ticket

Choose category and fill out the form

       From the menu, select the most appropriate category for your issue:


          · API and Integration Support: Use this category if you require assistance with existing native integrations, REST API functionalities, or
               STIX/TAXII 2.x protocols.

          · Integration development request: Select this option when you need to request the development of a new integration.

API and Integration Support

          · Choose sub category for your request:

Rest APIv2

All questions related to use of JSON API

STIX/TAXII 2.x

Questions related to STIX/TAXII 2.x

Native integration applications

Installation and troubleshooting of native applications

· Fill out the Required Information:


               For Rest APIv2:

User name

User’s email, where API token is established

Public IP

External IP of your instance, used for API communication

Used API routes

All API endpoints are listed here. Specify “None” if there is no any

Description

Add comments if you want to provide additional information

For STIX/TAXII 2.x:

User name

User’s email, where API token is established

Public IP

External IP of your instance, used for STIX/TAXII integration

Application

Application used for STIX/TAXII integration

Description

Add comments if you want to provide additional information

For Native integration applications:

User name

User’s email, where API token is established

Public IP

External IP of your instance, used for integration

Application

3rd party vendor application name

Description

Add comments if you want to provide additional information

· Submit the request Click the Send button to submit the request


       Integration development request

          · Describe the case

          · Drag and drop the necessary files


          · Submit the request Click the Send button to submit the request

By selecting the correct request type, you streamline the process and reduce the time it takes for our support team to resolve issues or respond to
       your inquiries.

Collections Overview
       Threats and Actors


          Submodule          Individual/Common                APIv2 Endpoint            TTL (Days)         Admiralty     Severity         Hunting Rules


               Actors        Common + Individual         apt/threat_actor/updated           360               None           9              Supported


                                                          hi/threat_actor/updated           360               None           9              Supported


         Last threats        Common + Individual            apt/threat/updated              360            Can differ        9              Supported


                                                             hi/threat/updated              360            Can differ        9              Supported


        Open Threats               Common                hi/open_threats/updated           None            Mostly B3         5              Supported


               Analytic            Common                   hi/analytic/updated            None                A1          N/A                 N/A

               Reports


       Note: For Last threats submodule reports can be found at the threat actor profile on the left side. Threats are mostly in the “Common” category, but
       some of them can be individual for clients. TTL is not provided in the API for the endpoints in this table.


       Malware


          Submodule          Individual/Common                APIv2 Endpoint            TTL (Days)         Admiralty     Severity         Hunting Rules


               Configs             Individual            malware/config/updated              30                A1            9                 N/A


               Reports             Common                 malware/malware/updat            None               None           9                 N/A

                                                                     ed


          Signatures               Common                malware/signature/updat           None               None           8                 N/A

           (Suricata)                                                ed

Submodule        Individual/Common         APIv2 Endpoint                TTL (Days)          Admiralty          Severity     Hunting Rules


           Yara rules           Common            malware/yara/updated               None                None                8             N/A


         Phishing Kits          Common           attacks/phishing_kit/upd             30               mostly B2             9          Supported

                                                             ated


        Vulnerabilities         Common           osi/vulnerability/updated            30                  A1                 9          Supported


       Darkweb


         Submodule        Individual/Common      APIv2 Endpoint        TTL (Days)           Admiralty          Severity     Comment    Hunting Rules


               Instant        Individual       compromised/messe             None               None             N/A         TTL not        N/A

        messengers                                nger/updated                                                              provided

         (Telegram)                                                                                                           in API


           Discord            Individual       compromised/discord           None               None             N/A         TTL not        N/A

                                                    /updated                                                                provided

                                                                                                                              in API


               Shops          Individual       compromised/access             90                A2               N/A         TTL not        N/A

                                                    /updated                                                                provided

                                                                                                                              in API


           Forums             Individual       darkweb/forums/upda           None               None             N/A         TTL not        N/A

                                                       ted                                                                  provided

                                                                                                                              in API


       Compromises

Submodule      Individual/Common       APIv2 Endpoint          TTL (Days)   Admiralty   Severity   Hunting Rules


           Accounts          Individual      compromised/account_g          90           A2         N/A          N/A

                                                  roup/updated


         Public leaks        Individual      osi/public_leak/updated        30           C3         N/A          N/A


           Git Leaks         Individual      osi/git_repository/update      30           A1         N/A          N/A

                                                        d


         Breached DB         Individual      compromised/breachedd          N/A          C3         N/A          N/A

                                                    b/updated


       Banking


          Submodule      Individual/Common       APIv2 Endpoint          TTL (Days)   Admiralty   Severity   Hunting Rules


          Bank cards         Individual      compromised/bank_card          90           A2         N/A          N/A

                                                 _group/updated


                                             compromised/masked_c           90           A2         N/A          N/A

                                                   ard/updated


          Suspicious         Common          compromised/spd/updat          90           A2         N/A          N/A

               Payment                                  ed

               Details


       Suspicious Indicators

Submodule        Individual/Common         APIv2 Endpoint              TTL (Days)          Admiralty          Severity     Hunting Rules


                 Tor            Common           suspicious_ip/tor_node/u           30                  A1                 3          Supported

                                                         pdated


          Open proxy            Common           suspicious_ip/open_prox            15                  C3                 3          Supported

                                                        y/updated


         Socks proxy            Common           suspicious_ip/socks_pro             2                  A1                 3          Supported

                                                       xy/updated


                VPN             Common           suspicious_ip/vpn/updat            30                  A2                 1          Supported

                                                           ed


         Scanning IP            Common           suspicious_ip/scanner/u            15                  C3                 1          Supported

                                                         pdated


                DDoS            Common            attacks/ddos/updated              30                  A2                 3          Supported


               Phishing         Common           attacks/phishing_group/            30                A2-A3                6          Supported

                                                         updated


               Deface           Common            attacks/deface/updated            30                  B2                 3             N/A


       Not presented in the interface


         Submodule        Individual/Common      APIv2 Endpoint       TTL (Days)         Admiralty           Severity     Comment    Hunting Rules


           Malware            Common           malware/cnc/updated          90                None               9         TTL not        N/A

                                                                                                                          provided

                                                                                                                            in API

Submodule       Individual/Common            APIv2 Endpoint             TTL (Days)        Admiralty      Severity    Comment          Hunting Rules


               IOC           Common                 ioc/primary/updated          Per record       Per record    Derive from   Replaces             N/A

                                                                                 (365-14600)                      riskScore   ioc/comm

                                                                                                                                 on.

                                                                                                                               Network

                                                                                                                                 (IP,

                                                                                                                               domain,

                                                                                                                              URL) and

                                                                                                                              file (hash)

                                                                                                                              indicators

                                                                                                                               with risk

                                                                                                                                score,

                                                                                                                              malware

                                                                                                                              and threat

                                                                                                                                actor

                                                                                                                              attribution

                                                                                                                              . Includes

                                                                                                                              malware/

                                                                                                                                 cnc

                                                                                                                              indicators

                                                                                                                                   .

       Utility & Analysis Endpoints


               Module              APIv2 Endpoint                      Type                    Description                             Hunting Rules


               General         user/granted_collections                Utility         Retrieve list of collections                         N/A

                                                                                    available to authenticated user.

                                                                                     Also serves as a health check

                                                                                                 endpoint.


               General              sequence_list                      Utility       Get sequence update numbers                            N/A

                                                                                     for all collections based on a

                                                                                               specific date.

Module                    APIv2 Endpoint                      Type                 Description                            Hunting Rules


               General                         search                       Utility        Global search across all                           N/A

                                                                                            available collections for

                                                                                       indicators, domains, IPs, hashes,

                                                                                             and other data types.


                Graph                  utils/graph/domain                  Analysis      Domain WHOIS information                             N/A

                                                                                        endpoint providing registration

                                                                                            and ownership data for

                                                                                         second-level domain names.


                Graph                     utils/graph/ip                   Analysis     IP address WHOIS information                          N/A

                                                                                        endpoint providing registration

                                                                                             and ownership data.


               Scoring                      scoring/ip                     Analysis     Returns a 0-100 risk score for                        N/A

                                                                                         one or more IPv4 addresses.


               Scoring                   scoring/domain                    Analysis     Returns a 0-100 risk score for                        N/A

                                                                                            one or more domains.


                 IMC                      imc/incidents                     Utility     Retrieve Incident Management                          N/A

                                                                                             Center incidents, their

                                                                                        aggregated events, and Prevyn

                                                                                                  AI insights.


       Legend

          · Common - collections, which consist of data that is displayed to all users.

          · Individual - collections, which consist of only user-related data. For example, if the client is a bank, he will receive only cards with the BIN
               numbers provided by his bank.

          · APIv2 Endpoint - the designation of the collection endpoint in Group-IB TI APIv2.

          ·

TTL (Time To Live) - maximum length of time indicator a dataset (package) can exist. Calculated in days. During this period, we ensure that
               this data is IoC.

          · Admiralty - Approximate Admiralty Code. You can learn more about calculating all types of risk scores in the article Data Classification.

          · Severity - refers to the level or degree of seriousness, commonly used in the context of cybersecurity to assess the importance of a
               vulnerability or incident. This measure helps cybersecurity professionals and administrators evaluate the necessity and urgency of taking
               actions to prevent or mitigate threats. Severity is typically assessed on a scale, for example, from 0 to 9, where 1 is low, and 9 - the highest.

          · Hunting Rules - refers to the request parameter apply_hunting_rules (set to 1 to enable or 0 to disable). Supported = the collection accepts this
               parameter. N/A = not applicable: either by nature of the collection (e.g. utilities, combined feeds, or collections where the parameter is not
               used) or because filtering by hunting rules is usually applied by default; the flag can still be used technically where applicable (for example, in
               search requests).

          · General Modules are common and available for all types of licenses.

Collections Details - Utilities
       User Granted Collections
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint retrieves a list of all collections that are granted/available to the authenticated user. It serves as both a health check endpoint and a way
       to discover which collections your account has access to. This is useful for programmatically determining which collection endpoints you can query.

       Collection-Specific Information


                                                   Property                                                                        Value


                                                   Method                                                                           GET


                                                     Path                                                            /api/v2/user/granted_collections


                                               Collection Name                                                             Granted Collections


                                                     Type                                                                          Utility


                                                  Rate Limit                                              1 request per 10 seconds per company per feed (see

                                                                                                                             API Limitations)


                                               Short Description                                        Utility endpoint to retrieve list of collections available to

                                                                                                         the authenticated user. Also serves as a health check

                                                                                                                                 endpoint.


       Request

       Request URL
        GET /api/v2/user/granted_collections
       Query Parameters


       This endpoint does not accept any query parameters.

       Request Headers


                 Header                Type                    Required                                Description                               Example


                 Accept               string                       No                      Content type accepted by the client               application/json

Header                 Type                       Required                                  Description                                   Example


               Authorization            string                        Yes                   Basic authentication credentials (see Initial                   Basic

                                                                                                               Steps)                            base64(LOGIN:API_KEY)


                User-Agent              string                        No                       User-Agent string with product metadata         SIEM/QRadar_2020.10.6/G

                                                                                               (optional but recommended - especially          roupIB_TI_1.0.0/gibuser@g

                                                                                                useful in troubleshooting on our end).          roup-ib.com/ciaops_3.0.0

                                                                                                               Format:

                                                                                           PlatformType/PlatformName_PlatformVersio

                                                                                           n/AppName_AppVersion/Username/LibNam

                                                                                                            e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                       Header                                                    Description                                                     Example


                    Content-Type                                            Response content type                                            application/json


                  Content-Encoding                                            Content encoding                                                      gzip


                    Cache-Control                                          Cache control directives                                         no-cache, private


                           Allow                                           Allowed HTTP methods                                                     GET


       Response Body Schema

       Root Object
       [ { "collection": string,     "label": string,   "route": string,    "huntingRulesUsed": boolean }, ... ]
       The response is an array of collection objects.

       Collection Object


                   Field                     Type                               Required                                               Description


                 collection                 string                                 Yes                                   Collection identifier (e.g., “apt/threat”,

                                                                                                                                  “malware/malware”)

Field                      Type                                Required                                                    Description


                    label                     string                                    Yes                          Human-readable label for the collection (e.g., “Threats &

                                                                                                                                   Actors :: Nation-State :: Report”)


                    route                     string                                    Yes                           Route identifier for the collection. May be “NO_ROUTE”

                                                                                                                                 for collections without a direct route


               huntingRulesUsed              boolean                                    Yes                         Whether hunting rules are used for this collection. If true,

                                                                                                                      the apply_hunting_rules parameter can be used when

                                                                                                                                         querying this collection


       Example Request

       Basic Request
        curl -X GET 'https://tap.group-ib.com/api/v2/user/granted_collections' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        [ { "collection": "apt/threat",       "label": "Threats & Actors :: Nation-State :: Report",         "route": "apt/report",     "huntingRulesUsed": true }, {
       "collection": "apt/threat_actor",     "label": "Threats & Actors :: Nation-State",         "route": "apt/threat_actor",     "huntingRulesUsed": true }, {          "collection":
       "hi/threat",     "label": "Threats & Actors :: Cybercriminals :: Report",        "route": "human_intel/threats",      "huntingRulesUsed": true }, {          "collection":
       "hi/threat_actor",     "label": "Threats & Actors :: Cybercriminals",        "route": "human_intel/threat_actor",         "huntingRulesUsed": true }, {        "collection":
       "hi/open_threats",      "label": "Threats & Actors :: Open Threats",        "route": "ta/open-threats",      "huntingRulesUsed": true }, {         "collection":
       "hi/analytic",     "label": "Threats & Actors :: Analytics",      "route": "__NO_ROUTE__",       "huntingRulesUsed": false }, {          "collection": "malware/malware",
          "label": "Malware/Source",      "route": "malware/reports",        "huntingRulesUsed": false }, {          "collection": "malware/cnc",      "label": "Malware/Source ::
       C2",      "route": "__NO_ROUTE__",      "huntingRulesUsed": false }, {           "collection": "malware/config",      "label": "Malware/Source",       "route":
       "malware/configs",        "huntingRulesUsed": true }, {          "collection": "malware/signature",       "label": "Malware :: Suricata signatures",      "route":
       "__NO_ROUTE__",         "huntingRulesUsed": false }, {          "collection": "malware/yara",      "label": "Malware :: Yara rules",     "route": "__NO_ROUTE__",
       "huntingRulesUsed": false }, {         "collection": "attacks/ddos",       "label": "Attack :: DDoS",     "route": "attacks/ddos",      "huntingRulesUsed": true }, {
       "collection": "attacks/phishing_group",         "label": "Attack :: Phishing",     "route": "attacks/phishing_group",          "huntingRulesUsed": true }, {
       "collection": "attacks/phishing_kit",      "label": "Malware :: Phishing kits",        "route": "attacks/phishing_kit",     "huntingRulesUsed": true }, {
       "collection": "compromised/account_group",            "label": "Compromise & leaks :: Accounts",           "route": "__NO_ROUTE__",        "huntingRulesUsed": true }, {
         "collection": "compromised/bank_card_group",            "label": "Compromise & leaks :: Bank cards",           "route": "__NO_ROUTE__",        "huntingRulesUsed": true
       }, {      "collection": "compromised/messenger",         "label": "Threats & Actors :: Instant Messengers",          "route": "__NO_ROUTE__",         "huntingRulesUsed":
       true }, {      "collection": "compromised/discord",         "label": "Threats & Actors :: Discord Messenger",          "route": "__NO_ROUTE__",        "huntingRulesUsed":
       true }, {      "collection": "suspicious_ip/vpn",      "label": "Suspicious IP :: VPN",      "route": "suspicious/vpn",        "huntingRulesUsed": true }, {
       "collection": "suspicious_ip/tor_node",         "label": "Suspicious IP :: Tor Nodes",       "route": "suspicious/tor",     "huntingRulesUsed": true }, {          "collection":
       "osi/vulnerability",    "label": "Malware :: Vulnerabilities",      "route": "osi/vulnerabilities",     "huntingRulesUsed": true }, {        "collection": "osi/public_leak",
          "label": "Compromise & leaks :: Public Leaks",         "route": "osi/public_leak",      "huntingRulesUsed": true }, {          "collection": "osi/git_repository",
       "label": "Compromise & leaks :: Code repositories",            "route": "osi/git_repository",    "huntingRulesUsed": true }, {         "collection": "ioc/common",
       "label": "IOC :: Common",       "route": "__NO_ROUTE__",         "huntingRulesUsed": false } ]
       Usage Patterns

       Health Check

This endpoint can be used as a health check to verify: - API authentication is working - API connectivity is available - User account is active and has
       granted collections
       curl 'https://tap.group-ib.com/api/v2/user/granted_collections' \ -u 'LOGIN:API_KEY'
       Discovering Available Collections


       Use this endpoint to programmatically discover which collections your account can access:
       # Get all granted collections curl 'https://tap.group-ib.com/api/v2/user/granted_collections' \ -u 'LOGIN:API_KEY' | jq '.[].collection'
       Filtering Collections by Hunting Rules Support


       To find collections that support hunting rules:
       curl 'https://tap.group-ib.com/api/v2/user/granted_collections' \ -u 'LOGIN:API_KEY' | jq '.[] | select(.huntingRulesUsed == true) | .collection'
       Related Endpoints


          · Get sequence update numbers: GET /api/v2/sequence_list?date=

Sequence List
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint retrieves a list of sequence update numbers for all available collections based on a specified date. This is useful for determining the
       starting seqUpdate value when you want to begin iterating through feeds from a specific date, rather than starting from the beginning (seqUpdate=0).

       Collection-Specific Information


                                                  Property                                                                       Value


                                                   Method                                                                         GET


                                                    Path                                                                /api/v2/sequence_list


                                              Collection Name                                                                Sequence List


                                                    Type                                                                         Utility


                                                  Rate Limit                                             1 request per 10 seconds per company per feed (see

                                                                                                                            API Limitations)


                                              Short Description                                          Utility endpoint to retrieve sequence update numbers

                                                                                                              for all collections based on a specific date.


       Request

       Request URL
        GET /api/v2/sequence_list
       Query Parameters


                 Parameter                Type                 Required               Default                    Description                      Example


                   date                  string                  Yes                      -           Date for which the sequence list is       2024-10-14

                                                                                                      requested. Format: YYYY-MM-DD

Parameter              Type              Required                  Default                        Description                       Example


                    collection             string               No                        -               Optional collection name to filter            apt/threat

                                                                                                          results for a specific collection. If

                                                                                                              provided, returns only the

                                                                                                          sequence update number for that

                                                                                                                       collection.


       Query Parameter Details:


          · date:


               · Required parameter

               · Format: YYYY-MM-DD (e.g., 2024-10-14)

               · Returns sequence update numbers for all collections as of this date


          · collection:


               · Optional parameter

               · If specified, returns only the sequence update number for the specified collection

               · Collection name format: module/submodule (e.g., apt/threat, malware/malware)


       Request Headers


                 Header                 Type                   Required                                  Description                                 Example


                  Accept                string                    No                          Content type accepted by the client                 application/json


               Authorization            string                    Yes                  Basic authentication credentials (see Initial                   Basic

                                                                                                            Steps)                          base64(LOGIN:API_KEY)

Header                Type                    Required                                  Description                              Example


               User-Agent             string                     No                       User-Agent string with product metadata     SIEM/QRadar_2020.10.6/G

                                                                                          (optional but recommended - especially      roupIB_TI_1.0.0/gibuser@g

                                                                                           useful in troubleshooting on our end).      roup-ib.com/ciaops_3.0.0

                                                                                                          Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                       e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                            Header                                          Description                                                 Example


                     Content-Type                                     Response content type                                         application/json


                 Content-Encoding                                        Content encoding                                                 gzip


                     Cache-Control                                    Cache control directives                                      no-cache, private


                            Allow                                     Allowed HTTP methods                                                GET


       Response Body Schema

       Root Object
       { "list": { "collection_name": integer,    ... } }


                  Field                   Type                             Required                                            Description


                     list                object                               Yes                         Object containing collection names as keys and their

                                                                                                          corresponding sequence update numbers as values


       List Object


       The list object contains key-value pairs where: - Key: Collection name (e.g., "apt/threat", "malware/malware", "suspicious_ip/vpn") - Value: Sequence
       update number (integer) for that collection as of the specified date


       Example structure:

{ "list": {   "apt/threat": 17287776262152,     "apt/threat_actor": 17286912357507,       "attacks/ddos": 1728853572756170,    "malware/malware":
       17287232595059,         "suspicious_ip/vpn": 1728863618842723 } }
       Example Request

       Basic Request (All Collections)
       curl -X GET 'https://tap.group-ib.com/api/v2/sequence_list?date=2024-10-14' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request for Specific Collection
       curl -X GET 'https://tap.group-ib.com/api/v2/sequence_list?date=2024-10-14&collection=apt/threat' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

       Success Response (200 OK) - All Collections
        { "list": { "apt/threat": 17287776262152, "apt/threat_actor": 17286912357507,             "attacks/ddos": 1728853572756170,    "attacks/deface":
       1728159944011312,         "attacks/phishing_group": 1728863999999999,       "attacks/phishing_kit": 1728861626744927,
       "compromised/account_group": 1720706185734061,             "compromised/bank_card_group": 1719857916092329,         "compromised/masked_card":
       1728845300540036,         "compromised/messenger": 1728853200000000,           "compromised/discord": 1727905789379160,        "hi/threat":
       17288283676769,         "hi/threat_actor": 17288283685184,    "hi/open_threats": 1728834812506702,       "ioc/common": 17288526154476,
       "malware/cnc": 1728777672644977,          "malware/config": 17288510093459,       "malware/malware": 17287232595059,      "malware/signature":
       17288479212942,         "malware/yara": 17219413666444,      "osi/git_repository": 1728734319944338,     "osi/public_leak": 1728863904288975,
       "osi/vulnerability": 17288546508036,      "suspicious_ip/open_proxy": 1728863532650054,         "suspicious_ip/scanner": 1728863423033642,
       "suspicious_ip/socks_proxy": 1728863966244699,           "suspicious_ip/tor_node": 1728846278012000,      "suspicious_ip/vpn": 1728863618842723 } }
       Success Response (200 OK) - Specific Collection


       If the collection parameter is provided, the response will contain only that collection:
       { "list": { "apt/threat": 17287776262152 } }
       Usage Patterns

       Getting Sequence Update for a Specific Date


       To start iterating through feeds from a specific date:


          · Get sequence update for the desired date:
               curl 'https://tap.group-ib.com/api/v2/sequence_list?date=2024-10-14&collection=apt/threat' \ -u 'LOGIN:API_KEY'

          · Extract the sequence update number from the response:
               { "list": { "apt/threat": 17287776262152 } }

          · Use this sequence update number in your first request to the collection endpoint:
               curl 'https://tap.group-ib.com/api/v2/apt/threat/updated?seqUpdate=17287776262152&limit=10' \ -u 'LOGIN:API_KEY'

        · Continue iterating using the top-level seqUpdate from subsequent responses
       Getting All Collections’ Sequence Updates


       To get sequence updates for all collections at once:
        curl 'https://tap.group-ib.com/api/v2/sequence_list?date=2024-10-14' \ -u 'LOGIN:API_KEY'
       This is useful for: - Monitoring multiple collections - Determining which collections have updates on a specific date - Bulk synchronization across
       collections

       Related Endpoints


          · Get active collections: GET /api/v2/user/granted_collections

Search
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint provides a global search functionality across all available collections in the Group-IB Threat Intelligence platform. It allows you to search
       for indicators, domains, IPs, hashes, and other data types across multiple collections simultaneously, returning a summary of matches in each
       collection along with direct links to query those collections.

       Collection-Specific Information


                                                  Property                                                                        Value


                                                   Method                                                                          GET


                                                     Path                                                                    /api/v2/search


                                              Collection Name                                                                 Global Search


                                                     Type                                                                         Utility


                                                  Rate Limit                                              1 request per 10 seconds per company per feed (see

                                                                                                                             API Limitations)


                                              Short Description                                            Global search endpoint to find indicators across all

                                                                                                                 available collections with direct links to

                                                                                                                       collection-specific queries.


       Request

       Request URL
        GET /api/v2/search
       Query Parameters


                 Parameter                Type                 Required               Default                     Description                       Example


                      q

Parameter               Type              Required                  Default                  Description                 Example


                                           string               Yes                        -             Search query. Can be an IP         8.8.8.8

                                                                                                      address, domain, hash, or other

                                                                                                       indicator type. The search will

                                                                                                     automatically detect the type and

                                                                                                     search across relevant collections.


                      df                   string                No                        -          Date from. Filter results to items   2024-01-01

                                                                                                       seen from this date onwards.

                                                                                                           Format: YYYY-MM-DD


                      dt                   string                No                        -           Date to. Filter results to items    2024-10-01

                                                                                                        seen up to this date. Format:

                                                                                                                YYYY-MM-DD


       Query Parameter Details:


          · q:


               · Required parameter

               · Can be various indicator types:

                   · IP addresses (IPv4): 8.8.8.8

                   · Domains: example.corp

                   · File hashes (MD5, SHA1, SHA256): abc123...

                   · URLs: http://example.corp/path

                   · Other indicator types supported by the platform


               · The search automatically detects the indicator type and searches across relevant collections


          · df (date from):


               · Optional parameter

               · Format: YYYY-MM-DD

               · Filters results to items that were first seen or detected from this date onwards

               · Useful for time-bounded searches


          · dt (date to):


               ·

Optional parameter

               · Format: YYYY-MM-DD

               · Filters results to items that were first seen or detected up to this date

               · Often used together with df to define a date range


       Request Headers


                 Header                  Type                    Required                                    Description                                 Example


                  Accept                 string                     No                           Content type accepted by the client                application/json


               Authorization             string                     Yes                      Basic authentication credentials (see Initial                Basic

                                                                                                                Steps)                          base64(LOGIN:API_KEY)


                User-Agent               string                     No                        User-Agent string with product metadata          SIEM/QRadar_2020.10.6/G

                                                                                              (optional but recommended - especially           roupIB_TI_1.0.0/gibuser@g

                                                                                               useful in troubleshooting on our end).          roup-ib.com/ciaops_3.0.0

                                                                                                               Format:

                                                                                        PlatformType/PlatformName_PlatformVersio

                                                                                         n/AppName_AppVersion/Username/LibNam

                                                                                                            e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                                 Description                                                      Example


                     Content-Type                                         Response content type                                              application/json


                  Content-Encoding                                          Content encoding                                                      gzip


                    Cache-Control                                        Cache control directives                               max-age=0, must-revalidate, private


                         Allow                                           Allowed HTTP methods                                                     GET

Response Body Schema

       Root Object
       [ { "apiPath": string,        "label": string,   "link": string,   "count": integer,     "time": number,      "detailedLinks": object | null }, ... ]
       The response is an array of search result objects, one for each collection that contains matches.

       Search Result Object


                   Field                       Type                               Required                                                    Description


                 apiPath                       string                                Yes                                Collection API path (e.g., “suspicious_ip/scanner”,

                                                                                                                                           “attacks/deface”)


                   label                       string                                Yes                             Human-readable label for the collection (e.g., “Suspicious

                                                                                                                                   IP :: Scanners”, “Attack :: Deface”)


                    link                       string                                Yes                               Direct API link to query this collection with the search

                                                                                                                      term. This link can be used to get detailed results from

                                                                                                                                         the specific collection


                  count                       integer                                Yes                                    Number of matches found in this collection


                   time                       number                                 Yes                             Query execution time in seconds (floating point number)


               detailedLinks               object | null                              No                                       Additional detailed links (usually null)


       Example Request

       Basic Search Request
        curl -X GET 'https://tap.group-ib.com/api/v2/search?q=8.8.8.8' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Search with Date Range
        curl -X GET 'https://tap.group-ib.com/api/v2/search?q=8.8.8.8&df=2024-01-01&dt=2024-10-01' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Search for Domain
        curl -X GET 'https://tap.group-ib.com/api/v2/search?q=example.corp' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Search for Hash
        curl -X GET 'https://tap.group-ib.com/api/v2/search?q=abc123def456...' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        [ { "apiPath": "suspicious_ip/scanner",            "label": "Suspicious IP :: Scanners",       "link":
       "https://tap.group-ib.com/api/v2/suspicious_ip/scanner?q=ip:8.8.8.8",                  "count": 1,     "time": 0.29085319,     "detailedLinks": null }, {       "apiPath":
       "attacks/deface",       "label": "Attack :: Deface",   "link": "https://tap.group-ib.com/api/v2/attacks/deface?q=ip:8.8.8.8",              "count": 1,       "time":
       0.406312784,        "detailedLinks": null }, {      "apiPath": "osi/public_leak",       "label": "Compromise & leaks :: Public Leaks",        "link":
       "https://tap.group-ib.com/api/v2/osi/public_leak?q=ip:8.8.8.8",             "count": 21847,          "time": 0.429146568,     "detailedLinks": null }, {       "apiPath":
       "suspicious_ip/open_proxy",         "label": "Suspicious IP :: Open Proxy",      "link": "https://tap.group-ib.com/api/v2/suspicious_ip/open_proxy?q=ip:8.8.8.8",
          "count": 17,     "time": 0.522133669,     "detailedLinks": null }, {      "apiPath": "malware/config",         "label": "Malware/Source",       "link":
       "https://tap.group-ib.com/api/v2/malware/config?q=ip:8.8.8.8",              "count": 20,       "time": 0.655176984,      "detailedLinks": null } ]

Usage Patterns

       Quick Indicator Lookup


       Use this endpoint for quick lookups across all collections:
       # Search for an IP address curl 'https://tap.group-ib.com/api/v2/search?q=8.8.8.8' \ -u 'LOGIN:API_KEY'
       Time-Bounded Search


       Search for indicators within a specific time range:
        # Search for indicators seen between January and October 2024 curl
       'https://tap.group-ib.com/api/v2/search?q=8.8.8.8&df=2024-01-01&dt=2024-10-01' \ -u 'LOGIN:API_KEY'
       Following Up on Search Results


       After getting search results, you can use the provided link to get detailed results from specific collections:
        # First, get search results SEARCH_RESULTS=$(curl 'https://tap.group-ib.com/api/v2/search?q=8.8.8.8' \ -u 'LOGIN:API_KEY') # Extract a link from
       the results (e.g., for suspicious_ip/scanner) # Then query that collection directly curl
       'https://tap.group-ib.com/api/v2/suspicious_ip/scanner?q=ip:8.8.8.8' \ -u 'LOGIN:API_KEY'
       Filtering Results by Count


       You can filter results to only show collections with matches:
       # Using jq to filter results with count > 0 curl 'https://tap.group-ib.com/api/v2/search?q=8.8.8.8' \ -u 'LOGIN:API_KEY' | jq '.[] | select(.count > 0)'
       Related Endpoints


          · Collection-specific search: GET /api/v2//updated?q=

IMC API
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       The Incident Management Center (IMC) API provides programmatic access to the incidents generated by your IMC rules. It returns incidents together
       with their aggregated events, the rule and rule revision that produced them, and the Prevyn AI insight when AI analysis is enabled for the rule. This lets
       you route IMC incidents into the systems your team already works in - SIEM, SOAR, or ITSM - instead of triaging them only in the portal.


       For an explanation of what IMC is, how rules and aggregation work, and how incidents are triaged in the interface, see Overview and Managing
       Incidents & Rules in the Manual.


       The API is built around three endpoints:


          · List updated incidents - retrieves incidents using a delta cursor, so each call returns only what changed since the previous one.

          · Fetch an incident - retrieves a single incident by its identifier.

          · List incident events - pages through the events aggregated into an incident, for one collection at a time.


       Note: The IMC API is read-only. It does not create, modify, or delete incidents, rules, or event statuses. Changing an incident status, reassigning an
       incident, and creating or editing rules are done in the Threat Intelligence portal.


       Note: The IMC API is not currently available in the ciaops Python library. Call it directly over HTTP.

       Collection-Specific Information


                                                     Property                                                                      Value


                                                      Method                                                                        GET


                                                       Path                                                                 /api/v2/imc/incidents


                                                 Collection Name                                                                  IMC API


                                                      Module                                                             Incident Management Center


                                                       Type                                                                        Utility


                                                    Rate Limit                                                               See API Limitations


                                                 Short Description                                         Retrieve Incident Management Center incidents, their

                                                                                                                aggregated events, and Prevyn AI insights.

Request

       Request URL
        GET /api/v2/imc/incidents/updated GET /api/v2/imc/incidents/{id} GET
       /api/v2/imc/incidents/{incidentId}/matches/{collection}
       List Updated Incidents


       Returns a page of incidents together with a nextSyncToken. Incidents are delivered in batches of up to 100 per request.


                  Parameter              Type             Required                  Default                    Description                    Example


                  syncToken             string               No                        -               Delta cursor returned by the       S1MAAAAA...O8AQ

                                                                                                     previous call as nextSyncToken.

                                                                                                    Omit it to start from the beginning

                                                                                                         of your incident history.


                 filter.statuses        string               No                        -               Incident status. Repeat the        INCIDENT_STATUS_

                                                                                                    parameter to match any of several          TO_DO

                                                                                                                statuses.


               filter.collections       string               No                        -             Collection the incident’s events     COLLECTION_DARK_

                                                                                                   belong to. Repeat the parameter to           WEB

                                                                                                    match any of several collections.


                filter.priorities       integer              No                        -            Rule priority, from 1 to 10. Repeat          2

                                                                                                      the parameter to match any of

                                                                                                            several priorities.


               filter.scoringFrom       integer              No                        -              Lower bound of the rule score,             50

                                                                                                              from 0 to 100.


                filter.scoringTo        integer              No                        -              Upper bound of the rule score,            100

                                                                                                      from 0 to 100. Must be greater

                                                                                                   than or equal to filter.scoringFrom.

Parameter                Type               Required                  Default                     Description                       Example


               filter.updatedAtFrom          string                No                        -              Return incidents updated at or         2026-09-01T00:00:0

                                                                                                            after this moment. Format: RFC                0Z

                                                                                                                         3339.


                filter.updatedAtTo           string                No                        -              Return incidents updated at or         2026-09-30T23:59:5

                                                                                                           before this moment. Format: RFC                9Z

                                                                                                                         3339.


               filter.incidentRuleIds        string                No                        -            Identifier of the rule that generated 019ed5d1-5517-73f8

                                                                                                             the incident. Must be a UUID.         -b3c4-65c91e0fcc56

                                                                                                            Repeat the parameter to match

                                                                                                                  any of several rules.


               filter.assigneeUserIds        integer               No                        -            Identifier of the user the incident is         12345

                                                                                                          assigned to. Repeat the parameter

                                                                                                            to match any of several users.


                filter.authorUserIds         integer               No                        -             Identifier of the user who created            12345

                                                                                                           the rule. Repeat the parameter to

                                                                                                              match any of several users.


                     filter.tags             string                No                        -             Tag inherited from the incident’s          ransomware

                                                                                                             rule. Repeat the parameter to

                                                                                                              match any of several tags.


       Query Parameter Details:


          · syncToken:


                 · Opaque, fixed-length cursor. Do not construct, parse, or truncate it - pass back exactly the value you received.

                 · URL-encode the value when adding it to a request. It may contain characters that are not safe in a query string.

                 · An invalid value returns 400 with a decode sync token message.


          · filter parameters:

· The filter. prefix is required. A parameter sent without it - for example statuses instead of filter.statuses - is ignored, and the request
                 returns unfiltered results.

               · Enumerated values must be given by name, not by number. filter.statuses=5 returns 400.

               · Repeating a parameter combines its values with OR. Different parameters combine with AND. For example, repeating filter.statuses
                 twice and adding filter.collections returns incidents that have either status and belong to that collection.


       Fetch an Incident


       Returns a single incident by its identifier, including its rule revision and Prevyn AI insight. The response body is the Incident object itself, not a wrapper.


                    Parameter                         Type                Required                             Description                           Example


                         id                         string                  Yes                     Incident identifier. Must be a UUID.     01a08c0d-413d-748c-8d

                                                                                                                                                b6-321dc0344aba


       A well-formed identifier that does not exist returns 404; a value that is not a UUID returns 400.

       List Incident Events


       Returns the events aggregated into an incident for a single collection. An incident that combines triggers from several collections is read one
       collection at a time; use the matchCounts.byCollection object of the incident to see which collections contain events and how many.


                    Parameter                         Type                Required                             Description                           Example


                     incidentId                     string                  Yes                     Incident identifier. Must be a UUID.     01a08b31-831d-7ae5-8b

                                                                                                                                                30-91c379fd47f4


                     collection                     string                  Yes                  Collection path segment. See the table           vulnerabilities

                                                                                                                  below.


                  Parameter                    Type            Required                   Default                      Description                     Example


                   sortOrder                   string             No                         -                  Order in which events are        SORT_ORDER_DESC

                                                                                                                      returned. Use

                                                                                                                   SORT_ORDER_DESC.

Parameter                  Type             Required         Default                  Description                  Example


                pageToken                 string                No              -            Cursor returned by the previous    ChoyMDI2LTA5...

                                                                                            call as nextPageToken. Omit it to

                                                                                                 request the first page.


       Important! Always page with sortOrder=SORT_ORDER_DESC. Paging with SORT_ORDER_ASC returns duplicate events on the second page and stops
       returning a page token, so the full set cannot be retrieved.


       Collection path segments:


                                     Collection                                                     Path segment


                                   Vulnerabilities                                                  vulnerabilities


                                     Accounts                                                   compromised-accounts


                                    Bank cards                                                   compromised-cards


                               Masked bank cards                                             compromised-masked-cards


                                       Shops                                                     compromised-shops


                                     Darkweb                                                           dark-web


                                   Breached DB                                                       breached-db


                           Suspicious payment details                                            suspicious-payments


                                    Public leaks                                                     public-leaks


                                    Last threats                                                        threats


                                     Git leaks                                                         git-leaks


       Request Headers

Header                 Type                     Required                                    Description                               Example


                  Accept                string                        No                         Content type accepted by the client               application/json


               Authorization            string                        Yes                   Basic authentication credentials (see Initial                Basic

                                                                                                               Steps)                          base64(LOGIN:API_KEY)


                User-Agent              string                        No                       User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                               (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                                useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                               Format:

                                                                                           PlatformType/PlatformName_PlatformVersio

                                                                                           n/AppName_AppVersion/Username/LibNam

                                                                                                            e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.


       All field names are in camelCase. Numeric identifiers of users are returned as strings. Objects that are not set are returned as null.

       Response Headers


                       Header                                                    Description                                                   Example


                    Content-Type                                            Response content type                                           application/json


                           Vary                              Headers affecting the cached representation                                    Accept-Encoding


       Response Body Schema

       Root Object


       The response of the List updated incidents endpoint:
        { "incidents": [ Incident, ... ], "nextSyncToken": string }


                   Field                     Type                               Required                                            Description


                 incidents

Field                   Type                            Required                                       Description


                                           array                             Yes                   Incidents in this batch. Up to 100 items. An empty array

                                                                                                             means there is nothing left to read.


               nextSyncToken              string                             Yes                        Cursor to pass as syncToken in the next call.


       The response of the List incident events endpoint:
        { "matches": [ { "matchInfo": RuleMatchInfo }, ... ], "nextPageToken": string }


                   Field                   Type                            Required                                       Description


                 matches                   array                             Yes                            Events in this page. Up to 100 items.


               nextPageToken              string                              No                   Cursor to pass as pageToken to request the next page.

                                                                                                                   Absent on the last page.


       Incident Object
        { "id": string, "status": string, "number": integer, "windowStart": string, "windowEnd": string, "matchCounts": RuleMatchCounts,
       "incidentRuleRevision": IncidentRuleRevision, "assignee": UserInfo, "aiSummary": AiSummary, "createdAt": string, "updatedAt": string }


                   Field                   Type                            Required                                       Description


                    id                    string                             Yes                   Unique incident identifier (UUID). Use this value to fetch

                                                                                                              the incident and to read its events.


                  status                  string                             Yes                         Current incident status. See Incident Status.


                  number                  integer                            Yes                     Sequence number of the incident within the rule that

                                                                                                     generated it. It is not unique across rules - use id to

                                                                                                                     identify an incident.


                windowStart               string                             Yes                      Start of the aggregation window that produced the

                                                                                                                 incident. Format: RFC 3339.

Field                       Type                              Required                                             Description


               windowEnd                      string                               Yes                          End of the aggregation window that produced the

                                                                                                                           incident. Format: RFC 3339.


               matchCounts                   object                                Yes                      Number of aggregated events, in total and per collection.


           incidentRuleRevision              object                                Yes                      The exact revision of the rule that generated the incident.


                assignee                  object | null                            No                       User the incident is assigned to, or null when the incident

                                                                                                                                  is unassigned.


               aiSummary                  object | null                            No                        Prevyn AI insight, or null when AI analysis is off for the

                                                                                                                        rule or has not produced a result.


                createdAt                     string                               Yes                         When the incident was created. Format: RFC 3339.


                updatedAt                     string                               Yes                      When the incident was last updated. Format: RFC 3339.


       RuleMatchCounts Object
       { "total": integer, "byCollection": {      "vulnerability": integer,   "compromisedAccount": integer,     "compromisedCard": integer,
       "compromisedMaskedCard": integer,           "compromisedShop": integer,        "darkWeb": integer,   "breachedDb": integer,    "suspiciousPayment": integer,
       "publicLeak": integer,     "threat": integer,   "gitLeak": integer } }


                  Field                       Type                              Required                                             Description


                  total                      integer                               Yes                         Total number of events aggregated into the incident.


               byCollection                  object                                Yes                         Number of events per collection. Every key is always

                                                                                                                    present; collections with no events are 0.


       IncidentRuleRevision Object
        { "id": string, "incidentRuleId": string, "isCurrent": boolean, "versionNumber": integer, "collectionRules": CollectionRules, "incidentRule":
       IncidentRule, "createdAt": string }

Field                   Type                             Required                                              Description


                     id                    string                               Yes                                   Identifier of this rule revision (UUID).


               incidentRuleId              string                               Yes                           Identifier of the rule (UUID). Stable across revisions.


                  isCurrent               boolean                               Yes                           Whether this revision is the rule’s current one. false

                                                                                                            means the rule has been edited since this incident was

                                                                                                                                    generated.


               versionNumber               integer                              Yes                           Revision number, incremented each time the rule is

                                                                                                                                      saved.


               collectionRules             object                               Yes                           Trigger queries of this revision, keyed by collection.

                                                                                                                      Collections without a trigger are null.


                incidentRule               object                               Yes                                    Rule attributes as of this revision.


                 createdAt                 string                               Yes                           When this revision was created. Format: RFC 3339.


       Each entry of collectionRules that is not null contains the trigger query:


                    Field                   Type                             Required                                              Description


                   query                   string                               Yes                         The Lucene query used as the trigger for this collection.


       IncidentRule Object
        { "id": string, "name": string, "author": UserInfo, "assignee": UserInfo, "tags": [ string, ... ], "priority": integer, "scoring": integer, "createdAt": string,
        "updatedAt": string }


                    Field                   Type                             Required                                              Description


                     id                    string                               Yes                                           Rule identifier (UUID).

Field                      Type                    Required                          Description


                  name                       string                    Yes                    Rule name as set in the portal.


                 author                     object                     Yes                      User who created the rule.


                assignee                 object | null                 No       Default assignee for incidents this rule generates, or null.


                  tags                       array                     Yes      Tags assigned to the rule. Incidents inherit them. Empty

                                                                                                when the rule has no tags.


                 priority                   integer                    Yes      Rule priority, from 1 (highest) to 10 (lowest). Corresponds

                                                                                                 to P1-P10 in the portal.


                 scoring                    integer                    Yes              Numeric score of the rule, from 0 to 100.


               createdAt                     string                    Yes           When the rule was created. Format: RFC 3339.


               updatedAt                     string                    Yes         When the rule was last updated. Format: RFC 3339.


       UserInfo Object


                  Field                      Type                    Required                          Description


                    id                       string                    Yes       User identifier. Returned as a string, but supplied as an

                                                                                integer in filter.assigneeUserIds and filter.authorUserIds.


                  email                      string                    Yes                         User email address.


       AiSummary Object
       { "title": string, "description": string, "level": string }


                  Field                      Type                    Required                          Description


                   title

Field                  Type                            Required                                            Description


                                          string                             Yes                           Generated one-line title describing the incident.


                 description              string                             Yes                         Generated narrative describing what the underlying

                                                                                                           events show and what to do next. Formatted as

                                                                                                            Markdown and may contain several sections.


                    level                 string                             Yes                          Assessed severity of the underlying threat. See AI

                                                                                                                            Summary Level.


       Note: Prevyn AI can make mistakes. Its insights are a preliminary assessment intended to accelerate triage, not replace it - we recommend verifying
       them before acting.

       RuleMatchInfo Object
       { "idInIncident": string, "collectionItemId": string, "status": string, "matchedAt": string }


                    Field                  Type                            Required                                            Description


                 idInIncident             string                             Yes                          Opaque identifier of the event within the incident.


               collectionItemId           string                             Yes                         Identifier of the record in the corresponding Threat

                                                                                                       Intelligence collection. Use it to retrieve the full record -

                                                                                                        see Resolving Events to Threat Intelligence Records.


                   status                 string                             Yes                         Current status of the event. See Rule Match Status.


                 matchedAt                string                             Yes                        When the event matched the rule. Format: RFC 3339.


       Enumerations


       Incident Status

Value                             Portal label


                  INCIDENT_STATUS_TO_DO                         To do


               INCIDENT_STATUS_PROCESSING                    In progress


                INCIDENT_STATUS_ON_HOLD                        On hold


                INCIDENT_STATUS_RESOLVED                      Resolved


           INCIDENT_STATUS_FALSE_POSITIVE                       False


                INCIDENT_STATUS_CANCELLED                    Cancelled


       Rule Match Status


       Event statuses are separate from incident statuses.


                           Value                             Portal label


                 RULE_MATCH_STATUS_NEW                          New


          RULE_MATCH_STATUS_IN_PROGRESS                      In progress


                RULE_MATCH_STATUS_DONE                          Done


        RULE_MATCH_STATUS_FALSE_POSITIVE                        False


       Collection


       Used in filter.collections.


                              Value                             Collection


                   COLLECTION_VULNERABILITY                   Vulnerabilities


               COLLECTION_COMPROMISED_ACCOUNT                    Accounts

Value                             Collection


               COLLECTION_COMPROMISED_CARD                  Bank cards


        COLLECTION_COMPROMISED_MASKED_CARD              Masked bank cards


               COLLECTION_COMPROMISED_SHOP                     Shops


                    COLLECTION_DARK_WEB                      Darkweb


                  COLLECTION_BREACHED_DB                   Breached DB


               COLLECTION_SUSPICIOUS_PAYMENT        Suspicious payment details


                  COLLECTION_PUBLIC_LEAK                    Public leaks


                     COLLECTION_THREAT                      Last threats


                    COLLECTION_GIT_LEAK                      Git leaks


       AI Summary Level


                                   Value                            Meaning


                              LEVEL_LOW                      Low assessed severity


                            LEVEL_MEDIUM                   Medium assessed severity


                             LEVEL_HIGH                      High assessed severity


       Sort Order


                                   Value                            Meaning


                           SORT_ORDER_DESC     Newest events first. The supported order for paging.

Value                                                                                      Meaning


                                   SORT_ORDER_ASC                                                  Oldest events first. Not supported for paging beyond the first page.


       Example Request


       Note: In the examples below, set the GIB_CREDENTIALS environment variable to your LOGIN:API_KEY pair before running the command.

       First Request
        curl -X GET 'https://tap.group-ib.com/api/v2/imc/incidents/updated' \ -u "$GIB_CREDENTIALS" \ -H 'Accept: application/json'
       Subsequent Requests
        curl -X GET -G 'https://tap.group-ib.com/api/v2/imc/incidents/updated' \ -u "$GIB_CREDENTIALS" \ -H 'Accept: application/json' \ --data-urlencode
       'syncToken=S1MAAAAA...O8AQ'
       Filtered Request
        curl -X GET -G 'https://tap.group-ib.com/api/v2/imc/incidents/updated' \ -u "$GIB_CREDENTIALS" \ -H 'Accept: application/json' \ --data-urlencode
       'filter.statuses=INCIDENT_STATUS_TO_DO' \ --data-urlencode 'filter.statuses=INCIDENT_STATUS_PROCESSING' \ --data-urlencode
       'filter.collections=COLLECTION_VULNERABILITY' \ --data-urlencode 'filter.scoringFrom=90' \ --data-urlencode 'filter.scoringTo=100'
       Fetch a Single Incident
        curl -X GET 'https://tap.group-ib.com/api/v2/imc/incidents/01a08c0d-413d-748c-8db6-321dc0344aba' \ -u "$GIB_CREDENTIALS" \ -H 'Accept:
       application/json'
       List the Events of an Incident
        curl -X GET -G 'https://tap.group-ib.com/api/v2/imc/incidents/01a08c0d-413d-748c-8db6-321dc0344aba/matches/threats' \ -u
       "$GIB_CREDENTIALS" \ -H 'Accept: application/json' \ --data-urlencode 'sortOrder=SORT_ORDER_DESC'
       Example Response

       Success Response (200 OK) - List Updated Incidents
        { "incidents": [ { "id": "01a08c0d-413d-748c-8db6-321dc0344aba",                               "status": "INCIDENT_STATUS_TO_DO",                   "number": 411,
       "windowStart": "2026-09-10T15:00:00Z",                  "windowEnd": "2026-09-10T16:00:00Z",               "matchCounts": {            "total": 2,       "byCollection": {
       "vulnerability": 0,          "compromisedAccount": 0,               "compromisedCard": 0,                "compromisedMaskedCard": 0,                    "compromisedShop": 0,
       "darkWeb": 0,          "breachedDb": 0,               "suspiciousPayment": 0,             "publicLeak": 0,          "threat": 2,        "gitLeak": 0           }    },
       "incidentRuleRevision": {            "id": "019f0462-ef69-713e-ba17-6f5a38264710",                     "incidentRuleId": "019ed5d1-5517-73f8-b3c4-65c91e0fcc56",
       "isCurrent": true,          "versionNumber": 3,           "collectionRules": {          "vulnerability": null,        "compromisedAccount": null,
       "compromisedCard": null,                "compromisedMaskedCard": null,                  "compromisedShop": null,               "darkWeb": null,               "breachedDb": null,
       "suspiciousPayment": null,               "publicLeak": null,         "threat": {          "query": "country:\"US\" AND expertise:\"Ransomware\""                            },
       "gitLeak": null       },         "incidentRule": {         "id": "019ed5d1-5517-73f8-b3c4-65c91e0fcc56",                    "name": "Last threats US",                   "author": {
       "id": "12345",             "email": "analyst@example.corp"                },       "assignee": null,         "tags": ["US ransomware", "darkweb"],                   "priority": 1,
       "scoring": 100,            "createdAt": "2026-06-17T13:42:06.359256Z",                    "updatedAt": "2026-07-17T14:11:13.225308Z"                     },        "createdAt":
       "2026-06-26T14:43:40.521077Z"                },       "assignee": null,        "aiSummary": {       "title": "example",        "description": "example",                 "level":
       "LEVEL_MEDIUM"              },     "createdAt": "2026-09-10T16:01:14.044968Z",                  "updatedAt": "2026-09-10T16:01:20.676338Z"                    } ], "nextSyncToken":
       "S1MAAAAA...O8AQ" }
       Success Response (200 OK) - List Incident Events
        { "matches": [ {   "matchInfo": {     "idInIncident": "eyJ0aW1lc3RhbXAiOiIyMDI2LTA5LTEwVDE1OjU5OjI1LjczMVoiLCJzZXFfbm8iOjJ9",
       "collectionItemId": "da00b1cbd51ad1559a492bc55f820a2a22812698",                               "status": "RULE_MATCH_STATUS_NEW",                       "matchedAt":
       "2026-09-10T15:59:25.731Z"               }   },   {      "matchInfo": {          "idInIncident":
       "eyJ0aW1lc3RhbXAiOiIyMDI2LTA5LTEwVDE1OjU5OjI1LjczMVoiLCJzZXFfbm8iOjF9",                                          "collectionItemId":
       "ff88e3833abb934b59d110a7acc83db71ad9e4a5",                           "status": "RULE_MATCH_STATUS_NEW",                     "matchedAt": "2026-09-10T15:59:25.731Z"                    }
       } ]}
       Error Response (400 Bad Request)
        { "code": 3, "message": "invalid parameter \"filter.statuses\": unknown enum: BOGUS_STATUS", "details": [] }
       Error Response (404 Not Found)
        { "code": 5, "message": "not found", "details": [] }
       Usage Patterns

       Incremental Synchronization

The List updated incidents endpoint is a delta feed. Each response carries a nextSyncToken that marks your position, and each call returns up to 100
       incidents.


          · Make the first call without a token to begin reading your incident history:     curl -G 'https://tap.group-ib.com/api/v2/imc/incidents/updated' -u
       "$GIB_CREDENTIALS"

          · Store the nextSyncToken from the response and pass it back on the next call:         curl -G 'https://tap.group-ib.com/api/v2/imc/incidents/updated' -u
       "$GIB_CREDENTIALS" \           --data-urlencode 'syncToken='

          · Repeat until incidents comes back empty. At that point you have read everything, and the response returns the same token you sent. Persist
               that token.

          · Poll on a schedule using the stored token. Each later call returns only the incidents created or updated since the previous one, and yields a
               new token to store in its place.
       Note: Determine that you are up to date by checking whether incidents is empty, not by checking the token. nextSyncToken is never empty once you
       have incidents to read.

       Resolving Events to Threat Intelligence Records


       The events returned by List incident events identify the matched record but do not embed it. Each event carries a collectionItemId that you resolve
       against the corresponding Threat Intelligence collection to retrieve the full record.


                      Collection                        Path segment                                             Resolve the record with


                    Vulnerabilities                      vulnerabilities                             GET /api/v2/osi/vulnerability/{collectionItemId}


                      Accounts                      compromised-accounts                       GET /api/v2/compromised/account_group/{collectionItemId}


                     Bank cards                       compromised-cards                       GET /api/v2/compromised/bank_card_group/{collectionItemId}


                 Masked bank cards                compromised-masked-cards                     GET /api/v2/compromised/masked_card/{collectionItemId}


                        Shops                        compromised-shops                            GET /api/v2/compromised/access/{collectionItemId}


                      Darkweb                              dark-web                                  GET /api/v2/darkweb/forums/{collectionItemId}


                    Breached DB                          breached-db                      GET /api/v2/compromised/breacheddb/updated?q=id:{collectionItemId}


          Suspicious payment details                 suspicious-payments                            GET /api/v2/compromised/spd/{collectionItemId}


                     Public leaks                         public-leaks                                GET /api/v2/osi/public_leak/{collectionItemId}

Collection                             Path segment                                         Resolve the record with


                  Last threats                               threats                                   GET /api/v2/hi/threat/{collectionItemId}


                    Git leaks                                git-leaks                             GET /api/v2/osi/git_repository/{collectionItemId}


       Note: Breached DB is the one collection that is not resolved through a path parameter. Look the record up on the Breached DB collection with the q
       search parameter, using the id field: q=id:. The response is a standard feed response, with the record as the single element of items. It is the record
       already matched to your monitored scope, and it carries the breach description, publication date, source download links, and the evaluation block
       (severity, reliability, credibility, TLP, and Admiralty code).


       A complete drill-down for one incident:


          · Read the incident and check which collections hold events:      curl 'https://tap.group-ib.com/api/v2/imc/incidents/' -u "$GIB_CREDENTIALS"

          · Page its events for a collection that has a non-zero count:   curl -G 'https://tap.group-ib.com/api/v2/imc/incidents//matches/threats' \     -u
       "$GIB_CREDENTIALS" --data-urlencode 'sortOrder=SORT_ORDER_DESC'

          · Retrieve each record by its collectionItemId:     curl 'https://tap.group-ib.com/api/v2/hi/threat/da00b1cbd51ad1559a492bc55f820a2a22812698' \
          -u "$GIB_CREDENTIALS"

          · Continue paging by passing nextPageToken as pageToken until the response no longer contains one.
       For the full list of collection endpoints and their properties, see Collections Overview.

       Filtering Incidents


       Filters apply to the List updated incidents endpoint and can be combined with syncToken.


       Retrieve open, high-scoring incidents only:
        curl -G 'https://tap.group-ib.com/api/v2/imc/incidents/updated' -u "$GIB_CREDENTIALS" \ --data-urlencode
       'filter.statuses=INCIDENT_STATUS_TO_DO' \ --data-urlencode 'filter.scoringFrom=90'
       Retrieve incidents from two specific rules:
        curl -G 'https://tap.group-ib.com/api/v2/imc/incidents/updated' -u "$GIB_CREDENTIALS" \ --data-urlencode
       'filter.incidentRuleIds=019ed5d1-5517-73f8-b3c4-65c91e0fcc56' \ --data-urlencode 'filter.incidentRuleIds=019d430f-f40b-7c67-9a6c-776bb0150908'
       Retrieve incidents updated within a time range:
        curl -G 'https://tap.group-ib.com/api/v2/imc/incidents/updated' -u "$GIB_CREDENTIALS" \ --data-urlencode
       'filter.updatedAtFrom=2026-09-01T00:00:00Z' \ --data-urlencode 'filter.updatedAtTo=2026-09-30T23:59:59Z'
       Warning: Omitting the filter. prefix does not produce an error. The parameter is ignored and the request returns unfiltered results, which can silently
       ingest far more data than intended.

       Related Endpoints


          · Get active collections: GET /api/v2/user/granted_collections - see User Granted Collections

          · Global search across collections: GET /api/v2/search - see Search

Collections
       Threats andDetails
                   Actors -- Feeds
                             APT Threat Actors
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint is part of a comprehensive threat intelligence system that provides both threat actor profiles and threat reports. The system
       differentiates between nation-state Advanced Persistent Threat (APT) groups and cybercrime groups. For complete threat intelligence coverage,
       consider integrating all four related endpoints: APT Threat Actor (profiles), APT Threat (reports), HI Threat Actor (profiles), and HI Threat (reports).
       This allows you to build comprehensive actor profiles with associated reports for both nation-state and cybercrime threats in your third-party security
       systems. In some integration scenarios, collecting only the report endpoints may be sufficient for your use case.


       Specifically, the APT Threat Actor endpoint provides threat actor profiles of nation-state APT groups, including their history, capabilities, and
       organizational details. It works alongside the APT Threat endpoint, which provides detailed reports on nation-state APT activities, to deliver complete
       threat intelligence coverage. Together, these endpoints enable you to build comprehensive actor profiles with associated reports for enhanced threat
       detection and response capabilities.

       Related Threat Intelligence Endpoints


       The following table provides an overview of all four threat intelligence endpoints and their characteristics:


                Endpoint          API Path               Data Type                 Actor Type                   IOC Severity                     Description


         APT Threat Actor    /api/v2/apt/threat_    Threat Actor Profiles       Nation-state APT                   Highest               Comprehensive profiles of

                               actor/updated                                                                                               government-sponsored

                                                                                                                                            Advanced Persistent

                                                                                                                                          Threat groups, including

                                                                                                                                          their history, capabilities,

                                                                                                                                         and organizational details.


               APT Threat    /api/v2/apt/threat/       Threat Reports           Nation-state APT                   Highest                   Detailed reports on

                                   updated                                                                                               nation-state APT activities,

                                                                                                                                           including IOCs, attack

                                                                                                                                             techniques, MITRE

                                                                                                                                          ATT&CK mappings, and

                                                                                                                                            tactical intelligence.

Endpoint              API Path                  Data Type             Actor Type                   IOC Severity                        Description


          HI Threat Actor        /api/v2/hi/threat_a     Threat Actor Profiles        Cybercrime                       High                   Comprehensive profiles of

                                    ctor/updated                                                                                                  cybercriminal groups

                                                                                                                                                    (non-government

                                                                                                                                                 sponsored), including

                                                                                                                                                financially motivated and

                                                                                                                                                 other organized threat

                                                                                                                                                         groups.

                HI Threat        /api/v2/hi/threat/u        Threat Reports            Cybercrime                       High                        Detailed reports on

                                       pdated                                                                                                     cybercriminal threat

                                                                                                                                                activities, including IOCs,

                                                                                                                                                attack techniques, MITRE

                                                                                                                                                ATT&CK mappings, and

                                                                                                                                                  tactical intelligence.


       Integration Recommendations:


          · Best Practice: Collect all four endpoints to build complete threat actor profiles with associated reports for both nation-state APT and
               cybercrime groups in your security systems. This provides the most comprehensive threat intelligence coverage.

          · Alternative: For integrations that focus primarily on threat detection and IOC enrichment, collecting only the report endpoints (APT Threat and
               HI Threat) may be sufficient. Reports contain IOCs with severity ratings that help prioritize security responses.

       Collection-Specific Information


                                                       Property                                                                         Value


                                                        Method                                                                          GET


                                                         Path                                                          /api/v2/apt/threat_actor/updated


                                                       Collection                                                                  apt/threat_actor


                                                   Collection Name                                                             APT Threat Actors


                                                        Module                                                                 Threats and Actors

Property                               Value


                                      Submodule                              Actors


                                         Type                         Common + Individual


                                      TTL (Days)              90 (recommended, not provided in API)


                                    Admiralty Code                            None


                                       Severity                                 9


                                    Collection Limit                 100 records per request


                                      Rate Limit        1 request per 10 seconds per company per feed (see

                                                                         API Limitations)


                                      IOC Types            Domain, IPv4, URL, File (MD5, SHA1, SHA256)


                                   Short Description   Comprehensive profiles of government-sponsored APT

                                                                             groups.


       Request

       Request URL
        GET /api/v2/apt/threat_actor/updated
       Query Parameters

Parameter              Type             Required                  Default                     Description                      Example


                     seqUpdate             integer              No                        0             Sequence update number to get           17274816349479

                                                                                                          the next data chunk. Use this

                                                                                                          parameter to iterate through

                                                                                                           feeds. The value should be

                                                                                                           obtained from the previous

                                                                                                        response’s top-level seqUpdate

                                                                                                      field or from /api/v2/sequence_list

                                                                                                        endpoint. Important: Always use

                                                                                                        the top-level seqUpdate field for

                                                                                                                     iteration.


                        limit              integer              No                      100            Limit the amount of returned data              100

                                                                                                          for this collection. Maximum

                                                                                                        allowed: 100 for this collection.


                         q                 string               No                        -            Search query. Can be used to filter id:221e05fe443deec

                                                                                                         results or search for a specific       1356b0006817931c

                                                                                                        entry by ID. Format: id: to search         a16974f68

                                                                                                             for one specific record.


                     is_tailored           integer              No                        0            Filter for tailored threat actors. Set          1

                                                                                                                  to 1 to enable.


               apply_hunting_rules         integer              No                        0            Apply hunting rules filter. Set to 1            1

                                                                                                                    to enable.


       Query Parameter Details:


          · seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:

· Maximum value: 100 for apt/threat_actor/updated collection

               · If not specified, defaults to 100

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                Required                                  Description                               Example


                  Accept                 string                 No                         Content type accepted by the client              application/json


               Authorization             string                 Yes                  Basic authentication credentials (see Initial                Basic

                                                                                                         Steps)                         base64(LOGIN:API_KEY)


                 User-Agent              string                 No                       User-Agent string with product metadata       SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                    PlatformType/PlatformName_PlatformVersio

                                                                                    n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                             Description                                                  Example


                     Content-Type                                     Response content type                                          application/json


                   Content-Encoding                                     Content encoding                                                  gzip

Header                                            Description                                          Example


                  Cache-Control                                   Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                        GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [ThreatActorItem], "seqUpdate": integer }


                 Field                   Type                           Required                                   Description


                 count                  integer                           Yes                 Number of threat actor items returned in this response


                 items            array[ThreatActorIt                     Yes                              Array of threat actor objects

                                          em]


               seqUpdate                integer                           Yes                    Sequence update number at the top level of the

                                                                                               response. Always use this top-level value in the next

                                                                                             request’s seqUpdate parameter to get the next portion of

                                                                                                                      feeds


       ThreatActorItem Object


                 Field                   Type                           Required                                   Description


                  id                     string                           Yes                   Unique identifier of the threat actor (SHA-1 hash)


                 name                    string                           Yes                               Name of the threat actor


                aliases               array[string]                       Yes                 Array of alternative names/aliases for the threat actor


                country               string | null                        No                           Country code (ISO 3166-1 alpha-2)

Field          Type         Required                          Description


                   isAPT         boolean          Yes       Whether this is an APT (Advanced Persistent Threat)

                                                                   group. For this collection, typically true


                 description      string          Yes         HTML-formatted description of the threat actor


                 createdAt        string          Yes        ISO 8601 timestamp when the record was created


                 updatedAt        string          Yes      ISO 8601 timestamp when the record was last updated


                 seqUpdate        integer         Yes          Sequence update number for this specific item


               techSeqUpdate   integer | null     No                Technical sequence update number


                    oldId      string | null      No                   Previous identifier (if migrated)


                  hasIocs        boolean          Yes      Whether the threat actor has associated indicators of

                                                                                 compromise


                   langs       array[string]      Yes                      Array of language codes


               spokenOnLangs   array[string]      Yes          Array of languages spoken by the threat actor


                   labels      array[string]      Yes            Array of label strings (e.g., [“hacker”, “spy”,

                                                                                “nation-state”])


                    roles      array[string]      Yes           Array of role strings (e.g., [“malware-author”,

                                                            “infrastructure-architect”, “infrastructure-operator”])


                   goals       array[string]      Yes       Array of goal strings (e.g., [“Information”, “Research”,

                                                                                 “Financial”])

Field               Type         Required                         Description


                     files               array          Yes                        Array of file objects


        addedToThreatLandscap         array | null      No                  Array of threat landscape options

                     eFor


        threatLandscapeOptions array[ThreatLandsc       Yes            Array of available threat landscape options

                                      apeOption]


                      stat          ThreatActorStat     Yes       Statistics object containing aggregated data about the

                                                                                       threat actor


                displayOptions      DisplayOptions      Yes                       Display options object


       ThreatActorStat Object


                     Field               Type         Required                         Description


               allIndicatorsCount       integer         Yes       Total number of indicators associated with this threat

                                                                                           actor


                allReportsCount         integer         Yes      Total number of reports associated with this threat actor


                contactsCount           integer         Yes       Number of contacts associated with this threat actor


         forumsAccountsCount            integer         Yes       Number of forum accounts associated with this threat

                                                                                           actor


       relatedThreatActorsCoun          integer         Yes                  Number of related threat actors

                       t


                   countries         array[string]      Yes      Array of country codes where this threat actor is active


                    regions          array[string]      Yes          Array of regions where this threat actor is active

Field              Type          Required                         Description


                   sectors          array[string]      Yes           Array of sectors targeted by this threat actor


                     cve            array[string]      Yes          Array of CVE identifiers used by this threat actor


                  malware           array[string]      Yes         Array of malware names used by this threat actor


                  expertise         array[string]      Yes      Array of expertise types (e.g., [“AutoReport”, “Backdoor”,

                                                                                    “Cobalt Strike”])


                dateFirstSeen          string          Yes         Date when the threat actor was first seen (format:

                                                                                     YYYY-MM-DD)


                dateLastSeen           string          Yes         Date when the threat actor was last seen (format:

                                                                                     YYYY-MM-DD)


                   reports        array[ReportSumm     Yes                  Array of report summary objects

                                        ary]


               targetedCompany      array[string]      Yes                 Array of targeted company names


        targetedPartnersAndClie     array[string]      Yes               Array of targeted partners and clients

                     nts


       ReportSummary Object


                    Field              Type          Required                         Description


                     id                string          Yes            Unique identifier of the report (SHA-1 hash)


                datePublished          string          Yes           Date when the report was published (format:

                                                                                     YYYY-MM-DD)

Field                   Type                           Required                                                           Description


                    name                   object                             Yes                               Object with language keys containing report names (e.g.,

                                                                                                                  {“en”: “APT41 - New indicators have been found”, “ru”:

                                                                                                                        “APT41 - New indicators have been found”})


                 companyId                  array                             Yes                                   Array of company IDs (empty for common reports)


       ThreatLandscapeOption Object


                    Field                   Type                           Required                                                           Description


                    label                  string                             Yes                                           Label for the threat landscape option


                    value                  string                             Yes                                           Value for the threat landscape option


       DisplayOptions Object


                    Field                   Type                           Required                                                           Description


                 isFavourite              boolean                             Yes                                         Whether the item is marked as favourite


                  isHidden                boolean                             Yes                                                    Whether the item is hidden


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/apt/threat_actor/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Search Query
       curl -X GET
       'https://tap.group-ib.com/api/v2/apt/threat_actor/updated?seqUpdate=0&limit=100&q=id:221e05fe443deec1356b0006817931ca16974f68' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/apt/threat_actor/updated?seqUpdate=0&limit=100&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H
       'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 19, "items": [ {      "addedToThreatLandscapeFor": null,          "aliases": ["CamoFei"],          "country": "CN",          "createdAt":
       "2019-02-20T17:44:21+00:00",        "description": "
       Experts gave the group the name ChamelGang...
       ",      "displayOptions": {   "isFavourite": false,    "isHidden": false      },     "files": [      {        "hash":
       "23f780c4ad6cdc16989acdb4f218712ba1d2d038e9c057026e54249b031957a3",                                "mime": "image/png",               "name":
       "23f780c4ad6cdc16989acdb4f218712ba1d2d038e9c057026e54249b031957a3",                                "size": 60084        }      ],      "goals": [],   "hasIocs": true,
       "id": "de70f8194526173b885baf2999f65225927c2f31",            "isAPT": true,        "labels": [],     "langs": ["en", "ru"],         "name": "ChamelGang",       "oldId": null,

"roles": [],   "seqUpdate": 17274816349479,            "spokenOnLangs": ["en"],         "stat": {        "allIndicatorsCount": 51,                 "allReportsCount": 6,
       "contactsCount": 4,             "countries": ["BR", "IN", "JP", "RU", "TW", "US"],     "cve": [],      "dateFirstSeen": "2022-11-01",                     "dateLastSeen": "2024-09-28",
                "expertise": ["AutoReport", "Brief Report", "Ransomware"],            "forumsAccountsCount": 0,               "malware": ["CatB", "Cobalt Strike"],               "regions":
       ["america:northern_america", "america:south_america", "asia", "europe"],                   "relatedThreatActorsCount": 0,                   "reports": [          {       "companyId":
       [],            "datePublished": "2024-09-28",            "id": "9c8d61663f8e4b2c58d9029238ac9b2e6d65793d",                              "name": {                "ru": "ChamelGang -
       New indicators have been found",                    "en": "ChamelGang - New indicators have been found"                        }       }          ],       "sectors":
       ["government-and-military", "health-care"],              "targetedCompany": [],        "targetedPartnersAndClients": []                },        "techSeqUpdate": null,
       "threatLandscapeOptions": [               {      "label": "company",         "value": "company"             },     {      "label": "partner",                "value": "partner"    },
         {           "label": "industry",      "value": "industry"      },      {      "label": "other",           "value": "other"       }        ],         "updatedAt":
       "2024-09-28T03:00:34+03:00"              } ], "seqUpdate": 17277408454364 }

Threats and Actors - APT Threat Reports
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint is part of a comprehensive threat intelligence system that provides both threat actor profiles and threat reports. The system
       differentiates between nation-state Advanced Persistent Threat (APT) groups and cybercrime groups. For complete threat intelligence coverage,
       consider integrating all four related endpoints: APT Threat Actor (profiles), APT Threat (reports), HI Threat Actor (profiles), and HI Threat (reports).
       This allows you to build comprehensive actor profiles with associated reports for both nation-state and cybercrime threats in your third-party security
       systems. In some integration scenarios, collecting only the report endpoints may be sufficient for your use case.


       Specifically, the APT Threat endpoint provides threat reports on nation-state APT activities, including IOCs, attack techniques, and MITRE ATT&CK
       mappings. It works alongside the APT Threat Actor endpoint, which provides comprehensive profiles of government-sponsored APT groups, to deliver
       complete threat intelligence coverage. Use this endpoint to stay informed about emerging APT activities and enhance your threat detection and
       response capabilities.


       Note: This endpoint includes IOCs, which are also part of the IOC Primary collection.

       Related Threat Intelligence Endpoints


       The following table provides an overview of all four threat intelligence endpoints and their characteristics:


                Endpoint          API Path               Data Type                 Actor Type                   IOC Severity                     Description


         APT Threat Actor    /api/v2/apt/threat_    Threat Actor Profiles       Nation-state APT                   Highest               Comprehensive profiles of

                                actor/updated                                                                                              government-sponsored

                                                                                                                                            Advanced Persistent

                                                                                                                                          Threat groups, including

                                                                                                                                          their history, capabilities,

                                                                                                                                         and organizational details.


               APT Threat    /api/v2/apt/threat/       Threat Reports           Nation-state APT                   Highest                   Detailed reports on

                                   updated                                                                                               nation-state APT activities,

                                                                                                                                           including IOCs, attack

                                                                                                                                             techniques, MITRE

                                                                                                                                          ATT&CK mappings, and

                                                                                                                                            tactical intelligence.

Endpoint              API Path                  Data Type             Actor Type                   IOC Severity                     Description


          HI Threat Actor        /api/v2/hi/threat_a     Threat Actor Profiles        Cybercrime                       High                 Comprehensive profiles of

                                    ctor/updated                                                                                                cybercriminal groups

                                                                                                                                                  (non-government

                                                                                                                                                sponsored), including

                                                                                                                                             financially motivated and

                                                                                                                                              other organized threat

                                                                                                                                                      groups.

                HI Threat        /api/v2/hi/threat/u        Threat Reports            Cybercrime                       High                      Detailed reports on

                                       pdated                                                                                                   cybercriminal threat

                                                                                                                                             activities, including IOCs,

                                                                                                                                             attack techniques, MITRE

                                                                                                                                             ATT&CK mappings, and

                                                                                                                                                tactical intelligence.


       Integration Recommendations:


          · Best Practice: Collect all four endpoints to build complete threat actor profiles with associated reports for both nation-state APT and
               cybercrime groups in your security systems. This provides the most comprehensive threat intelligence coverage.

          · Alternative: For integrations that focus primarily on threat detection and IOC enrichment, collecting only the report endpoints (APT Threat and
               HI Threat) may be sufficient. Reports contain IOCs with severity ratings that help prioritize security responses.

          · Note on Severity Classification: Both threat report feeds (APT Threat and HI Threat) contain high severity IOCs; however, APT IOCs are more
               rare and by nature are the most important.

       Collection-Specific Information


                                                       Property                                                                      Value


                                                        Method                                                                        GET


                                                         Path                                                             /api/v2/apt/threat/updated


                                                       Collection                                                                  apt/threat


                                                   Collection Name                                                            APT Threat Reports


                                                        Module                                                                 Threats and Actors

Property                               Value


                                      Submodule                             Last threats


                                           Type                         Common + Individual


                                      TTL (Days)       360 (recommended one and in most cases not provided

                                                                               in API)


                                    Admiralty Code                            Can differ


                                          Severity                                9


                                    Collection Limit                   10 records per request


                                         Rate Limit     1 request per 10 seconds per company per feed (see

                                                                          API Limitations)


                                         IOC Types         Domain, IPv4, URL, File (MD5, SHA1, SHA256)


                                   Short Description   Reports on nation-state APT activities with IOCs, attack

                                                             techniques, and MITRE ATT&CK mappings.


       Request

       Request URL
        GET /api/v2/apt/threat/updated
       Query Parameters

Parameter              Type             Required                  Default                    Description                     Example


                     seqUpdate             integer              No                        0             Sequence update number to get          16172928022293

                                                                                                         the next data chunk. Use this

                                                                                                          parameter to iterate through

                                                                                                          feeds. The value should be

                                                                                                          obtained from the previous

                                                                                                        response’s top-level seqUpdate

                                                                                                      field or from /api/v2/sequence_list

                                                                                                        endpoint. Important: Always use

                                                                                                        the top-level seqUpdate field for

                                                                                                                    iteration.


                       limit               integer              No                       10            Limit the amount of returned data             10

                                                                                                         for this collection. Maximum

                                                                                                         allowed: 10 for this collection.


                        q                  string               No                        -            Search query. Can be used to filter id:e8bee5b0e6e286c

                                                                                                         results or search for a specific     a753feed347664943

                                                                                                        entry by ID. Format: id: to search        8e4e4488

                                                                                                            for one specific record.


               apply_hunting_rules         integer              No                        0            Apply hunting rules filter. Set to 1          1

                                                                                                                   to enable.


       Query Parameter Details:


          · seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 10 for apt/threat/updated collection

                ·

If not specified, defaults to 10

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types (e.g., ip:8.8.8.8, domain:example.corp)


       Request Headers


                  Header                  Type                 Required                                  Description                                 Example


                  Accept                  string                  No                         Content type accepted by the client                application/json


               Authorization              string                 Yes                     Basic authentication credentials (see Initial                Basic

                                                                                                            Steps)                          base64(LOGIN:API_KEY)


                 User-Agent               string                  No                      User-Agent string with product metadata          SIEM/QRadar_2020.10.6/G

                                                                                          (optional but recommended - especially           roupIB_TI_1.0.0/gibuser@g

                                                                                           useful in troubleshooting on our end).          roup-ib.com/ciaops_3.0.0

                                                                                                           Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                        e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                         Header                                             Description                                                     Example


                     Content-Type                                      Response content type                                             application/json


                   Content-Encoding                                       Content encoding                                                    gzip

Header                                          Description                                         Example


                     Cache-Control                                 Cache control directives                     max-age=0, must-revalidate, private


                             Allow                                 Allowed HTTP methods                                          GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [ThreatItem], "seqUpdate": integer }


                    Field                  Type                            Required                                 Description


                    count                 integer                            Yes                 Number of threat items returned in this response


                    items            array[ThreatItem]                       Yes                               Array of threat objects


                 seqUpdate                integer                            Yes                  Sequence update number at the top level of the

                                                                                                response. Always use this top-level value in the next

                                                                                              request’s seqUpdate parameter to get the next portion of

                                                                                                                       feeds


       ThreatItem Object


                    Field                  Type                            Required                                 Description


                      id                   string                            Yes                 Unique identifier of the threat report (SHA-1 hash)


                     title                 string                            Yes                              Title of the threat report


                  shortTitle            string | null                        No                            Short title of the threat report


                 description               string                            Yes                     HTML-formatted description of the threat


               shortDescription         string | null                        No                            Short description of the threat

Field           Type         Required                         Description


                   type           string          Yes                 Type of the threat. Value: “event”


               reportNumber       string          Yes                      Internal report number


               dateFirstSeen      string          Yes           Date when the threat was first seen (format:

                                                                               YYYY-MM-DD)


               dateLastSeen       string          Yes           Date when the threat was last seen (format:

                                                                               YYYY-MM-DD)


               datePublished      string          Yes          Date when the report was published (format:

                                                                               YYYY-MM-DD)


                 createdAt        string          Yes        ISO 8601 timestamp when the record was created


                 updatedAt        string          Yes      ISO 8601 timestamp when the record was last updated


                isPublished      boolean          Yes                 Whether the threat is published


                 isTailored      boolean          Yes         Whether the threat is tailored for specific clients


                 isAutogen       boolean          Yes         Whether the report was automatically generated


                  hasIocs        boolean          Yes        Whether the threat has indicators of compromise


                   langs       array[string]      Yes      Array of language codes (at this point, only Enis up to

                                                                          date - no other laguages)


                seqUpdate         integer         Yes         Sequence update number for this specific item


               techSeqUpdate   integer | null     No                Technical sequence update number

Field            Type         Required                    Description


                    oldId         string | null     No              Previous identifier (if migrated)


                  contacts           array          Yes        Array of contact objects (usually empty)


                  countries          array          Yes                Array of country objects


                   regions           array          Yes                 Array of region objects


                   sectors           array          Yes                 Array of sector objects


                    labels           array          Yes                  Array of label objects


                   cveList           array          Yes                 Array of CVE identifiers


                  expertise       array[string]     Yes      Array of expertise types (e.g., [“AutoReport”])


                  sourceList         array          Yes                 Array of source objects


                   sources           array          Yes               Array of source identifiers


                    files            array          Yes                   Array of file objects


               forumsAccounts        array          Yes             Array of forum account objects


                 malwareList         array          Yes                Array of malware objects


                   toolList          array          Yes                  Array of tool objects


           relatedThreatActors       array          Yes          Array of related threat actor objects


               targetedCompany       array          Yes           Array of targeted company objects


        targetedPartnersAndClie      array          Yes         Array of targeted partners and clients

                     nts


                 companyId           array          Yes                  Array of company IDs

Field                  Type           Required                     Description


                  author               string | null       No                     Author of the report


                 indicators          array[Indicator]      Yes                 Array of indicator objects


               indicatorsIds          array[string]        Yes                   Array of indicator IDs


          indicatorRelationships          array            Yes           Array of indicator relationship objects


       indicatorMalwareRelation           array            Yes      Array of indicator-malware relationship objects

                   ships


       indicatorToolRelationship          array            Yes         Array of indicator-tool relationship objects

                     s


           unreliableIndicators           array            Yes            Array of unreliable indicator objects


       unreliableIndicatorsRelati         array            Yes      Array of unreliable indicator relationship objects

                    ons


                threatActor         ThreatActor | null     No                Associated threat actor object


                mitreMatrix               array            Yes          Array of MITRE ATT&CK matrix objects


                 evaluation            Evaluation          Yes      Evaluation object containing threat assessment


               displayOptions        DisplayOptions        Yes                   Display options object


       Indicator Object


                   Field                  Type           Required                     Description


                     id                   string           Yes       Unique identifier of the indicator (SHA-1 hash)

Field               Type            Required                        Description


                   type               string             Yes       Type of indicator. Possible values: “network”, “file”,

                                                                                       “email”, etc.


                    title          string | null         No                        Title of the indicator


                description        string | null         No                    Description of the indicator


               dateFirstSeen          string             Yes         Date when the indicator was first seen (format:

                                                                                      YYYY-MM-DD)


               dateLastSeen           string             Yes         Date when the indicator was last seen (format:

                                                                                      YYYY-MM-DD)


                  deleted            boolean             Yes                 Whether the indicator is deleted


                seqUpdate            integer             Yes           Sequence update number for this indicator


               techSeqUpdate      integer | null         No                Technical sequence update number


                   langs           array[string]         Yes                    Array of language codes


                  sources          array[string]         Yes                    Array of source identifiers


               malwareIdList    array[string] | null     No                   Array of related malware IDs


                malwareList            array             Yes                    Array of malware objects


                 attributes        object | null         No                        Additional attributes


                  params        IndicatorParams          Yes      Indicator parameters object (contains actual indicator

                                                                                           data)


       IndicatorParams Object


                   Field               Type            Required                        Description


                  domain

Field          Type         Required                        Description


                               string | null     No                           Domain name


                    ipv4       array[string]     Yes                    Array of IPv4 addresses


                    ipv6       array[string]     Yes                    Array of IPv6 addresses


                     url          string         Yes                   URL (can be empty string)


                    ssl           array          Yes                 Array of SSL certificate objects


       ThreatActor Object


                   Field          Type         Required                        Description


                     id           string         Yes       Unique identifier of the threat actor (SHA-1 hash)


                   name           string         Yes                    Name of the threat actor


                  country         string         Yes               Country code (ISO 3166-1 alpha-2)


                   isAPT         boolean         Yes      Whether this is an APT (Advanced Persistent Threat)

                                                                                  group


       Evaluation Object


                   Field          Type         Required                        Description


               admiraltyCode      string         Yes                   Admiralty Code (e.g., “C3”)


                 credibility     integer         Yes                    Credibility score (0-100)


                 reliability     integer         Yes                     Reliability score (0-100)


                  severity        string         Yes           Severity level (e.g., “red”, “amber”, “green”)

Field                                 Type                                          Required                                                               Description


                        tlp                                 string                                              Yes                                Traffic Light Protocol level (e.g., “red”, “amber”, “green”,

                                                                                                                                                                                      “white”)


                        ttl                           integer | null                                            No                                    Time to live in days (usually null for this collection)


       DisplayOptions Object


                      Field                                 Type                                          Required                                                               Description


                   isFavourite                           boolean                                                Yes                                            Whether the item is marked as favourite


                     isHidden                            boolean                                                Yes                                                    Whether the item is hidden


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/apt/threat/updated?seqUpdate=0&limit=10' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Search Query
       curl -X GET 'https://tap.group-ib.com/api/v2/apt/threat/updated?seqUpdate=0&limit=10&q=id:e8bee5b0e6e286ca753feed3476649438e4e4488' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/apt/threat/updated?seqUpdate=0&limit=10&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

       Success Response (200 OK)
        { "count": 57, "items": [ {                      "contacts": [],      "countries": [],              "createdAt": "2024-09-23T23:20:09+03:00",                         "cveList": [],        "dateFirstSeen":
       "2024-09-23",              "dateLastSeen": "2024-09-23",                 "datePublished": "2024-09-24",                       "description": "",             "displayOptions": {            "isFavourite": false,
         "isHidden": false               },      "evaluation": {          "admiraltyCode": "C3",                      "credibility": 60,         "reliability": 60,         "severity": "red",            "tlp": "red",
       "ttl": null      },        "expertise": [            "AutoReport"         ],        "files": [],         "forumsAccounts": [],              "hasIocs": true,         "id":
       "d1da0a53543a18e5240ece12d031b6ad711a8202",                                         "indicatorMalwareRelationships": [],                      "indicatorRelationships": [],
       "indicatorToolRelationships": [],                    "indicators": [           {         "attributes": null,               "dateFirstSeen": "2024-09-23",                       "dateLastSeen": "2024-09-23",
               "description": null,               "id": "6ecb34d68b26c7bc369dd209f0db9cc3a9c6a8c7",                                        "langs": [               "ru"        ],         "malwareIdList": null,
       "malwareList": [],                     "params": {            "domain": null,                 "ipv4": [               "95.179.134.240"                  ],          "ipv6": [],            "ssl": [],            "url": ""
           },         "seqUpdate": 17271228138607,                           "sources": [                  "panda_playbook"                 ],         "techSeqUpdate": null,                    "title": null,          "type":
       "network"              }     ],         "indicatorsIds": [          "6ecb34d68b26c7bc369dd209f0db9cc3a9c6a8c7"                                     ],        "isAutogen": true,           "isPublished": true,
       "isTailored": false,              "labels": [],       "langs": [       "en",           "ru"         ],     "malwareList": [],             "mitreMatrix": [],        "oldId": null,         "regions": [],
       "relatedThreatActors": [],                  "reportNumber": "CP-2809-2320",                        "sectors": [],        "seqUpdate": 17271360303706,                         "shortDescription": null,
       "shortTitle": null,           "sourceList": [],          "sources": [],            "targetedCompany": [],                "targetedPartnersAndClients": [],                    "techSeqUpdate": null,
       "threatActor": {             "country": "CN",               "id": "59a1326f2bed234dcb864a69e7ab28b2fa4b14e9",                                       "isAPT": true,              "name": "APT41"             },       "title":
       "APT41 - New indicators have been found",                           "toolList": [],         "type": "event",            "unreliableIndicators": [],              "unreliableIndicatorsRelations": [],
       "updatedAt": "2024-09-24T03:00:30+03:00"                            } ], "seqUpdate": 17272224279604 }

Threats and Actors - HI Threat Actors
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint is part of a comprehensive threat intelligence system that provides both threat actor profiles and threat reports. The system
       differentiates between nation-state Advanced Persistent Threat (APT) groups and cybercrime groups. For complete threat intelligence coverage,
       consider integrating all four related endpoints: APT Threat Actor (profiles), APT Threat (reports), HI Threat Actor (profiles), and HI Threat (reports).
       This allows you to build comprehensive actor profiles with associated reports for both nation-state and cybercrime threats in your third-party security
       systems. In some integration scenarios, collecting only the report endpoints may be sufficient for your use case.


       Specifically, the HI Threat Actor endpoint provides threat actor profiles of cybercriminal groups (non-government sponsored), including financially
       motivated and organized threat groups. It works alongside the HI Threat endpoint, which provides detailed reports on cybercriminal activities, to
       deliver complete threat intelligence coverage. Together, these endpoints enable you to build comprehensive actor profiles with associated reports for
       enhanced threat detection and response capabilities.

       Related Threat Intelligence Endpoints


       The following table provides an overview of all four threat intelligence endpoints and their characteristics:


                Endpoint          API Path               Data Type                 Actor Type                   IOC Severity                     Description


         APT Threat Actor    /api/v2/apt/threat_    Threat Actor Profiles       Nation-state APT                   Highest               Comprehensive profiles of

                               actor/updated                                                                                               government-sponsored

                                                                                                                                            Advanced Persistent

                                                                                                                                          Threat groups, including

                                                                                                                                          their history, capabilities,

                                                                                                                                         and organizational details.


               APT Threat    /api/v2/apt/threat/       Threat Reports           Nation-state APT                   Highest                   Detailed reports on

                                   updated                                                                                               nation-state APT activities,

                                                                                                                                           including IOCs, attack

                                                                                                                                             techniques, MITRE

                                                                                                                                          ATT&CK mappings, and

                                                                                                                                            tactical intelligence.

Endpoint              API Path                  Data Type             Actor Type                   IOC Severity                        Description


          HI Threat Actor        /api/v2/hi/threat_a     Threat Actor Profiles        Cybercrime                       High                   Comprehensive profiles of

                                    ctor/updated                                                                                                  cybercriminal groups

                                                                                                                                                    (non-government

                                                                                                                                                 sponsored), including

                                                                                                                                                financially motivated and

                                                                                                                                                 other organized threat

                                                                                                                                                         groups.

                HI Threat        /api/v2/hi/threat/u        Threat Reports            Cybercrime                       High                        Detailed reports on

                                       pdated                                                                                                     cybercriminal threat

                                                                                                                                                activities, including IOCs,

                                                                                                                                                attack techniques, MITRE

                                                                                                                                                 ATT&CK mappings, and

                                                                                                                                                  tactical intelligence.


       Integration Recommendations:


          · Best Practice: Collect all four endpoints to build complete threat actor profiles with associated reports for both nation-state APT and
               cybercrime groups in your security systems. This provides the most comprehensive threat intelligence coverage.

          · Alternative: For integrations that focus primarily on threat detection and IOC enrichment, collecting only the report endpoints (APT Threat and
               HI Threat) may be sufficient. Reports contain IOCs with severity ratings that help prioritize security responses.

       Collection-Specific Information


                                                       Property                                                                         Value


                                                        Method                                                                          GET


                                                         Path                                                           /api/v2/hi/threat_actor/updated


                                                       Collection                                                                  hi/threat_actor


                                                   Collection Name                                                                 HI Threat Actors


                                                        Module                                                                         Threats

Property                              Value


                                      Submodule                              Actors


                                          Type                        Common + Individual


                                       TTL (Days)             90 (recommended, not provided in API)


                                    Admiralty Code                            None


                                        Severity                                9


                                    Collection Limit                 100 records per request


                                       Rate Limit       1 request per 10 seconds per company per feed (see

                                                                         API Limitations)


                                       IOC Types           Domain, IPv4, URL, File (MD5, SHA1, SHA256)


                                    Short Description    Comprehensive profiles of cybercriminal groups.


       Request

       Request URL
        GET /api/v2/hi/threat_actor/updated
       Query Parameters

Parameter              Type             Required                  Default                     Description                      Example


                     seqUpdate             integer              No                        0             Sequence update number to get           17597831696284

                                                                                                          the next data chunk. Use this

                                                                                                          parameter to iterate through

                                                                                                           feeds. The value should be

                                                                                                           obtained from the previous

                                                                                                        response’s top-level seqUpdate

                                                                                                      field or from /api/v2/sequence_list

                                                                                                        endpoint. Important: Always use

                                                                                                        the top-level seqUpdate field for

                                                                                                                     iteration.


                        limit              integer              No                      100            Limit the amount of returned data              100

                                                                                                          for this collection. Maximum

                                                                                                        allowed: 100 for this collection.


                         q                 string               No                        -            Search query. Can be used to filter id:221e05fe443deec

                                                                                                         results or search for a specific       1356b0006817931c

                                                                                                        entry by ID. Format: id: to search         a16974f68

                                                                                                             for one specific record.


                     is_tailored           integer              No                        0            Filter for tailored threat actors. Set          1

                                                                                                                  to 1 to enable.


               apply_hunting_rules         integer              No                        0            Apply hunting rules filter. Set to 1            1

                                                                                                                    to enable.


       Query Parameter Details:


          · seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:

· Maximum value: 100 for hi/threat_actor/updated collection

               · If not specified, defaults to 100

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                Required                                  Description                               Example


                  Accept                 string                 No                         Content type accepted by the client              application/json


               Authorization             string                 Yes                  Basic authentication credentials (see Initial                Basic

                                                                                                         Steps)                         base64(LOGIN:API_KEY)


                 User-Agent              string                 No                       User-Agent string with product metadata       SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                    PlatformType/PlatformName_PlatformVersio

                                                                                    n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                             Description                                                  Example


                     Content-Type                                     Response content type                                          application/json


                   Content-Encoding                                     Content encoding                                                  gzip

Header                                            Description                                          Example


                  Cache-Control                                   Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                        GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [ThreatActorItem], "seqUpdate": integer }


                 Field                   Type                           Required                                   Description


                 count                  integer                           Yes                 Number of threat actor items returned in this response


                 items            array[ThreatActorIt                     Yes                              Array of threat actor objects

                                          em]


               seqUpdate                integer                           Yes                    Sequence update number at the top level of the

                                                                                               response. Always use this top-level value in the next

                                                                                             request’s seqUpdate parameter to get the next portion of

                                                                                                                      feeds


       ThreatActorItem Object


                 Field                   Type                           Required                                   Description


                  id                     string                           Yes                   Unique identifier of the threat actor (SHA-1 hash)


                 name                    string                           Yes                               Name of the threat actor


                aliases               array[string]                       Yes                 Array of alternative names/aliases for the threat actor


                country               string | null                        No                           Country code (ISO 3166-1 alpha-2)

Field           Type         Required                         Description


                   isAPT          boolean          Yes       Whether this is an APT (Advanced Persistent Threat)

                                                                  group. For HI threats, this is typically false


                 description       string          Yes         HTML-formatted description of the threat actor


                 createdAt         string          Yes        ISO 8601 timestamp when the record was created


                 updatedAt         string          Yes      ISO 8601 timestamp when the record was last updated


                 seqUpdate         integer         Yes         Sequence update number for this specific item


               techSeqUpdate    integer | null     No                Technical sequence update number


                    oldId       string | null      No                  Previous identifier (if migrated)


                  hasIocs         boolean          Yes      Whether the threat actor has associated indicators of

                                                                                  compromise


                   langs        array[string]      Yes                     Array of language codes


               spokenOnLangs    array[string]      Yes          Array of languages spoken by the threat actor


                   labels       array[string]      Yes                       Array of label strings


                    roles       array[string]      Yes                        Array of role strings


                   goals        array[string]      Yes                       Array of goal strings


                    files           array          Yes                        Array of file objects


        addedToThreatLandscap    array | null      No                 Array of threat landscape options

                    eFor

Field               Type         Required                         Description


        threatLandscapeOptions array[ThreatLandsc       Yes            Array of available threat landscape options

                                      apeOption]


                      stat          ThreatActorStat     Yes       Statistics object containing aggregated data about the

                                                                                       threat actor


                displayOptions      DisplayOptions      Yes                       Display options object


       ThreatActorStat Object


                     Field               Type         Required                         Description


               allIndicatorsCount       integer         Yes       Total number of indicators associated with this threat

                                                                                           actor


                allReportsCount         integer         Yes      Total number of reports associated with this threat actor


                contactsCount           integer         Yes       Number of contacts associated with this threat actor


         forumsAccountsCount            integer         Yes       Number of forum accounts associated with this threat

                                                                                           actor


       relatedThreatActorsCoun          integer         Yes                  Number of related threat actors

                       t


                   countries         array[string]      Yes      Array of country codes where this threat actor is active


                    regions          array[string]      Yes          Array of regions where this threat actor is active


                    sectors          array[string]      Yes            Array of sectors targeted by this threat actor

Field              Type          Required                      Description


                     cve            array[string]      Yes       Array of CVE identifiers used by this threat actor


                  malware           array[string]      Yes      Array of malware names used by this threat actor


                  expertise         array[string]      Yes                   Array of expertise types


                dateFirstSeen          string          Yes      Date when the threat actor was first seen (format:

                                                                                  YYYY-MM-DD)


                dateLastSeen           string          Yes      Date when the threat actor was last seen (format:

                                                                                  YYYY-MM-DD)


                   reports        array[ReportSumm     Yes               Array of report summary objects

                                        ary]


               targetedCompany      array[string]      Yes              Array of targeted company names


        targetedPartnersAndClie     array[string]      Yes            Array of targeted partners and clients

                     nts


       ReportSummary Object


                    Field              Type          Required                      Description


                     id                string          Yes         Unique identifier of the report (SHA-1 hash)


                datePublished          string          Yes         Date when the report was published (format:

                                                                                  YYYY-MM-DD)


                    name               object          Yes      Object with language keys containing report names


                 companyId             array           Yes      Array of company IDs (empty for common reports)

ThreatLandscapeOption Object


                     Field                            Type                                   Required                                                             Description


                     label                            string                                   Yes                                                Label for the threat landscape option


                     value                            string                                   Yes                                                Value for the threat landscape option


       DisplayOptions Object


                     Field                            Type                                   Required                                                             Description


                 isFavourite                        boolean                                    Yes                                              Whether the item is marked as favourite


                    isHidden                        boolean                                    Yes                                                      Whether the item is hidden


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/hi/threat_actor/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Search Query
       curl -X GET
       'https://tap.group-ib.com/api/v2/hi/threat_actor/updated?seqUpdate=0&limit=100&q=id:221e05fe443deec1356b0006817931ca16974f68' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/hi/threat_actor/updated?seqUpdate=0&limit=100&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H
       'Accept: application/json'
       Example Response

       Success Response (200 OK)


       The response structure is similar to apt/threat_actor/updated, with the main difference being that isAPT is typically false for HI threat actors.
        { "count": 150, "items": [             {    "addedToThreatLandscapeFor": null,                     "aliases": [],      "country": null,        "createdAt": "2019-02-20T17:44:21+00:00",
            "description": "
       Threat actor description...
       ",      "displayOptions": {             "isFavourite": false,         "isHidden": false        },        "files": [],    "goals": [],      "hasIocs": true,         "id": "example_id_hash",
       "isAPT": false,         "labels": [],       "langs": ["en", "ru"],     "name": "Example Threat Actor",                  "oldId": null,      "roles": [],     "seqUpdate": 17597831696284,
            "spokenOnLangs": [],          "stat": {         "allIndicatorsCount": 100,             "allReportsCount": 5,              "contactsCount": 0,               "countries": ["US", "GB"],
       "cve": [],      "dateFirstSeen": "2020-01-01",                  "dateLastSeen": "2024-09-30",                  "expertise": ["AutoReport"],            "forumsAccountsCount": 0,
       "malware": [],          "regions": ["america:northern_america", "europe"],                    "relatedThreatActorsCount": 0,                    "reports": [],       "sectors": [],
       "targetedCompany": [],              "targetedPartnersAndClients": []             },     "techSeqUpdate": null,               "threatLandscapeOptions": [                 {       "label":
       "company",              "value": "company"              },    {         "label": "partner",            "value": "partner"          },       {        "label": "industry",         "value":
       "industry"        },       {        "label": "other",             "value": "other"      }      ],       "updatedAt": "2024-09-30T03:00:45+03:00"                     } ], "seqUpdate":
       17597831696284 }

Threats and Actors - HI Threat Reports
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint is part of a comprehensive threat intelligence system that provides both threat actor profiles and threat reports. The system
       differentiates between nation-state Advanced Persistent Threat (APT) groups and cybercrime groups. For complete threat intelligence coverage,
       consider integrating all four related endpoints: APT Threat Actor (profiles), APT Threat (reports), HI Threat Actor (profiles), and HI Threat (reports).
       This allows you to build comprehensive actor profiles with associated reports for both nation-state and cybercrime threats in your third-party security
       systems. In some integration scenarios, collecting only the report endpoints may be sufficient for your use case.


       Specifically, the HI Threat endpoint provides threat reports on cybercriminal activities, including IOCs, attack techniques, and MITRE ATT&CK
       mappings. It works alongside the HI Threat Actor endpoint, which provides comprehensive profiles of cybercriminal groups, to deliver complete threat
       intelligence coverage. Use this endpoint to stay informed about emerging cybercriminal threats and enhance your threat detection and response
       capabilities.


       Note: This endpoint includes IOCs, which are also part of the IOC Primary collection.

       Related Threat Intelligence Endpoints


       The following table provides an overview of all four threat intelligence endpoints and their characteristics:


                Endpoint          API Path               Data Type                 Actor Type                   IOC Severity                     Description


         APT Threat Actor    /api/v2/apt/threat_    Threat Actor Profiles       Nation-state APT                   Highest               Comprehensive profiles of

                               actor/updated                                                                                               government-sponsored

                                                                                                                                            Advanced Persistent

                                                                                                                                          Threat groups, including

                                                                                                                                          their history, capabilities,

                                                                                                                                         and organizational details.


               APT Threat    /api/v2/apt/threat/       Threat Reports           Nation-state APT                   Highest                   Detailed reports on

                                   updated                                                                                               nation-state APT activities,

                                                                                                                                           including IOCs, attack

                                                                                                                                             techniques, MITRE

                                                                                                                                          ATT&CK mappings, and

                                                                                                                                            tactical intelligence.

Endpoint              API Path                  Data Type             Actor Type                   IOC Severity                     Description


          HI Threat Actor        /api/v2/hi/threat_a     Threat Actor Profiles        Cybercrime                       High                Comprehensive profiles of

                                    ctor/updated                                                                                               cybercriminal groups

                                                                                                                                                 (non-government

                                                                                                                                               sponsored), including

                                                                                                                                            financially motivated and

                                                                                                                                               other organized threat

                                                                                                                                                      groups.

                HI Threat        /api/v2/hi/threat/u        Threat Reports            Cybercrime                       High                     Detailed reports on

                                       pdated                                                                                                   cybercriminal threat

                                                                                                                                            activities, including IOCs,

                                                                                                                                            attack techniques, MITRE

                                                                                                                                             ATT&CK mappings, and

                                                                                                                                                tactical intelligence.


       Integration Recommendations:


          · Best Practice: Collect all four endpoints to build complete threat actor profiles with associated reports for both nation-state APT and
               cybercrime groups in your security systems. This provides the most comprehensive threat intelligence coverage.

          · Alternative: For integrations that focus primarily on threat detection and IOC enrichment, collecting only the report endpoints (APT Threat and
               HI Threat) may be sufficient. Reports contain IOCs with severity ratings that help prioritize security responses.

          · Note on Severity Classification: Both threat report feeds (APT Threat and HI Threat) contain high severity IOCs; however, APT IOCs are more
               rare and by nature are the most important.

       Collection-Specific Information


                                                       Property                                                                     Value


                                                        Method                                                                       GET


                                                         Path                                                              /api/v2/hi/threat/updated


                                                       Collection                                                                  hi/threat


                                                   Collection Name                                                             HI Threat Reports


                                                        Module                                                                     Threats

Property                             Value


                                        Submodule                          Last threats


                                          Type                        Common + Individual


                                        TTL (Days)           90 (recommended, not provided in API)


                                    Admiralty Code                          Can differ


                                         Severity                               9


                                    Collection Limit                 10 records per request


                                        Rate Limit     1 request per 10 seconds per company per feed (see

                                                                         API Limitations)


                                        IOC Types         Domain, IPv4, URL, File (MD5, SHA1, SHA256)


                                   Short Description   Reports on cybercriminal threat activities with IOCs,

                                                        attack techniques, and MITRE ATT&CK mappings.


       Request

       Request URL
        GET /api/v2/hi/threat/updated
       Query Parameters

Parameter              Type             Required                  Default                    Description                      Example


                     seqUpdate             integer              No                        0             Sequence update number to get          16738668845708

                                                                                                         the next data chunk. Use this

                                                                                                          parameter to iterate through

                                                                                                          feeds. The value should be

                                                                                                          obtained from the previous

                                                                                                        response’s top-level seqUpdate

                                                                                                      field or from /api/v2/sequence_list

                                                                                                        endpoint. Important: Always use

                                                                                                        the top-level seqUpdate field for

                                                                                                                    iteration.


                       limit               integer              No                       10            Limit the amount of returned data             10

                                                                                                         for this collection. Maximum

                                                                                                         allowed: 10 for this collection.


                        q                  string               No                        -            Search query. Can be used to filter    id:e3fa2b5e0c1e7f5

                                                                                                         results or search for a specific     916db3480cd43faf4

                                                                                                        entry by ID. Format: id: to search        00a5eee8

                                                                                                            for one specific record.


               apply_hunting_rules         integer              No                        0            Apply hunting rules filter. Set to 1           1

                                                                                                                   to enable.


       Query Parameter Details:


          · seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 10 for hi/threat/updated collection

                ·

If not specified, defaults to 10

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types (e.g., ip:8.8.8.8, domain:example.corp)


       Request Headers


                  Header                  Type                 Required                                  Description                                 Example


                  Accept                  string                  No                         Content type accepted by the client                application/json


               Authorization              string                 Yes                     Basic authentication credentials (see Initial                Basic

                                                                                                            Steps)                          base64(LOGIN:API_KEY)


                 User-Agent               string                  No                      User-Agent string with product metadata          SIEM/QRadar_2020.10.6/G

                                                                                          (optional but recommended - especially           roupIB_TI_1.0.0/gibuser@g

                                                                                           useful in troubleshooting on our end).          roup-ib.com/ciaops_3.0.0

                                                                                                           Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                        e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                         Header                                             Description                                                     Example


                     Content-Type                                      Response content type                                             application/json


                   Content-Encoding                                       Content encoding                                                    gzip

Header                                          Description                                         Example


                     Cache-Control                                 Cache control directives                     max-age=0, must-revalidate, private


                             Allow                                 Allowed HTTP methods                                          GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [ThreatItem], "seqUpdate": integer }


                    Field                  Type                            Required                                 Description


                    count                 integer                            Yes                 Number of threat items returned in this response


                    items            array[ThreatItem]                       Yes                               Array of threat objects


                 seqUpdate                integer                            Yes                  Sequence update number at the top level of the

                                                                                                response. Always use this top-level value in the next

                                                                                              request’s seqUpdate parameter to get the next portion of

                                                                                                                       feeds


       ThreatItem Object


                    Field                  Type                            Required                                 Description


                      id                   string                            Yes                 Unique identifier of the threat report (SHA-1 hash)


                     title                 string                            Yes                              Title of the threat report


                  shortTitle            string | null                        No                            Short title of the threat report


                 description               string                            Yes                     HTML-formatted description of the threat


               shortDescription         string | null                        No                            Short description of the threat

Field           Type         Required                         Description


                   type           string          Yes       Type of the threat. Possible values: “event”, “threat”


               reportNumber       string          Yes                      Internal report number


               dateFirstSeen      string          Yes           Date when the threat was first seen (format:

                                                                               YYYY-MM-DD)


               dateLastSeen       string          Yes           Date when the threat was last seen (format:

                                                                               YYYY-MM-DD)


               datePublished      string          Yes          Date when the report was published (format:

                                                                               YYYY-MM-DD)


                 createdAt        string          Yes        ISO 8601 timestamp when the record was created


                 updatedAt        string          Yes      ISO 8601 timestamp when the record was last updated


                isPublished      boolean          Yes                 Whether the threat is published


                 isTailored      boolean          Yes         Whether the threat is tailored for specific clients


                 isAutogen       boolean          Yes         Whether the report was automatically generated


                  hasIocs        boolean          Yes        Whether the threat has indicators of compromise


                   langs       array[string]      Yes      Array of language codes (at this point, only En is up to

                                                                         date - no other languages)


                seqUpdate         integer         Yes         Sequence update number for this specific item


               techSeqUpdate   integer | null     No                Technical sequence update number

Field            Type         Required                         Description


                    oldId         string | null     No                  Previous identifier (if migrated)


                  contacts           array          Yes                     Array of contact objects


                  countries          array          Yes                     Array of country objects


                   regions           array          Yes                      Array of region objects


                   sectors           array          Yes                      Array of sector objects


                    labels           array          Yes                       Array of label objects


                   cveList           array          Yes                     Array of CVE identifiers


                  expertise       array[string]     Yes      Array of expertise types (e.g., [“AutoReport”], [“Leak”],

                                                                                [“Ransomware”])


                  sourceList         array          Yes                     Array of source objects


                   sources           array          Yes                    Array of source identifiers


                    files            array          Yes                       Array of file objects


               forumsAccounts        array          Yes                 Array of forum account objects


                 malwareList         array          Yes                    Array of malware objects


                   toolList          array          Yes                       Array of tool objects


           relatedThreatActors       array          Yes               Array of related threat actor objects


               targetedCompany       array          Yes               Array of targeted company objects


        targetedPartnersAndClie      array          Yes              Array of targeted partners and clients

                     nts


                 companyId           array          Yes                      Array of company IDs

Field                  Type           Required                     Description


                  author               string | null       No                     Author of the report


                 indicators          array[Indicator]      Yes                 Array of indicator objects


               indicatorsIds          array[string]        Yes                   Array of indicator IDs


          indicatorRelationships          array            Yes           Array of indicator relationship objects


       indicatorMalwareRelation           array            Yes      Array of indicator-malware relationship objects

                   ships


       indicatorToolRelationship          array            Yes         Array of indicator-tool relationship objects

                     s


           unreliableIndicators           array            Yes            Array of unreliable indicator objects


       unreliableIndicatorsRelati         array            Yes      Array of unreliable indicator relationship objects

                    ons


                threatActor         ThreatActor | null     No                Associated threat actor object


                mitreMatrix               array            Yes          Array of MITRE ATT&CK matrix objects


                 evaluation            Evaluation          Yes      Evaluation object containing threat assessment


               displayOptions        DisplayOptions        Yes                   Display options object


       Indicator Object


                   Field                  Type           Required                     Description


                     id                   string           Yes       Unique identifier of the indicator (SHA-1 hash)

Field               Type            Required                          Description


                   type               string             Yes      Type of indicator. Possible values: “network”, “file”, etc.


                    title          string | null         No                         Title of the indicator


                description        string | null         No                     Description of the indicator


               dateFirstSeen          string             Yes          Date when the indicator was first seen (format:

                                                                                       YYYY-MM-DD)


               dateLastSeen           string             Yes          Date when the indicator was last seen (format:

                                                                                       YYYY-MM-DD)


                  deleted            boolean             Yes                  Whether the indicator is deleted


                seqUpdate            integer             Yes            Sequence update number for this indicator


               techSeqUpdate      integer | null         No                 Technical sequence update number


                   langs           array[string]         Yes                      Array of language codes


                  sources          array[string]         Yes                     Array of source identifiers


               malwareIdList    array[string] | null     No                     Array of related malware IDs


                malwareList            array             Yes                      Array of malware objects


                 attributes        object | null         No                         Additional attributes


                  params        IndicatorParams          Yes      Indicator parameters object (contains actual indicator

                                                                                            data)


       IndicatorParams Object


                   Field               Type            Required                          Description


                  domain

Field          Type         Required                        Description


                               string | null     No                           Domain name


                    ipv4       array[string]     Yes                    Array of IPv4 addresses


                    ipv6       array[string]     Yes                    Array of IPv6 addresses


                     url          string         Yes                   URL (can be empty string)


                    ssl           array          Yes                Array of SSL certificate objects


       ThreatActor Object


                   Field          Type         Required                        Description


                     id           string         Yes       Unique identifier of the threat actor (SHA-1 hash)


                   name           string         Yes                    Name of the threat actor


                  country      string | null     No                Country code (ISO 3166-1 alpha-2)


                   isAPT         boolean         Yes      Whether this is an APT (Advanced Persistent Threat)

                                                               group. For HI threats, this is typically false


       Evaluation Object


                   Field          Type         Required                        Description


               admiraltyCode      string         Yes                Admiralty Code (e.g., “A1”, “C3”)


                 credibility     integer         Yes                    Credibility score (0-100)


                 reliability     integer         Yes                     Reliability score (0-100)

Field                          Type                                      Required                                                              Description


                    severity                           string                                        Yes                                    Severity level (e.g., “red”, “amber”, “orange”, “green”)


                         tlp                           string                                        Yes                                   Traffic Light Protocol level (e.g., “red”, “amber”, “green”,

                                                                                                                                                                        “white”)


                         ttl                       integer | null                                    No                                      Time to live in days (usually null for this collection)


       DisplayOptions Object


                        Field                          Type                                      Required                                                              Description


                 isFavourite                          boolean                                        Yes                                            Whether the item is marked as favourite


                   isHidden                           boolean                                        Yes                                                     Whether the item is hidden


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/hi/threat/updated?seqUpdate=0&limit=10' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Search Query
       curl -X GET 'https://tap.group-ib.com/api/v2/hi/threat/updated?seqUpdate=0&limit=10&q=id:e3fa2b5e0c1e7f5916db3480cd43faf400a5eee8' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/hi/threat/updated?seqUpdate=0&limit=10&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

       Success Response (200 OK)
        { "count": 1355, "items": [ {                   "contacts": [],        "countries": ["CA"],          "createdAt": "2024-09-23T06:16:41+03:00",                     "cveList": [],
       "dateFirstSeen": "2024-09-23",                 "dateLastSeen": "2024-09-23",                "datePublished": "2024-09-23",                   "description": "
       2024-09-23 Qilin ransomware attacked Canstar Restorations canstarrestorations[.]com.
       ...",     "displayOptions": {              "isFavourite": false,           "isHidden": false          },         "evaluation": {        "admiraltyCode": "A1",            "credibility": 100,
       "reliability": 100,         "severity": "orange",               "tlp": "amber",         "ttl": null        },     "expertise": [        "Leak",        "Ransomware",            "AutoReport"          ],
         "files": [],      "forumsAccounts": [],            "hasIocs": false,          "id": "d4a164b9caecc0d28041bb042bfad1acfb91f77a",                                "indicatorMalwareRelationships":
       [],     "indicatorRelationships": [],             "indicatorToolRelationships": [],               "indicators": [],        "indicatorsIds": [],         "isAutogen": false,          "isPublished":
       true,       "isTailored": false,           "labels": [],       "langs": ["en", "ru"],      "malwareList": [],           "mitreMatrix": [          {        "attackPatternId":
       "attack-pattern--b80d107d-fa0d-4b60-9684-b0433e8bdba0",                                    "attackTactic": "impact",                 "attackType": "enterprise_tactics",                "id": null,
       "mitreId": "T1486",              "params": null            }       ],    "oldId": null,       "regions": ["america:northern_america"],                   "relatedThreatActors": [],
       "reportNumber": "CP-2809-0616",                    "sectors": ["real-estate:construction"],                     "seqUpdate": 17270614084038,              "shortDescription": null,
       "shortTitle": null,        "sourceList": [],          "sources":
       ["http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/site/view?uuid=f73f99c9-0a5d-36ff-8fab-36e936caab39"],
       "targetedCompany": ["Canstar Restorations"],                        "targetedPartnersAndClients": [],                  "techSeqUpdate": null,           "threatActor": {        "country": null,
       "id": "18c14c0707e5cdaeb7975576fa54a4346d154619",                                  "isAPT": false,                "name": "Qilin"       },     "title": "Qilin Ransomware attack on Canstar
       Restorations",           "toolList": [],       "type": "threat",        "unreliableIndicators": [],               "unreliableIndicatorsRelations": [],           "updatedAt":
       "2024-09-23T06:16:48+03:00"                   } ], "seqUpdate": 17270858675384 }

Threats and Actors - Open Threats
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information from the Open Threats collection, which consolidates real-time public reports on cybersecurity threats
       from global sources. The data is categorized by criteria such as threat actor, malware or country and tagged with common identifiers and maybe be
       tagged by threat actor, malware, CVE, or country, facilitating easy filtering and integration with your security measures. This makes it easier to
       understand the content at a glance and apply intelligent filtering based on specific tags.


       Important Note: Indicators from this feed can be automatically parsed for integration with your current security measures, but you should consider this
       feed as low severity. Threat Intelligence team doesn’t review these indicators, and we assume it can produce some false positive alerts in your
       environment.

       Collection-Specific Information


                                                  Property                                                                        Value


                                                   Method                                                                          GET


                                                    Path                                                            /api/v2/hi/open_threats/updated


                                                 Collection                                                                  hi/open_threats


                                              Collection Name                                                                 Open Threats


                                                   Module                                                                  Threats and Actors


                                                 Submodule                                                                    Open Threats


                                                    Type                                                                        Common


                                                 TTL (Days)                                                           None (usually specified as 0)


                                               Admiralty Code                                                                   Mostly B3


                                                  Severity                                                                  5 (recommended)


                                              Collection Limit                                                           100 records per request

Property                                                     Value


                                         Rate Limit                           1 request per 10 seconds per company per feed (see

                                                                                                 API Limitations)


                                         IOC Types                               Domain, IPv4, URL, File (MD5, SHA1, SHA256)


                                   Short Description                         Consolidated public reports from various cybersecurity

                                                                                       vendors and researchers globally.


       Request

       Request URL
        GET /api/v2/hi/open_threats/updated
       Query Parameters


                 Parameter      Type                  Required   Default              Description                    Example


                 seqUpdate     integer                  No         0        Sequence update number to get        1664217109400513

                                                                             the next data chunk. Use this

                                                                              parameter to iterate through

                                                                               feeds. The value should be

                                                                              obtained from the previous

                                                                            response’s top-level seqUpdate

                                                                           field or from /api/v2/sequence_list

                                                                            endpoint. Important: Always use

                                                                            the top-level seqUpdate field for

                                                                                        iteration.


                   limit       integer                  No        100      Limit the amount of returned data           100

                                                                              for this collection. Maximum

                                                                            allowed: 100 for this collection.

Parameter               Type            Required                  Default                          Description                       Example


                        q                    string             No                           -              Search query. Can be used to filter id:4b5f9b40d0207d3

                                                                                                              results or search for a specific       2412338000bbb24b

                                                                                                             entry by ID. Format: id: to search          4a7eb4397

                                                                                                                  for one specific record.


               apply_hunting_rules          integer             No                          0                Apply hunting rules filter. Set to 1             1

                                                                                                                          to enable.


       Query Parameter Details:


          · seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 100 for hi/open_threats/updated collection

                · If not specified, defaults to 100

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific entry: q=id:

                · Supports various search types (e.g., ip:8.8.8.8, domain:example.corp)


       Request Headers


                  Header                  Type                  Required                                    Description                                Example


                   Accept                 string                   No                            Content type accepted by the client                application/json


               Authorization              string                  Yes                     Basic authentication credentials (see Initial                  Basic

                                                                                                               Steps)                         base64(LOGIN:API_KEY)

Header                Type                  Required                                  Description                             Example


               User-Agent             string                   No                       User-Agent string with product metadata     SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially      roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).     roup-ib.com/ciaops_3.0.0

                                                                                                        Format:

                                                                                    PlatformType/PlatformName_PlatformVersio

                                                                                    n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                      Header                                              Description                                                Example


                   Content-Type                                     Response content type                                         application/json


                 Content-Encoding                                      Content encoding                                                gzip


                   Cache-Control                                    Cache control directives                            max-age=0, must-revalidate, private


                          Allow                                     Allowed HTTP methods                                               GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [OpenThreatItem], "seqUpdate": integer }


                  Field                   Type                           Required                                            Description


                  count                  integer                           Yes                         Number of open threat items returned in this response


                  items             array[OpenThreatIt                     Yes                                      Array of open threat objects

                                           em]

Field           Type         Required                         Description


                seqUpdate        integer         Yes          Sequence update number at the top level of the

                                                            response. Always use this top-level value in the next

                                                          request’s seqUpdate parameter to get the next portion of

                                                                                   feeds


       OpenThreatItem Object


                  Field           Type         Required                         Description


                    id            string         Yes      Unique identifier of the open threat report (SHA-1 hash)


                   title          string         Yes                   Title of the open threat report


                   text           string         Yes                Full text content of the threat report


                   link           string         Yes               URL link to the original source article


                 original         string         Yes             Original source URL (can be empty string)


                 source           string         Yes                Source website or publication name


               sourceType         string         Yes           Type of source (e.g., “Blog”, “News”, “Forum”)


                  author       Author | null     No                      Author information object


                createdAt         string         Yes         ISO 8601 timestamp when the record was created


                updatedAt         string         Yes      ISO 8601 timestamp when the record was last updated


               dateDetected       string         Yes        ISO 8601 timestamp when the threat was detected

Field               Type             Required                         Description


                 detected              string             Yes      ISO 8601 timestamp when the threat was detected (same

                                                                                      as dateDetected)


                seqUpdate             integer             Yes          Sequence update number for this specific item


                threatActors    array[ThreatActor] |      No               Array of associated threat actor objects

                                        null


                   data             ThreatData            Yes       Threat data object containing categorized information


                 evaluation         Evaluation            Yes          Evaluation object containing threat assessment


               displayOptions     DisplayOptions          Yes                      Display options object


       Author Object


                   Field               Type             Required                         Description


                   name                string             Yes               Author’s name (can be empty string)


                 profileUrl            string             Yes             Author’s profile URL (can be empty string)


                screenName             string             Yes            Author’s screen name (can be empty string)


                   userId              string             Yes               Author’s user ID (can be empty string)


       ThreatData Object


                   Field               Type             Required                         Description


                 countries      array[Country] | null     No           Array of country objects mentioned in the threat

Field             Type          Required                         Description


                companyTags           array           Yes                       Array of company tags


                cryptoWallets      array | null       No              Array of cryptocurrency wallet addresses


                    cve            array | null       No                       Array of CVE identifiers


                  domains          array | null       No                       Array of domain names


                   emails          array | null       No       Array of email addresses - not recommeded to use for

                                                                                       detection


                    files          array | null       No                       Array of file information


                   hashes          array | null       No                         Array of file hashes


                     ip            array | null       No                        Array of IP addresses


                  malware        array[Malware] |     No                      Array of malware objects

                                       null


                  pdbPaths         array | null       No              Array of PDB (Program Database) paths


                    rules          array | null       No                        Array of security rules


                    tags           array[string]      Yes      Array of tag strings (e.g., [“Access”, “Bank”, “COVID-19”,

                                                                              “Cashout”, “Leak”, “Rent”])


               telegramApiKeys     array | null       No                     Array of Telegram API keys


       Country Object


                    Field             Type          Required                         Description


                   country            string          Yes                           Country name


                countryCode           string          Yes                Country code (ISO 3166-1 alpha-2)


       Malware Object

Field          Type         Required                       Description


                     id           string         Yes       Unique identifier of the malware (SHA-1 hash)


                   name           string         Yes                    Name of the malware


                threatLevel       string         Yes             Threat level (can be empty string)


                 platform      string | null     No                     Platform information


                 category      string | null     No                       Malware category


                   class       string | null     No                         Malware class


       ThreatActor Object


                   Field          Type         Required                       Description


                     id           string         Yes      Unique identifier of the threat actor (SHA-1 hash)


                   name           string         Yes                  Name of the threat actor


       Evaluation Object


                   Field          Type         Required                       Description


               admiraltyCode      string         Yes              Admiralty Code (e.g., “B3”, “C3”)


                 credibility     integer         Yes                   Credibility score (0-100)


                 reliability     integer         Yes                   Reliability score (0-100)


                  severity        string         Yes         Severity level (e.g., “red”, “orange”, “green”)

Field                              Type                                     Required                                                         Description


                          tlp                            string                                       Yes                            Traffic Light Protocol level (e.g., “red”, “amber”, “green”,

                                                                                                                                                                        “white”)


                          ttl                            integer                                      Yes                                 Time to live in days (usually 0 for this collection)


       DisplayOptions Object


                      Field                              Type                                     Required                                                         Description


                   isFavourite                       boolean                                          Yes                                          Whether the item is marked as favourite


                    isHidden                         boolean                                          Yes                                                Whether the item is hidden


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/hi/open_threats/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Search Query
       curl -X GET
       'https://tap.group-ib.com/api/v2/hi/open_threats/updated?seqUpdate=0&limit=100&q=id:4b5f9b40d0207d32412338000bbb24b4a7eb4397' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/hi/open_threats/updated?seqUpdate=0&limit=100&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H
       'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 294234, "items": [                {      "author": {          "name": "",          "profileUrl": "",     "screenName": "",            "userId": ""            },            "createdAt":
       "2022-05-25T09:30:41+00:00",                      "data": {        "countries": [          {          "country": "Brazil",          "countryCode": "BR"                        },            {          "country":
       "New Zealand",                     "countryCode": "NZ"               },      {          "country": "Argentina",              "countryCode": "AR"                     },             {            "country":
       "France",                "countryCode": "FR"                },        {          "country": "Ireland",             "countryCode": "IE"            },        {              "country": "Japan",
       "countryCode": "JP"                   },      {             "country": "Uruguay",               "countryCode": "UY"            }       ],       "companyTags": [],                         "cryptoWallets": null,
               "cve": null,         "domains": null,            "emails": null,          "files": null,       "hashes": null,       "ip": null,        "malware": null,                        "pdbPaths": null,
       "rules": null,            "tags": [        "Access",              "Bank",         "COVID-19",             "Cashout",         "Leak",            "Rent"          ],        "telegramApiKeys": null
       },      "dateDetected": "2022-09-26T18:31:49+00:00",                         "detected": "2022-09-26T18:31:49+00:00",                   "displayOptions": {                    "isFavourite": false,
       "isHidden": false             },      "evaluation": {            "admiraltyCode": "B3",            "credibility": 50,      "reliability": 50,          "severity": "green",                      "tlp": "white",
        "ttl": 0     },         "id": "4b5f9b40d0207d32412338000bbb24b4a7eb4397",                               "link":
       "https://www.welivesecurity.com/2022/05/25/5-reasons-why-gdpr-milestone-data-protection/",                                           "original": "",       "seqUpdate": 1664217109388512,
            "source": "welivesecurity.com",                "sourceType": "Blog",            "text": "The landmark regulation changed everyone's mindset on how companies
       worldwide collect and use the personal data of EU citizens...",                           "threatActors": null,          "title": "5 reasons why GDPR was a milestone for data
       protection",             "updatedAt": "2022-09-26T18:31:49+00:00"                    } ], "seqUpdate": 1664217109400513 }

Threats and Actors - Analyst Reports
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint provides updated information on analytic reports. This collection provides reports on known incidents and cybercrime trends as well as
       tailored reports for clients. It also contains reports on specific threats and complex malware and attacks being prepared against Group-IB customers.
       Such reports contain detailed information on malicious activity, indicators, and artifacts as well as expert recommendations.


       The strategic data contained in the reports helps companies prepare months before attacks take place and improve their existing security policies.
       Therefore, in such materials the research and forecasts based on analyses of actual data are key.


       This endpoint does not allow direct download of report files. However, it provides portal links (portalLink in the file objects) that can be used to access
       and download the reports through the Group-IB Threat Intelligence portal.

       Collection-Specific Information


                                                  Property                                                                        Value


                                                   Method                                                                          GET


                                                    Path                                                               /api/v2/hi/analytic/updated


                                                 Collection                                                                     hi/analytic


                                              Collection Name                                                                Analytic Reports


                                                   Module                                                                  Threats and Actors


                                                 Submodule                                                                   Analytic Reports


                                                    Type                                                                        Common


                                                 TTL (Days)                                                            None (not provided in API)


                                               Admiralty Code                                                                       A1


                                                  Severity                                                                         N/A


                                              Collection Limit                                                           500 records per request

Property                                                     Value


                                            Rate Limit                           1 request per 10 seconds per company per feed (see

                                                                                                    API Limitations)


                                      Short Description                        Reports on known incidents, cybercrime trends, specific

                                                                                      threats, and complex malware with expert

                                                                                                   recommendations.


       Request

       Request URL
        GET /api/v2/hi/analytic/updated
       Query Parameters


                 Parameter        Type                   Required   Default              Description                      Example


                 seqUpdate        integer                  No         0        Sequence update number to get           17295160323428

                                                                                the next data chunk. Use this

                                                                                 parameter to iterate through

                                                                                  feeds. The value should be

                                                                                 obtained from the previous

                                                                               response’s top-level seqUpdate

                                                                              field or from /api/v2/sequence_list

                                                                               endpoint. Important: Always use

                                                                               the top-level seqUpdate field for

                                                                                           iteration.


                   limit          integer                  No        500      Limit the amount of returned data             500

                                                                                 for this collection. Maximum

                                                                               allowed: 500 for this collection.


                      q           string                   No          -      Search query. Can be used to filter id:0326ee95e173174

                                                                                results or search for a specific    a1ff9e4250f1f5bf02

                                                                               entry by ID. Format: id: to search         6bcc08e

                                                                                   for one specific record.


       Query Parameter Details:

· seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 500 for hi/analytic/updated collection

               · If not specified, defaults to 500

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                  Required                               Description                             Example


                  Accept                 string                   No                      Content type accepted by the client              application/json


               Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                         Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                        Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                               Description                                       Example


                  Content-Type                                      Response content type                                application/json


                Content-Encoding                                       Content encoding                                            gzip


                  Cache-Control                                    Cache control directives                     max-age=0, must-revalidate, private


                          Allow                                     Allowed HTTP methods                                           GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [AnalyticItem], "seqUpdate": integer }


                 Field                    Type                           Required                                   Description


                 count                   integer                              Yes                Number of analytic items returned in this response


                 items             array[AnalyticItem]                        Yes                         Array of analytic report objects


               seqUpdate                 integer                              Yes                 Sequence update number at the top level of the

                                                                                                response. Always use this top-level value in the next

                                                                                              request’s seqUpdate parameter to get the next portion of

                                                                                                                       feeds


       AnalyticItem Object


                 Field                    Type                           Required                                   Description


                   id                     string                              Yes               Unique identifier of the analytic report (SHA-1 hash)


                 oldId                 string | null                          No                          Previous identifier (if migrated)


                  title                   string                              Yes                                   Report title

Field           Type         Required                        Description


                description        string         Yes                       Report description


               datePublished       string         Yes      ISO 8601 date when the report was published (format:

                                                                              YYYY-MM-DD)


                seqUpdate         integer         Yes         Sequence update number for this specific item


                   type            string         Yes                     Report type (e.g., “pdf”)


                   langs        array[string]     Yes              Array of language codes (e.g., [“en”])


                   cover         FileObject       Yes                     Cover image file object


                    file         FileObject       Yes                     Report file object (PDF)


                 evaluation     Evaluation        Yes         Evaluation object containing threat assessment


               displayOptions   object | null     No                      Display options object


       FileObject Object


                   Field           Type         Required                        Description


                   name            string         Yes                         File path/name


                   hash            string         Yes                    SHA-256 hash of the file


                   mime            string         Yes        MIME type (e.g., “application/pdf”, “image/png”)


                    size          integer         Yes          File size in bytes (usually 0 in API response)


                  fileData      object | null     No           File data object (usually null in API response)

Field                       Type                            Required                                                        Description


                coverData                 object | null                           No                                     Cover data object (usually null in API response)


                 portalLink                    string                             Yes                                              Portal link to download the file


       Evaluation Object


                   Field                       Type                            Required                                                        Description


               admiraltyCode                   string                             Yes                                                   Admiralty Code (e.g., “A1”)


                 credibility                 integer                              Yes                                                    Credibility score (0-100)


                 reliability                 integer                              Yes                                                    Reliability score (0-100)


                  severity                     string                             Yes                                      Severity level (e.g., “green”, “orange”, “red”)


                     tlp                       string                             Yes                              Traffic Light Protocol level (e.g., “amber”, “red”, “green”,

                                                                                                                                                 “white”)


                     ttl                  integer | null                          No                                Time to live in days (usually null for analytic reports)


       Example Request

       Basic Request
        curl -X GET 'https://tap.group-ib.com/api/v2/hi/analytic/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 2, "items": [ {        "cover": {       "name":
       "/8eee15f5471d44e819d09d4def4d31c3c2e53a91/file/2b20e97a18e1c811cbd0c63da05a99dde7f2841ed4b8972bd3602226eca979c8",                                                         "hash":
       "2b20e97a18e1c811cbd0c63da05a99dde7f2841ed4b8972bd3602226eca979c8",                              "mime": "image/png",                "size": 0,        "fileData": null,
       "coverData": null,      "portalLink":
       "https://tap.group-ib.com/api/v2/hi/analytic/8eee15f5471d44e819d09d4def4d31c3c2e53a91/file/2b20e97a18e1c811cbd0c63da05a99dde7f2841ed
       4b8972bd3602226eca979c8"              },      "datePublished": "2024-10-18",      "description": "Each quarter, Group-IB publishes an in-depth report that
       highlights trends in high-tech cybercrime, forecasts future threats, and identifies significant global cyber risks. The report focuses on advanced
       persistent threats (APTs) and cybercriminal activities across regions including Europe, Latin America, the Middle East and Africa (MEA), and
       Asia-Pacific. It analyzes industry and government trends in areas such as ransomware, initial access brokers, data leaks, and compromised hosts,
       while also addressing notable state-sponsored targeted attacks.",              "displayOptions": null,      "evaluation": {           "admiraltyCode": "A1",
       "credibility": 100,     "reliability": 100,      "severity": "green",   "tlp": "amber",       "ttl": null    },      "file": {       "name":
       "/8eee15f5471d44e819d09d4def4d31c3c2e53a91/file/aaa3b70927b5ea8bfc58dc961b69665d39700b0257e13208604ad9da0c24efbd",                                                         "hash":
       "aaa3b70927b5ea8bfc58dc961b69665d39700b0257e13208604ad9da0c24efbd",                              "mime": "application/pdf",               "size": 0,       "fileData": null,
       "coverData": null,      "portalLink":

"https://tap.group-ib.com/api/v2/hi/analytic/8eee15f5471d44e819d09d4def4d31c3c2e53a91/file/aaa3b70927b5ea8bfc58dc961b69665d39700b025
       7e13208604ad9da0c24efbd"       },     "id": "8eee15f5471d44e819d09d4def4d31c3c2e53a91",              "langs": [   "en"   ],   "oldId": null,
       "seqUpdate": 17295160323428,        "title": "Threat evolution in Q3 2024",   "type": "pdf"   } ], "seqUpdate": 17295168766104 }

IOC Primary
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides indicators of compromise (IOCs) from Group-IB research: IP addresses, domains, URLs and file hashes. Each indicator comes
       with a risk score, attribution to malware families and threat actors, and evaluation metadata (Admiralty Code, TLP, TTL). Use it to block known-bad
       infrastructure, detect hosts that contacted it, and enrich alerts and investigations.


       IOC Primary replaces IOC Common (ioc/common). It returns the same indicators as IOC Common, plus risk scores, evaluation metadata, tags and
       source information that IOC Common does not include. IOC Common is deprecated (see Deprecated Collections); move your integrations to IOC
       Primary.


       Note: Indicators from Malware - C2 are included in IOC Primary. If you ingest IOC Primary, you do not need to ingest Malware - C2 separately for
       indicators.

       Collection-Specific Information


                                                  Property                                                                     Value


                                                   Method                                                                       GET


                                                     Path                                                          /api/v2/ioc/primary/updated


                                                  Collection                                                                ioc/primary


                                              Collection Name                                                   Primary Indicators of Compromise


                                                   Module                                                          Not presented in the interface


                                                 Submodule                                                                      Mix


                                                    Type                                                                     Common


                                                 TTL (Days)                                           Set per record in evaluation.TTL. Values range from 365

                                                                                                               to 14600 depending on the indicator


                                               Admiralty Code                                         Set per record in evaluation.admiraltyCode. Values vary

                                                                                                                            by indicator

Property                                                              Value


                                                  Severity                                     Not provided. Derive severity from riskScore (see “Risk

                                                                                                             Score and Severity” below)


                                               Hunting Rules                                   Not applicable. The apply_hunting_rules parameter has

                                                                                                             no effect on this collection


                                              Collection Limit                                                2500 records per request


                                                 Rate Limit                                         1 request per second (see API Limitations)


                                                 IOC Types                                          IP, Domain, URL, File (MD5, SHA1, SHA256)


                                             Short Description                                 Group-IB’s main IOC feed: IPs, domains, URLs and file

                                                                                                    hashes, each with a risk score, malware and

                                                                                                 threat-actor attribution, and a TTL. Use it to block,

                                                                                                                 detect and enrich.


       Use Cases


                      Use case                               How it works                                   Where it is used


               Block adversary network      Take IPs, domains and URLs from network                   NGFW/FW, SOAR, TIP, SIEM

                    infrastructure        records and block those above your riskScore

                                           threshold. Any later connection attempt to a

                                                 blocked indicator is an incident.


          Detect a host that contacted     Match IPs, domains and URLs against DNS,                SIEM, NTA/NDR, EDR/XDR, SOAR

               known-bad infrastructure   proxy, NetFlow, firewall and EDR logs, both for

                                          new events and retrospectively. A match opens

                                          an incident with the indicator, its riskScore, the

                                            malware family from malwareList, and the

                                          dateFirstSeen–dateLastSeen window in which

                                                     the indicator was active.

Use case                              How it works                                Where it is used


         Detect malware execution or      Match file hashes (md5, sha1, sha256) against      EDR/XDR, SIEM, SOAR, Email protection

                 delivery by hash         endpoint and mail gateway telemetry. A match

                                          is a malware execution or delivery incident with

                                               the malware family already identified.


           Identify the malware family     Look up an IP, domain, URL or hash from the             SOAR, SIEM, TIP, EDR/XDR

        behind an indicator in an open       case with q=<value>. The record returns

                       case               malwareList, threatList and tags, which identify

                                             the family and help choose the response

                                                             playbook.


        Publish curated indicators with      Publish each indicator with its riskScore,                   TIP, SOAR

               attribution and expiry     malwareList and threatList attribution and tags,

                                            and use evaluation.TTL as the expiry date.

                                          Respect the TLP value when sharing indicators

                                                              further.


          Keep an indicator history for   Store records in your own system keyed on id,                      SIEM

                  trend reporting             with the indicator values, scores, dates,

                                          attribution and evaluation. Report trends from

                                             your stored history; the count field in the

                                             response is not a total for the collection.


       Request

       Request URL
        GET /api/v2/ioc/primary/updated
       Query Parameters

Parameter               Type               Required                  Default                      Description                     Example


                     seqUpdate              integer               Yes                        -               Sequence update number that                   1

                                                                                                           marks where to start reading. Use

                                                                                                             1 for the first request, then the

                                                                                                               seqUpdate value from the

                                                                                                           previous response. Do not use 0 or

                                                                                                               omit the parameter: on this

                                                                                                              collection the feed does not

                                                                                                             advance and the same page is

                                                                                                               returned on every request.


                       limit                integer                No                        -                Number of records to return.               2500

                                                                                                            Maximum allowed: 2500 for this

                                                                                                                       collection.


                        q                    string                No                        -              Search query. Use it to look up a         192.0.2.10

                                                                                                            specific indicator value or record

                                                                                                                  ID. See details below.


               apply_hunting_rules          integer                No                        -              Has no effect on this collection.              -


       Query Parameter Details:


          · seqUpdate:


                · Start with seqUpdate=1. This returns the full history of the collection from the oldest record (2020), so the first run is a full download.

                · After each response, save the top-level seqUpdate value and send it in the next request. Continue until a response returns no items.

                · On later runs, continue from the last saved seqUpdate value instead of starting from 1 again.

                · Sequence List can return 1 for this collection instead of a date-based value. If it does, there is no date-based starting point available:
                  either retry the request, or start from seqUpdate=1 and expect a full download.


          · limit:


                · Maximum value: 2500 for ioc/primary/updated collection

                · Set the value explicitly in every request


          · q:

· To look up an indicator: q=, for example q=192.0.2.10 or q=malicious.example.corp. The response can also contain other records, so
                 keep only records that contain the exact value you searched for.

               · To look up a record by ID: q=id: or q=

               · For incremental collection, use seqUpdate instead of q


       Request Headers


                 Header                 Type                   Required                                  Description                                Example


                  Accept                string                    No                         Content type accepted by the client               application/json


               Authorization            string                   Yes                    Basic authentication credentials (see Initial                Basic

                                                                                                           Steps)                          base64(LOGIN:API_KEY)


                User-Agent              string                    No                       User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                           (optional but recommended - especially         roupIB_TI_1.0.0/user@exa

                                                                                            useful in troubleshooting on our end).         mple.corp/ciaops_3.2.1

                                                                                                           Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                       n/AppName_AppVersion/Username/LibNam

                                                                                                        e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                               Description                                                   Example


                    Content-Type                                       Response content type                                            application/json


                  Content-Encoding                                        Content encoding                                                   gzip


                    Cache-Control                                      Cache control directives                            max-age=0, must-revalidate, private


                         Allow                                         Allowed HTTP methods                                                  GET

Response Body Schema

       Root Object
       { "count": integer, "items": [Indicator], "seqUpdate": integer }


                   Field                   Type                            Required                                             Description


                  count                   integer                             Yes                          Number of records remaining after this response. It

                                                                                                         decreases as you read the feed and is not the number of

                                                                                                                           items in this response


                  items               array[Indicator]                        Yes                                        Array of indicator records


                seqUpdate                 integer                             Yes                          Sequence update number to send in the next request


       Indicator Object


       Each record is either a network record (type is network) or a file record (type is file). The fields below are present on both.


                   Field                   Type                            Required                                             Description


                    id                     string                             Yes                           Unique record identifier. Usually 40 characters; file

                                                                                                        records can use the 64-character SHA256 value as the ID.

                                                                                                                       Use it to deduplicate records


                seqUpdate                 integer                             Yes                                Sequence update number of this record


                   type                    string                             Yes                                       Record type: network or file


               dateFirstSeen               string                             Yes                         ISO 8601 timestamp when the indicator was first seen


               dateLastSeen                string                             Yes                         ISO 8601 timestamp when the indicator was last seen


                    ip                 array[IpEntry]                         Yes                              IP address indicators. Empty on file records

Field                Type                          Required                                             Description


                  domain          array[DomainEntry]                     Yes                                 Domain indicators. Empty on file records


                     url            array[UrlEntry]                      Yes                                   URL indicators. Empty on file records


                    hash            object (Hash)                         No                                 File hashes. Present on file records only


                 riskScore              integer                           No                         Risk score of the file, 0-100. Present on file records only;

                                                                                                        network records have a score per indicator instead


                malwareList         array[Malware]                       Yes                          Malware families associated with the indicator. Can be

                                                                                                                               empty


                 threatList          array[Threat]                       Yes                           Threats associated with the indicator. Can be empty


               threatActorList           array                           Yes                            Threat actors associated with the indicator. Can be

                                                                                                                               empty


                    tags             array[string]                       Yes                         Category labels, for example Phishing, RAT, Ransomware,

                                                                                                                       Exploit. May be empty


                   source               string                           Yes                                 Type of source the indicator came from


               potentialNames            array                           Yes                          Possible names associated with the indicator. Can be

                                                                                                                               empty


                 evaluation       object (Evaluation)                    Yes                                    Evaluation metadata of the record


       Network Record Entries


       A network record can contain IPs, domains and URLs at the same time. Read all three arrays.

Object                  Field              Type                     Required                                  Description


                   IpEntry                  ip                string                      Yes                  IPv4 address. This collection does not contain

                                                                                                                               IPv6 addresses


                   IpEntry              riskScore            integer                       No                        Risk score of the IP address, 0-100


               DomainEntry               domain               string                      Yes                                  Domain name


               DomainEntry              riskScore            integer                       No                     Risk score of the domain, 0-100. May be

                                                                                                                                   absent


                   UrlEntry                 url               string                      Yes                                       URL


                   UrlEntry             riskScore            integer                       No                           Risk score of the URL, 0-100


       Hash Object


                    Field                 Type                          Required                                          Description


                    md5                  string                            No                                              MD5 hash


                    sha1                 string                            No                                             SHA1 hash


                   sha256                string                            No                                            SHA256 hash


                    other                string                            No                               Hash calculated with another algorithm


       Note: Any of the hash values can be missing, including sha256. A small number of file records have no hash object at all. Check each value before
       using it.

       Malware Object


                    Field                 Type                          Required                                          Description


                    name                 string                           Yes                                        Malware family name


                   aliases         array[string] | null                    No                        Alternative names of the malware family. Can be null

Threat Object


                      Field                 Type                        Required                                            Description


                      name                  string                         Yes                                          Name of the threat


                       title                string                         Yes                                   Title of the threat. Can be empty


       Evaluation Object


                      Field                 Type                        Required                                            Description


               admiraltyCode                string                         Yes                         Admiralty Code, for example A1, B2 or C3 (see Data

                                                                                                                           Classification)


                 credibility                integer                        Yes                                  Credibility of the information, 0-100


                  reliability               integer                        Yes                                    Reliability of the source, 0-100


                       TLP                  string                         Yes                       Traffic Light Protocol value, including the TLP: prefix, for

                                                                                                     example TLP:AMBER. Remove the prefix if your system

                                                                                                                 expects a value such as AMBER


                       TTL                  integer                        Yes                      Time to live of the indicator in days, for example 365, 730,

                                                                                                        1825, 2555 or 14600. Use it to set the expiry of the

                                                                                                                      indicator in your system


       Note: The TLP and TTL field names are uppercase. This collection does not return a severity field.

       Risk Score and Severity


       This collection does not return a severity value. Use riskScore to assign severity in your system. The ranges below are the same as for IP Scoring and
       Domain Scoring.


               Score             Category                           Suggested severity                                       Suggested action


               0-39

Score                  Category                                       Suggested severity                                              Suggested action


                                            Low                                             Low                                                         No action


               40-59                 Suspicious                                           Medium                                                          Monitor


               60-79                        High                                           High                                                         Investigate


               80-100                 Malicious                                           Critical                                                     Block or alert


       Where to find the score:


          · Network records: each entry in ip, domain and url has its own riskScore. There is no top-level riskScore on network records.

          · File records: one top-level riskScore applies to all hashes in the record.


       If riskScore is not present, the indicator has not been scored. Do not treat a missing score as 0.

       Data Handling


          · Respect the TLP value of each record when you share indicators with other teams or organizations.

          · Indicators point to malicious infrastructure. Defang values when displaying them (for example, hxxp://malicious[.]example[.]corp) so that they
               cannot be opened by accident.

       Example Request


       Note: In the examples below, set the GIB_CREDENTIALS environment variable to your LOGIN:API_KEY (your email and API key) before running the
       command.

       First Request
        curl -X GET 'https://tap.group-ib.com/api/v2/ioc/primary/updated?seqUpdate=1&limit=2500' \ -u "$GIB_CREDENTIALS" \ -H 'Accept:
       application/json'
       Next Request


       Replace with the top-level seqUpdate value from the previous response.
        curl -X GET 'https://tap.group-ib.com/api/v2/ioc/primary/updated?seqUpdate=&limit=2500' \ -u "$GIB_CREDENTIALS" \ -H 'Accept: application/json'

       Look Up an Indicator
        curl -X GET 'https://tap.group-ib.com/api/v2/ioc/primary/updated?q=192.0.2.10' \ -u "$GIB_CREDENTIALS" \ -H 'Accept: application/json'
       Look Up a Record by ID
        curl -X GET 'https://tap.group-ib.com/api/v2/ioc/primary/updated?q=id:0a1b2c3d4e5f60718293a4b5c6d7e8f901234567' \ -u "$GIB_CREDENTIALS"
       \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)


       The example contains one network record and one file record. All values are examples.
        { "count": 182340, "items": [                {      "id": "0a1b2c3d4e5f60718293a4b5c6d7e8f901234567",                 "seqUpdate": 17762117245804,                "type": "network",
             "dateFirstSeen": "2026-09-15T00:00:00Z",                 "dateLastSeen": "2026-10-02T00:00:00Z",         "ip": [       {      "ip": "192.0.2.10",            "riskScore": 95
         }      ],     "domain": [          {            "domain": "malicious.example.corp"       }   ],   "url": [      {         "url": "http://malicious.example.corp/login.php",
               "riskScore": 100         }       ],        "malwareList": [    {       "name": "ExampleRAT",           "aliases": null       }   ],     "threatList": [],
       "threatActorList": [],        "tags": ["RAT"],           "source": "example-source",     "potentialNames": [],         "evaluation": {    "admiraltyCode": "B2",
       "credibility": 80,         "reliability": 80,           "TLP": "TLP:AMBER",       "TTL": 365    }   },   {     "id":
       "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",                                  "seqUpdate": 17762117245805,                "type": "file",

"dateFirstSeen": "2026-09-20T00:00:00Z",          "dateLastSeen": "2026-09-20T00:00:00Z",              "ip": [],   "domain": [],         "url": [],      "hash": {     "md5":
       "d41d8cd98f00b204e9800998ecf8427e",                "sha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709",                        "sha256":
       "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"                             },     "riskScore": 100,       "malwareList": [              {        "name":
       "ExampleStealer",           "aliases": ["ExampleStealer v2"]    }   ],     "threatList": [],        "threatActorList": [],        "tags": [],         "source": "example-source",
           "potentialNames": [],      "evaluation": {    "admiraltyCode": "A1",      "credibility": 100,           "reliability": 100,         "TLP": "TLP:AMBER",             "TTL":
       1825      }   } ], "seqUpdate": 17762117245805 }

IOC Common
       Deprecated: IOC Common is replaced by IOC Primary, which returns the same indicators with risk scores, evaluation metadata and attribution. New
       integrations should use IOC Primary.

       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information from the Common IoCs collection, which consolidates Indicators of Compromise (IOCs) from multiple TI
       modules - Threats and Malware. This collection is specially created to get only IoCs and has no extra context (in some cases - attribution to malware
       family of threat actor), making it ideal for firewall rules and security filtering.


       Important Note: The Common IoCs collection contains indicators from the following collections: - malware/cnc (C2 servers) - hi/threat (Human
       Intelligence threats) - apt/threat (Advanced Persistent Threat reports)


       The main idea of IOC Common collection is to use it for firewall rules and security filtering without the need for additional context or attribution.

       Collection-Specific Information


                                                    Property                                                                       Value


                                                     Method                                                                         GET


                                                       Path                                                           /api/v2/ioc/common/updated


                                                    Collection                                                                 ioc/common


                                                Collection Name                                                    Common Indicators of Compromise


                                                     Module                                                           Not presented in the interface


                                                   Submodule                                                                        Mix


                                                       Type                                                                Common + Individual


                                                   TTL (Days)                                                     90 (recommended, not provided in API)


                                                 Admiralty Code                                                                    None


                                                     Severity                                                                        9


                                                 Collection Limit                                                        5000 records per request

Property                                                     Value


                                        Rate Limit                           1 request per 10 seconds per company per feed (see

                                                                                                API Limitations)


                                        IOC Types                                 Domain, IP, URL, File (MD5, SHA1, SHA256)


                                  Short Description                         Consolidated Indicators of Compromise from multiple

                                                                                          threat intelligence sources.


       Request

       Request URL
        GET /api/v2/ioc/common/updated
       Query Parameters


                 Parameter    Type                   Required   Default              Description                      Example


                 seqUpdate    integer                  No         0        Sequence update number to get           17272224279604

                                                                            the next data chunk. Use this

                                                                             parameter to iterate through

                                                                              feeds. The value should be

                                                                             obtained from the previous

                                                                           response’s top-level seqUpdate

                                                                          field or from /api/v2/sequence_list

                                                                           endpoint. Important: Always use

                                                                           the top-level seqUpdate field for

                                                                                       iteration.


                   limit      integer                  No        5000     Limit the amount of returned data              5000

                                                                             for this collection. Maximum

                                                                           allowed: 5000 for this collection.


                      q       string                   No          -      Search query. Can be used to filter id:6c3e5247ee68545

                                                                            results or search for a specific    c60d850af02c2bc21

                                                                           entry by ID. Format: id: to search         0aa08e50

                                                                               for one specific record.

Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 5000 for ioc/common/updated collection

               · If not specified, defaults to 5000

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types (e.g., ip:8.8.8.8, domain:example.corp, hash:abc123...)


       Request Headers


                  Header                 Type                  Required                                  Description                          Example


                  Accept                string                    No                      Content type accepted by the client              application/json


               Authorization            string                   Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                           Steps)                      base64(LOGIN:API_KEY)


                 User-Agent             string                    No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                          Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                              Description                                          Example


                  Content-Type                                       Response content type                                 application/json


                Content-Encoding                                          Content encoding                                        gzip


                  Cache-Control                                     Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                      Allowed HTTP methods                                          GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [Indicator], "seqUpdate": integer }


                 Field                    Type                             Required                                   Description


                 count                   integer                              Yes                Number of indicator items returned in this response


                 items               array[Indicator]                         Yes                             Array of indicator objects


               seqUpdate                 integer                              Yes                  Sequence update number at the top level of the

                                                                                                 response. Always use this top-level value in the next

                                                                                               request’s seqUpdate parameter to get the next portion of

                                                                                                                         feeds


       Indicator Object


                 Field                    Type                             Required                                   Description


                   id                     string                              Yes                   Unique identifier of the indicator (SHA-1 hash)


                  type                    string                              Yes              Type of indicator. Possible values: “network”, “file”, etc.

Field                 Type                            Required                                          Description


               dateFirstSeen             string                            Yes                       ISO 8601 timestamp when the indicator was first seen

                                                                                                            (format: YYYY-MM-DDTHH:mm:ss+03:00)


               dateLastSeen              string                            Yes                        ISO 8601 timestamp when the indicator was last seen

                                                                                                            (format: YYYY-MM-DDTHH:mm:ss+03:00)


                seqUpdate               integer                            Yes                           Sequence update number for this specific item


                   hash               array[string]                        No                        Array of file hash values (MD5, SHA1, SHA256). Present

                                                                                                                     for file-type indicators.


               malwareList          array[Malware]                         Yes                       Array of malware objects associated with this indicator


                 threatList          array[Threat]                         Yes                        Array of threat objects associated with this indicator


       Note: The structure varies based on indicator type: - File indicators: Include hash array with MD5, SHA1, and/or SHA256 values - Network indicators:
       May include IP addresses, domains, or URLs (structure may vary)

       Malware Object


                   Field                 Type                            Required                                          Description


                   name                  string                            Yes                                        Name of the malware


                  aliases             array[string]                        Yes                         Array of alternative names/aliases for the malware


       Threat Object


                   Field                 Type                            Required                                          Description


                   name                  string                            Yes                                         Name of the threat

Field                  Type                             Required                                             Description


                  title                string                              Yes                                      Title or description of the threat


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/ioc/common/updated?seqUpdate=0&limit=5000' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Search Query
       curl -X GET 'https://tap.group-ib.com/api/v2/ioc/common/updated?seqUpdate=0&limit=5000&q=id:6c3e5247ee68545c60d850af02c2bc210aa08e50'
       \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with IP Search
        curl -X GET 'https://tap.group-ib.com/api/v2/ioc/common/updated?seqUpdate=0&limit=5000&q=ip:8.8.8.8' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

       Success Response - hashes (200 OK)
        { "count": 15234, "items": [ { "id": "6337a9653cd46b5e2fc5394696201951027905b6",                "type": "file",    "dateFirstSeen":
       "2024-10-05T00:00:00+03:00",    "dateLastSeen": "2024-10-05T00:00:00+03:00",          "seqUpdate": 15996048022320,          "hash": [
       "73fe053e733bd116d605b76e02b74fb1456326a7",            "fe16a85a3f0094134eef4ba209c188a186ed269de90a6b5a84bcc4b90470cc79",
       "b372fd09864d839112b79b7f0675f7df"        ],   "malwareList": [      {       "name": "CobInt",      "aliases": []      }    ],   "threatList": [   {
       "name": "Cobalt",    "title": "Attacks of Cobalt gang based on using CobInt"      }    ]   } ], "seqUpdate": 15996048022320 }

Malware - C2
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on Command and Control (C2) servers. The CNC collection contains information on the control center
       where malware related to targeted attacks use to store stolen data or download commands from.


       Note: This endpoint includes IOCs, which are also part of the IOC Primary collection.

       Collection-Specific Information


                                                  Property                                                                 Value


                                                   Method                                                                   GET


                                                    Path                                                       /api/v2/malware/cnc/updated


                                                 Collection                                                            malware/cnc


                                              Collection Name                                                  Command and Control Servers


                                                   Module                                                                Malware


                                                    Type                                                                 Common


                                                 TTL (Days)                                                90 (recommended, not provided in API)


                                               Admiralty Code                                                              None


                                                  Severity                                                                   9


                                              Collection Limit                                                   1000 records per request


                                                 Rate Limit                                         1 request per 10 seconds per company per feed (see

                                                                                                                      API Limitations)


                                                 IOC Types                                                           Domain, IPv4, URL

Property                                                   Value


                                      Short Description                       Information on control centers where malware related

                                                                                  to targeted attacks use to store stolen data or

                                                                                            download commands from.


       Request

       Request URL
        GET /api/v2/malware/cnc/updated
       Query Parameters


                 Parameter        Type                 Required   Default              Description                    Example


                 seqUpdate        integer                No         0        Sequence update number to get          13700304004

                                                                              the next data chunk. Use this

                                                                               parameter to iterate through

                                                                                feeds. The value should be

                                                                               obtained from the previous

                                                                             response’s top-level seqUpdate

                                                                            field or from /api/v2/sequence_list

                                                                             endpoint. Important: Always use

                                                                             the top-level seqUpdate field for

                                                                                         iteration.


                   limit          integer                No        1000     Limit the amount of returned data           1000

                                                                               for this collection. Maximum

                                                                             allowed: 1000 for this collection.


                      q           string                 No          -      Search query. Can be used to filter id:cb08296b420fcce

                                                                              results or search for a specific    499ef84edb7ac3149

                                                                             entry by ID. Format: id: to search       70953a00

                                                                                 for one specific record.


       Query Parameter Details:


          · seqUpdate:

· Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 1000 for malware/cnc/updated collection

               · If not specified, defaults to 1000

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types (e.g., ip:8.8.8.8, domain:example.corp)


       Request Headers


                  Header                 Type                  Required                                  Description                             Example


                  Accept                string                    No                         Content type accepted by the client              application/json


               Authorization            string                   Yes                     Basic authentication credentials (see Initial             Basic

                                                                                                            Steps)                        base64(LOGIN:API_KEY)


                 User-Agent             string                    No                      User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                          (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                           useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                           Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                        e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                             Description                                          Example


                  Content-Type                                     Response content type                                 application/json


                Content-Encoding                                        Content encoding                                        gzip


                  Cache-Control                                    Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                         GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [CncItem], "seqUpdate": integer }


                 Field                   Type                            Required                                   Description


                 count                  integer                             Yes                 Number of C2 server items returned in this response


                 items              array[CncItem]                          Yes                              Array of C2 server objects


               seqUpdate                integer                             Yes                   Sequence update number at the top level of the

                                                                                                response. Always use this top-level value in the next

                                                                                              request’s seqUpdate parameter to get the next portion of

                                                                                                                       feeds


       CncItem Object


                 Field                   Type                            Required                                   Description


                  id                     string                             Yes                   Unique identifier of the C2 server (SHA-1 hash)


                  cnc                    string                             Yes                Command and control server identifier (domain or IP)


                domain                   string                             Yes                         Domain name (can be empty string)

Field             Type           Required                        Description


                    url              string           Yes                    URL (can be empty string)


                   ipv4        array[IPv4Object]      Yes                  Array of IPv4 address objects


                   ipv6        array[IPv6Object]      Yes                  Array of IPv6 address objects


               dateDetected          string           Yes      ISO 8601 timestamp when the C2 server was detected


               dateFirstSeen         string           Yes      ISO 8601 timestamp when the C2 server was first seen


               dateLastSeen          string           Yes      ISO 8601 timestamp when the C2 server was last seen


                seqUpdate           integer           Yes          Sequence update number for this specific item


                 platform            string           Yes              Platform string (can be empty string)


                    file          object | null       No                      File object (usually null)


               malwareList           array            Yes                    Array of malware objects


                threatActor    array[ThreatActorR     Yes                 Array of threat actor references

                                       ef]


       IPv4Object Object


                   Field             Type           Required                        Description


                    ip               string           Yes                          IPv4 address


               countryCode           string           Yes      Country code (ISO 3166-1 alpha-2, can be empty string)

Field                                Type                                Required                                                           Description


               countryName                              string                                 Yes                                       Country name (can be empty string)


                    city                                string                                 Yes                                            City name (can be empty string)


                  region                                string                                 Yes                                       Region name (can be empty string)


                 provider                               string                                 Yes                                    ISP/provider name (can be empty string)


                   asn                                  string                                 Yes                                           ASN number (can be empty string)


       ThreatActorRef Object


                   Field                                Type                                Required                                                           Description


                    id                                  string                                 Yes                               Unique identifier of the threat actor (SHA-1 hash)


                  name                                  string                                 Yes                                                 Name of the threat actor


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/malware/cnc/updated?seqUpdate=0&limit=1000' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Search Query
       curl -X GET 'https://tap.group-ib.com/api/v2/malware/cnc/updated?seqUpdate=0&limit=1000&q=id:cb08296b420fcce499ef84edb7ac314970953a00'
       \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 148783, "items": [               {      "cnc": "hint09.9966.org",        "dateDetected": "2013-05-31T20:00:00Z",                 "dateFirstSeen":
       "2013-05-31T20:00:00Z",                   "dateLastSeen": "2013-05-31T20:00:00Z",              "domain": "hint09.9966.org",           "file": null,        "id":
       "cb08296b420fcce499ef84edb7ac314970953a00",                           "ipv4": [],      "ipv6": [],   "malwareList": [],       "platform": "",            "seqUpdate": 13700304004,
       "threatActor": [          {          "id": "96054da361e4092a5a509862356f9f2541b86e9e",                          "name": "NetTraveler"               }       ],     "url": ""     },   {    "cnc":
       "82.113.19.75",          "dateDetected": "2014-08-06T20:00:00Z",                    "dateFirstSeen": "2014-08-06T20:00:00Z",                "dateLastSeen": "2014-08-06T20:00:00Z",
           "domain": "",        "file": null,       "id": "d67606f9fb3f81dbddbea74f3231613a742dc397",                    "ipv4": [       {          "asn": "",            "city": "",
       "countryCode": "",              "countryName": "",            "ip": "82.113.19.75",           "provider": "",      "region": ""         }      ],        "ipv6": [],     "malwareList": [],
       "platform": "",      "seqUpdate": 14073552002,                 "threatActor": [         {        "id": "03cf30aa129ecf2eba833773e10786b1558ac212",                                    "name":
       "Turla"      }      ],        "url": ""    } ], "seqUpdate": 14139216000 }

Malware - Config
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated malware configuration files from the Config submodule. These configs are collected from diverse malware files and
       incident investigations.

       Collection-Specific Information


                                                  Property                                                                  Value


                                                   Method                                                                    GET


                                                    Path                                                      /api/v2/malware/config/updated


                                                 Collection                                                            malware/config


                                              Collection Name                                                    Malware Configuration Files


                                                   Module                                                                  Malware


                                                 Submodule                                                                 Configs


                                                    Type                                                                  Individual


                                                 TTL (Days)                                                30 (recommended, not provided in API)


                                               Admiralty Code                                                                 A1


                                                  Severity                                                                    9


                                              Collection Limit                                                     100 records per request


                                                 Rate Limit                                          1 request per 10 seconds per company per feed (see

                                                                                                                       API Limitations)


                                                 IOC Types                                                       none - only data for analysis

Property                                                    Value


                                         Short Description                        Extracted configuration files from malware samples.


       Request

       Request URL
        GET /api/v2/malware/config/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                     Example


                   seqUpdate         integer                No         0        Sequence update number to get          17270645076338

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        100      Limit the amount of returned data            100

                                                                                  for this collection. Maximum

                                                                                allowed: 100 for this collection.


                       q             string                 No          -      Search query. Can be used to filter id:9f61d4e05e77994

                                                                                 results or search for a specific     724f7e29bc0fb810b

                                                                                entry by ID. Format: id: to search        26c2bb3c

                                                                                    for one specific record.


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1          1

                                                                                           to enable.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 100 for malware/config/updated collection

                · If not specified, defaults to 100

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific entry: q=id:

                · Supports various search types


       Request Headers


                  Header                  Type                  Required                               Description                             Example


                   Accept                 string                   No                      Content type accepted by the client              application/json


                Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                          Steps)                        base64(LOGIN:API_KEY)


                 User-Agent               string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                             Description                                         Example


                  Content-Type                                     Response content type                                 application/json


                Content-Encoding                                      Content encoding                                          gzip


                  Cache-Control                                    Cache control directives                              no-cache, private


                         Allow                                     Allowed HTTP methods                                         GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [ConfigItem], "seqUpdate": integer }


                 Field                   Type                              Required                                 Description


                 count                  integer                              Yes                  Number of config items returned in this response


                 items             array[ConfigItem]                         Yes                              Array of config objects


               seqUpdate                integer                              Yes                  Sequence update number at the top level of the

                                                                                                response. Always use this top-level value in the next

                                                                                              request’s seqUpdate parameter to get the next portion of

                                                                                                                       feeds


       ConfigItem Object


                 Field                   Type                              Required                                 Description


                   id                    string                              Yes                    Unique identifier of the config (SHA-1 hash)


                 hash                    string                              Yes                            Hash of the config (SHA-1)


               malwareId                 string                              Yes              Unique identifier of the associated malware (SHA-1 hash)

Field            Type           Required                    Description


                 malware         MalwareRef          Yes                Malware reference object


               dateFirstSeen        string           Yes       Date when the config was first seen (format:

                                                                             YYYY-MM-DD)


               dateLastSeen         string           Yes       Date when the config was last seen (format:

                                                                             YYYY-MM-DD)


                 seqUpdate         integer           Yes      Sequence update number for this specific item


                  content           string           Yes          Config content (can be empty string)


                contentLen         integer           Yes              Length of the config content


               configSummary     string | null       No                  Summary of the config


                    file       array[FileObject]     Yes                   Array of file objects


                domainList          array            Yes                 Array of domain objects


                   ipList           array            Yes               Array of IP address objects


       MalwareRef Object


                   Field            Type           Required                    Description


                     id             string           Yes      Unique identifier of the malware (SHA-1 hash)


                   name             string           Yes                  Name of the malware


       FileObject Object

Field                       Type                               Required                                          Description


                     name                        string                               Yes                                              File name


                     sha1                        string                               Yes                                        SHA-1 hash of the file


                    sha256                  string | null                             No                                       SHA-256 hash of the file


                      md5                   string | null                             No                                         MD5 hash of the file


                  timestamp                      string                               Yes                            ISO 8601 timestamp when the file was seen


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/malware/config/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Search Query
       curl -X GET
       'https://tap.group-ib.com/api/v2/malware/config/updated?seqUpdate=0&limit=100&q=id:9f61d4e05e77994724f7e29bc0fb810b26c2bb3c' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/malware/config/updated?seqUpdate=0&limit=100&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H
       'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 1411, "items": [ {            "configSummary": null,      "content": "",     "contentLen": 0,   "dateFirstSeen": "2024-09-23",   "dateLastSeen":
       "2024-09-23",         "domainList": [],     "file": [   {    "md5": null,            "name":
       "2e432426a7a0a10a0068c035368f749c298e1ef1add61e31a8b25da74676fcaa.exe",                                "sha1": "3fff365af65a3d3312c222acfe0a4d7447d0e78d",
               "sha256": null,      "timestamp": "2024-09-23T00:00:00+03:00"                }   ],    "hash": "5d6ba0fd685e89e3d03e4a63de67dfaec3c5fc17",        "id":
       "5d6ba0fd685e89e3d03e4a63de67dfaec3c5fc17",                  "ipList": [],     "malware": {      "id": "e3ad9c65499117cc68bbf3ee9e39bd93ce815547",
       "name": "AsyncRAT"           },    "malwareId": "e3ad9c65499117cc68bbf3ee9e39bd93ce815547",                 "seqUpdate": 17270645076338       } ], "seqUpdate":
       17270743540724 }

Malware - Reports
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated malware reports from the Malware collection. The Malware collection contains detailed information about specific
       malware detected through analyzing Threat Actors activity. Can contain malware names, desciption, related attacker names and additionally
       legitimate tools used by attackers during an attack.


       Note: This endpoint includes IOCs, which are also part of the IOC Primary collection.

       Collection-Specific Information


                                                  Property                                                                  Value


                                                   Method                                                                    GET


                                                    Path                                                     /api/v2/malware/malware/updated


                                                 Collection                                                           malware/malware


                                              Collection Name                                                          Malware Reports


                                                   Module                                                                  Malware


                                                 Submodule                                                                 Reports


                                                    Type                                                                  Common


                                                 TTL (Days)                                                       None (not provided in API)


                                               Admiralty Code                                                               None


                                                  Severity                                                                    9


                                              Collection Limit                                                     100 records per request


                                                 Rate Limit                                          1 request per 10 seconds per company per feed (see

                                                                                                                       API Limitations)

Property                                                    Value


                                            IOC Types                              Domain, IPv4, URL, File (MD5, SHA1, SHA256)


                                      Short Description                        Detailed information about specific malware detected

                                                                                      through analyzing Threat Actors activity.


       Request

       Request URL
        GET /api/v2/malware/malware/updated
       Query Parameters


                 Parameter        Type                  Required   Default              Description                    Example


                 seqUpdate        integer                 No         0        Sequence update number to get         16904733083037

                                                                               the next data chunk. Use this

                                                                                parameter to iterate through

                                                                                 feeds. The value should be

                                                                                obtained from the previous

                                                                              response’s top-level seqUpdate

                                                                             field or from /api/v2/sequence_list

                                                                              endpoint. Important: Always use

                                                                              the top-level seqUpdate field for

                                                                                          iteration.


                   limit          integer                 No        100      Limit the amount of returned data            100

                                                                                for this collection. Maximum

                                                                              allowed: 100 for this collection.


                      q           string                  No          -      Search query. Can be used to filter id:653654fb986b47a

                                                                               results or search for a specific    31c73d92f4a20a273

                                                                              entry by ID. Format: id: to search       acd2f779

                                                                                  for one specific record.


       Query Parameter Details:

· seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 100 for malware/malware/updated collection

               · If not specified, defaults to 100

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                  Required                               Description                             Example


                  Accept                 string                   No                      Content type accepted by the client              application/json


               Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                         Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                        Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                           Description                                           Example


                  Content-Type                                    Response content type                                 application/json


                Content-Encoding                                     Content encoding                                          gzip


                 Cache-Control                                    Cache control directives                              no-cache, private


                         Allow                                    Allowed HTTP methods                                         GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [MalwareItem], "seqUpdate": integer }


                 Field                   Type                          Required                                    Description


                 count                  integer                             Yes                Number of malware items returned in this response


                 items             array[MalwareItem]                       Yes                             Array of malware objects


               seqUpdate                integer                             Yes                  Sequence update number at the top level of the

                                                                                               response. Always use this top-level value in the next

                                                                                             request’s seqUpdate parameter to get the next portion of

                                                                                                                      feeds


       MalwareItem Object


                 Field                   Type                          Required                                    Description


                  id                     string                             Yes                   Unique identifier of the malware (SHA-1 hash)


                 name                    string                             Yes                               Name of the malware


                aliases               array[string]                         Yes                Array of alternative names/aliases for the malware

Field               Type           Required                           Description


                 description            string           Yes      Description of the malware (can be “Sorry, no description

                                                                                             yet.”)


               shortDescription      string | null       No                    Short description of the malware


                  category           array[string]       Yes           Array of category strings (e.g., [“atm-malware”],

                                                                     [“Downloader”], [“Remote Access Trojan”, “Rootkit”,

                                                                                           “Trojan”])


                    class            string | null       No                             Malware class


                  platform           array[string]       Yes      Array of platform strings (e.g., [“atm”, “Windows”, “Linux”],

                                                                                         [“Windows”])


                 threatLevel            string           Yes                 Threat level (e.g., “High”, “Medium”)


                 isPublished           boolean           Yes                  Whether the malware is published


                    langs            array[string]       Yes                       Array of language codes


                 seqUpdate             integer           Yes           Sequence update number for this specific item


                 sequenceId            integer           Yes                             Sequence ID


                 updatedAt              string           Yes       ISO 8601 timestamp when the record was last updated


                 geoRegion           array[string]       Yes      Array of geographic regions where the malware is active


               sourceCountry         array[string]       Yes         Array of source country codes (ISO 3166-1 alpha-2)


                    taList        array[ThreatActorR     Yes                   Array of threat actor references

                                          ef]


               threatActorList          array            Yes                     Array of threat actor objects

Field              Type          Required                      Description


                linkedMalware     array[MalwareRef]     Yes             Array of linked malware references


               malwareAliasList         array           Yes                  Array of malware aliases


                  fileIocList           array           Yes                Array of file indicator objects


                 fileIocIdList          array           Yes                  Array of file indicator IDs


                networkIocList          array           Yes             Array of network indicator objects


               networkIocIdList         array           Yes               Array of network indicator IDs


                deletedIocList       array | null       No                  Array of deleted indicators


                 attachedFile           array           Yes                Array of attached file objects


                 mitreMatrix            array           Yes           Array of MITRE ATT&CK matrix objects


                signatureIdList         array           Yes                   Array of signature IDs


                  yaraIdList            array           Yes                   Array of YARA rule IDs


                  portalLink         string | null      No               Portal link to the malware profile


       ThreatActorRef Object


                     Field              Type          Required                      Description


                      id                string          Yes      Unique identifier of the threat actor (SHA-1 hash)


                    name                string          Yes                  Name of the threat actor


                      url               string          Yes      URL to threat actor profile (can be empty string)


       MalwareRef Object

Field                        Type                                     Required                                                      Description


                      id                          string                                       Yes                               Unique identifier of the linked malware (SHA-1 hash)


                    name                          string                                       Yes                                            Name of the linked malware


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/malware/malware/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Search Query
        curl -X GET
       'https://tap.group-ib.com/api/v2/malware/malware/updated?seqUpdate=0&limit=100&q=id:653654fb986b47a31c73d92f4a20a273acd2f779' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 36, "items": [ {            "aliases": [],       "attachedFile": [],        "category": ["atm-malware"],          "class": null,   "deletedIocList": null,
       "description": "Sorry, no description yet.",             "fileIocIdList": [],      "fileIocList": [],    "geoRegion": ["asia", "europe", "america:northern_america"],             "id":
       "d7fde57f6ed2051ffae9257ba6beefe0fc99192f",                        "isPublished": true,          "langs": ["ru", "en"],    "linkedMalware": [],       "malwareAliasList": [],
       "mitreMatrix": [],         "name": "FASTCash",           "networkIocIdList": [],         "networkIocList": [],       "platform": ["atm", "Windows", "Linux"],         "portalLink": null,
               "seqUpdate": 16904733083037,            "sequenceId": 16269766696153,                    "shortDescription": "This malware in turn intercepts fraudulent Lazarus
       cash withdrawal requests and sends fake approval responses, allowing the attackers to steal cash from ATMs.",                                     "signatureIdList": [],
       "sourceCountry": ["KP", "KR", "RU", "US"],           "taList": [        {       "id": "5e9f20fdcf5876b5772b3d09b432f4080711ac5f",                          "name": "Lazarus",
       "url": ""      }      ],    "threatActorList": [],       "threatLevel": "High",         "updatedAt": "2024-10-22T14:58:02+03:00",              "yaraIdList": []     } ], "seqUpdate":
       17020334285354 }

Malware - Suricata
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated malware signature data used to detect and mitigate cyber threats. Each signature includes details such as the
       malware name, severity level, signature ID (SID), rule content, and associated metadata. The signatures are categorized by class (e.g., Trojan activity)
       and can be used for network and endpoint monitoring. These signatures provide crucial information for identifying malicious activity, such as
       observing specific SSL/TLS certificates or DNS queries linked to known malware families like QBot and MageCart.

       Collection-Specific Information


                                                  Property                                                                       Value


                                                   Method                                                                        GET


                                                    Path                                                         /api/v2/malware/signature/updated


                                                 Collection                                                               malware/signature


                                              Collection Name                                                       Malware Signatures (Suricata)


                                                   Module                                                                      Malware


                                                 Submodule                                                               Signatures (Suricata)


                                                    Type                                                                       Common


                                                 TTL (Days)                                                           None (not provided in API)


                                               Admiralty Code                                                                    None


                                                  Severity                                                                         8


                                              Collection Limit                                                         5000 records per request


                                                 Rate Limit                                              1 request per 10 seconds per company per feed (see

                                                                                                                           API Limitations)

Property                                                   Value


                                      Short Description                      Malware signatures that can be used to enrich malware

                                                                                   security feeds, detect potentially confidential

                                                                               information and identify specific malware promptly.


       Request

       Request URL
        GET /api/v2/malware/signature/updated
       Query Parameters


                 Parameter        Type                 Required   Default              Description                      Example


                 seqUpdate        integer                No         0        Sequence update number to get         17285596516319

                                                                              the next data chunk. Use this

                                                                               parameter to iterate through

                                                                                feeds. The value should be

                                                                               obtained from the previous

                                                                             response’s top-level seqUpdate

                                                                            field or from /api/v2/sequence_list

                                                                             endpoint. Important: Always use

                                                                             the top-level seqUpdate field for

                                                                                         iteration.


                   limit          integer                No        5000     Limit the amount of returned data             5000

                                                                               for this collection. Maximum

                                                                             allowed: 5000 for this collection.


                      q           string                 No          -      Search query. Can be used to filter        id:137224

                                                                              results or search for a specific

                                                                             entry by ID. Format: id: to search

                                                                                 for one specific record.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 5000 for malware/signature/updated collection

                · If not specified, defaults to 5000

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific entry: q=id:

                · Supports various search types


       Request Headers


                  Header                  Type                  Required                               Description                             Example


                   Accept                string                    No                      Content type accepted by the client              application/json


                Authorization            string                   Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                          Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                    No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                           Description                                            Example


                  Content-Type                                     Response content type                                  application/json


                Content-Encoding                                      Content encoding                                           gzip


                  Cache-Control                                    Cache control directives                               no-cache, private


                         Allow                                     Allowed HTTP methods                                          GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [SignatureItem], "seqUpdate": integer }


                 Field                   Type                           Required                                    Description


                 count                  integer                               Yes               Number of signature items returned in this response


                 items             array[SignatureIte                         Yes                            Array of signature objects

                                           m]


               seqUpdate                integer                               Yes                 Sequence update number at the top level of the

                                                                                                response. Always use this top-level value in the next

                                                                                              request’s seqUpdate parameter to get the next portion of

                                                                                                                        feeds


       SignatureItem Object


                 Field                   Type                           Required                                    Description


                   id                   integer                               Yes                  Unique identifier of the signature (numeric ID)


                  sid                   integer                               Yes                 Signature ID (SID) - Suricata signature identifier


                 name                    string                               Yes                              Name of the signature

Field                   Type                            Required                                           Description


                  class                   string                             Yes                               Signature class (e.g., “trojan-activity”)


                 content                  string                             Yes                                     Raw Suricata rule content


                severity                 integer                             Yes                                Severity level (numeric, typically 1-5)


               seqUpdate                 integer                             Yes                           Sequence update number for this specific item


                createdAt                 string                             Yes                        ISO 8601 timestamp when the signature was created


                malware             array[MalwareRef]                        Yes                          Array of malware references associated with this

                                                                                                                              signature


                alertNum                 integer                             Yes                                      Alert number (typically 0)


               sourceName              string | null                         No                                    Source name for the signature


       MalwareRef Object


                  Field                   Type                            Required                                           Description


                   id                     string                             Yes                           Unique identifier of the malware (SHA-1 hash)


                 name                     string                             Yes                                       Name of the malware


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/malware/signature/updated?seqUpdate=0&limit=5000' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Search Query
        curl -X GET 'https://tap.group-ib.com/api/v2/malware/signature/updated?seqUpdate=0&limit=5000&q=id:137224' \ -u 'LOGIN:API_KEY' \ -H
       'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "items": [ { "alertHistory": [],     "alertNum": 0,   "class": "trojan-activity",   "content": "alert tls $EXTERNAL_NET any -> $HOME_NET any
       (msg:\"TROJAN Observed Malicious SSL/TLS Certificate (QakBot)\"; target:dest_ip; flow:established,to_client; tls_cert_subject; content:\"C=PT, ST=IO,
       L=Enbdyd Mpbuv, O=Pswouppu Vnc Inc., CN=ragouxvase.biz\"; depth:67; fast_pattern; isdataat:!1,relative;
       reference:url,twitter.com/Unit42_Intel/status/1585046057339207680; classtype:trojan-activity; sid:2039577; rev:2; metadata:attack_target
       Client_Endpoint, created_at 2022_10_26, deployment Perimeter, deprecation_reason Age, malware_family Qbot, signature_severity Major, updated_at
       2024_10_08, reviewed_at 2024_10_08, severity 3, ti_malware_id e323de16fc8162e02aad6683b0f48a0e4008cbae, ti_malware_name QBot, rule_origin

etpro;)",    "createdAt": "2024-10-10T06:31:01+00:00",     "id": 1294223,   "malware": [        {      "id":
       "e323de16fc8162e02aad6683b0f48a0e4008cbae",              "name": "QBot"      }      ],     "name": "TROJAN Observed Malicious SSL/TLS Certificate
       (QakBot)",     "seqUpdate": 17285596516319,      "severity": 3,   "sid": 2039577,        "sourceName": null    } ], "count": 347, "seqUpdate":
       17285721594209 }

Malware - Yara
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated YARA rule data used for detecting and identifying specific malware threats. Each YARA rule includes information
       such as the rule name, description, associated malware, severity level, and detection conditions (e.g., file hashes, strings, patterns). These rules aid in
       identifying malware families by scanning for particular characteristics within files or processes. This information is essential for enhancing malware
       detection and improving threat-hunting capabilities.

       Collection-Specific Information


                                                  Property                                                                         Value


                                                   Method                                                                           GET


                                                    Path                                                              /api/v2/malware/yara/updated


                                                  Collection                                                                   malware/yara


                                              Collection Name                                                                   YARA Rules


                                                   Module                                                                        Malware


                                                 Submodule                                                                       Yara rules


                                                    Type                                                                         Common


                                                 TTL (Days)                                                             None (not provided in API)


                                               Admiralty Code                                                                      None


                                                   Severity                                                                          8


                                               Collection Limit                                                          5000 records per request


                                                 Rate Limit                                               1 request per 10 seconds per company per feed (see

                                                                                                                              API Limitations)

Property                                                                       Value


                                              Short Description                                         YARA rules set by Group-IB and containing information

                                                                                                                   about specific malware families.


       Request

       Request URL
        GET /api/v2/malware/yara/updated
       Query Parameters


                     Parameter             Type                Required               Default                    Description                   Example


                     seqUpdate            integer                No                      0             Sequence update number to get        16753451595662

                                                                                                        the next data chunk. Use this

                                                                                                         parameter to iterate through

                                                                                                          feeds. The value should be

                                                                                                         obtained from the previous

                                                                                                       response’s top-level seqUpdate

                                                                                                     field or from /api/v2/sequence_list

                                                                                                       endpoint. Important: Always use

                                                                                                       the top-level seqUpdate field for

                                                                                                                   iteration.


                       limit              integer                No                    5000           Limit the amount of returned data          5000

                                                                                                         for this collection. Maximum

                                                                                                       allowed: 5000 for this collection.


       Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               ·

Maximum value: 5000 for malware/yara/updated collection

               · If not specified, defaults to 5000

               · The limit depends on the amount of data to not overload the JSON output


       Request Headers


                 Header                  Type                Required                                  Description                                 Example


                  Accept                string                  No                          Content type accepted by the client              application/json


               Authorization            string                  Yes                   Basic authentication credentials (see Initial                 Basic

                                                                                                          Steps)                         base64(LOGIN:API_KEY)


                User-Agent              string                  No                       User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).         roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                    PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                       e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                             Description                                                    Example


                     Content-Type                                     Response content type                                           application/json


                  Content-Encoding                                       Content encoding                                                   gzip


                    Cache-Control                                    Cache control directives                                         no-cache, private


                         Allow                                       Allowed HTTP methods                                                   GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [YaraItem], "seqUpdate": integer }

Field           Type          Required                         Description


                 count           integer          Yes       Number of YARA rule items returned in this response


                 items       array[YaraItem]      Yes                     Array of YARA rule objects


               seqUpdate         integer          Yes          Sequence update number at the top level of the

                                                             response. Always use this top-level value in the next

                                                           request’s seqUpdate parameter to get the next portion of

                                                                                    feeds


       YaraItem Object


                  Field           Type          Required                         Description


                   id            integer          Yes           Unique identifier of the YARA rule (numeric ID)


                 name             string          Yes                      Name of the YARA rule


                  class           string          Yes                  Rule class (can be empty string)


                 content          string          Yes                      Raw YARA rule content


               seqUpdate         integer          Yes          Sequence update number for this specific item


                createdAt         string          Yes          ISO 8601 timestamp when the rule was created


                malware     array[MalwareRef]     Yes       Array of malware references associated with this rule


                alertNum         integer          Yes                     Alert number (typically 0)


               sourceName      string | null      No              Source name for the rule (e.g., “polygon”)


       MalwareRef Object

Field                      Type                             Required                                            Description


                   id                        string                             Yes                           Unique identifier of the malware (SHA-1 hash)


                 name                        string                             Yes                                         Name of the malware


       Example Request

       Basic Request
        curl -X GET 'https://tap.group-ib.com/api/v2/malware/yara/updated?seqUpdate=0&limit=5000' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "items": [ { "alertNum": 0,          "class": "",    "content": "import \"hash\"\n\nrule ccleaner\n{\n meta:\n        description = \"Infected
       CCleaner\"\n       severity = 300\n      enabled = 1\n        ti_malware_id = \"dbbb8f0188cff98f30908263bfa8e667a2bbc026\"\n              ti_malware_name =
       \"404Keylogger\"\n\n condition:\n              hash.md5 ( 0 , filesize ) == \"75735db7291a19329190757437bdb847\" or hash.md5 ( 0 , filesize ) ==
       \"ef694b89ad7addb9a16bb6f26f1efaf7\" or hash.md5 ( 0 , filesize ) == \"a3d00b7362db6df0fcc49b6ab17b3cf0\" or hash.md5 ( 0 , filesize ) ==
       \"d488e4b61c233293bec2ee09553d3a2f\"\n}\n",                "createdAt": "2020-09-30T11:03:52+00:00",    "id": 9,    "malware": [      {      "id":
       "dbbb8f0188cff98f30908263bfa8e667a2bbc026",                   "name": "404Keylogger"     }    ],   "name": "ccleaner",      "seqUpdate": 16753451595662,
          "sourceName": "polygon"    } ], "count": 10000, "seqUpdate": 16753451601281 }

Malware - Vulnerability
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on software vulnerabilities, categorized by vendor and product (e.g., Microsoft Windows, Apache HTTP
       Server). In addition to general vulnerabilities’ information, the subsection also contains data on existing exploits, with the option to view links to PoC
       (Proof-of-Concept), and additional information.

       Collection-Specific Information


                                                  Property                                                                         Value


                                                   Method                                                                           GET


                                                    Path                                                             /api/v2/osi/vulnerability/updated


                                                  Collection                                                                  osi/vulnerability


                                              Collection Name                                                                  Vulnerabilities


                                                   Module                                                                         Malware


                                                 Submodule                                                                     Vulnerabilities


                                                    Type                                                                         Common


                                                 TTL (Days)                                                       30 (recommended, not provided in API)


                                               Admiralty Code                                                                        A1


                                                   Severity                                                                           9


                                               Collection Limit                                                           200 records per request


                                                  Rate Limit                                               1 request per 10 seconds per company per feed (see

                                                                                                                              API Limitations)

Property                                                    Value


                                         Short Description                       Software vulnerabilities detected by version, including

                                                                                            exploit information and PoC links.


       Request

       Request URL
        GET /api/v2/osi/vulnerability/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                     Example


                   seqUpdate         integer                No         0        Sequence update number to get         15677944090287

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        200      Limit the amount of returned data            200

                                                                                  for this collection. Maximum

                                                                                allowed: 200 for this collection.


                       q             string                 No          -      Search query. Can be used to filter    “WPVDB-ID:7181”

                                                                                 results or search for a specific

                                                                                entry by ID. Format: “” to search

                                                                                    for one specific record.


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1          1

                                                                                           to enable.


       Query Parameter Details:

· seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 200 for osi/vulnerability/updated collection

               · If not specified, defaults to 200

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific vulnerability: q=""

               · Supports various search types


       Request Headers


                  Header                 Type                   Required                              Description                             Example


                  Accept                 string                   No                      Content type accepted by the client              application/json


               Authorization             string                   Yes                 Basic authentication credentials (see Initial             Basic

                                                                                                         Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                        Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                            Description                                            Example


                   Content-Type                                     Response content type                                  application/json


                Content-Encoding                                       Content encoding                                           gzip


                  Cache-Control                                     Cache control directives                     max-age=0, must-revalidate, private


                          Allow                                     Allowed HTTP methods                                          GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [VulnerabilityItem], "seqUpdate": integer }


                  Field                   Type                           Required                                     Description


                 count                   integer                            Yes                Number of vulnerability items returned in this response


                 items             array[VulnerabilityIt                    Yes                             Array of vulnerability objects

                                           em]


               seqUpdate                 integer                            Yes                    Sequence update number at the top level of the

                                                                                                 response. Always use this top-level value in the next

                                                                                               request’s seqUpdate parameter to get the next portion of

                                                                                                                         feeds


       VulnerabilityItem Object


                  Field                   Type                           Required                                     Description


                   id                     string                            Yes                       Unique identifier of the vulnerability (e.g.,

                                                                                                                  “WPVDB-ID:7181”)


                  title                   string                            Yes                                    Vulnerability title


               description                string                            Yes                                Vulnerability description

Field               Type           Required                         Description


                datePublished           string           Yes          ISO 8601 timestamp when the vulnerability was

                                                                                         published


                dateModified            string           Yes        ISO 8601 timestamp when the vulnerability was last

                                                                                          modified


                dateLastSeen            string           Yes      ISO 8601 timestamp when the vulnerability was last seen


                  seqUpdate            integer           Yes          Sequence update number for this specific item


                bulletinFamily          string           Yes                  Bulletin family (e.g., “software”)


                     type               string           Yes                Vulnerability type (e.g., “wpvulndb”)


                   reporter             string           Yes                          Reporter name


                   provider             string           Yes                           Provider name


                     href               string           Yes                  Link to the vulnerability details


                    cvss             CvssObject          Yes                        CVSS score object


               cvssAttackVector         string           Yes             CVSS attack vector (can be empty string)


                 mergedCvss            integer           Yes                        Merged CVSS score


                   cveList              array            Yes                      Array of CVE identifiers


                 cveListEpss            array            Yes                      Array of CVE EPSS data


                    epss             EpssObject          Yes          EPSS (Exploit Prediction Scoring System) object


               affectedSoftware   array[AffectedSoft     Yes                 Array of affected software objects

                                     wareObject]

Field            Type         Required                      Description


                    cpe             array          Yes                   Array of CPE identifiers


                 cpeTable           array          Yes                  Array of CPE table entries


                exploitCount       integer         Yes                 Number of available exploits


                 hasExploit        boolean         Yes                Whether exploits are available


                 exploitList        array          Yes                  Array of exploit references


                exploitation        array          Yes                  Array of exploitation data


               githubLinkList       array          Yes                     Array of GitHub links


                references          array          Yes                   Array of reference links


                 darkweb            array          Yes                Array of dark web references


                   twitter          array          Yes                 Array of Twitter references


                  threats           array          Yes                  Array of threat references


                threatsList         array          Yes                  Array of threat list entries


               softwareMixed        array          Yes                Array of mixed software data


               timeLineData         array          Yes                    Array of timeline data


               seenInTheWild       boolean         Yes      Whether the vulnerability has been seen in the wild


               extDescription       string         Yes         Extended description (can be empty string)


                 portalLink         string         Yes               Portal link (can be empty string)


               displayOptions   DisplayOptions     Yes                    Display options object


       CvssObject Object

Field                 Type     Required                  Description


                 score                 integer     Yes                     CVSS score


                 vector                 string     Yes                 CVSS vector string


       EpssObject Object


                  Field                 Type     Required                  Description


                  cve                   string     Yes        CVE identifier (can be empty string)


                  epss                 number      Yes                  EPSS score (0-1)


               percentile              number      Yes              EPSS percentile (0-100)


                  date                  string     Yes        ISO 8601 timestamp of EPSS data


       AffectedSoftwareObject Object


                  Field                 Type     Required                  Description


                 name                   string     Yes                   Software name


                version                 string     Yes                  Software version


                operator                string     Yes      Version operator (e.g., “lt” for less than)


       DisplayOptions Object


                  Field                 Type     Required                  Description


               isFavourite             boolean     Yes      Whether the item is marked as favourite


                isHidden               boolean     Yes            Whether the item is hidden

Field                       Type                                Required                                                  Description


         favouriteForCompanies                   array                                  Yes                              Array of company IDs that marked this as favourite


               hideForCompanies                  array                                  Yes                                     Array of company IDs that hid this item


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/osi/vulnerability/updated?seqUpdate=0&limit=200' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Hunting Rules
       curl -X GET 'https://tap.group-ib.com/api/v2/osi/vulnerability/updated?seqUpdate=0&limit=200&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H
       'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 454062, "items": [        {     "affectedSoftware": [         {          "name": "shrimptest",         "operator": "lt",       "version": "1.0b3"         }       ],
       "bulletinFamily": "software",       "cpe": [],    "cpeTable": [],     "cveList": [],      "cveListEpss": [],      "cvss": {     "score": 0,        "vector": "NONE"           },
       "cvssAttackVector": "",        "darkweb": [],     "dateLastSeen": "2018-09-17T17:26:04+01:00",                 "dateModified": "2015-05-14T22:00:00+01:00",
       "datePublished": "2014-07-31T21:00:00+01:00",              "description": "WordPress Vulnerability - ShrimpTest 1.0b2 - plugins/plugin-notification.php
       Unspecified XSS\n",        "displayOptions": {        "favouriteForCompanies": [],              "hideForCompanies": [],         "isFavourite": false,        "isHidden": false
          },     "epss": {   "cve": "",      "date": "0001-01-01T00:00:00Z",              "epss": 0,        "percentile": 0    },    "exploitCount": 0,        "exploitList": [],
       "exploitation": [],   "extDescription": "",       "githubLinkList": [],       "hasExploit": false,      "href": "https://wpvulndb.com/vulnerabilities/7181",                 "id":
       "WPVDB-ID:7181",        "lastseen": "2018-09-17T17:26:04+01:00",                "mergedCvss": 0,         "modified": "2015-05-14T22:00:00+01:00",              "portalLink": "",
         "provider": "vulners.com",       "published": "2014-07-31T21:00:00+01:00",               "references": [],     "reporter": "wpvulndb",       "seenInTheWild": false,
       "seqUpdate": 15677944090287,              "softwareMixed": [],      "threats": [],      "threatsList": [],     "timeLineData": [],     "title": "ShrimpTest 1.0b2 -
       plugins/plugin-notification.php Unspecified XSS",            "twitter": [],     "type": "wpvulndb"       } ], "seqUpdate": 15677944270178 }

Malware - Phishing Kit
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on phishing kits. A Phishing kit is a collection of pages, scripts, and images that keep a phishing website
       up and running. In other words, it is a ready-made phishing website with a relevant settings file that specifies the parameters of how the page needs to
       be displayed.

       Collection-Specific Information


                                                  Property                                                                      Value


                                                   Method                                                                        GET


                                                    Path                                                        /api/v2/attacks/phishing_kit/updated


                                                 Collection                                                              attacks/phishing_kit


                                              Collection Name                                                               Phishing Kits


                                                   Module                                                                      Malware


                                                 Submodule                                                                  Phishing Kits


                                                    Type                                                                      Common


                                                 TTL (Days)                                                    30 (recommended, not provided in API)


                                               Admiralty Code                                                                 Mostly B2


                                                  Severity                                                                        9


                                              Collection Limit                                                        1000 records per request


                                                 Rate Limit                                             1 request per 10 seconds per company per feed (see

                                                                                                                           API Limitations)


                                                 IOC Types                                                           none - only data for analysis

Property                                                    Value


                                         Short Description                        Collection of pages, scripts, and images that keep a

                                                                                            phishing website up and running.


       Request

       Request URL
        GET /api/v2/attacks/phishing_kit/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                     Example


                   seqUpdate         integer                No         0        Sequence update number to get          1523520752839

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        1000     Limit the amount of returned data            1000

                                                                                  for this collection. Maximum

                                                                                allowed: 1000 for this collection.


                       q             string                 No          -      Search query. Can be used to filter id:5cf5afc22dfa0825

                                                                                 results or search for a specific     2e990c9e3fc51e287

                                                                                entry by ID. Format: id: to search    ff54dc53742767a74

                                                                                    for one specific record.           28dc31b25dd606


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1            1

                                                                                           to enable.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 1000 for attacks/phishing_kit/updated collection

                · If not specified, defaults to 1000

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific entry: q=id:

                · Supports various search types


       Request Headers


                  Header                  Type                  Required                               Description                             Example


                   Accept                string                    No                      Content type accepted by the client              application/json


                Authorization            string                   Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                          Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                    No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                            Description                                                Example


                  Content-Type                                      Response content type                                      application/json


                Content-Encoding                                       Content encoding                                               gzip


                  Cache-Control                                     Cache control directives                          max-age=0, must-revalidate, private


                         Allow                                      Allowed HTTP methods                                              GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [PhishingKitItem], "seqUpdate": integer, "settings": object }


                 Field                    Type                           Required                                         Description


                 count                   integer                            Yes                      Number of phishing kit items returned in this response


                 items             array[PhishingKitIte                     Yes                                   Array of phishing kit objects

                                           m]


               seqUpdate                 integer                            Yes                         Sequence update number at the top level of the

                                                                                                      response. Always use this top-level value in the next

                                                                                                    request’s seqUpdate parameter to get the next portion of

                                                                                                                             feeds


                settings                 object                             Yes                      Search settings object (contains search configuration)


       PhishingKitItem Object


                 Field                    Type                           Required                                         Description


                   id                     string                            Yes                       Unique identifier of the phishing kit (SHA-256 hash)


                 hash                     string                            Yes                               Hash of the phishing kit (SHA-256)

Field              Type          Required                         Description


                 seqUpdate           integer           Yes          Sequence update number for this specific item


                dateDetected          string           Yes      ISO 8601 timestamp when the phishing kit was detected


                dateFirstSeen         string           Yes      ISO 8601 timestamp when the phishing kit was first seen


                dateLastSeen          string           Yes      ISO 8601 timestamp when the phishing kit was last seen


                    login             string           Yes            Login/user who uploaded or detected the kit


                    path              string           Yes             API path to download the phishing kit file


                   source          array[string]       Yes                    Array of source identifiers


               downloadedFrom   array[DownloadSou      Yes                 Array of download source objects

                                       rce]


                   emails              array           Yes                     Array of email addresses


                 targetBrand           array           Yes                   Array of target brand names


                 telegramIds        array | null       No                       Array of Telegram IDs


                  variables      array[Variable] |     No        Array of variable objects (database credentials, URLs,

                                       null                                              etc.)


                 threatActors       array | null       No                    Array of threat actor objects


                  evaluation       Evaluation          Yes          Evaluation object containing threat assessment


                 isFavourite         boolean           Yes              Whether the item is marked as favourite


                  isHidden           boolean           Yes                    Whether the item is hidden

DownloadSource Object


                   Field          Type         Required                         Description


                   date           string         Yes        ISO 8601 timestamp when the kit was downloaded


                     url          string         Yes             URL from which the kit was downloaded


                phishingUrl       string         Yes               Phishing URL (can be empty string)


                  domain          string         Yes                           Domain name


                 fileName         string         Yes                 File name (can be empty string)


       Variable Object


                   Field          Type         Required                         Description


                    type          string         Yes            Type of variable (e.g., “DB”, “LOG”, “CURL”)


                  filePath        string         Yes               File path where the variable is found


                  values       array[string]     Yes      Array of variable values (may contain masked sensitive

                                                                                    data)


       Evaluation Object


                   Field          Type         Required                         Description


               admiraltyCode      string         Yes                    Admiralty Code (e.g., “B2”)


                 credibility     integer         Yes                     Credibility score (0-100)


                 reliability     integer         Yes                     Reliability score (0-100)


                  severity        string         Yes                Severity level (e.g., “orange”, “red”)

Field                            Type                                 Required                                                     Description


                      tlp                             string                                 Yes                           Traffic Light Protocol level (e.g., “amber”, “red”, “green”,

                                                                                                                                                         “white”)


                      ttl                             integer                                Yes                                                  Time to live in days


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/attacks/phishing_kit/updated?seqUpdate=0&limit=1000' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/attacks/phishing_kit/updated?seqUpdate=0&limit=1000&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \
       -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 122834, "items": [             {      "id": "5cf5afc22dfa08252e990c9e3fc51e287ff54dc53742767a7428dc31b25dd606",                               "hash":
       "5cf5afc22dfa08252e990c9e3fc51e287ff54dc53742767a7428dc31b25dd606",                                      "seqUpdate": 1523520752839,              "dateDetected":
       "2018-03-09T22:19:59+00:00",                   "dateFirstSeen": "2018-03-09T22:19:59+00:00",              "dateLastSeen": "2018-03-27T13:18:38+00:00",
       "downloadedFrom": [               {        "date": "2018-03-09T22:19:59+03:00",                "url": "https://gt-mywyty186338.codeanyapp.com/cb.zip",
       "phishingUrl": "",            "domain": "gt-mywyty186338.codeanyapp.com",                      "fileName": ""       }    ],      "emails": [],     "login": "PhishingKitFetcher",
       "path":
       "https://tap.group-ib.com/api/v2/malware/phishing_kit/5cf5afc22dfa08252e990c9e3fc51e287ff54dc53742767a7428dc31b25dd606/file/5cf5afc22d
       fa08252e990c9e3fc51e287ff54dc53742767a7428dc31b25dd606",                                 "source": ["ci-PhishKit"],     "targetBrand": [],         "telegramIds": null,
       "variables": [          {        "type": "DB",           "filePath": "./cb/pages/jsp-ns/cargando.php",             "values": [          "host: $mysql_host",              "login:
       ***********",               "password: ***************"            ]     }    ],     "threatActors": null,      "evaluation": {        "admiraltyCode": "B2",          "credibility":
       80,       "reliability": 70,          "severity": "orange",       "tlp": "amber",       "ttl": 30   },     "isFavourite": false,       "isHidden": false       } ], "settings": {
       "search": {          "fields": ["company", "domain", "has_connection_vars", "target_brand"],                 "tags": ["203051", "options", "target_brand"]          } }, "seqUpdate":
       1523520767270 }

Darkweb - Discord
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information from Discord channels and servers. Similar to Telegram, the Threat Intelligence system analyzes Discord
       channels and servers. Here records can contain bank/personal credentials, media, files, links, ip-addresses and domains of the companies that can be
       targeted in the nearest future, or were already attacked and it was discussed in the specific channel/server.

       Collection-Specific Information


                                                  Property                                                                        Value


                                                   Method                                                                          GET


                                                    Path                                                       /api/v2/compromised/discord/updated


                                                 Collection                                                               compromised/discord


                                              Collection Name                                                     Compromised Discord Messages


                                                   Module                                                                       Darkweb


                                                 Submodule                                                             Instant messengers (Discord)


                                                    Type                                                                        Individual


                                                 TTL (Days)                                                             None (not provided in API)


                                               Admiralty Code                                                                     None


                                                  Severity                                                                         N/A


                                              Collection Limit                                                           100 records per request


                                                 Rate Limit                                             1 request per 10 seconds per company per feed (see

                                                                                                                             API Limitations)


                                              Short Description                                            Information from Discord channels and servers.

Request

       Request URL
        GET /api/v2/compromised/discord/updated
       Query Parameters


                     Parameter             Type             Required                  Default                    Description                    Example


                     seqUpdate            integer              No                        0             Sequence update number to get        1729505868852513

                                                                                                        the next data chunk. Use this

                                                                                                         parameter to iterate through

                                                                                                         feeds. The value should be

                                                                                                         obtained from the previous

                                                                                                       response’s top-level seqUpdate

                                                                                                     field or from /api/v2/sequence_list

                                                                                                       endpoint. Important: Always use

                                                                                                       the top-level seqUpdate field for

                                                                                                                   iteration.


                       limit              integer              No                      100            Limit the amount of returned data           100

                                                                                                        for this collection. Maximum

                                                                                                       allowed: 100 for this collection.


                        q                 string               No                        -            Search query. Can be used to filter   id:7901bb2b140073

                                                                                                        results or search for a specific    4126168ab9bacc28

                                                                                                       entry by ID. Format: id: to search          bc

                                                                                                           for one specific record.


       Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               ·

Maximum value: 100 for compromised/discord/updated collection

               · If not specified, defaults to 100

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                Required                                  Description                               Example


                  Accept                 string                 No                         Content type accepted by the client              application/json


               Authorization             string                 Yes                  Basic authentication credentials (see Initial                Basic

                                                                                                         Steps)                         base64(LOGIN:API_KEY)


                 User-Agent              string                 No                       User-Agent string with product metadata       SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                    PlatformType/PlatformName_PlatformVersio

                                                                                    n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                             Description                                                  Example


                     Content-Type                                     Response content type                                          application/json


                   Content-Encoding                                     Content encoding                                                  gzip

Header                                                   Description                                                   Example


                  Cache-Control                                          Cache control directives                             max-age=0, must-revalidate, private


                         Allow                                           Allowed HTTP methods                                                 GET


       Response Body Schema


       The response structure is similar to compromised/messenger/updated, containing Discord messages with similar fields including message content,
       author information, channel statistics, and metadata.

       Root Object
       { "count": integer, "items": [DiscordItem], "seqUpdate": integer, "settings": array }


                 Field                      Type                              Required                                             Description


                 count                      integer                             Yes                            Number of Discord items returned in this response


                 items                array[DiscordItem]                        Yes                                    Array of Discord message objects


               seqUpdate                    integer                             Yes                             Sequence update number at the top level of the

                                                                                                              response. Always use this top-level value in the next

                                                                                                            request’s seqUpdate parameter to get the next portion of

                                                                                                                                     feeds


                settings                    array                               Yes                                      Settings array (usually empty)


       DiscordItem Object


       The structure is similar to MessengerItem from compromised/messenger/updated, containing message content, author information, channel/server
       statistics, and metadata specific to Discord.

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/discord/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

       Success Response (200 OK)


       The response structure is similar to compromised/messenger/updated, with items containing Discord messages.
        { "count": 5000, "items": [     {   "id": "example_id_hash",       "message": "Example Discord message content",          "messageId": 123456,
       "messageTs": "2024-10-16T05:19:02+03:00",           "author": {      "id": 123456789,        "userName": "example_user",      "type": "user"    },
       "seqUpdate": 1729505868852513          } ], "settings": [], "seqUpdate": 1729506374088157 }

Darkweb - Telegram
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information from Telegram chats and channels. Here records can contain bank/personal credentials, media, files,
       links, ip-addresses and domains of the companies that can be targeted in the nearest future, or were already attacked and it was discussed in the
       specific chat/channel.

       Collection-Specific Information


                                                  Property                                                                    Value


                                                   Method                                                                      GET


                                                    Path                                                   /api/v2/compromised/messenger/updated


                                                 Collection                                                         compromised/messenger


                                              Collection Name                                                          Telegram Messages


                                                   Module                                                                    Darkweb


                                                 Submodule                                                       Instant messengers (Telegram)


                                                    Type                                                                    Individual


                                                 TTL (Days)                                                         None (not provided in API)


                                               Admiralty Code                                                                 None


                                                  Severity                                                                     N/A


                                              Collection Limit                                                       100 records per request


                                                 Rate Limit                                            1 request per 10 seconds per company per feed (see

                                                                                                                         API Limitations)


                                              Short Description                                          Information from Telegram chats and channels.

Request

       Request URL
        GET /api/v2/compromised/messenger/updated
       Query Parameters


                     Parameter             Type             Required                  Default                    Description                    Example


                     seqUpdate            integer              No                        0             Sequence update number to get        1729505868852513

                                                                                                        the next data chunk. Use this

                                                                                                         parameter to iterate through

                                                                                                         feeds. The value should be

                                                                                                         obtained from the previous

                                                                                                       response’s top-level seqUpdate

                                                                                                     field or from /api/v2/sequence_list

                                                                                                       endpoint. Important: Always use

                                                                                                       the top-level seqUpdate field for

                                                                                                                   iteration.


                       limit              integer              No                      100            Limit the amount of returned data           100

                                                                                                        for this collection. Maximum

                                                                                                       allowed: 100 for this collection.


                        q                 string               No                        -            Search query. Can be used to filter   id:7901bb2b140073

                                                                                                        results or search for a specific    4126168ab9bacc28

                                                                                                       entry by ID. Format: id: to search          bc

                                                                                                           for one specific record.


       Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               ·

Maximum value: 100 for compromised/messenger/updated collection

               · If not specified, defaults to 100

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                Required                                  Description                               Example


                  Accept                 string                 No                         Content type accepted by the client              application/json


               Authorization             string                 Yes                  Basic authentication credentials (see Initial                Basic

                                                                                                         Steps)                         base64(LOGIN:API_KEY)


                 User-Agent              string                 No                       User-Agent string with product metadata       SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                    PlatformType/PlatformName_PlatformVersio

                                                                                    n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                             Description                                                  Example


                     Content-Type                                     Response content type                                          application/json


                   Content-Encoding                                     Content encoding                                                  gzip

Header                                           Description                                              Example


                  Cache-Control                                    Cache control directives                        max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                            GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [MessengerItem], "seqUpdate": integer, "settings": array }


                 Field                   Type                           Required                                       Description


                 count                  integer                           Yes                     Number of messenger items returned in this response


                 items            array[MessengerIte                      Yes                             Array of messenger message objects

                                          m]


               seqUpdate                integer                           Yes                        Sequence update number at the top level of the

                                                                                                   response. Always use this top-level value in the next

                                                                                                 request’s seqUpdate parameter to get the next portion of

                                                                                                                          feeds


                settings                 array                            Yes                                 Settings array (usually empty)


       MessengerItem Object


                 Field                   Type                           Required                                       Description


                   id                    string                           Yes                         Unique identifier of the message (SHA-1 hash)


               message                   string                           Yes                                       Message content


               messageId                integer                           Yes                                     Telegram message ID


               messageTs                 string                           Yes                       ISO 8601 timestamp when the message was sent

Field               Type            Required                        Description


                   lastEditTs            string            Yes      ISO 8601 timestamp when the message was last edited


                    isReply             boolean            Yes                 Whether this is a reply message


                repliedMessage        object | null        No                      Replied message object


                     name                string            Yes                       Chat/channel name


               translatedMessage         string            Yes            Translated message (can be empty string)


                  seqUpdate             integer            Yes          Sequence update number for this specific item


                    author           AuthorObject          Yes                          Author object


                   chatStat         ChatStatObject         Yes                      Chat statistics object


                   highlight          object | null        No                          Highlight object


                   selected             boolean            Yes                Whether the message is selected


                     edits         array[EditObject] |     No                       Array of edit objects

                                          null


                    deleted              string            Yes            Deletion information (can be empty string)


                    media            MediaObject           Yes                          Media object


       AuthorObject Object


                     Field               Type            Required                        Description


                       id               integer            Yes                         Author user ID


                  userName               string            Yes             Author username (can be empty string)

Field               Type           Required                  Description


                    avatar           object | null       No                     Avatar object


                     type               string           Yes           Author type (e.g., “user”, “bot”)


                  firstName             string           Yes          First name (can be empty string)


                  lastName              string           Yes          Last name (can be empty string)


       ChatStatObject Object


                    Field               Type           Required                  Description


                      id               integer           Yes                  Chat/channel ID


                    name                string           Yes                Chat/channel name


                     title              string           Yes                 Chat/channel title


                     type               string           Yes      Chat type (e.g., “supergroup”, “channel”)


                    about         array[AboutObject]     Yes               Array of about objects


                    avatar          AvatarObject         Yes                    Avatar object


               firstMessageDate         string           Yes      ISO 8601 timestamp of the first message


               lastMessageDate          string           Yes      ISO 8601 timestamp of the last message


                messageNum             integer           Yes            Total number of messages


                  userNum              integer           Yes                  Number of users


       AboutObject Object

Field            Type         Required                    Description


                   value           string          Yes                     About text value


               detected_date       string          Yes            Date when the about was detected


       AvatarObject Object


                   Field            Type         Required                    Description


                    id          integer | null     No                          Avatar ID


                  sha256           string          Yes                SHA-256 hash of the avatar


               detected_date       string          Yes            Date when the avatar was detected


       EditObject Object


                   Field            Type         Required                    Description


                 message           string          Yes                 Edited message content


               detected_date       string          Yes             Date when the edit was detected


           message_translated      string          Yes      Translated edited message (can be empty string)


       MediaObject Object


                   Field            Type         Required                    Description


                  name             string          Yes           Media file name (can be empty string)


                   type            string          Yes             Media type (can be empty string)


                   size            integer         Yes                  Media file size in bytes


       Example Request

Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/messenger/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

       Success Response (200 OK)
        { "items": [ { "id": "49d0aedd8eecac841b05357108d49613",                               "message": "Card -> 5555555555555557|06|29|420\n\nBIN-> 555555\nBrand->
       MASTERCARD\nType-> DEBIT\nLevel-> PREPAID\nBank-> CIAGROUP\nPhone-> ------\nFlag-> BR\nCurrency-> BRL\nCountry-> BRAZIL (BR)",
       "messageId": 2351042,             "isReply": false,      "repliedMessage": null,           "messageTs": "2024-10-16T05:19:02+03:00",             "lastEditTs":
       "0001-01-01T00:00:00Z",                "name": "RevyDrops",         "translatedMessage": "",         "chatStat": {      "id": -1001692680982,           "name": "RevyDrops",
       "title": "Revy Drops",          "about": [        {       "value": "",            "detected_date": "2024-08-15 15:12:48"            }      ],        "type": "supergroup",
       "avatar": {       "id": null,           "sha256": "1494923bf27455a3fd3f36f18b158fe1e4e67af1cfd20592fee6ad3f6cfe475f",                                  "detected_date":
       "2024-08-15 15:13:26"             },       "firstMessageDate": "2023-02-18T03:31:30+03:00",                    "lastMessageDate": "2024-10-23T08:37:58+03:00",
       "messageNum": 1782175,                   "userNum": 0         },    "author": {        "id": 5011192745,        "userName": "AkenoBaby",             "avatar": null,      "type":
       "user",       "firstName": "i am just a birmd",           "lastName": ""          },     "highlight": null,    "selected": false,   "edits": null,       "deleted": "",    "media":
       {       "name": "",      "type": "",         "size": 0   },        "seqUpdate": 1729505868852513              } ], "count": 5501, "settings": [], "seqUpdate":
       1729506374088157 }

Darkweb - Shops
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information from shops and marketplaces on compromised access. This collection displays the freshest information
       about compromised data from various darkweb marketplaces. Most often it is credentials, cookies, cards and so on. The information obtained from
       this collection can help detect relevant threats that compromise company employees, customers or systems on the internal network.

       Collection-Specific Information


                                                  Property                                                                 Value


                                                   Method                                                                   GET


                                                    Path                                                   /api/v2/compromised/access/updated


                                                 Collection                                                        compromised/access


                                              Collection Name                                                              Shops


                                                   Module                                                                Darkweb


                                                 Submodule                                                                 Shops


                                                    Type                                                                 Individual


                                                 TTL (Days)                                                90 (recommended, not provided in API)


                                               Admiralty Code                                                               A2


                                                  Severity                                                                  N/A


                                              Collection Limit                                                    500 records per request


                                                 Rate Limit                                         1 request per 10 seconds per company per feed (see

                                                                                                                      API Limitations)


                                              Short Description                                      Information about compromised data from various

                                                                                                                  darkweb marketplaces.

Request

       Request URL
        GET /api/v2/compromised/access/updated
       Query Parameters


                     Parameter             Type             Required                  Default                    Description                     Example


                     seqUpdate            integer              No                        0             Sequence update number to get        1450014347005000

                                                                                                        the next data chunk. Use this

                                                                                                         parameter to iterate through

                                                                                                         feeds. The value should be

                                                                                                         obtained from the previous

                                                                                                       response’s top-level seqUpdate

                                                                                                     field or from /api/v2/sequence_list

                                                                                                       endpoint. Important: Always use

                                                                                                       the top-level seqUpdate field for

                                                                                                                   iteration.


                       limit              integer              No                      500            Limit the amount of returned data            500

                                                                                                        for this collection. Maximum

                                                                                                       allowed: 500 for this collection.


                        q                 string               No                        -            Search query. Can be used to filter   id:96339c2618783a

                                                                                                        results or search for a specific    2ffd3fe3f0e855bc63

                                                                                                       entry by ID. Format: id: to search       b4890688

                                                                                                           for one specific record.


       Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               ·

Maximum value: 500 for compromised/access/updated collection

               · If not specified, defaults to 500

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                Required                                  Description                               Example


                  Accept                 string                 No                         Content type accepted by the client              application/json


               Authorization             string                 Yes                  Basic authentication credentials (see Initial                Basic

                                                                                                         Steps)                         base64(LOGIN:API_KEY)


                 User-Agent              string                 No                       User-Agent string with product metadata       SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                    PlatformType/PlatformName_PlatformVersio

                                                                                    n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                             Description                                                  Example


                     Content-Type                                     Response content type                                          application/json


                   Content-Encoding                                     Content encoding                                                  gzip

Header                                            Description                                              Example


                  Cache-Control                                    Cache control directives                        max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                            GET


       Response Body Schema


       The response structure is similar to compromised/account_group/updated, containing compromised access credentials for shops and marketplaces.
       The schema includes account information, service details, events, and evaluation data.

       Root Object
       { "count": integer, "items": [AccessItem], "seqUpdate": integer, "settings": object }


                 Field                   Type                           Required                                       Description


                 count                  integer                            Yes                      Number of access items returned in this response


                 items             array[AccessItem]                       Yes                                   Array of access objects


               seqUpdate                integer                            Yes                       Sequence update number at the top level of the

                                                                                                   response. Always use this top-level value in the next

                                                                                                request’s seqUpdate parameter to get the next portion of

                                                                                                                          feeds


                settings                 object                            Yes                   Search settings object (contains search configuration)


       AccessItem Object


       The structure is similar to AccountGroupItem from compromised/account_group/updated, containing login, password, service information, events,
       and evaluation data specific to shop/marketplace access.

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/access/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

       Success Response (200 OK)


       The response structure is similar to compromised/account_group/updated, with items containing compromised access credentials for shops and
       marketplaces.

{ "count": 1000000, "items": [      {     "id": "example_id_hash",       "login": "examplelogin",          "password": "password123",       "dateFirstSeen":
       "2013-05-21T00:00:00+00:00",         "dateLastSeen": "2013-05-21T00:00:00+00:00",                  "service": {      "domain": "example-shop.com",       "url":
       "http://example-shop.com/",         "host": "example-shop.com"           },        "events": [],   "evaluation": {      "admiraltyCode": "A2",    "credibility": 80,
       "reliability": 100,   "severity": "red",     "tlp": "red",   "ttl": 30        },      "seqUpdate": 1450014347005000          } ], "seqUpdate": 1450014347019000 }

Darkweb - Forums
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides posts collected from monitored cybercrime and general underground forums. Each record represents a single forum post and
       includes the message text, the topic/thread it belongs to, the forum and board where it was published, the author’s nickname, and a set of topic tags.
       Posts may reference bank/personal credentials, stolen data, access offers, tools, and mentions of companies that are being targeted or have already
       been attacked. This information supports monitoring, early warning, and investigation of activity discussed on underground forums.


       This is an intelligence and monitoring collection. Records do not include an evaluation block, so no Admiralty Code, TLP, severity, or credibility values
       are returned for this collection.

       Collection-Specific Information


                                                  Property                                                                        Value


                                                   Method                                                                         GET


                                                    Path                                                           /api/v2/darkweb/forums/updated


                                                 Collection                                                                 darkweb/forums


                                              Collection Name                                                                    Forums


                                                   Module                                                                       Darkweb


                                                 Submodule                                                                       Forums


                                                    Type                                                                        Individual


                                                 TTL (Days)                                                            None (not provided in API)


                                               Admiralty Code                                                                     None


                                                  Severity                                                                         N/A


                                              Collection Limit                                                          100 records per request


                                                 Rate Limit                                              1 request per 10 seconds per company per feed (see

                                                                                                                            API Limitations)

Property                                                   Value


                                      Short Description                      Posts collected from monitored cybercrime and general

                                                                                               underground forums.


       Request

       Request URL
        GET /api/v2/darkweb/forums/updated
       Query Parameters


                   Parameter      Type                 Required   Default              Description                    Example


                   seqUpdate      integer                No         0        Sequence update number to get        1729505868852513

                                                                              the next data chunk. Use this

                                                                               parameter to iterate through

                                                                                feeds. The value should be

                                                                               obtained from the previous

                                                                             response’s top-level seqUpdate

                                                                            field or from /api/v2/sequence_list

                                                                             endpoint. Important: Always use

                                                                             the top-level seqUpdate field for

                                                                                         iteration.


                     limit        integer                No        100      Limit the amount of returned data           100

                                                                               for this collection. Maximum

                                                                             allowed: 100 for this collection.


                      q           string                 No          -      Search query. Can be used to filter   id:7901bb2b140073

                                                                              results or search for a specific    4126168ab9bacc28

                                                                             entry by ID. Format: id: to search          bc

                                                                                 for one specific record.


       Query Parameter Details:


          · seqUpdate:


               ·

Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 100 for darkweb/forums/updated collection

               · If not specified, defaults to 100

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Note: This is a high-volume collection. To keep results focused, narrow your requests using the search query (for example, by forum, categories, or
       specific keywords) rather than retrieving the full feed.

       Request Headers


                  Header                 Type                     Required                            Description                             Example


                  Accept                 string                     No                    Content type accepted by the client              application/json


               Authorization             string                     Yes               Basic authentication credentials (see Initial             Basic

                                                                                                         Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                     No                 User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                        Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                           Description                                           Example


                  Content-Type                                      Response content type                                application/json


                Content-Encoding                                      Content encoding                                          gzip


                  Cache-Control                                    Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                         GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [ForumItem], "seqUpdate": integer, "settings": array }


                 Field                   Type                           Required                                    Description


                 count                  integer                            Yes                   Number of forum items returned in this response


                 items             array[ForumItem]                        Yes                              Array of forum post objects


               seqUpdate                integer                            Yes                    Sequence update number at the top level of the

                                                                                                response. Always use this top-level value in the next

                                                                                              request’s seqUpdate parameter to get the next portion of

                                                                                                                       feeds


                settings                 array                             Yes                             Settings array (usually empty)


       ForumItem Object


                 Field                   Type                           Required                                    Description


                   id                    string                            Yes                              Unique identifier of the post


               message                   string                            Yes                   Post content. May contain sensitive data such as

                                                                                              credentials, card data, or personal information (see Data

                                                                                                                 Sensitivity below)

Field           Type         Required                         Description


               message_hash         string         Yes                     Hash of the post content


                message_len        integer         Yes                    Length of the post content


               message_lang      string | null     No                 Detected language of the message


                    topic           string         Yes              Title of the thread the post belongs to


                 topicHash          string         Yes                       Hash of the topic title


                 topic_info      object | null     No               Additional information about the topic


                  thread_id         string         Yes                      Identifier of the thread


                  first_post       boolean         Yes        Whether this post is the opening post of the thread


                   forum            string         Yes         Forum host where the post was published (e.g.,

                                                                              “breachforums.vc”)


               forum_path_tree   array[string]     Yes               Board/section path within the forum


                   domain           string         Yes                          Forum domain


                     url            string         Yes                          URL of the post


                  nickname          string         Yes                 Author’s handle (pseudonymous)


                nicknameUrl         string         No          URL to the author’s profile (can be empty string)


                 categories      array[string]     Yes      Topic tags assigned to the post (e.g., “Domain”, “Bank”,

                                                                    “Credit card”, “Sale”, “Logs”, “Access”)


                    lang         array[string]     Yes                 Detected language(s) of the post

Field                        Type                          Required                                               Description


                 datetime                        string                           Yes                              ISO 8601 timestamp when the post was published


                uploadTime                       string                           Yes                              ISO 8601 timestamp when the post was ingested


           updateDatetimeAlert              string | null                         No                                 ISO 8601 timestamp of the latest update alert


                 isFavorite                  boolean                              Yes                                  Whether the item is marked as favourite


                 isHidden                    boolean                              Yes                                          Whether the item is hidden


                ocr_analyser                object | null                         No                               Text recognized from images attached to the post


                seqUpdate                        integer                          Yes                               Sequence update number for this specific item


       Note: This collection does not return an evaluation object. No Admiralty Code, TLP, severity, credibility, or reliability values are provided for forum
       posts.

       Data Sensitivity


       The message field contains raw post content and may include credentials, payment card data, or other personal information. Handle, mask, and store
       this data in accordance with your data-protection requirements, and do not add victim data to threat-intelligence watchlists or blocklists. Treat
       matches as analyst leads for investigation.

       Example Request


       Note: In the examples below, set the GIB_CREDENTIALS environment variable to your LOGIN:API_KEY (your email and API key) before running the
       command.

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/darkweb/forums/updated?seqUpdate=0&limit=100' \ -u "$GIB_CREDENTIALS" \ -H 'Accept:
       application/json'
       Example Response

       Success Response (200 OK)
        { "count": 254320, "items": [        {      "id": "7901bb2b1400734126168ab9bacc28bc",          "message": "Selling access to example-company.com admin
       panel. DM for price.",       "message_hash": "3d2a1f9c4b7e08d5a6c1e2f3b4a5d6c7",               "message_len": 62,        "message_lang": "en",       "topic":
       "Access for sale",       "topicHash": "a1b2c3d4e5f60718293a4b5c6d7e8f90",             "topic_info": null,     "thread_id": "1048576",     "first_post": true,
       "forum": "example-forum.tld",         "forum_path_tree": ["Marketplace", "Access"],     "domain": "example-forum.tld",         "url":
       "https://example-forum.tld/threads/1048576/post-1",            "nickname": "example_seller",       "nicknameUrl": "",      "categories": ["Access", "Sale",
       "Domain"],       "lang": ["en"],   "datetime": "2026-05-25T14:03:21+03:00",        "uploadTime": "2026-05-25T14:20:10+03:00",            "updateDatetimeAlert":
       null,     "isFavorite": false,     "isHidden": false,   "ocr_analyser": null,    "seqUpdate": 1779670773451213           } ], "settings": [], "seqUpdate":
       1779670773451850 }

Compromises - Account
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on compromised accounts. Hackers use phishing websites and malware to steal logins and passwords.
       These can be credentials for the internal corporate systems or external services for clients. Malicious programs transfer the intercepted data to
       attacker-controlled remote servers. This server is the central data collection point for intercepted passwords and other information that malware
       gathers. All data is distributed into the following groups service, host, login and password.

       Collection-Specific Information


                                                  Property                                                                      Value


                                                   Method                                                                       GET


                                                    Path                                                   /api/v2/compromised/account_group/updated


                                                 Collection                                                        compromised/account_group


                                              Collection Name                                                         Compromised Accounts


                                                   Module                                                                  Compromises


                                                 Submodule                                                                    Accounts


                                                    Type                                                                      Individual


                                                 TTL (Days)                                                    90 (recommended, not provided in API)


                                               Admiralty Code                                                                    A2


                                                  Severity                                                                      N/A


                                              Collection Limit                                                        500 records per request


                                                 Rate Limit                                             1 request per 10 seconds per company per feed (see

                                                                                                                          API Limitations)

Property                                                   Value


                                  Short Description                       Credentials collected from various phishing resources,

                                                                          botnets, C&C servers, and drop email accounts used by

                                                                                                  hackers.


       Request

       Request URL
        GET /api/v2/compromised/account_group/updated
       Query Parameters


                 Parameter     Type                Required   Default              Description                     Example


                 seqUpdate    integer                No         0        Sequence update number to get        1450014347005000

                                                                          the next data chunk. Use this

                                                                           parameter to iterate through

                                                                            feeds. The value should be

                                                                           obtained from the previous

                                                                         response’s top-level seqUpdate

                                                                        field or from /api/v2/sequence_list

                                                                         endpoint. Important: Always use

                                                                         the top-level seqUpdate field for

                                                                                     iteration.


                   limit      integer                No        500      Limit the amount of returned data            500

                                                                           for this collection. Maximum

                                                                         allowed: 500 for this collection.


                      q       string                 No          -      Search query. Can be used to filter   id:96339c2618783a

                                                                          results or search for a specific    2ffd3fe3f0e855bc63

                                                                         entry by ID. Format: id: to search       b4890688

                                                                             for one specific record.

Parameter              Type            Required                  Default                     Description                 Example


                      unique               integer             No                        0            Filter for unique credentials. Set to     1

                                                                                                     1 to return only unique credentials.

                                                                                                           Note: 0 is interpreted as

                                                                                                         “parameter not provided” for

                                                                                                           backward compatibility.


                     combolist             integer             No                        0             Filter for combo-list credentials.       1

                                                                                                      Set to 1 to return only combo-list

                                                                                                      credentials. Note: 0 is interpreted

                                                                                                       as “parameter not provided” for

                                                                                                           backward compatibility.


        probable_corporate_access          integer             No                        0               Filter for probable corporate          1

                                                                                                        access credentials. Set to 1 to

                                                                                                                    enable.


       Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 500 for compromised/account_group/updated collection

               · If not specified, defaults to 500

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


          · unique and combolist:


               ·

unique=1&combolist=0 -> only unique credentials

               · unique=0&combolist=1 -> only combo-list credentials

               · unique=1&combolist=1 (or omit both) -> all credentials

               · Note: 0 is interpreted as “parameter not provided” for backward compatibility, so unique=0&combolist=0 and unique=1&combolist=1
                 both return all records


       Request Headers


                 Header                    Type               Required                                  Description                                Example


                  Accept                   string                No                          Content type accepted by the client              application/json


               Authorization               string                Yes                   Basic authentication credentials (see Initial                Basic

                                                                                                           Steps)                         base64(LOGIN:API_KEY)


                User-Agent                 string                No                       User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                          (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                           useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                          Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                        e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                       Header                                               Description                                                   Example


                    Content-Type                                       Response content type                                           application/json


                  Content-Encoding                                        Content encoding                                                  gzip


                    Cache-Control                                     Cache control directives                             max-age=0, must-revalidate, private


                        Allow                                         Allowed HTTP methods                                                  GET

Response Body Schema

       Root Object
       { "count": integer, "items": [AccountGroupItem], "seqUpdate": integer, "settings": object }


                   Field                 Type                          Required                                            Description


                  count                 integer                           Yes                        Number of account group items returned in this response


                  items           array[AccountGrou                       Yes                                    Array of account group objects

                                        pItem]


                seqUpdate               integer                           Yes                            Sequence update number at the top level of the

                                                                                                       response. Always use this top-level value in the next

                                                                                                     request’s seqUpdate parameter to get the next portion of

                                                                                                                              feeds


                 settings               object                            Yes                         Search settings object (contains search configuration)


       AccountGroupItem Object


                   Field                 Type                          Required                                            Description


                    id                   string                           Yes                          Unique identifier of the account group (SHA-1 hash)


                   login                 string                           Yes                                            Login/username


                password                 string                           Yes                                               Password


               dateFirstSeen             string                           Yes                         ISO 8601 timestamp when the account was first seen


               dateLastSeen              string                           Yes                          ISO 8601 timestamp when the account was last seen


         dateFirstCompromised         string | null                        No                            ISO 8601 timestamp when the account was first

                                                                                                                          compromised

Field              Type           Required                     Description


         dateLastCompromised       string | null       No       ISO 8601 timestamp when the account was last

                                                                                 compromised


                    port          integer | null       No                        Port number


                seqUpdate            integer           Yes      Sequence update number for this specific item


                parsedLogin       ParsedLogin          Yes                    Parsed login object


                  service         ServiceObject        Yes      Service object (where the credentials were used)


                  events        array[EventObject]     Yes                   Array of event objects


                eventCount           integer           Yes      Number of events associated with this account


                 evaluation        Evaluation          Yes      Evaluation object containing threat assessment


               displayOptions    DisplayOptions        Yes                   Display options object


                 malware              array            Yes               Array of malware references


                threatActor           array            Yes              Array of threat actor references


                  source              array            Yes                 Array of source identifiers


                sourceType            array            Yes                Array of source type strings


                 sourceId             array            Yes                    Array of source IDs


                silentInsert       object | null       No                     Silent insert object


       ParsedLogin Object

Field             Type         Required                  Description


               domain          string | null     No              Domain extracted from login


                  ip           string | null     No            IP address extracted from login


       ServiceObject Object


                Field             Type         Required                  Description


               domain             string         Yes                Service domain name


                  ip           string | null     No                   Service IP address


                 url              string         Yes                     Service URL


                 host             string         Yes                     Service host


       EventObject Object


                Field             Type         Required                  Description


                  id              string         Yes      Unique identifier of the event (SHA-1 hash)


                oldId             string         Yes           Previous identifier (if migrated)


               stixGuid           string         Yes                      STIX GUID


                 cnc           CncObject         Yes         Command and control server object


                client        ClientObject       Yes          Client object (victim information)


               source         SourceObject       Yes                    Source object


               person         object | null      No                     Person object


               malware        object | null      No                    Malware object

Field             Type           Required                       Description


                 threatActor       object | null       No                       Threat actor object


                 dateDetected         string           Yes       ISO 8601 timestamp when the event was detected


               dateCompromised     string | null       No           ISO 8601 timestamp when the account was

                                                                                   compromised


                additionalData     object | null       No                      Additional data object


       CncObject Object


                    Field             Type           Required                       Description


                     cnc              string           Yes      Command and control server identifier (can be empty

                                                                                      string)


                   domain          string | null       No                          Domain name


                     ipv4        IPv4Object | null     No                       IPv4 address object


                     ipv6        IPv6Object | null     No                       IPv6 address object


                     url           string | null       No                              URL


       ClientObject Object


                    Field             Type           Required                       Description


                     ipv4        IPv4Object | null     No             IPv4 address object of the client/victim


                     ipv6        IPv6Object | null     No             IPv6 address object of the client/victim

IPv4Object Object


                   Field          Type         Required               Description


                     ip           string         Yes                 IPv4 address


               countryCode     string | null     No       Country code (ISO 3166-1 alpha-2)


               countryName     string | null     No                  Country name


                    city       string | null     No                    City name


                  region       string | null     No                  Region name


                 provider      string | null     No               ISP/provider name


                    asn        string | null     No                  ASN number


       SourceObject Object


                   Field          Type         Required               Description


                     id           string         Yes        Source ID (can be empty string)


                    type          string         Yes       Source type (can be empty string)


                  idType          string         Yes      Source ID type (can be empty string)


       Evaluation Object


                   Field          Type         Required               Description


               admiraltyCode      string         Yes          Admiralty Code (e.g., “A2”)


                 credibility     integer         Yes            Credibility score (0-100)


                 reliability     integer         Yes            Reliability score (0-100)

Field                            Type                                       Required                                                         Description


                   severity                           string                                        Yes                                               Severity level (e.g., “red”, “orange”)


                       tlp                            string                                        Yes                              Traffic Light Protocol level (e.g., “red”, “amber”, “green”,

                                                                                                                                                                      “white”)


                       ttl                           integer                                        Yes                                                       Time to live in days


       DisplayOptions Object


                     Field                            Type                                       Required                                                         Description


                  isFavourite                       boolean                                         Yes                                         Whether the item is marked as favourite


                   isHidden                         boolean                                         Yes                                                   Whether the item is hidden


         favouriteForCompanies                        array                                         Yes                                   Array of company IDs that marked this as favourite


               hideForCompanies                       array                                         Yes                                             Array of company IDs that hid this item


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/account_group/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Unique Credentials Filter
        curl -X GET 'https://tap.group-ib.com/api/v2/compromised/account_group/updated?seqUpdate=0&limit=500&unique=1&combolist=0' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 630118817, "items": [                {      "id": "96339c2618783a2ffd3fe3f0e855bc63b4890688",                               "dateFirstSeen": "2013-05-21T00:00:00+00:00",
       "dateLastSeen": "2013-05-21T00:00:00+00:00",                       "dateFirstCompromised": null,                 "dateLastCompromised": null,                  "port": null,        "login":
       "examplelogin",             "password": "123456789",            "parsedLogin": {               "domain": null,         "ip": null       },      "service": {       "domain":
       "example.example.corp",                 "ip": null,       "url": "http://example.example.corp/",                  "host": "example.example.corp"                  },       "events": [          {
       "id": "63b797f8b9924391d6669f55b80bbb43f1a7f285",                                  "oldId": "6285",         "stixGuid": "1db49a6a-4844-4d80-d2a6-e990a14bcba2",                                     "cnc": {
                 "cnc": "",           "domain": null,            "ipv4": null,             "ipv6": null,        "url": null          },         "client": {           "ipv4": {             "asn": "AS2854",
                  "city": "Moscow",                "region": "Europe",                  "provider": "LLC Orange Business Services",                         "countryCode": "RU",
       "countryName": "Russian Federation",                         "ip": "192.168.0.1"                 },      "ipv6": null              },        "source": {          "id": "",           "type": "",
       "idType": ""           },        "person": null,           "malware": null,               "threatActor": null,         "dateDetected": "2013-05-21T00:00:00+00:00",
       "dateCompromised": null,                    "additionalData": null           }      ],      "eventCount": 1,        "silentInsert": null,          "evaluation": {            "admiraltyCode": "A2",
           "credibility": 80,          "reliability": 100,        "severity": "red",            "tlp": "red",    "ttl": 30      },        "seqUpdate": 1450014347005000,
       "displayOptions": {             "favouriteForCompanies": [],                "hideForCompanies": [],              "isHidden": false,             "isFavourite": false           },    "malware": [],
       "threatActor": [],          "source": [],      "sourceType": [],          "sourceId": []       } ], "settings": {      "search": {           "tags": ["victim_country", "service_domain",
       "login", "threat_actor", "malware", "source", "id"],               "fields": ["login", "service_domain", "victim_ip", "threat_actor", "malware", "source", "id"],                              "sorts":
       ["first_seen", "last_seen", "seqUpdate"]                } }, "seqUpdate": 1450014347019000 }

Compromises - Git Repository
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on GIT repository leaks. This collection monitors open-source code repositories, like GitHub, for sensitive
       client-related information such as domain names, IP addresses, API tokens or credentials. They are often used by threat actors planning to attack a
       specific company. Alerts clients of any findings and provides detailed leak information, including data type and affected files.

       Collection-Specific Information


                                                  Property                                                                       Value


                                                   Method                                                                         GET


                                                    Path                                                          /api/v2/osi/git_repository/updated


                                                 Collection                                                                osi/git_repository


                                              Collection Name                                                            GIT Repository Leaks


                                                   Module                                                                    Compromises


                                                 Submodule                                                                     GIT Leaks


                                                    Type                                                                       Individual


                                                 TTL (Days)                                                     30 (recommended, not provided in API)


                                               Admiralty Code                                                                      A1


                                                  Severity                                                                        N/A


                                              Collection Limit                                                          500 records per request


                                                 Rate Limit                                              1 request per 10 seconds per company per feed (see

                                                                                                                            API Limitations)


                                              Short Description                                            Sensitive information leaked in open-source code

                                                                                                                        repositories like GitHub.

Request

       Request URL
        GET /api/v2/osi/git_repository/updated
       Query Parameters


                     Parameter             Type             Required                  Default                    Description                     Example


                     seqUpdate            integer              No                        0             Sequence update number to get        1450014347005000

                                                                                                        the next data chunk. Use this

                                                                                                         parameter to iterate through

                                                                                                         feeds. The value should be

                                                                                                         obtained from the previous

                                                                                                       response’s top-level seqUpdate

                                                                                                     field or from /api/v2/sequence_list

                                                                                                       endpoint. Important: Always use

                                                                                                       the top-level seqUpdate field for

                                                                                                                   iteration.


                       limit              integer              No                      500            Limit the amount of returned data            500

                                                                                                        for this collection. Maximum

                                                                                                       allowed: 500 for this collection.


                        q                 string               No                        -            Search query. Can be used to filter   id:96339c2618783a

                                                                                                        results or search for a specific    2ffd3fe3f0e855bc63

                                                                                                       entry by ID. Format: id: to search       b4890688

                                                                                                           for one specific record.


       Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               ·

Maximum value: 500 for osi/git_repository/updated collection

               · If not specified, defaults to 500

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                 Required                                  Description                               Example


                  Accept                 string                  No                         Content type accepted by the client              application/json


               Authorization             string                  Yes                  Basic authentication credentials (see Initial                Basic

                                                                                                          Steps)                         base64(LOGIN:API_KEY)


                 User-Agent              string                  No                       User-Agent string with product metadata       SIEM/QRadar_2020.10.6/G

                                                                                          (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                           useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                          Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                       e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                        Header                                              Description                                                  Example


                     Content-Type                                      Response content type                                          application/json


                   Content-Encoding                                      Content encoding                                                  gzip

Header                                                            Description                                                      Example


                   Cache-Control                                                   Cache control directives                              max-age=0, must-revalidate, private


                           Allow                                                   Allowed HTTP methods                                                    GET


       Response Body Schema


       The response structure is similar to osi/public_leak/updated, containing GIT repository leak information with repository details, file information, and
       detected sensitive data.

       Root Object
       { "count": integer, "items": [GitRepositoryItem], "seqUpdate": integer }


                   Field                            Type                                Required                                                Description


                  count                             integer                               Yes                        Number of GIT repository items returned in this response


                  items                   array[GitRepository                             Yes                                    Array of GIT repository leak objects

                                                    Item]


               seqUpdate                            integer                               Yes                              Sequence update number at the top level of the

                                                                                                                         response. Always use this top-level value in the next

                                                                                                                     request’s seqUpdate parameter to get the next portion of

                                                                                                                                                  feeds


       GitRepositoryItem Object


       The structure contains repository information including repository URL, file paths, detected sensitive data (credentials, API keys, domains, IPs), and
       metadata.

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/osi/git_repository/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

       Success Response (200 OK)


       The response structure is similar to osi/public_leak/updated, with items containing GIT repository leak information.
        { "count": 100000, "items": [           {      "id": "example_id_hash",        "repository": "https://github.com/example/repo",          "file": "config/database.yml",
       "dateFirstSeen": "2023-05-21T00:00:00+00:00",                   "dateLastSeen": "2023-05-21T00:00:00+00:00",           "evaluation": {      "admiraltyCode": "A1",
       "credibility": 100,         "reliability": 100,        "severity": "red",     "tlp": "amber",    "ttl": 30   },    "seqUpdate": 1450014347005000             } ],
       "seqUpdate": 1450014347019000 }

Compromises - Public Leak
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on public leaks. There are specialized websites for exchanging textual information (such as Pastebin and
       analogous resources). They can be used to upload texts and send anyone a link to them. Both legitimate IT specialists and hackers actively use such
       resources. IT professionals may underestimate the risks and load configuration files for network equipment, export tables from databases, code
       fragments containing access credentials, and much more. Hackers mainly post lists of usernames, passwords, bank card details, Trojan configuration
       files, attack outcomes, and various logs.

       Collection-Specific Information


                                                    Property                                                                 Value


                                                    Method                                                                    GET


                                                     Path                                                       /api/v2/osi/public_leak/updated


                                                   Collection                                                           osi/public_leak


                                              Collection Name                                                             Public Leaks


                                                    Module                                                               Compromises


                                                   Submodule                                                              Public leaks


                                                     Type                                                                  Individual


                                                   TTL (Days)                                               30 (recommended, not provided in API)


                                               Admiralty Code                                                                 C3


                                                    Severity                                                                  N/A


                                              Collection Limit                                                      100 records per request


                                                   Rate Limit                                         1 request per 10 seconds per company per feed (see

                                                                                                                        API Limitations)

Property                                                   Value


                                      Short Description                          Textual information leaked on public paste sites,

                                                                              including credentials, configuration files, and sensitive

                                                                                                        data.


       Request

       Request URL
        GET /api/v2/osi/public_leak/updated
       Query Parameters


                 Parameter        Type                 Required   Default              Description                      Example


                 seqUpdate        integer                No         0        Sequence update number to get         16202106434186

                                                                              the next data chunk. Use this

                                                                               parameter to iterate through

                                                                                feeds. The value should be

                                                                               obtained from the previous

                                                                             response’s top-level seqUpdate

                                                                            field or from /api/v2/sequence_list

                                                                             endpoint. Important: Always use

                                                                             the top-level seqUpdate field for

                                                                                         iteration.


                   limit          integer                No        100      Limit the amount of returned data             100

                                                                               for this collection. Maximum

                                                                             allowed: 100 for this collection.


                      q           string                 No          -      Search query. Can be used to filter id:0083e0516cac929

                                                                              results or search for a specific    a5f5267f8f5ebebb77

                                                                             entry by ID. Format: id: to search         063f235

                                                                                 for one specific record.


       Query Parameter Details:


          · seqUpdate:

· Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 100 for osi/public_leak/updated collection

               · If not specified, defaults to 100

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                  Required                               Description                             Example


                  Accept                 string                   No                      Content type accepted by the client              application/json


               Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                         Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                        Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                            Description                                          Example


                  Content-Type                                     Response content type                                application/json


                Content-Encoding                                      Content encoding                                         gzip


                  Cache-Control                                   Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                        GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [PublicLeakItem], "seqUpdate": integer }


                 Field                    Type                          Required                                   Description


                 count                   integer                          Yes                 Number of public leak items returned in this response


                 items             array[PublicLeakIte                    Yes                              Array of public leak objects

                                           m]


               seqUpdate                 integer                          Yes                    Sequence update number at the top level of the

                                                                                               response. Always use this top-level value in the next

                                                                                             request’s seqUpdate parameter to get the next portion of

                                                                                                                      feeds


       PublicLeakItem Object


                 Field                    Type                          Required                                   Description


                  id                     string                           Yes                       Unique identifier of the leak (SHA-1 hash)


                 hash                    string                           Yes                           Hash of the leak content (SHA-1)


                 data                    string                           Yes                                  Leaked data content

Field             Type           Required                          Description


                 language            string           Yes        Programming language or file type (e.g., “xml”, “java”,

                                                                                         “text”)


                  created            string           Yes          ISO 8601 timestamp when the leak was created


                  updated            string           Yes        ISO 8601 timestamp when the leak was last updated


                seqUpdate           integer           Yes           Sequence update number for this specific item


                   bind              array            Yes                        Array of bind objects


                  linkList      array[LinkObject]     Yes      Array of link objects (sources where the leak was found)


                 matches        MatchesObject         Yes      Matches object containing detected sensitive information


                 evaluation        Evaluation         Yes          Evaluation object containing threat assessment


               displayOptions   DisplayOptions        Yes                       Display options object


       LinkObject Object


                   Field             Type           Required                          Description


                    link             string           Yes                           URL to the leak


                   hash              string           Yes                  Hash of the link content (SHA-1)


                  source             string           Yes                 Source name (e.g., “pastebin.com”)


                  author             string           Yes                 Author name (can be empty string)

Field           Type         Required                     Description


                     title          string         Yes                Title (can be empty string)


                 dateDetected       string         Yes      ISO 8601 timestamp when the link was detected


                datePublished       string         Yes      ISO 8601 timestamp when the link was published


                 itemSource         string         Yes                   Item source identifier


                     size          integer         Yes                Size of the content in bytes


                    status         integer         Yes                       Status code


               sequenceUpdate      integer         Yes           Sequence update number for this link


       MatchesObject Object


                    Field           Type         Required                     Description


               commonKeywords      object          Yes      Object containing common keywords found (e.g.,

                                                                          password, api_key)


                    email        object | null     No          Object containing email addresses found


       Evaluation Object


                    Field           Type         Required                     Description


                admiralty_code      string         Yes                Admiralty Code (e.g., “C3”)


                  credibility      integer         Yes                 Credibility score (0-100)


                  reliability      integer         Yes                 Reliability score (0-100)

Field                    Type                             Required                                                    Description


                severity                   string                                Yes                               Severity level (e.g., “green”, “orange”, “red”)


                   tlp                     string                                Yes                      Traffic Light Protocol level (e.g., “amber”, “red”, “green”,

                                                                                                                                         “white”)


                   ttl                    integer                                Yes                                            Time to live in days


       DisplayOptions Object


                  Field                    Type                             Required                                                    Description


               isFavourite                boolean                                Yes                                Whether the item is marked as favourite


                isHidden                  boolean                                Yes                                         Whether the item is hidden


       Example Request

       Basic Request
        curl -X GET 'https://tap.group-ib.com/api/v2/osi/public_leak/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 24353999, "items": [    {      "bind": [],   "created": "2022-05-05T20:26:25+03:00",     "data": "networks:\r\n default:\r\n name:
       datahub_network\r\nservices:\r\n broker:\r\n container_name: broker\r\n depends_on:\r\n                - zookeeper\r\n environment:\r\n                     -
       KAFKA_BROKER_ID=1\r\n       - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181\r\n                  -
       KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT\r\n                                    -
       KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://broker:29092,PLAINTEXT_HOST://localhost:9092\r\n                           -
       KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1\r\n                   - KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0\r\n                       -
       KAFKA_HEAP_OPTS=-Xms256m -Xmx256m\r\n hostname: broker\r\n image: confluentinc/cp-kafka:5.4.0\r\n ports:\r\n                                     - 29092:29092\r\n     -
       9092:9092\r\n datahub-actions:\r\n depends_on:\r\n            - datahub-gms\r\n environment:\r\n        - GMS_HOST=datahub-gms\r\n                      -
       GMS_PORT=8080\r\n       - KAFKA_BOOTSTRAP_SERVER=broker:29092\r\n                - SCHEMA_REGISTRY_URL=http://schema-registry:8081\r\n                          -
       METADATA_AUDIT_EVENT_NAME=MetadataAuditEvent_v4\r\n                   -
       METADATA_CHANGE_LOG_VERSIONED_TOPIC_NAME=MetadataChangeLog_Versioned_v1\r\n                             -
       DATAHUB_SYSTEM_CLIENT_ID=__datahub_system\r\n                  - DATAHUB_SYSTEM_CLIENT_SECRET=JohnSnowKnowsNothing\r\n                              -
       KAFKA_PROPERTIES_SECURITY_PROTOCOL=PLAINTEXT\r\n hostname: actions\r\n image:
       public.ecr.aws/datahub/acryl-datahub-actions:${ACTIONS_VERSION:-head}\r\n restart: on-failure:5\r\n datahub-frontend-react:\r\n
       container_name: datahub-frontend-react\r\n depends_on:\r\n            - datahub-gms\r\n environment:\r\n              - DATAHUB_GMS_HOST=datahub-gms\r\n
          - DATAHUB_GMS_PORT=8080\r\n             - DATAHUB_SECRET=YouKnowNothing\r\n           - DATAHUB_APP_VERSION=1.0\r\n                       -
       DATAHUB_PLAY_MEM_BUFFER_SIZE=10MB\r\n                    - JAVA_OPTS=-Xms512m -Xmx512m -Dhttp.port=9002
       -Dconfig.file=datahub-frontend/conf/application.conf -Djava.security.auth.login.config=datahub-frontend/conf/jaas.conf
       -Dlogback.configurationFile=datahub-frontend/conf/logback.xml -Dlogback.debug=false -Dpidfile.path=/dev/null\r\n                    -
       KAFKA_BOOTSTRAP_SERVER=broker:29092\r\n                  - DATAHUB_TRACKING_TOPIC=DataHubUsageEvent_v1\r\n                   -
       ELASTIC_CLIENT_HOST=elasticsearch\r\n             - ELASTIC_CLIENT_PORT=9200\r\n        - AUTH_OIDC_ENABLED=true\r\n                     -
       AUTH_OIDC_CLIENT_ID=${DATAHUB_IAM_ID}\r\n                 - AUTH_OIDC_CLIENT_SECRET=${DATAHUB_IAM_SECRET}\r\n                        -
       AUTH_OIDC_DISCOVERY_URI=${DATAHUB_IAM_URI}\r\n                  - AUTH_OIDC_BASE_URL=${DATAHUB_URL}\r\n                  #- AUTH_OIDC_SCOPE=\\\"\\\"\r\n
       - METADATA_SERVICE_AUTH_ENABLED=true\r\n hostname: datahub-frontend-react\r\n image:

linkedin/datahub-frontend-react:${DATAHUB_VERSION:-head}\r\n ports:\r\n                                - 9002:9002\r\n volumes:\r\n               -
       ${HOME}/.datahub/plugins:/etc/datahub/plugins\r\n                   -
       ${HOME}/.datahub/plugins/frontend/auth/user.props:/datahub-frontend/conf/user.props\r\n datahub-gms:\r\n container_name: datahub-gms\r\n
        depends_on:\r\n          - mysql\r\n environment:\r\n          - DATASET_ENABLE_SCSI=false\r\n                     - EBEAN_DATASOURCE_USERNAME=datahub\r\n                                     -
       EBEAN_DATASOURCE_PASSWORD=datahub\r\n                         - EBEAN_DATASOURCE_HOST=mysql:3306\r\n                           -
       EBEAN_DATASOURCE_URL=jdbc:mysql://mysql:3306/datahub?verifyServerCertificate=false&useSSL=true&useUnicode=yes&characterEncoding=UTF-
       8\r\n          - EBEAN_DATASOURCE_DRIVER=com.mysql.jdbc.Driver\r\n                       - KAFKA_BOOTSTRAP_SERVER=broker:29092\r\n                               -
       KAFKA_SCHEMAREGISTRY_URL=http://schema-registry:8081\r\n                               - ELASTICSEARCH_HOST=elasticsearch\r\n                         -
       ELASTICSEARCH_PORT=9200\r\n                - GRAPH_SERVICE_IMPL=elasticsearch\r\n                         - JAVA_OPTS=-Xms1g -Xmx1g\r\n                      -
       ENTITY_REGISTRY_CONFIG_PATH=/datahub/datahub-gms/resources/entity-registry.yml\r\n                                     - MAE_CONSUMER_ENABLED=true\r\n                                 -
       MCE_CONSUMER_ENABLED=true\r\n                     - UI_INGESTION_ENABLED=true\r\n                      - UI_INGESTION_DEFAULT_CLI_VERSION=0.8.26.6\r\n                             -
       METADATA_SERVICE_AUTH_ENABLED=true\r\n hostname: datahub-gms\r\n image: linkedin/datahub-gms:${DATAHUB_VERSION:-head}\r\n
       ports:\r\n        - 8080:8080\r\n volumes:\r\n          - ${HOME}/.datahub/plugins:/etc/datahub/plugins\r\n elasticsearch:\r\n container_name:
       elasticsearch\r\n environment:\r\n               - discovery.type=single-node\r\n              - xpack.security.enabled=false\r\n                - ES_JAVA_OPTS=-Xms256m
       -Xmx256m -Dlog4j2.formatMsgNoLookups=true\r\n healthcheck:\r\n                             retries: 4\r\n       start_period: 2m\r\n             test:\r\n           - CMD-SHELL\r\n                 -
       curl -sS --fail 'http://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=0s' || exit 1\r\n hostname: elasticsearch\r\n image:
       elasticsearch:7.9.3\r\n mem_limit: 1g\r\n ports:\r\n                    - 9200:9200\r\n volumes:\r\n              - esdata:/usr/share/elasticsearch/data\r\n
       elasticsearch-setup:\r\n container_name: elasticsearch-setup\r\n depends_on:\r\n                               - elasticsearch\r\n environment:\r\n                      -
       ELASTICSEARCH_HOST=elasticsearch\r\n                   - ELASTICSEARCH_PORT=9200\r\n                       - ELASTICSEARCH_PROTOCOL=http\r\n hostname:
       elasticsearch-setup\r\n image: linkedin/datahub-elasticsearch-setup:${DATAHUB_VERSION:-head}\r\n kafka-setup:\r\n container_name:
       kafka-setup\r\n depends_on:\r\n                - broker\r\n    - schema-registry\r\n environment:\r\n                  -
       KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181\r\n                          - KAFKA_BOOTSTRAP_SERVER=broker:29092\r\n hostname: kafka-setup\r\n image:
       linkedin/datahub-kafka-setup:${DATAHUB_VERSION:-head}\r\n mysql:\r\n command: --character-set-server=utf8mb4
       --collation-server=utf8mb4_bin\r\n container_name: mysql\r\n environment:\r\n                               - MYSQL_DATABASE=datahub\r\n                         -
       MYSQL_USER=datahub\r\n              - MYSQL_PASSWORD=datahub\r\n                       - MYSQL_ROOT_PASSWORD=datahub\r\n hostname: mysql\r\n image:
       mysql:5.7\r\n ports:\r\n          - 3306:3306\r\n volumes:\r\n                - ../mysql/init.sql:/docker-entrypoint-initdb.d/init.sql\r\n                 -
       mysqldata:/var/lib/mysql\r\n mysql-setup:\r\n container_name: mysql-setup\r\n depends_on:\r\n                                      - mysql\r\n environment:\r\n                        -
       MYSQL_HOST=mysql\r\n              - MYSQL_PORT=3306\r\n                 - MYSQL_USERNAME=datahub\r\n                  - MYSQL_PASSWORD=datahub\r\n                            -
       DATAHUB_DB_NAME=datahub\r\n hostname: mysql-setup\r\n image: acryldata/datahub-mysql-setup:head\r\n schema-registry:\r\n
       container_name: schema-registry\r\n depends_on:\r\n                      - zookeeper\r\n         - broker\r\n environment:\r\n               -
       SCHEMA_REGISTRY_HOST_NAME=schemaregistry\r\n                            - SCHEMA_REGISTRY_KAFKASTORE_CONNECTION_URL=zookeeper:2181\r\n hostname:
       schema-registry\r\n image: confluentinc/cp-schema-registry:5.4.0\r\n ports:\r\n                             - 8081:8081\r\n zookeeper:\r\n container_name:
       zookeeper\r\n environment:\r\n             - ZOOKEEPER_CLIENT_PORT=2181\r\n                        - ZOOKEEPER_TICK_TIME=2000\r\n hostname: zookeeper\r\n
       image: confluentinc/cp-zookeeper:5.4.0\r\n ports:\r\n                   - 2181:2181\r\n volumes:\r\n               - zkdata:/var/opt/zookeeper\r\nversion:
       '2.3'\r\nvolumes:\r\n esdata: null\r\n mysqldata: null\r\n zkdata: null\r\n",                     "displayOptions": {          "isFavourite": false,                 "isHidden": false          },
         "evaluation": {        "admiralty_code": "C3",         "credibility": 50,       "reliability": 50,         "severity": "green",       "tlp": "amber",                "ttl": 30           },
       "hash": "0083e0516cac929a5f5267f8f5ebebb77063f235",                        "id": "0083e0516cac929a5f5267f8f5ebebb77063f235",                              "language": "xml",
       "linkList": [       {      "author": "",        "hash": "024c788fdacdd8b8827de9e50c13ea0e6dde1988",                                "link": "https://pastebin.com/HPjD9kmj",
       "title": "",        "source": "pastebin.com",          "dateDetected": "2022-05-05T20:26:25+03:00",                        "datePublished": "2022-05-05T17:16:43+00:00",
        "itemSource": "api",          "size": 6625,         "status": 1,         "sequenceUpdate": 1651771585142655                        }   ],        "matches": {
       "commonKeywords": {               "password": [           "PASSWORD"               ]       }      },      "seqUpdate": -1651773180003874,                    "updated":
       "2022-05-05T20:26:25+03:00"            } ], "seqUpdate": 16202106434186 }

Compromises - Breached DB
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides credential exposures identified in known breached databases (for example, large aggregated leaks published on hacker
       forums). Each record ties an exposed email address, and a password when present, to the breach it originated from, along with the breach name,
       description, publication date, and the source download links. By default, records are matched to your monitored scope, so you receive exposures
       relevant to your organization. This information supports credential-exposure monitoring, breach investigation, and exposure governance.

       Collection-Specific Information


                                                  Property                                                                   Value


                                                   Method                                                                     GET


                                                    Path                                                  /api/v2/compromised/breacheddb/updated


                                                 Collection                                                        compromised/breacheddb


                                              Collection Name                                                            Breached DB


                                                   Module                                                                Compromises


                                                 Submodule                                                               Breached DB


                                                    Type                                                                   Individual


                                                 TTL (Days)                                                                   N/A


                                               Admiralty Code                                                                 C3


                                                  Severity                                                                    N/A


                                              Collection Limit                                                      100 records per request


                                                 Rate Limit                                           1 request per 10 seconds per company per feed (see

                                                                                                                        API Limitations)

Property                                                    Value


                                  Short Description                         Credential exposures identified in known breached

                                                                              databases matched to your monitored scope.


       Request

       Request URL
        GET /api/v2/compromised/breacheddb/updated
       Query Parameters


                 Parameter    Type                 Required   Default               Description                     Example


                 seqUpdate    integer                No         0        Sequence update number to get                 0

                                                                          the next data chunk. Use this

                                                                           parameter to iterate through

                                                                          feeds. For this collection, start

                                                                        iteration at 0 (see the note below).

                                                                        Use the top-level seqUpdate field

                                                                         from the previous response for

                                                                              subsequent requests.


                   limit      integer                No        100      Limit the amount of returned data             100

                                                                          for this collection. Maximum

                                                                         allowed: 100 for this collection.


               has_password   integer                No         0       Filter by password presence. Set               1

                                                                          to 1 to return only records that

                                                                               include a password.


                      q       string                 No          -      Search query. Can be used to filter    id:96339c2618783a

                                                                          results or search for a specific     2ffd3fe3f0e855bc63

                                                                         entry by ID. Format: id: to search        b4890688

                                                                             for one specific record.

Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: For this collection, start iteration at seqUpdate=0, then continue with the top-level seqUpdate value returned in each
                 response

               · Unlike most other collections, this collection does not support bootstrapping a cursor from a specific date via /api/v2/sequence_list -
                 a date-based cursor returns an empty result set. Always start at 0.


          · limit:


               · Maximum value: 100 for compromised/breacheddb/updated collection

               · If not specified, defaults to 100

               · The limit depends on the amount of data to not overload the JSON output


          · has_password:


               · has_password=1 returns only records that include a password

               · If not specified, all matching records are returned regardless of password presence


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                 Header                  Type                   Required                                Description                             Example


                  Accept                 string                    No                       Content type accepted by the client             application/json


               Authorization             string                    Yes                  Basic authentication credentials (see Initial                Basic

                                                                                                           Steps)                       base64(LOGIN:API_KEY)

Header                 Type                Required                                  Description                             Example


               User-Agent             string                  No                       User-Agent string with product metadata     SIEM/QRadar_2020.10.6/G

                                                                                       (optional but recommended - especially      roupIB_TI_1.0.0/gibuser@g

                                                                                        useful in troubleshooting on our end).     roup-ib.com/ciaops_3.0.0

                                                                                                       Format:

                                                                                   PlatformType/PlatformName_PlatformVersio

                                                                                   n/AppName_AppVersion/Username/LibNam

                                                                                                    e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                      Header                                             Description                                                Example


                   Content-Type                                    Response content type                                         application/json


                 Content-Encoding                                     Content encoding                                                gzip


                   Cache-Control                                   Cache control directives                            max-age=0, must-revalidate, private


                          Allow                                    Allowed HTTP methods                                               GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [BreachedDbItem], "seqUpdate": integer }


                  Field                   Type                          Required                                            Description


                  count                  integer                          Yes                        Number of breached DB items returned in this response


                  items             array[BreachedDbIt                    Yes                              Array of breached database exposure objects

                                           em]

Field            Type         Required                         Description


                  seqUpdate         integer         Yes           Sequence update number at the top level of the

                                                               response. Always use this top-level value in the next

                                                             request’s seqUpdate parameter to get the next portion of

                                                                                      feeds


       BreachedDbItem Object


                    Field            Type         Required                         Description


                      id          array[string]     Yes              Record hash(es) identifying the exposure


                  leakName           string         Yes       Name of the breach the exposure originated from (e.g.,

                                                                                 “Collection #2”)


                 description         string         Yes                     Description of the breach


                leakPublished        string         Yes        ISO 8601 timestamp when the breach was published


                   authors        array[string]     Yes      Handles of those who published the leak (leak publishers,

                                                                                   not victims)


                    email            string         Yes               Exposed email address (personal data)


                  password        string | null     No           Exposed password. Present when available; use

                                                             has_password=1 to return only records that include one


                   addInfo        object | null     No          Additional leaked fields associated with the record

                                                                                (varies by breach)


               downloadLinkList   array[string]     Yes                  Links to the source breach data


               reaperMessageId    string | null     No         Reference to the source message where the leak was

                                                                                    observed

Field                   Type                           Required                                            Description


                evaluation              Evaluation                          Yes                            Evaluation object containing threat assessment


                uploadTime                string                            Yes                          ISO 8601 timestamp when the record was ingested


                updateTime                string                            Yes                        ISO 8601 timestamp when the record was last updated


       Evaluation Object


                   Field                   Type                           Required                                            Description


               admiraltyCode              string                            Yes                                       Admiralty Code (e.g., “C3”)


                 credibility              integer                           Yes                                        Credibility score (0-100)


                 reliability              integer                           Yes                                         Reliability score (0-100)


                  severity                string                            Yes                              Severity level (e.g., “green”, “orange”, “red”)


                     tlp                  string                            Yes                        Traffic Light Protocol level (e.g., “amber”, “red”, “green”,

                                                                                                                                “white”)


       Note: The evaluation block is provided per record. Read its values at runtime rather than assuming a fixed value for the whole collection.

       Data Sensitivity


       Records in this collection contain victim data: email (personal data), password (plaintext when present), and addInfo (additional leaked fields). The
       downloadLinkList field points to the source breach data. Mask, restrict, and store this data in accordance with your data-protection requirements. Do
       not add victim email addresses to threat-intelligence watchlists or blocklists - use this data to drive account-protection and incident-response
       workflows. The authors field lists leak publishers, not victims.

       Example Request


       Note: In the examples below, set the GIB_CREDENTIALS environment variable to your LOGIN:API_KEY (your email and API key) before running the
       command.

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/breacheddb/updated?seqUpdate=0&limit=100' \ -u "$GIB_CREDENTIALS" \ -H 'Accept:
       application/json'

Request with Password Filter
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/breacheddb/updated?seqUpdate=0&limit=100&has_password=1' \ -u
       "$GIB_CREDENTIALS" \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 636, "items": [ {       "id": ["96339c2618783a2ffd3fe3f0e855bc63b4890688"],                  "leakName": "Example Collection",        "description":
       "Aggregated credential dump published on an underground forum.",             "leakPublished": "2019-01-18T00:00:00",          "authors": ["example_author"],
       "email": "user@example-company.com",             "password": "examplePassword",         "addInfo": {        "registrationDate": "2016-04-02"      },
       "downloadLinkList": [       "https://example-forum.tld/leaks/example-collection"              ],   "reaperMessageId": "3d2a1f9c4b7e08d5a6c1e2f3b4a5d6c7",
          "evaluation": {      "admiraltyCode": "C3",      "credibility": 60,   "reliability": 60,        "severity": "green",   "tlp": "amber"     },    "uploadTime":
       "2025-03-14T09:12:00+00:00",         "updateTime": "2025-03-14T09:12:00+00:00"           } ], "seqUpdate": 1780224348744247 }

Banking - Cards
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on compromised bank cards. This includes data collected from card shops, specialized forums, and
       public sources. All data collected is grouped by card number.

       Collection-Specific Information


                                                  Property                                                                 Value


                                                   Method                                                                   GET


                                                    Path                                              /api/v2/compromised/bank_card_group/updated


                                                 Collection                                                   compromised/bank_card_group


                                              Collection Name                                                    Compromised Bank Cards


                                                   Module                                                                 Banking


                                                 Submodule                                                              Bank cards


                                                    Type                                                                 Individual


                                                 TTL (Days)                                                90 (recommended, not provided in API)


                                               Admiralty Code                                                               A2


                                                  Severity                                                                  N/A


                                              Collection Limit                                                    500 records per request


                                                 Rate Limit                                         1 request per 10 seconds per company per feed (see

                                                                                                                      API Limitations)

Property                                                    Value


                                      Short Description                        Compromised bank card information collected from

                                                                                  underground markets, forums, and messaging

                                                                                                      platforms.


       Request

       Request URL
        GET /api/v2/compromised/bank_card_group/updated
       Query Parameters


                 Parameter        Type                 Required   Default              Description                      Example


                 seqUpdate        integer                No         0        Sequence update number to get         1450014347005000

                                                                              the next data chunk. Use this

                                                                               parameter to iterate through

                                                                                feeds. The value should be

                                                                               obtained from the previous

                                                                             response’s top-level seqUpdate

                                                                            field or from /api/v2/sequence_list

                                                                             endpoint. Important: Always use

                                                                             the top-level seqUpdate field for

                                                                                         iteration.


                   limit          integer                No        500      Limit the amount of returned data             500

                                                                               for this collection. Maximum

                                                                             allowed: 500 for this collection.


                      q           string                 No          -      Search query. Can be used to filter    id:96339c2618783a

                                                                              results or search for a specific     2ffd3fe3f0e855bc63

                                                                             entry by ID. Format: id: to search        b4890688

                                                                                 for one specific record.


       Query Parameter Details:


          · seqUpdate:

· Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 500 for compromised/bank_card_group/updated collection

               · If not specified, defaults to 500

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                  Required                               Description                             Example


                  Accept                 string                   No                      Content type accepted by the client              application/json


               Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                         Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                        Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                            Description                                                    Example


                  Content-Type                                     Response content type                                         application/json


                Content-Encoding                                     Content encoding                                                   gzip


                  Cache-Control                                   Cache control directives                              max-age=0, must-revalidate, private


                         Allow                                    Allowed HTTP methods                                                  GET


       Response Body Schema


       The response structure is similar to other compromised collections, containing bank card information grouped by card details.

       Root Object
       { "count": integer, "items": [BankCardGroupItem], "seqUpdate": integer, "settings": object }


                 Field                   Type                          Required                                             Description


                 count                  integer                           Yes                            Number of bank card group items returned in this

                                                                                                                             response


                 items             array[BankCardGro                      Yes                                    Array of bank card group objects

                                        upItem]


               seqUpdate                integer                           Yes                             Sequence update number at the top level of the

                                                                                                        response. Always use this top-level value in the next

                                                                                                      request’s seqUpdate parameter to get the next portion of

                                                                                                                               feeds


                settings                object                            Yes                          Search settings object (contains search configuration)


       BankCardGroupItem Object


       The structure contains bank card information including card number (masked), expiration date, CVV, BIN, bank information, and associated
       events/metadata.

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/bank_card_group/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

Success Response (200 OK)


       The response contains bank card group items with card information and associated metadata.
        { "count": 1000000, "items": [   {   "id": "example_id_hash",     "dateFirstSeen": "2013-05-21T00:00:00+00:00",           "dateLastSeen":
       "2013-05-21T00:00:00+00:00",      "evaluation": {   "admiraltyCode": "A2",      "credibility": 80,   "reliability": 100,       "severity": "red",   "tlp":
       "red",    "ttl": 30   },   "seqUpdate": 1450014347005000         } ], "seqUpdate": 1450014347019000 }

Banking - Masked cards
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on compromised masked bank cards. Masked Card collection contains information about compromised
       cards. This includes data collected from card shops, specialized forums, and public sources. The main difference from the Compromised Cards
       collection is that, in most cases, the card details are partially masked.

       Collection-Specific Information


                                                   Property                                                                Value


                                                   Method                                                                   GET


                                                     Path                                              /api/v2/compromised/masked_card/updated


                                                  Collection                                                    compromised/masked_card


                                              Collection Name                                                  Compromised Masked Cards


                                                   Module                                                                 Banking


                                                 Submodule                                                              Bank cards


                                                     Type                                                                Individual


                                                 TTL (Days)                                                90 (recommended, not provided in API)


                                               Admiralty Code                                                               A2


                                                   Severity                                                                 N/A


                                               Collection Limit                                                   500 records per request


                                                  Rate Limit                                        1 request per 10 seconds per company per feed (see

                                                                                                                      API Limitations)

Property                                                    Value


                                      Short Description                       Compromised masked bank card information collected

                                                                               from underground markets, forums, and messaging

                                                                                                      platforms.


       Request

       Request URL
        GET /api/v2/compromised/masked_card/updated
       Query Parameters


                 Parameter        Type                 Required   Default              Description                      Example


                 seqUpdate        integer                No         0        Sequence update number to get         1450014347005000

                                                                              the next data chunk. Use this

                                                                               parameter to iterate through

                                                                                feeds. The value should be

                                                                               obtained from the previous

                                                                             response’s top-level seqUpdate

                                                                            field or from /api/v2/sequence_list

                                                                             endpoint. Important: Always use

                                                                             the top-level seqUpdate field for

                                                                                         iteration.


                   limit          integer                No        500      Limit the amount of returned data             500

                                                                               for this collection. Maximum

                                                                             allowed: 500 for this collection.


                      q           string                 No          -      Search query. Can be used to filter    id:96339c2618783a

                                                                              results or search for a specific     2ffd3fe3f0e855bc63

                                                                             entry by ID. Format: id: to search        b4890688

                                                                                 for one specific record.


       Query Parameter Details:


          · seqUpdate:

· Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 500 for compromised/masked_card/updated collection

               · If not specified, defaults to 500

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types


       Request Headers


                  Header                 Type                  Required                               Description                             Example


                  Accept                 string                   No                      Content type accepted by the client              application/json


               Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                         Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                        (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                         useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                        Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                     e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                            Description                                                 Example


                  Content-Type                                     Response content type                                      application/json


                Content-Encoding                                     Content encoding                                                gzip


                  Cache-Control                                   Cache control directives                           max-age=0, must-revalidate, private


                         Allow                                    Allowed HTTP methods                                               GET


       Response Body Schema


       The response structure is similar to compromised/bank_card_group/updated, containing masked bank card information.

       Root Object
       { "count": integer, "items": [MaskedCardItem], "seqUpdate": integer, "settings": object }


                 Field                   Type                          Required                                          Description


                 count                  integer                           Yes                      Number of masked card items returned in this response


                 items             array[MaskedCardI                      Yes                                   Array of masked card objects

                                         tem]


               seqUpdate                integer                           Yes                          Sequence update number at the top level of the

                                                                                                     response. Always use this top-level value in the next

                                                                                                   request’s seqUpdate parameter to get the next portion of

                                                                                                                            feeds


                settings                object                            Yes                       Search settings object (contains search configuration)


       MaskedCardItem Object


       The structure contains masked bank card information where the card number is partially obscured, along with expiration date, CVV, BIN, bank
       information, and associated events/metadata.

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/masked_card/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Example Response

Success Response (200 OK)


       The response contains masked card items with partially obscured card information and associated metadata.
        { "count": 1000000, "items": [   {   "id": "example_id_hash",     "dateFirstSeen": "2013-05-21T00:00:00+00:00",           "dateLastSeen":
       "2013-05-21T00:00:00+00:00",      "evaluation": {   "admiraltyCode": "A2",      "credibility": 80,   "reliability": 100,       "severity": "red",   "tlp":
       "red",    "ttl": 30   },   "seqUpdate": 1450014347005000         } ], "seqUpdate": 1450014347019000 }

Banking - SPD
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on Suspicious Payment Details (SPD). This collection provides a curated feed of payment identifiers that
       have been linked to laundering operations, ransomware transactions, illegal online casinos, and other forms of illicit financial activity. This data helps
       anti-fraud and risk teams proactively detect and disrupt suspicious financial flows before damage occurs. SPD replaces the deprecated Mules section,
       offering improved granularity, new identifier types, and enriched attribution.

       Collection-Specific Information


                                                  Property                                                                        Value


                                                   Method                                                                          GET


                                                    Path                                                           /api/v2/compromised/spd/updated


                                                 Collection                                                                 compromised/spd


                                              Collection Name                                                          Suspicious Payment Details


                                                   Module                                                                        Banking


                                                 Submodule                                                             Suspicious Payment Details


                                                    Type                                                                        Individual


                                                 TTL (Days)                                                      90 (recommended, not provided in API)


                                               Admiralty Code                                                                       A2


                                                   Severity                                                                        N/A


                                               Collection Limit                                                          500 records per request


                                                 Rate Limit                                               1 request per 10 seconds per company per feed (see

                                                                                                                             API Limitations)

Property                                                   Value


                                  Short Description                      Suspicious payment details collected from underground

                                                                               markets, forums, and messaging platforms.


       Request

       Request URL
        GET /api/v2/compromised/spd/updated
       Query Parameters


                 Parameter    Type                 Required   Default              Description                     Example


                 seqUpdate    integer                No         0        Sequence update number to get         1450014347005000

                                                                           the next data chunk. Use this

                                                                           parameter to iterate through

                                                                            feeds. The value should be

                                                                            obtained from the previous

                                                                         response’s top-level seqUpdate

                                                                        field or from /api/v2/sequence_list

                                                                         endpoint. Important: Always use

                                                                         the top-level seqUpdate field for

                                                                                     iteration.


                   limit      integer                No        500      Limit the amount of returned data            500

                                                                           for this collection. Maximum

                                                                         allowed: 500 for this collection.


                   type       string                 No          -      Filter records by payment identifier     mobileNumber

                                                                        type. Returns only records whose

                                                                         identifier matches the specified

                                                                          type. See the supported values

                                                                                      below.

Parameter                Type             Required               Default                    Description                     Example


                        q                     string              No                     -            Search query. Can be used to filter   id:96339c2618783a

                                                                                                        results or search for a specific    2ffd3fe3f0e855bc63

                                                                                                       entry by ID. Format: id: to search       b4890688

                                                                                                           for one specific record.


       Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 500 for compromised/spd/updated collection

               · If not specified, defaults to 500

               · The limit depends on the amount of data to not overload the JSON output


          · type:


               · Filters the feed to a single payment identifier type

               · Supported values:

                     · bankAccountNumber

                     · mobileNumber

                     · cryptocurrencyWallet

                     · iban

                     · bankCard

                     · qrPaymentString

                     · unknown


               · Example: /api/v2/compromised/spd/updated?seqUpdate=0&limit=500&type=mobileNumber

               · Note: in the response, the type field is returned as a human-readable label (for example, mobileNumber is returned as Mobile Number)


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types

Request Headers


                 Header              Type                   Required                                   Description                                Example


                  Accept             string                     No                         Content type accepted by the client               application/json


               Authorization         string                    Yes                    Basic authentication credentials (see Initial                Basic

                                                                                                         Steps)                          base64(LOGIN:API_KEY)


                User-Agent           string                     No                       User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                    PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                       Header                                              Description                                                   Example


                    Content-Type                                     Response content type                                            application/json


                  Content-Encoding                                      Content encoding                                                   gzip


                    Cache-Control                                    Cache control directives                            max-age=0, must-revalidate, private


                        Allow                                        Allowed HTTP methods                                                  GET


       Response Body Schema


       The response structure is similar to other compromised collections, containing special personal data information.

       Root Object
       { "count": integer, "items": [SpdItem], "seqUpdate": integer }

Field           Type         Required                          Description


                  count          integer         Yes          Number of SPD items returned in this response


                  items       array[SpdItem]     Yes                        Array of SPD objects


               seqUpdate         integer         Yes          Sequence update number at the top level of the

                                                            response. Always use this top-level value in the next

                                                          request’s seqUpdate parameter to get the next portion of

                                                                                    feeds


       SpdItem Object


                  Field           Type         Required                          Description


                    id            string         Yes                   Unique identifier of the record


                  type            string         Yes      Payment identifier type as a human-readable label (e.g.,

                                                          “Mobile Number”, “Cryptocurrency Wallet”, “Bank Account

                                                             Number”, “IBAN”, “Bank card”, “QR payment string”,

                                                            “Unknown”). Use the type query parameter to filter by

                                                                                 these values


               serviceType     string | null     No           Additional classification of the identifier (e.g., a

                                                          cryptocurrency family such as “BTCLike”, a bank code, or

                                                                         an e-wallet service name)


               ownerName       string | null     No         Name associated with the identifier, when available


               illegalScore      integer         Yes       Numeric estimate (0-100) of how likely the identifier is

                                                                    being used for unlawful transactions

Field              Type           Required                         Description


                   value             object            Yes        The payment identifier and related fields (see Value

                                                                                     Object below)


                  events        array[EventObject]     Yes        Occurrences where the identifier was observed (see

                                                                                 Event Object below)


                 evaluation        Evaluation          Yes          Evaluation object containing threat assessment


               displayOptions        object            Yes                  Display flags (e.g., isFavourite)


                 malware              array            Yes                 Associated malware references


                threatActor           array            Yes                Associated threat actor references


                   tags               array            Yes                 Tags associated with the record


                  sources             array            Yes                        Source references


                  country             array            Yes                  Associated country information


                 createdAt            string           Yes      ISO 8601 timestamp when the record was created in the

                                                                                        system


                firstSeenAt           string           Yes      ISO 8601 timestamp when the identifier was first seen


                lastSeenAt            string           Yes       ISO 8601 timestamp when the identifier was last seen


                seqUpdate            integer           Yes          Sequence update number for this specific item


       Value Object

Field          Type         Required                       Description


                   value          string         Yes       The payment identifier (e.g., wallet address, phone

                                                                       number, account number)


                   email       string | null     No            Associated email address, when available


                 bankCard      string | null     No          Associated bank card number, when available


                    iban       string | null     No                Associated IBAN, when available


       Event Object


                   Field          Type         Required                       Description


               compromisedAt      string         Yes          ISO 8601 timestamp when the identifier was

                                                                             compromised


                 detectedAt       string         Yes      ISO 8601 timestamp when the identifier was detected


                  source       object | null     No                Source of the record (name, type)


                  malware         array          Yes              Malware associated with this event


                threatActor       array          Yes            Threat actors associated with this event


                    tags          array          Yes                Tags associated with this event


                illegalScore     integer         Yes               Illegal score for this event (0-100)


       Evaluation Object


                   Field          Type         Required                       Description


               admiraltyCode      string         Yes                   Admiralty Code (e.g., “A2”)


                 credibility     integer         Yes                    Credibility score (0-100)

Field                           Type                                 Required                                                          Description


                reliability                        integer                                   Yes                                                   Reliability score (0-100)


                 severity                          string                                    Yes                                   Severity level (e.g., “red”, “orange”, “green”)


                     tlp                           string                                    Yes                            Traffic Light Protocol level (e.g., “amber”, “red”, “green”,

                                                                                                                                                            “white”)


                     ttl                           integer                                   Yes                                                     Time to live in days


       Example Request


       Note: In the examples below, set the GIB_CREDENTIALS environment variable to your LOGIN:API_KEY (your email and API key) before running the
       command.

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/compromised/spd/updated?seqUpdate=0&limit=500' \ -u "$GIB_CREDENTIALS" \ -H 'Accept:
       application/json'
       Request Filtered by Type
        curl -X GET 'https://tap.group-ib.com/api/v2/compromised/spd/updated?seqUpdate=0&limit=500&type=mobileNumber' \ -u "$GIB_CREDENTIALS" \
       -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 134418, "seqUpdate": 1751526185843, "items": [                        {    "id": "example_id_hash",         "type": "Cryptocurrency Wallet",               "serviceType":
       "BTCLike",          "ownerName": null,         "illegalScore": 100,       "displayOptions": {         "isFavourite": false         },       "value": {      "value":
       "bc1qexampleexampleexampleexampleexamplexxxxx",                              "email": null,     "bankCard": null,         "iban": null         },     "events": [       {
       "compromisedAt": "2025-04-29T00:00:00Z",                      "detectedAt": "2025-04-29T00:00:00Z",                  "source": {             "name": "Example Leak",              "type":
       "Example Leak"             },          "malware": [],        "threatActor": [],        "tags": [],         "illegalScore": 100          }     ],     "seqUpdate": 1751526184752,
        "createdAt": "2025-07-03T07:03:04.752Z",                  "firstSeenAt": "2025-04-29T00:00:00Z",              "lastSeenAt": "2025-04-29T00:00:00Z",                "evaluation": {
       "admiraltyCode": "A2",            "credibility": 80,        "reliability": 100,       "severity": "red",       "tlp": "amber",          "ttl": 30     },   "malware": [],
       "threatActor": [],       "tags": [],      "sources": [],     "country": []     } ]}

Suspicious indicators - Deface
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on defacement attacks. Defacement attacks are often conducted by web-hooligans (a form of
       vandalism) or hacktivists (politically or religiously motivated actors) whose aim is to draw attention to something. After a successful attack, the threat
       actors publish information on special sites dedicated to defacement, social media, or their personal sites.


       The section contains defaced pages along with dynamic content. In the submenu, you can also find aliases, contact details, and the names of the
       groups involved in the defacement attack.

       Collection-Specific Information


                                                   Property                                                                      Value


                                                   Method                                                                         GET


                                                    Path                                                             /api/v2/attacks/deface/updated


                                                 Collection                                                                  attacks/deface


                                              Collection Name                                                             Defacement Attacks


                                                   Module                                                                 Suspicious Indicators


                                                 Submodule                                                                       Deface


                                                    Type                                                                        Common


                                                 TTL (Days)                                                     30 (recommended, not provided in API)


                                               Admiralty Code                                                                      B2


                                                   Severity                                                                         3


                                              Collection Limit                                                          100 records per request


                                                 Rate Limit                                              1 request per 10 seconds per company per feed (see

                                                                                                                            API Limitations)

Property                                                    Value


                                            IOC Types                                             Domain, IPv4, URL


                                      Short Description                        Information on defaced websites, typically conducted

                                                                                          by web-hooligans or hacktivists.


       Request

       Request URL
        GET /api/v2/attacks/deface/updated
       Query Parameters


                 Parameter        Type                  Required   Default              Description                    Example


                 seqUpdate        integer                 No         0        Sequence update number to get        1508430053029213

                                                                               the next data chunk. Use this

                                                                                parameter to iterate through

                                                                                 feeds. The value should be

                                                                                obtained from the previous

                                                                              response’s top-level seqUpdate

                                                                             field or from /api/v2/sequence_list

                                                                              endpoint. Important: Always use

                                                                              the top-level seqUpdate field for

                                                                                          iteration.


                   limit          integer                 No        100      Limit the amount of returned data           100

                                                                                for this collection. Maximum

                                                                              allowed: 100 for this collection.


                      q           string                  No          -      Search query. Can be used to filter id:59695fabb196560

                                                                               results or search for a specific       0014bae7b

                                                                              entry by ID. Format: id: to search

                                                                                  for one specific record.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 100 for attacks/deface/updated collection

                · If not specified, defaults to 100

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific entry: q=id:

                · Supports various search types (e.g., ip:8.8.8.8, domain:example.corp)


       Request Headers


                  Header                  Type                  Required                                  Description                             Example


                   Accept                 string                   No                         Content type accepted by the client              application/json


                Authorization             string                  Yes                     Basic authentication credentials (see Initial             Basic

                                                                                                             Steps)                        base64(LOGIN:API_KEY)


                 User-Agent               string                   No                      User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                           (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                            useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                            Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                         e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                             Description                                        Example


                  Content-Type                                     Response content type                                application/json


                Content-Encoding                                      Content encoding                                          gzip


                  Cache-Control                                   Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                         GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [DefaceItem], "seqUpdate": integer }


                 Field                   Type                              Required                                Description


                 count                  integer                              Yes             Number of defacement items returned in this response


                 items             array[DefaceItem]                         Yes                          Array of defacement objects


               seqUpdate                integer                              Yes                 Sequence update number at the top level of the

                                                                                               response. Always use this top-level value in the next

                                                                                             request’s seqUpdate parameter to get the next portion of

                                                                                                                      feeds


       DefaceItem Object


                 Field                   Type                              Required                                Description


                  id                     string                              Yes             Unique identifier of the defacement (MongoDB ObjectId)


                  url                    string                              Yes                           URL of the defaced website


                siteUrl                  string                              Yes                                     Site URL

Field              Type          Required                         Description


               targetDomain            string          Yes                 Target domain that was defaced


          targetDomainProvider      string | null      No                       Target domain provider


                  targetIp           IPObject          Yes                     Target IP address object


               providerDomain          string          Yes      Provider domain (source of the defacement information)


                   source              string          Yes                         Source identifier


                    date               string          Yes        ISO 8601 timestamp when the defacement occurred


                  tsCreate             string          Yes         ISO 8601 timestamp when the record was created


                 seqUpdate            integer          Yes          Sequence update number for this specific item


                 threatActor     ThreatActorObject     Yes                        Threat actor object


                 evaluation         Evaluation         Yes          Evaluation object containing threat assessment


                  contacts             array           Yes                     Array of contact objects


                 mirrorLink            string          Yes                Link to mirror of the defaced page


                 portalLink            string          Yes                Link to the defacement in the portal


       IPObject Object


                    Field              Type          Required                         Description


                     ip                string          Yes                            IP address

Field             Type         Required                      Description


               countryCode           string         Yes             Country code (ISO 3166-1 alpha-2)


               countryName           string         Yes                       Country name


                    city          string | null     No                          City name


                  region             string         Yes                        Region name


                 provider            string         Yes                     ISP/provider name


                    asn              string         Yes                        ASN number


       ThreatActorObject Object


                   Field             Type         Required                      Description


                     id              string         Yes      Unique identifier of the threat actor (SHA-1 hash)


                   name              string         Yes                  Name of the threat actor


                  country         string | null     No              Country code (ISO 3166-1 alpha-2)


                   isAPT           boolean          Yes      Whether this is an APT group (typically false for

                                                                               defacement)


                 stixGuid         string | null     No                          STIX GUID


       Evaluation Object


                   Field             Type         Required                      Description


               admiraltyCode         string         Yes                 Admiralty Code (e.g., “B2”)


                 credibility        integer         Yes                  Credibility score (0-100)

Field                         Type                                  Required                                                      Description


               reliability                    integer                                  Yes                                                   Reliability score (0-100)


                severity                       string                                  Yes                                           Severity level (e.g., “orange”, “red”)


                   tlp                         string                                  Yes                               Traffic Light Protocol level (e.g., “amber”, “red”, “green”,

                                                                                                                                                     “white”)


                   ttl                        integer                                  Yes                                                     Time to live in days


       Example Request

       Basic Request
        curl -X GET 'https://tap.group-ib.com/api/v2/attacks/deface/updated?seqUpdate=0&limit=100' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 17197503, "items": [         {     "contacts": [],   "date": "2016-04-26T05:42:48Z",                 "evaluation": {       "admiraltyCode": "B2",             "credibility":
       80,     "reliability": 80,       "severity": "orange",      "tlp": "amber",       "ttl": 30        },    "id": "59695fabb1965600014bae7b",               "mirrorLink":
       "https://deface.ti-files.com/id:-59695fabb1965600014bae7b:",                  "portalLink":
       "https://tap-stage.ci-kuber.gibdev.net/attacks/deface?searchValue=id:59695fabb1965600014bae7b",                                "providerDomain": "defacer.id",
       "seqUpdate": 1508430053029213,               "siteUrl": "http://med-supplies.de/?sky008",               "source": "defacer.id",       "targetDomain": "med-supplies.de",
       "targetDomainProvider": null,         "targetIp": {      "asn": "AS25504",         "city": null,         "countryCode": "DE",          "countryName": "Germany",                "ip":
       "89.200.168.133",            "provider": "Vautron Rechenzentrum AG",            "region": "Europe"          },     "threatActor": {       "country": null,        "id":
       "9c94863e3602876b5e0150a7cbb926dda6556e03",                       "isAPT": false,        "name": "Sky008",             "stixGuid": null      },   "tsCreate":
       "2016-04-26T05:42:48Z",           "url": "http://med-supplies.de/?sky008"         } ], "seqUpdate": 1508430053049467 }

Suspicious indicators - DDoS
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on DDoS (Distributed Denial of Service) attacks. An attack that creates a load on the server and is
       executed simultaneously from a large number of computers (often a network of infected zombie computers is used) in order to create an artificial
       increase in requests to a resource and thereby disable it. The data is replenished and updated in real time. IOCs are included, as well as DDoS victim
       IPs.

       Collection-Specific Information


                                                  Property                                                                      Value


                                                   Method                                                                        GET


                                                    Path                                                           /api/v2/attacks/ddos/updated


                                                 Collection                                                                 attacks/ddos


                                              Collection Name                                                               DDoS Attacks


                                                   Module                                                               Suspicious Indicators


                                                 Submodule                                                                      DDoS


                                                    Type                                                                      Common


                                                 TTL (Days)                                                    30 (recommended, not provided in API)


                                               Admiralty Code                                                                    A2


                                                  Severity                                                                        3


                                              Collection Limit                                                        5000 records per request


                                                 Rate Limit                                             1 request per 10 seconds per company per feed (see

                                                                                                                           API Limitations)


                                                 IOC Types                                                                Domain, IPv4, URL

Property                                                                     Value


                                           Short Description                                                     Information on DDoS attacks.


       Note: We do not recommend using victim IPs as IOCs because it can lead to many false positives. However, CNC data can still be used for detection
       and blocking depending on your use cases.

       Request

       Request URL
        GET /api/v2/attacks/ddos/updated
       Query Parameters


                   Parameter            Type                Required              Default                    Description                     Example


                   seqUpdate           integer                No                     0             Sequence update number to get            1677065083

                                                                                                    the next data chunk. Use this

                                                                                                     parameter to iterate through

                                                                                                      feeds. The value should be

                                                                                                     obtained from the previous

                                                                                                   response’s top-level seqUpdate

                                                                                                 field or from /api/v2/sequence_list

                                                                                                   endpoint. Important: Always use

                                                                                                   the top-level seqUpdate field for

                                                                                                               iteration.


                      limit            integer                No                   5000           Limit the amount of returned data             5000

                                                                                                     for this collection. Maximum

                                                                                                   allowed: 5000 for this collection.


                       q               string                 No                     -            Search query. Can be used to filter    id:7927ec532db08b

                                                                                                    results or search for a specific     2e420b33cff2a9068

                                                                                                   entry by ID. Format: id: to search       ca8487e76

                                                                                                       for one specific record.


               apply_hunting_rules     integer                No                     0            Apply hunting rules filter. Set to 1           1

                                                                                                              to enable.

Query Parameter Details:


          · seqUpdate:


               · Each row in the database has its own unique sequence update number

               · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

               · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


               · Maximum value: 5000 for attacks/ddos/updated collection

               · If not specified, defaults to 5000

               · The limit depends on the amount of data to not overload the JSON output


          · q:


               · Can be used for general search queries

               · To search for a specific entry: q=id:

               · Supports various search types (e.g., ip:8.8.8.8, domain:example.corp)


       Request Headers


                  Header                 Type                  Required                                  Description                             Example


                  Accept                string                    No                         Content type accepted by the client              application/json


               Authorization            string                   Yes                     Basic authentication credentials (see Initial             Basic

                                                                                                            Steps)                        base64(LOGIN:API_KEY)


                 User-Agent             string                    No                      User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                          (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                           useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                           Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                        e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                           Description                                           Example


                  Content-Type                                      Response content type                                application/json


                Content-Encoding                                      Content encoding                                          gzip


                  Cache-Control                                    Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                         GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [DdosItem], "seqUpdate": integer, "settings": object }


                 Field                   Type                           Required                                    Description


                 count                   integer                           Yes                Number of DDoS attack items returned in this response


                 items              array[DdosItem]                        Yes                             Array of DDoS attack objects


               seqUpdate                 integer                           Yes                    Sequence update number at the top level of the

                                                                                                response. Always use this top-level value in the next

                                                                                              request’s seqUpdate parameter to get the next portion of

                                                                                                                       feeds


                settings                 object                            Yes                 Search settings object (contains search configuration)


       DdosItem Object


                 Field                   Type                           Required                                    Description


                   id                    string                            Yes                   Unique identifier of the DDoS attack (SHA-1 hash)

Field         Type         Required                       Description


                   cnc        CncObject        Yes             Command and control server object


                  target     TargetObject      Yes              Target object (the attacked server)


                dateBegin       string         Yes          ISO 8601 timestamp when the attack began


                 dateEnd        string         Yes          ISO 8601 timestamp when the attack ended


                 dateReg        string         Yes      ISO 8601 timestamp when the attack was registered


                 duration      integer         Yes               Duration of the attack in seconds


                protocol        string         Yes         Protocol used in the attack (e.g., “udp”, “tcp”)


                  type          string         Yes         Type of DDoS attack (e.g., “DNS Reflection”)


               seqUpdate       integer         Yes        Sequence update number for this specific item


                 source         string         Yes                   Source of the attack data


               sourceRowId      string         Yes                     Source row identifier


                  oldId      string | null     No                 Previous identifier (if migrated)


                 stixGuid    string | null     No                            STIX GUID


                malware      object | null     No                   Associated malware object


               threatActor   object | null     No                 Associated threat actor object


                evaluation    Evaluation       Yes        Evaluation object containing threat assessment


               requestData   RequestData       Yes                      Request data object

Field              Type          Required               Description


               messageLink        string | null       No                 Link to message


               displayOptions   DisplayOptions        Yes             Display options object


       CncObject Object


                   Field              Type          Required               Description


                    cnc              string           Yes      Command and control server identifier


                  domain          string | null       No                  Domain name


                    ipv4        IPv4Object | null     No               IPv4 address object


                    ipv6        IPv6Object | null     No               IPv6 address object


                    url           string | null       No                       URL


                    port          integer | null      No                   Port number


       TargetObject Object


                   Field              Type          Required               Description


                    ipv4        IPv4Object | null     No         IPv4 address object of the target


                  domain          string | null       No            Domain name of the target


                    url           string | null       No                 URL of the target


                    port             integer          Yes            Port number of the target


                 category         string | null       No              Category of the target

Field          Type         Required                          Description


               domainsCount      integer         Yes          Number of domains associated with the target


       IPv4Object Object


                   Field          Type         Required                          Description


                     ip           string         Yes                            IPv4 address


               countryCode     string | null     No                  Country code (ISO 3166-1 alpha-2)


               countryName     string | null     No                             Country name


                    city       string | null     No                               City name


                  region       string | null     No                             Region name


                 provider      string | null     No                          ISP/provider name


                    asn        string | null     No                              ASN number


       Evaluation Object


                   Field          Type         Required                          Description


               admiraltyCode      string         Yes                     Admiralty Code (e.g., “C2”)


                 credibility     integer         Yes                      Credibility score (0-100)


                 reliability     integer         Yes                       Reliability score (0-100)


                  severity        string         Yes                 Severity level (e.g., “orange”, “red”)


                     tlp          string         Yes      Traffic Light Protocol level (e.g., “green”, “amber”, “red”,

                                                                                   “white”)

Field                       Type                                  Required                                                           Description


                        ttl                       integer                                  Yes                                                          Time to live in days


       RequestData Object


                       Field                       Type                                  Required                                                           Description


                       link                     string | null                              No                                                           Link to request data


                   headers                         object                                  Yes                                                      HTTP headers object


                headersHash                     string | null                              No                                                            Hash of headers


                       body                     string | null                              No                                                              Request body


                  bodyHash                      string | null                              No                                                       Hash of request body


       DisplayOptions Object


                       Field                       Type                                  Required                                                           Description


                 isFavourite                      boolean                                  Yes                                        Whether the item is marked as favourite


                  isHidden                        boolean                                  Yes                                                   Whether the item is hidden


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/attacks/ddos/updated?seqUpdate=0&limit=5000' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Request with Hunting Rules
       curl -X GET 'https://tap.group-ib.com/api/v2/attacks/ddos/updated?seqUpdate=0&limit=5000&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H
       'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 44739317, "items": [             {      "id": "7927ec532db08b2e420b33cff2a9068ca8487e76",                        "cnc": {        "cnc": "6lxdx.s3.amazonaws.com",
       "port": null,           "domain": "6lxdx.s3.amazonaws.com",              "ipv4": null,       "ipv6": null,     "url": "http://6lxdx.s3.amazonaws.com"                      },
       "dateBegin": "2019-10-23T05:34:25+00:00",                    "dateEnd": "2019-10-23T05:35:16+00:00",             "dateReg": "2019-10-23T00:00:00+00:00",                         "malware":
       null,      "evaluation": {         "admiraltyCode": "C2",          "credibility": 70,     "reliability": 60,       "severity": "orange",              "tlp": "green",           "ttl": 30   },
        "messageLink": null,            "oldId": "192868705",         "duration": 51,     "protocol": "udp",        "seqUpdate": 1677065083,                  "source": "honeypot_logs:1",
       "sourceRowId": "11054565",               "stixGuid": "9232056c-0c7d-21a7-ac4f-a7fa243adc57",                   "target": {           "ipv4": {         "asn": null,        "city": "Fairfield",
                "region": "Connecticut",           "provider": "Amazon.com",              "countryCode": "US",           "countryName": "United States",                       "ip": "3.15.14.164"
           },      "url": null,        "category": null,        "domainsCount": 0,        "port": 5353,         "domain": null         },       "threatActor": null,         "requestData": {
       "link": null,          "headers": {},     "headersHash": null,          "body": null,     "bodyHash": null          },       "type": "DNS Reflection",            "displayOptions": {
       "isHidden": false,            "isFavourite": false       }   } ], "settings": {    "search": {      "tags": ["target_ip_country_name", "target_category",

"cnc_ip_country_name", "malware", "type", "source", "id"],    "fields": ["target_ip", "ip", "target_domain", "domain", "cnc_ip", "malware", "type", "source",
       "id"],   "sorts": ["last_seen", "date_reg", "seqUpdate"]   } }, "seqUpdate": 1677065083 }

Suspicious indicators - Open Proxies IP
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on open proxy servers. The Open proxy collection shows information about lists of proxy servers that are
       publicly available on various Internet resources related to anonymity. In addition, proxy servers may be configured as open proxies intentionally or as a
       result of misconfiguration or breaches. These records can be used to identify or block connections from and to open proxy servers.

       Collection-Specific Information


                                                  Property                                                                      Value


                                                   Method                                                                        GET


                                                    Path                                                     /api/v2/suspicious_ip/open_proxy/updated


                                                 Collection                                                           suspicious_ip/open_proxy


                                              Collection Name                                                            Open Proxy Servers


                                                   Module                                                               Suspicious Indicators


                                                 Submodule                                                                    Open proxy


                                                    Type                                                                       Common


                                                 TTL (Days)                                                    15 (recommended, not provided in API)


                                               Admiralty Code                                                                     C3


                                                  Severity                                                                         3


                                              Collection Limit                                                         500 records per request


                                                 Rate Limit                                              1 request per 10 seconds per company per feed (see

                                                                                                                           API Limitations)


                                                 IOC Types                                                                       IPv4

Property                                                    Value


                                         Short Description                      Open proxy servers identified by the Group-IB TI system.


       Request

       Request URL
        GET /api/v2/suspicious_ip/open_proxy/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                     Example


                   seqUpdate         integer                No         0        Sequence update number to get         1671657409977576

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        500      Limit the amount of returned data            500

                                                                                  for this collection. Maximum

                                                                                allowed: 500 for this collection.


                       q             string                 No          -      Search query. Can be used to filter    “188.250.243.135”

                                                                                 results or search for a specific

                                                                                entry by IP. Format: “” to search

                                                                                    for one specific record.


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1          1

                                                                                           to enable.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 500 for suspicious_ip/open_proxy/updated collection

                · If not specified, defaults to 500

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific IP: q=""

                · Supports various search types


       Request Headers


                  Header                  Type                  Required                               Description                             Example


                   Accept                 string                   No                      Content type accepted by the client              application/json


                Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                          Steps)                        base64(LOGIN:API_KEY)


                 User-Agent               string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                             Description                                                   Example


                  Content-Type                                      Response content type                                        application/json


                Content-Encoding                                      Content encoding                                                  gzip


                  Cache-Control                                    Cache control directives                            max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                                 GET


       Response Body Schema


       The response structure is similar to suspicious_ip/vpn/updated, containing open proxy server information with IP addresses, dates, evaluation data,
       and proxy type information.

       Root Object
       { "count": integer, "items": [OpenProxyItem], "seqUpdate": integer }


                 Field                     Type                         Required                                           Description


                 count                    integer                          Yes                        Number of open proxy items returned in this response


                 items               array[OpenProxyIte                    Yes                                     Array of open proxy objects

                                            m]


               seqUpdate                  integer                          Yes                           Sequence update number at the top level of the

                                                                                                       response. Always use this top-level value in the next

                                                                                                    request’s seqUpdate parameter to get the next portion of

                                                                                                                               feeds


       OpenProxyItem Object


       The structure is similar to VpnItem, containing IP address, dates, evaluation data, and open proxy-specific metadata.

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/open_proxy/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/open_proxy/updated?seqUpdate=0&limit=500&apply_hunting_rules=1' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)

The response structure is similar to suspicious_ip/vpn/updated, with items containing open proxy server information.
        { "count": 500000, "items": [   {      "id": "188.250.243.135",   "dateFirstSeen": "2021-04-22T12:43:38+00:00",           "dateLastSeen":
       "2021-04-22T12:43:38+00:00",         "evaluation": {    "admiraltyCode": "C3",   "credibility": 50,   "reliability": 50,       "severity": "green",   "tlp":
       "amber",     "ttl": 15   },   "seqUpdate": 1671657409977576          } ], "seqUpdate": 1671657410005695 }

Suspicious indicators - Phishing
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on phishing URLs. The Phishing displays information about various phishing resources (including sites
       masqueraded as Google, Microsoft, etc.). Group-IB collects this data with the help of Passive-DNS analysis performed by Managed XDR
       (ManagedExtended Detection and Response) systems, alerts received by CERT-GIB, tracked SPAM messages, malicious contextual advertising, new
       domain names, and other valuable data.

       Collection-Specific Information


                                                  Property                                                                   Value


                                                   Method                                                                    GET


                                                    Path                                                   /api/v2/attacks/phishing_group/updated


                                                 Collection                                                         attacks/phishing_group


                                              Collection Name                                                          Phishing Groups


                                                   Module                                                            Suspicious Indicators


                                                 Submodule                                                                 Phishing


                                                    Type                                                                   Common


                                                 TTL (Days)                                                 30 (recommended, not provided in API)


                                               Admiralty Code                                                               A2-A3


                                                  Severity                                                                     6


                                              Collection Limit                                                     1000 records per request


                                                 Rate Limit                                          1 request per 10 seconds per company per feed (see

                                                                                                                        API Limitations)


                                                 IOC Types                                                            Domain, IPv4, URL

Property                                                    Value


                                         Short Description                           Information about various phishing resources.


       Request

       Request URL
        GET /api/v2/attacks/phishing_group/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                      Example


                   seqUpdate         integer                No         0        Sequence update number to get         1401373055098642

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        1000     Limit the amount of returned data            1000

                                                                                  for this collection. Maximum

                                                                                allowed: 1000 for this collection.


                       q             string                 No          -      Search query. Can be used to filter id:74ee810f703000d

                                                                                 results or search for a specific     318bb144a1307abc

                                                                                entry by ID. Format: id: to search    e9c05abee41465c30

                                                                                    for one specific record.          303922156e7ed36a


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1          1

                                                                                           to enable.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 1000 for attacks/phishing_group/updated collection

                · If not specified, defaults to 1000

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific entry: q=id:

                · Supports various search types (e.g., ip:8.8.8.8, domain:example.corp)


       Request Headers


                  Header                  Type                  Required                                  Description                             Example


                   Accept                string                    No                         Content type accepted by the client              application/json


                Authorization            string                   Yes                     Basic authentication credentials (see Initial             Basic

                                                                                                             Steps)                        base64(LOGIN:API_KEY)


                 User-Agent              string                    No                      User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                           (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                            useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                            Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                         e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                           Description                                           Example


                  Content-Type                                    Response content type                                 application/json


                Content-Encoding                                     Content encoding                                          gzip


                 Cache-Control                                    Cache control directives                     max-age=0, must-revalidate, private


                         Allow                                    Allowed HTTP methods                                         GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [PhishingGroupItem], "seqUpdate": integer }


                 Field                   Type                          Required                                    Description


                 count                  integer                           Yes                    Number of phishing group items returned in this

                                                                                                                    response


                 items             array[PhishingGrou                     Yes                            Array of phishing group objects

                                        pItem]


               seqUpdate                integer                           Yes                    Sequence update number at the top level of the

                                                                                               response. Always use this top-level value in the next

                                                                                             request’s seqUpdate parameter to get the next portion of

                                                                                                                      feeds


       PhishingGroupItem Object


                 Field                   Type                          Required                                    Description


                  id                     string                           Yes                 Unique identifier of the phishing group (SHA-256 hash)


                 brand                   string                           Yes                           Brand name being impersonated


                domain                   string                           Yes                           Domain name of the phishing site

Field               Type           Required                      Description


                 domainTitle           string            Yes                     Title of the domain


                countPhishing          integer           Yes           Number of phishing URLs in this group


                 seqUpdate             integer           Yes      Sequence update number for this specific item


                    date             DateObject          Yes        Date object containing various timestamps


                 domainInfo         DomainInfo           Yes                 Domain information object


                      ip           array[IPObject]       Yes                 Array of IP address objects


                  objective         array[string]        Yes      Array of objective strings (e.g., [“Login harvest”])


                 evaluation          Evaluation          Yes      Evaluation object containing threat assessment


                   status              integer           Yes                   Status code (1 = active)


                falsePositive         boolean            Yes         Whether this is marked as a false positive


                  whitelist           boolean            Yes                 Whether this is whitelisted


                groupLifetime          integer           Yes                  Group lifetime in seconds


                   source           array[string]        Yes                  Array of source identifiers


                  signature       SignatureObject        Yes                       Signature object


               phishingKitArray         array            Yes               Array of phishing kit references


                 screenshot       ScreenshotObject       Yes                      Screenshot object


                 uniqueTitles     array[TitleObject]     Yes                 Array of unique title objects

Field               Type           Required                        Description


                threatActor     ThreatActorObject       Yes                       Threat actor object


                  phishing      array[PhishingItem]     Yes            Array of individual phishing URL objects


                 urlListLink           string           Yes              Link to URL list (can be empty string)


               displayOptions     DisplayOptions        Yes                     Display options object


       DateObject Object


                   Field               Type           Required                        Description


                   added               string           Yes        ISO 8601 timestamp when the group was added


                  detected             string           Yes       ISO 8601 timestamp when the group was detected


                  blocked              string           Yes        ISO 8601 timestamp when the group was blocked


                  updated              string           Yes      ISO 8601 timestamp when the group was last updated


               blockedIndexed       string | null       No       ISO 8601 timestamp when the group was blocked and

                                                                                       indexed


       DomainInfo Object


                   Field               Type           Required                        Description


                  domain               string           Yes                         Domain name


                domainPuny             string           Yes                    Punycode domain name

Field           Type         Required               Description


                     tld           string         Yes               Top-level domain


                    title          string         Yes      Domain title (can be empty string)


                 category          array          Yes           Array of category strings


                 registered     string | null     No                Registration date


               expirationDate   string | null     No                 Expiration date


                 registrar      string | null     No                 Registrar name


       IPObject Object


                   Field           Type         Required               Description


                     ip            string         Yes                   IP address


               countryCode         string         Yes      Country code (ISO 3166-1 alpha-2)


               countryName         string         Yes                 Country name


                  provider         string         Yes              ISP/provider name


       Evaluation Object


                   Field           Type         Required               Description


               admiraltyCode       string         Yes       Admiralty Code (e.g., “C3”, “A2”)


                 credibility      integer         Yes           Credibility score (0-100)


                 reliability      integer         Yes           Reliability score (0-100)


                  severity         string         Yes      Severity level (e.g., “red”, “orange”)

Field             Type         Required                          Description


                   tlp              string         Yes      Traffic Light Protocol level (e.g., “amber”, “red”, “green”,

                                                                                     “white”)


                   ttl             integer         Yes                   Time to live in days (usually 0)


       SignatureObject Object


                  Field             Type         Required                          Description


                resource         array[string]     Yes                 Array of resource signature strings


                 screen          array[string]     Yes                  Array of screen signature strings


                 manual          array[string]     Yes                 Array of manual signature strings


       ScreenshotObject Object


                  Field             Type         Required                          Description


                pageHtml          FileObject       Yes                       HTML page file object


               pageScreen         FileObject       Yes                        Screenshot file object


       FileObject Object


                  Field             Type         Required                          Description


               hashSha256           string         Yes                      SHA-256 hash of the file


                 filetype           string         Yes                               File type


                filename            string         Yes                              File name


                 mime               string         Yes                              MIME type

Field              Type        Required                    Description


               fileHashMd5            string        Yes             MD5 hash (can be empty string)


       TitleObject Object


                   Field              Type        Required                    Description


                   title              string        Yes                        Title string


               faviconHashes      FaviconHashes     Yes                   Favicon hash object


       FaviconHashes Object


                   Field              Type        Required                    Description


                   md5                string        Yes             MD5 hash (can be empty string)


                   sha1               string        Yes             SHA-1 hash (can be empty string)


                  sha256              string        Yes           SHA-256 hash (can be empty string)


       ThreatActorObject Object


                   Field              Type        Required                    Description


                    id                string        Yes           Threat actor ID (can be empty string)


                   name               string        Yes         Threat actor name (can be empty string)


               nameIndexed            string        Yes      Indexed threat actor name (can be empty string)


                  isAPT              boolean        Yes               Whether this is an APT group


       PhishingItem Object

Field                  Type          Required                       Description


                    id                   string          Yes      Unique identifier of the phishing URL (SHA-256 hash)


                   url                   string          Yes                         Phishing URL


                   title                 string          Yes                Page title (can be empty string)


                  date             PhishingDateObjec     Yes               Date object for this phishing URL

                                            t


                  status                integer          Yes                    Status code (1 = active)


                objective             array[string]      Yes                   Array of objective strings


                 source               array[string]      Yes                   Array of source identifiers


                  client              object | null      No                          Client object


                 domain            PhishingDomainOb      Yes                        Domain object

                                          ject


                    ip             PhishingIPObject      Yes                       IP address object


               phishingKit               array           Yes                Array of phishing kit references


                 screen            ScreenshotObject      Yes                       Screenshot object


               renderedUrls           array[string]      Yes                    Array of rendered URLs


       PhishingDateObject Object


                  Field                  Type          Required                       Description


                  added                  string          Yes         ISO 8601 timestamp when the URL was added

Field              Type     Required                    Description


                detected             string     Yes      ISO 8601 timestamp when the URL was detected


                 blocked             string     Yes      ISO 8601 timestamp when the URL was blocked


       PhishingDomainObject Object


                  Field              Type     Required                    Description


                 domain              string     Yes                      Domain name


                  puny               string     Yes                 Punycode domain name


                    tld              string     Yes                    Top-level domain


                   title             string     Yes            Domain title (can be empty string)


                category             array      Yes                 Array of category strings


                registered           string     Yes          Registration date (can be empty string)


                expiration           string     Yes           Expiration date (can be empty string)


                 registrar           string     Yes           Registrar name (can be empty string)


       PhishingIPObject Object


                  Field              Type     Required                    Description


                    ip               string     Yes                        IP address


               countryCode           string     Yes            Country code (ISO 3166-1 alpha-2)


               countryName           string     Yes                      Country name


                   city              string     Yes             City name (can be empty string)

Field                                Type                                                 Required                                                                Description


                    provider                               string                                                  Yes                                                              ISP/provider name


       DisplayOptions Object


                      Field                                Type                                                 Required                                                                Description


                   isFavourite                           boolean                                                   Yes                                             Whether the item is marked as favourite


                    isHidden                             boolean                                                   Yes                                                       Whether the item is hidden


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/attacks/phishing_group/updated?seqUpdate=0&limit=1000' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/attacks/phishing_group/updated?seqUpdate=0&limit=1000&apply_hunting_rules=1' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 8439182, "items": [                    {     "brand": "VKontakte (vk.com)",                             "countPhishing": 1,            "date": {         "blocked": "2016-04-27T14:55:20+03:00",
           "added": "2014-05-29T18:17:35+04:00",                                "detected": "2014-05-29T18:17:35+04:00",                                 "blockedIndexed": null,                 "updated":
       "2020-12-24T04:04:37+03:00"                        },    "domain": "vkontakte.0catch.com",                               "domainInfo": {                "domain": "vkontakte.0catch.com",
       "domainPuny": "vkontakte.0catch.com",                            "expirationDate": null,                       "registered": null,            "registrar": null,              "tld": "com",             "title": "",
       "category": []         },          "domainTitle": "Login | VKontakte",                        "evaluation": {              "admiraltyCode": "C3",                "credibility": 50,             "reliability": 50,
       "severity": "red",             "tlp": "amber",           "ttl": 0            },         "falsePositive": false,            "groupLifetime": 1006417,                  "id":
       "74ee810f703000d318bb144a1307abce9c05abee41465c30303922156e7ed36a",                                                                 "ip": [         {        "ip": "69.27.174.10",                  "countryCode": "US",
               "countryName": "United States",                      "provider": "U.s. Colo, LLC (uscolo)"                           }      ],      "objective": ["Login harvest"],                 "phishingKitArray": [],
       "screenshot": {               "pageHtml": {              "hashSha256": "h:7297723b6093126c7ab2f037beac6cac256207c7492acc6b923f2cffe1fab5b4",
       "filetype": "pageHtml",                     "filename": "h:7297723b6093126c7ab2f037beac6cac256207c7492acc6b923f2cffe1fab5b4",                                                                     "mime": "text/html",
          "fileHashMd5": ""                 },        "pageScreen": {                    "hashSha256": "s:1118760d55ebd9969f89fbc786b93276eb631cea84765d8f5d5bb908217bf632",
               "filetype": "pageScreen",                  "filename": "s:1118760d55ebd9969f89fbc786b93276eb631cea84765d8f5d5bb908217bf632",                                                                           "mime":
       "image/jpeg",                 "fileHashMd5": ""              }          },        "seqUpdate": 1401373055098642,                          "signature": {            "resource": [],             "screen": [],           "manual":
       ["VK_vhod"]           },       "source": ["Cert", "ci-VirusTotal", "openphish"],                             "status": 1,         "threatActor": {             "id": "",        "name": "",              "nameIndexed": "",
          "isAPT": false             },      "uniqueTitles": [             {                  "faviconHashes": {                 "md5": "",              "sha1": "",               "sha256": ""            },           "title": ""       }
          ],      "urlListLink": "",             "whitelist": false,           "phishing": [              {          "id":
       "844923a0d22aa6141c5aa3d4e9997eea523ab0a1bb70898945e49befa57f3454",                                                                      "url": "http://vkontakte.0catch.com",                          "date": {
       "blocked": "2016-04-27T14:55:20+03:00",                                      "added": "2014-05-29T18:17:35+04:00",                                "detected": "2014-05-29T18:17:35+04:00"                                },
       "status": 1,               "objective": ["Login harvest"],                        "source": ["Cert", "openphish", "ci-VirusTotal"],                         "client": null,              "title": "",           "domain": {
          "registrar": "",                "domain": "vkontakte.0catch.com",                                   "registered": "",           "title": "",            "category": [],                "expiration": "",               "tld":
       "com",            "puny": "vkontakte.0catch.com"                                  },         "ip": {               "countryCode": "US",                 "city": "Provo",             "provider": "U.s. Colo, LLC
       (uscolo)",                 "ip": "69.27.174.10",                 "countryName": "United States"                              },          "phishingKit": [],                "screen": {            "pageHtml": {
       "hashSha256": "h:7297723b6093126c7ab2f037beac6cac256207c7492acc6b923f2cffe1fab5b4",                                                                              "filetype": "pageHtml",                        "filename":
       "h:7297723b6093126c7ab2f037beac6cac256207c7492acc6b923f2cffe1fab5b4",                                                                      "mime": "text/html",                    "fileHashMd5": ""                     },
       "pageScreen": {                      "hashSha256": "s:1118760d55ebd9969f89fbc786b93276eb631cea84765d8f5d5bb908217bf632",                                                                                 "filetype":
       "pageScreen",                      "filename": "s:1118760d55ebd9969f89fbc786b93276eb631cea84765d8f5d5bb908217bf632",                                                                           "mime": "image/jpeg",
               "fileHashMd5": ""                  }        },       "renderedUrls": [""]                       }     ],      "displayOptions": {               "isFavourite": false,              "isHidden": false              }    } ],

"seqUpdate": 1430425612098642 }

Suspicious indicators - Scanning IP
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on scanning IP addresses. This collection contains data about public and private IP-addresses that were
       identified by the Group-IB TI system. These records can be used to identify or block connections between the corporate network and servers detected.

       Collection-Specific Information


                                                  Property                                                                   Value


                                                   Method                                                                     GET


                                                    Path                                                    /api/v2/suspicious_ip/scanner/updated


                                                 Collection                                                          suspicious_ip/scanner


                                              Collection Name                                                       Scanning IP Addresses


                                                   Module                                                            Suspicious Indicators


                                                 Submodule                                                                Scanning IP


                                                    Type                                                                   Common


                                                 TTL (Days)                                                 15 (recommended, not provided in API)


                                               Admiralty Code                                                                 C3


                                                  Severity                                                                     1


                                              Collection Limit                                                      500 records per request


                                                 Rate Limit                                           1 request per 10 seconds per company per feed (see

                                                                                                                        API Limitations)


                                                 IOC Types                                                                    IPv4

Property                                                    Value


                                         Short Description                          IP addresses identified as performing scanning

                                                                                          activities by the Group-IB TI system.


       Request

       Request URL
        GET /api/v2/suspicious_ip/scanner/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                     Example


                   seqUpdate         integer                No         0        Sequence update number to get         1671657409977576

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        500      Limit the amount of returned data            500

                                                                                  for this collection. Maximum

                                                                                allowed: 500 for this collection.


                       q             string                 No          -      Search query. Can be used to filter    “188.250.243.135”

                                                                                 results or search for a specific

                                                                                entry by IP. Format: “” to search

                                                                                    for one specific record.


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1          1

                                                                                           to enable.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 500 for suspicious_ip/scanner/updated collection

                · If not specified, defaults to 500

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific IP: q=""

                · Supports various search types


       Request Headers


                  Header                  Type                  Required                               Description                             Example


                   Accept                 string                   No                      Content type accepted by the client              application/json


                Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                          Steps)                        base64(LOGIN:API_KEY)


                 User-Agent               string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                                Description                                                Example


                  Content-Type                                      Response content type                                         application/json


                Content-Encoding                                       Content encoding                                                 gzip


                  Cache-Control                                     Cache control directives                            max-age=0, must-revalidate, private


                         Allow                                      Allowed HTTP methods                                                GET


       Response Body Schema


       The response structure is similar to suspicious_ip/vpn/updated, containing scanning IP information with IP addresses, dates, evaluation data, and
       scanning activity metadata.

       Root Object
       { "count": integer, "items": [ScannerItem], "seqUpdate": integer }


                 Field                     Type                          Required                                           Description


                 count                    integer                            Yes                        Number of scanner items returned in this response


                 items               array[ScannerItem]                      Yes                                     Array of scanner IP objects


               seqUpdate                  integer                            Yes                          Sequence update number at the top level of the

                                                                                                        response. Always use this top-level value in the next

                                                                                                     request’s seqUpdate parameter to get the next portion of

                                                                                                                               feeds


       ScannerItem Object


       The structure is similar to VpnItem, containing IP address, dates, evaluation data, and scanning activity-specific metadata.

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/scanner/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/scanner/updated?seqUpdate=0&limit=500&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \
        -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)

The response structure is similar to suspicious_ip/vpn/updated, with items containing scanning IP information.
        { "count": 500000, "items": [   {      "id": "188.250.243.135",   "dateFirstSeen": "2021-04-22T12:43:38+00:00",           "dateLastSeen":
       "2021-04-22T12:43:38+00:00",         "evaluation": {    "admiraltyCode": "C3",   "credibility": 50,   "reliability": 50,       "severity": "green",   "tlp":
       "amber",     "ttl": 15   },   "seqUpdate": 1671657409977576          } ], "seqUpdate": 1671657410005695 }

Suspicious indicators - Socks Proxy IP
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on SOCKS proxy servers. The Socks proxy collection shows information about addresses where malware
       that turns infected computers into SOCKS proxies has been installed. Such computers (bots) are rented out and used in various attacks to ensure the
       attacker as much anonymity as possible. These records can be used to identify or block connections from or to SOCKS proxy servers.

       Collection-Specific Information


                                                  Property                                                                   Value


                                                   Method                                                                    GET


                                                    Path                                                 /api/v2/suspicious_ip/socks_proxy/updated


                                                 Collection                                                       suspicious_ip/socks_proxy


                                              Collection Name                                                        SOCKS Proxy Servers


                                                   Module                                                            Suspicious Indicators


                                                 Submodule                                                               Socks proxy


                                                    Type                                                                   Common


                                                 TTL (Days)                                                  2 (recommended, not provided in API)


                                               Admiralty Code                                                                 A1


                                                  Severity                                                                     3


                                              Collection Limit                                                      500 records per request


                                                 Rate Limit                                          1 request per 10 seconds per company per feed (see

                                                                                                                       API Limitations)


                                                 IOC Types                                                                   IPv4

Property                                                    Value


                                         Short Description                         SOCKS proxy servers identified by the Group-IB TI

                                                                                                         system.


       Request

       Request URL
        GET /api/v2/suspicious_ip/socks_proxy/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                     Example


                   seqUpdate         integer                No         0        Sequence update number to get         1671657409977576

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        500      Limit the amount of returned data            500

                                                                                  for this collection. Maximum

                                                                                allowed: 500 for this collection.


                       q             string                 No          -      Search query. Can be used to filter    “188.250.243.135”

                                                                                 results or search for a specific

                                                                                entry by IP. Format: “” to search

                                                                                    for one specific record.


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1          1

                                                                                           to enable.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 500 for suspicious_ip/socks_proxy/updated collection

                · If not specified, defaults to 500

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific IP: q=""

                · Supports various search types


       Request Headers


                  Header                  Type                  Required                               Description                             Example


                   Accept                 string                   No                      Content type accepted by the client              application/json


                Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                          Steps)                        base64(LOGIN:API_KEY)


                 User-Agent               string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                             Description                                                    Example


                  Content-Type                                     Response content type                                          application/json


                Content-Encoding                                      Content encoding                                                   gzip


                  Cache-Control                                    Cache control directives                           max-age=0, must-revalidate, private


                         Allow                                     Allowed HTTP methods                                                  GET


       Response Body Schema


       The response structure is similar to suspicious_ip/vpn/updated, containing SOCKS proxy server information with IP addresses, dates, evaluation data,
       and proxy type information.

       Root Object
       { "count": integer, "items": [SocksProxyItem], "seqUpdate": integer }


                 Field                     Type                         Required                                          Description


                 count                    integer                         Yes                       Number of SOCKS proxy items returned in this response


                 items               array[SocksProxyIt                   Yes                                    Array of SOCKS proxy objects

                                            em]


               seqUpdate                  integer                         Yes                           Sequence update number at the top level of the

                                                                                                      response. Always use this top-level value in the next

                                                                                                    request’s seqUpdate parameter to get the next portion of

                                                                                                                                feeds


       SocksProxyItem Object


       The structure is similar to VpnItem, containing IP address, dates, evaluation data, and SOCKS proxy-specific metadata.

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/socks_proxy/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/socks_proxy/updated?seqUpdate=0&limit=500&apply_hunting_rules=1' \ -u
       'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)

The response structure is similar to suspicious_ip/vpn/updated, with items containing SOCKS proxy server information.
        { "count": 500000, "items": [   {      "id": "188.250.243.135",   "dateFirstSeen": "2021-04-22T12:43:38+00:00",       "dateLastSeen":
       "2021-04-22T12:43:38+00:00",         "evaluation": {    "admiraltyCode": "A1",   "credibility": 100,   "reliability": 100,   "severity": "green",   "tlp":
       "amber",     "ttl": 2   },   "seqUpdate": 1671657409977576         } ], "seqUpdate": 1671657410005695 }

Suspicious indicators - TOR IP
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on Tor nodes. The Tor collection displays data about Tor exit nodes, which are the final Tor relays in the
       circuit. The nodes act as an intermediary between a Tor client and public Internet. These records can be used to identify or block connections from Tor
       network.

       Collection-Specific Information


                                                  Property                                                                      Value


                                                   Method                                                                        GET


                                                    Path                                                      /api/v2/suspicious_ip/tor_node/updated


                                                 Collection                                                            suspicious_ip/tor_node


                                              Collection Name                                                                Tor Nodes


                                                   Module                                                               Suspicious Indicators


                                                 Submodule                                                                       Tor


                                                    Type                                                                      Common


                                                 TTL (Days)                                                    30 (recommended, not provided in API)


                                               Admiralty Code                                                                    A1


                                                  Severity                                                                        3


                                              Collection Limit                                                         500 records per request


                                                 Rate Limit                                             1 request per 10 seconds per company per feed (see

                                                                                                                           API Limitations)


                                                 IOC Types                                                                      IPv4

Property                                                    Value


                                         Short Description                          Tor exit nodes and relay nodes identified by the

                                                                                                   Group-IB TI system.


       Request

       Request URL
        GET /api/v2/suspicious_ip/tor_node/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                     Example


                   seqUpdate         integer                No         0        Sequence update number to get         1671657409977576

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        500      Limit the amount of returned data            500

                                                                                  for this collection. Maximum

                                                                                allowed: 500 for this collection.


                       q             string                 No          -      Search query. Can be used to filter    “188.250.243.135”

                                                                                 results or search for a specific

                                                                                entry by IP. Format: “” to search

                                                                                    for one specific record.


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1          1

                                                                                           to enable.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 500 for suspicious_ip/tor_node/updated collection

                · If not specified, defaults to 500

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific IP: q=""

                · Supports various search types


       Request Headers


                  Header                  Type                  Required                               Description                             Example


                   Accept                 string                   No                      Content type accepted by the client              application/json


                Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                          Steps)                        base64(LOGIN:API_KEY)


                 User-Agent               string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                               Description                                                   Example


                  Content-Type                                       Response content type                                          application/json


                Content-Encoding                                        Content encoding                                                  gzip


                  Cache-Control                                      Cache control directives                             max-age=0, must-revalidate, private


                         Allow                                       Allowed HTTP methods                                                 GET


       Response Body Schema


       The response structure is similar to suspicious_ip/vpn/updated, containing Tor node information with IP addresses, dates, evaluation data, and node
       type information.

       Root Object
       { "count": integer, "items": [TorNodeItem], "seqUpdate": integer }


                 Field                    Type                            Required                                            Description


                 count                   integer                             Yes                         Number of Tor node items returned in this response


                 items             array[TorNodeItem]                        Yes                                       Array of Tor node objects


               seqUpdate                 integer                             Yes                            Sequence update number at the top level of the

                                                                                                         response. Always use this top-level value in the next

                                                                                                       request’s seqUpdate parameter to get the next portion of

                                                                                                                                 feeds


       TorNodeItem Object


       The structure is similar to VpnItem, containing IP address, dates, evaluation data, and Tor-specific metadata (node type, exit/relay status, etc.).

       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/tor_node/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/tor_node/updated?seqUpdate=0&limit=500&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY'
       \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)

The response structure is similar to suspicious_ip/vpn/updated, with items containing Tor node information.
        { "count": 500000, "items": [   {      "id": "188.250.243.135",   "dateFirstSeen": "2021-04-22T12:43:38+00:00",       "dateLastSeen":
       "2021-04-22T12:43:38+00:00",         "evaluation": {    "admiraltyCode": "A1",   "credibility": 100,   "reliability": 100,   "severity": "green",   "tlp":
       "amber",     "ttl": 30   },   "seqUpdate": 1671657409977576          } ], "seqUpdate": 1671657410005695 }

Suspicious indicators - VPN IP
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This collection provides updated information on VPN servers. This collection contains information about public and private VPNs servers that were
       identified by the Group-IB TI system. These records can be used to identify or block connections between the corporate network and servers detected.

       Collection-Specific Information


                                                  Property                                                                   Value


                                                   Method                                                                    GET


                                                    Path                                                      /api/v2/suspicious_ip/vpn/updated


                                                 Collection                                                           suspicious_ip/vpn


                                              Collection Name                                                            VPN Servers


                                                   Module                                                            Suspicious Indicators


                                                 Submodule                                                                   VPN


                                                    Type                                                                   Common


                                                 TTL (Days)                                                 30 (recommended, not provided in API)


                                               Admiralty Code                                                                 A2


                                                  Severity                                                                     1


                                              Collection Limit                                                      500 records per request


                                                 Rate Limit                                          1 request per 10 seconds per company per feed (see

                                                                                                                       API Limitations)


                                                 IOC Types                                                                   IPv4

Property                                                    Value


                                         Short Description                          Public and private VPN servers identified by the

                                                                                                   Group-IB TI system.


       Request

       Request URL
        GET /api/v2/suspicious_ip/vpn/updated
       Query Parameters


                   Parameter         Type                 Required   Default              Description                     Example


                   seqUpdate         integer                No         0        Sequence update number to get         1671657409977576

                                                                                 the next data chunk. Use this

                                                                                  parameter to iterate through

                                                                                   feeds. The value should be

                                                                                  obtained from the previous

                                                                                response’s top-level seqUpdate

                                                                               field or from /api/v2/sequence_list

                                                                                endpoint. Important: Always use

                                                                                the top-level seqUpdate field for

                                                                                            iteration.


                      limit          integer                No        500      Limit the amount of returned data            500

                                                                                  for this collection. Maximum

                                                                                allowed: 500 for this collection.


                       q             string                 No          -      Search query. Can be used to filter    “188.250.243.135”

                                                                                 results or search for a specific

                                                                                entry by IP. Format: “” to search

                                                                                    for one specific record.


               apply_hunting_rules   integer                No         0       Apply hunting rules filter. Set to 1          1

                                                                                           to enable.


       Query Parameter Details:


          ·

seqUpdate:


                · Each row in the database has its own unique sequence update number

                · Important: Always use the top-level seqUpdate field from the previous response to get the next portion of feeds

                · Use /api/v2/sequence_list endpoint to get the required seqUpdate number for a specific date


          · limit:


                · Maximum value: 500 for suspicious_ip/vpn/updated collection

                · If not specified, defaults to 500

                · The limit depends on the amount of data to not overload the JSON output


          · q:


                · Can be used for general search queries

                · To search for a specific IP: q=""

                · Supports various search types


       Request Headers


                  Header                  Type                  Required                               Description                             Example


                   Accept                 string                   No                      Content type accepted by the client              application/json


                Authorization             string                  Yes                  Basic authentication credentials (see Initial             Basic

                                                                                                          Steps)                        base64(LOGIN:API_KEY)


                 User-Agent               string                   No                   User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                         (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                          useful in troubleshooting on our end).       roup-ib.com/ciaops_3.0.0

                                                                                                         Format:

                                                                                      PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                      e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers

Header                                           Description                                         Example


                    Content-Type                                   Response content type                                application/json


                  Content-Encoding                                      Content encoding                                       gzip


                   Cache-Control                                  Cache control directives                     max-age=0, must-revalidate, private


                           Allow                                   Allowed HTTP methods                                        GET


       Response Body Schema

       Root Object
       { "count": integer, "items": [VpnItem], "seqUpdate": integer }


                   Field                 Type                            Required                                  Description


                  count                 integer                             Yes                  Number of VPN items returned in this response


                  items              array[VpnItem]                         Yes                            Array of VPN server objects


                seqUpdate               integer                             Yes                  Sequence update number at the top level of the

                                                                                               response. Always use this top-level value in the next

                                                                                             request’s seqUpdate parameter to get the next portion of

                                                                                                                      feeds


       VpnItem Object


                   Field                 Type                            Required                                  Description


                    id                   string                             Yes                       IP address (used as unique identifier)


               dateFirstSeen             string                             Yes              ISO 8601 timestamp when the VPN server was first seen


               dateLastSeen              string                             Yes              ISO 8601 timestamp when the VPN server was last seen

Field         Type         Required                       Description


                seqUpdate      integer         Yes        Sequence update number for this specific item


                  ipv4       IPv4Object        Yes                      IPv4 address object


                 names       array[string]     Yes      Array of VPN service names (e.g., [“SoftEther VPN”])


                  types      array[string]     Yes            Array of VPN types (e.g., [“self-hosted”])


                  rules      array[string]     Yes                 Array of detection rule names


                 source         string         Yes                        Source identifier


                 sources     array[string]     Yes                   Array of source identifiers


                evaluation   Evaluation        Yes        Evaluation object containing threat assessment


                  bind       object | null     No                            Bind object


                portalLink   string | null     No                  Portal link to the VPN record


       IPv4Object Object


                  Field         Type         Required                       Description


                    ip          string         Yes                          IPv4 address


               countryCode   string | null     No               Country code (ISO 3166-1 alpha-2)


               countryName   string | null     No                          Country name


                   city      string | null     No                            City name


                 region      string | null     No                           Region name

Field                            Type                                        Required                                                         Description


                 provider                     string | null                                         No                                                       ISP/provider name


                    asn                       string | null                                         No                                                          ASN number


       Evaluation Object


                   Field                            Type                                        Required                                                         Description


               admiraltyCode                        string                                          Yes                                                Admiralty Code (e.g., “A2”)


                 credibility                        integer                                         Yes                                                    Credibility score (0-100)


                 reliability                        integer                                         Yes                                                    Reliability score (0-100)


                  severity                          string                                          Yes                                     Severity level (e.g., “green”, “orange”, “red”)


                     tlp                            string                                          Yes                               Traffic Light Protocol level (e.g., “amber”, “red”, “green”,

                                                                                                                                                                   “white”)


                     ttl                            integer                                         Yes                                                      Time to live in days


       Example Request

       Basic Request
       curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/vpn/updated?seqUpdate=0&limit=500' \ -u 'LOGIN:API_KEY' \ -H 'Accept:
       application/json'
       Request with Hunting Rules
        curl -X GET 'https://tap.group-ib.com/api/v2/suspicious_ip/vpn/updated?seqUpdate=0&limit=500&apply_hunting_rules=1' \ -u 'LOGIN:API_KEY' \ -H
       'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "count": 741499, "items": [           {          "bind": null,       "dateFirstSeen": "2021-04-22T12:43:38+00:00",                   "dateLastSeen": "2021-04-22T12:43:38+00:00",
           "evaluation": {      "admiraltyCode": "A2",                     "credibility": 80,       "reliability": 90,      "severity": "green",            "tlp": "amber",        "ttl": 2    },   "id":
       "188.250.243.135",         "ipv4": {          "asn": "AS3243",               "city": null,        "countryCode": "PT",           "countryName": null,           "ip": "188.250.243.135",
       "provider": null,       "region": null         },       "names": [           "SoftEther VPN"          ],     "portalLink": null,       "rules": [        "vpn_soft_ether"          ],
       "seqUpdate": 1671657409977576,                      "source": "playbook",           "sources": [           "playbook"     ],       "types": [         "self-hosted"     ]     } ], "seqUpdate":
       1671657410005695 }

Collections Details - Analysis
       Domain Whois
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint retrieves WHOIS information for second-level domain names. It provides access to domain registration and ownership data sourced
       from the Graph module, including current and historical WHOIS records with parsed and raw data.

       Collection-Specific Information


                                                  Property                                                                   Value


                                                   Method                                                                     GET


                                                    Path                                                           /api/v2/utils/graph/domain


                                              Collection Name                                                            Domain Whois


                                                   Module                                                                    Graph


                                                    Type                                                               Utility for Analysis


                                                  Rate Limit                                        1 request per 10 seconds per company per feed (see

                                                                                                                        API Limitations)


                                              Short Description                                          Domain WHOIS API collection provides access to

                                                                                                   domain registration and ownership data sourced from

                                                                                                                         Graph module.


       Request

       Request URL
        GET /api/v2/utils/graph/domain
       Query Parameters


                 Parameter                Type                 Required               Default                  Description                      Example


                  domain                 string                  Yes                      -        Second-level domain name to                group-ib.com

                                                                                                    query WHOIS information for

Query Parameter Details:


          · domain:

               · Required parameter

               · Must be a valid second-level domain name (e.g., group-ib.com)

               · The endpoint will retrieve WHOIS information for the specified domain

               · Only second-level domains are supported (e.g., group-ib.com, not subdomain.group-ib.com)


       Request Headers


                 Header                Type                   Required                                  Description                                Example


                  Accept               string                    No                         Content type accepted by the client               application/json


               Authorization           string                    Yes                   Basic authentication credentials (see Initial                Basic

                                                                                                          Steps)                          base64(LOGIN:API_KEY)


                User-Agent             string                    No                       User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                          (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                           useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                          Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                      n/AppName_AppVersion/Username/LibNam

                                                                                                       e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                       Header                                               Description                                                   Example


                    Content-Type                                       Response content type                                           application/json


                  Content-Encoding                                       Content encoding                                                   gzip


                    Cache-Control                                     Cache control directives                            max-age=0, must-revalidate, private

Header                                            Description                                                  Example


                           Allow                                     Allowed HTTP methods                                                  GET


       Response Body Schema

       Root Object
       { "id": string, "name": string, "created_at": string, "updated_at": string, "is_sld": boolean, "zone": string, "whois": array, "whois_history": array,
       "dns": array, "dns_list": array, "netoscope": array, "createdAt": string, "updatedAt": string, "isSld": boolean }
       The response is a single object containing domain metadata and WHOIS information.

       Root Object Fields


                   Field                  Type                            Required                                             Description


                    id                    string                             Yes                               Domain identifier (same as domain name)


                  name                    string                             Yes                                              Domain name


                created_at                string                             Yes                           ISO 8601 timestamp when the domain record was

                                                                                                                           created in the system


                updated_at                string                             Yes                        ISO 8601 timestamp when the domain record was last

                                                                                                                                 updated


                  is_sld                 boolean                             Yes                               Indicates if this is a second-level domain


                   zone                   string                             Yes                           Top-level domain (TLD) zone (e.g., com, org, net)


                  whois                   array                              Yes                          Array of current WHOIS records (see Whois Record

                                                                                                                              Object below)


               whois_history              array                              Yes                         Array of historical WHOIS records (see Whois History

                                                                                                                           Record Object below)


                   dns                    array                              Yes                                 Array of DNS records (may be empty)


                 dns_list                 array                              Yes                                Array of DNS list entries (may be empty)


                netoscope                 array                              Yes                              Array of netoscope entries (may be empty)

Field                   Type                             Required                          Description


               createdAt                 string                             Yes      ISO 8601 timestamp (alternative format for creation date)


               updatedAt                 string                             Yes      ISO 8601 timestamp (alternative format for update date)


                 isSld                 boolean                              Yes        Indicates if this is a second-level domain (alternative

                                                                                                              format)


       Whois Record Object


       Each object in the whois array represents a current WHOIS record:


                 Field                   Type                             Required                          Description


                 level                  integer                             Yes          WHOIS query level (0 = registry, 1 = registrar, 2 =

                                                                                                             registrant)


                 server                  string                             Yes               WHOIS server that provided this record


                parsed                   array                              Yes       Array of parsed WHOIS fields (see Parsed Field Object

                                                                                                              below)


               response                  string                             Yes                     Raw WHOIS response text


               checked_at             string | null                         No          ISO 8601 timestamp when this record was checked


               checkedAt               boolean                              Yes              Indicates if the record has been checked


                 values                 object                              Yes          Additional parsed values (may be empty object)


       Parsed Field Object


       Each object in the parsed array represents a parsed WHOIS field:

Field                             Type                                Required                                                       Description


                  field                            string                                 Yes                             Field name (e.g., Registrar, NameServers, CreationDate,

                                                                                                                          ExpirationDate, Status, Phone, Email, Address, City, State,

                                                                                                                                        Country, Zipcode, Org, Name)


                 value                             array                                  Yes                             Array of string values for this field (may be empty array)


       Whois History Record Object


       Each object in the whois_history array represents a historical WHOIS record. It has the same structure as a Whois Record Object, with additional fields:


                 Field                             Type                                Required                                                       Description


                 level                            integer                                 Yes                                 WHOIS query level (0 = registry, 1 = registrar, 2 =

                                                                                                                                                      registrant)


                 server                            string                                 Yes                                      WHOIS server that provided this record


                parsed                             array                                  Yes                              Array of parsed WHOIS fields (see Parsed Field Object

                                                                                                                                                        above)


               response                            string                                 Yes                                             Raw WHOIS response text


               checked_at                       string | null                             No                                ISO 8601 timestamp when this record was checked


               first_seen                       string | null                             No                                   ISO 8601 date when this record was first seen


               last_seen                        string | null                             No                                   ISO 8601 date when this record was last seen


       Example Request

       Basic WHOIS Query
        curl -X GET 'https://tap.group-ib.com/api/v2/utils/graph/domain?domain=group-ib.com' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "id": "group-ib.com", "name": "group-ib.com", "created_at": "2015-12-11T05:32:59Z", "updated_at": "2025-12-23T14:37:59.697Z", "is_sld": true,
       "zone": "com", "whois": [       {        "level": 1,      "server": "whois.crsnic.net",       "parsed": [      {       "field": "Registrar",        "value": [
       "godaddy.com, llc"          ]       },        {          "field": "NameServers",          "value": [        "dora.ns.cloudflare.com",              "tom.ns.cloudflare.com"

]       },       {          "field": "Status",       "value": [      "clientdeleteprohibited https://icann.org/epp#clientdeleteprohibited",
       "clientrenewprohibited https://icann.org/epp#clientrenewprohibited",                       "clienttransferprohibited https://icann.org/epp#clienttransferprohibited",
               "clientupdateprohibited https://icann.org/epp#clientupdateprohibited"                   ]     }    ],    "response": "[Raw WHOIS response text - truncated
       for brevity]",           "checked_at": "2025-12-23 13:49:50",         "checkedAt": true,    "values": {}   } ], "whois_history": [     {      "level": 2,       "server":
       "whois.reg.com",               "parsed": [       {     "field": "name",      "value": [      "Domain Administrator",             "Ilya Sachkov"             ]     },        {
       "field": "org",            "value": [         "\"Group IB Service\" Ltd.",       "Group IB Service Ltd."         ]    },     {        "field": "country",              "value": [
           "RU"             ]     }     ],     "response": "[Raw WHOIS response text - truncated for brevity]",        "checked_at": null,        "first_seen": "2018-12-19",
       "last_seen": "2019-01-17"               } ], "dns": [], "dns_list": [], "netoscope": [], "createdAt": "2015-12-11T05:32:59Z", "updatedAt":
       "2025-12-23T14:37:59.697Z", "isSld": true }

IP Whois
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint retrieves WHOIS information for IP addresses. It provides access to IP registration and ownership data sourced from the Graph module,
       including ASN (Autonomous System Number), organization details, allocation range, registry data, and historical WHOIS records with parsed
       information.

       Collection-Specific Information


                                                  Property                                                                  Value


                                                   Method                                                                    GET


                                                    Path                                                            /api/v2/utils/graph/ip


                                              Collection Name                                                              IP Whois


                                                   Module                                                                   Graph


                                                    Type                                                              Utility for Analysis


                                                 Rate Limit                                          1 request per 10 seconds per company per feed (see

                                                                                                                       API Limitations)


                                              Short Description                                     The IP WHOIS API provides access to registration and

                                                                                                    ownership information for IP addresses sourced from

                                                                                                       the Graph module, including details such as ASN,

                                                                                                       organization, allocation range, and registry data.


       Request

       Request URL
        GET /api/v2/utils/graph/ip
       Query Parameters


                 Parameter                Type                Required                Default                Description                     Example


                      ip

Parameter              Type              Required                    Default                        Description                   Example


                                           string              Yes                          -                  IP address to query WHOIS           3.72.181.255,

                                                                                                                       information for          2a01:4f8:10b:90f::2


       Query Parameter Details:


          · ip:

               · Required parameter

               · Must be a valid IP address (IPv4 or IPv6)

               · The endpoint will retrieve WHOIS information for the specified IP address

               · Returns allocation range, ASN, organization, and registry information


       Request Headers


                   Header               Type                   Required                                    Description                            Example


                   Accept              string                     No                            Content type accepted by the client            application/json


               Authorization           string                     Yes                    Basic authentication credentials (see Initial               Basic

                                                                                                              Steps)                       base64(LOGIN:API_KEY)


                  User-Agent           string                     No                      User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                           (optional but recommended - especially        roupIB_TI_1.0.0/gibuser@g

                                                                                            useful in troubleshooting on our end).         roup-ib.com/ciaops_3.0.0

                                                                                                             Format:

                                                                                     PlatformType/PlatformName_PlatformVersio

                                                                                     n/AppName_AppVersion/Username/LibNam

                                                                                                           e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                         Header                                            Description                                                     Example


                      Content-Type

Header                                               Description                                                     Example


                                                                        Response content type                                            application/json


                  Content-Encoding                                         Content encoding                                                     gzip


                   Cache-Control                                       Cache control directives                                max-age=0, must-revalidate, private


                           Allow                                        Allowed HTTP methods                                                    GET


       Response Body Schema

       Root Object
       { "id": string, "start": string, "end": string, "provider": string, "created_at": string | null, "updated_at": string | null, "whois_history": array,
       "whois_summary": object, "createdAt": string | null, "updatedAt": string | null, "whoisHistory": array, "whoisSummary": object }
       The response is a single object containing IP metadata and WHOIS information.

       Root Object Fields


                   Field                    Type                             Required                                              Description


                    id                      string                              Yes                                IP address identifier (same as queried IP)


                   start                    string                              Yes                            Start of the IP allocation range (CIDR block start)


                   end                      string                              Yes                             End of the IP allocation range (CIDR block end)


                 provider                   string                              Yes                         Regional Internet Registry (RIR) provider (e.g., ripe, arin,

                                                                                                                               apnic, lacnic, afrinic)


                created_at               string | null                          No                          ISO 8601 timestamp when the IP record was created in

                                                                                                                                    the system


                updated_at               string | null                          No                         ISO 8601 timestamp when the IP record was last updated


               whois_history                array                               Yes                         Array of historical IP WHOIS records (see Whois History

                                                                                                                               Entry Object below)

Field                 Type                           Required                                       Description


               whois_summary             object                            Yes                    Summary of current IP WHOIS information (see Whois

                                                                                                                 Summary Object below)


                 createdAt            string | null                        No                    ISO 8601 timestamp (alternative format for creation date)


                 updatedAt            string | null                        No                    ISO 8601 timestamp (alternative format for update date)


                whoisHistory             array                             Yes                   Array of historical IP WHOIS records (alternative naming,

                                                                                                                 same as whois_history)


               whoisSummary              object                            Yes                    Summary of current IP WHOIS information (alternative

                                                                                                            naming, same as whois_summary)


       Whois History Entry Object


       Each object in the whois_history array represents a historical WHOIS record entry:


                   Field                 Type                           Required                                       Description


                 first_seen              string                            Yes                         Date when this record was first seen (format:

                                                                                                                      YYYY-MM-DD)


                 last_seen               string                            Yes                         Date when this record was last seen (format:

                                                                                                                      YYYY-MM-DD)


                   data                  array                             Yes                     Array of WHOIS data objects (see Whois Data Object

                                                                                                                          below)


       Whois Data Object


       Each object in the data array within a history entry contains parsed WHOIS information:


                   Field                 Type                           Required                                       Description


                 first_seen

Field                 Type                             Required                         Description


                                         string                             Yes       ISO 8601 timestamp when this data was first seen


                 last_seen               string                             Yes       ISO 8601 timestamp when this data was last seen


                   md5                   string                             Yes         MD5 hash of the WHOIS data for deduplication


                  parsed                 array                              Yes      Array of parsed WHOIS fields (see Parsed Field Object

                                                                                                             below)


                   type                  string                             Yes           Type of WHOIS record (e.g., route, inetnum)


                  values                object                              Yes         Additional parsed values (may be empty object)


                values_raw              object                              Yes            Raw parsed values (may be empty object)


               first_appeared          boolean                              Yes       Indicates if this is the first appearance of this data


               last_appeared           boolean                              Yes        Indicates if this is the last appearance of this data


                 firstSeen               string                             Yes      ISO 8601 timestamp (alternative format for first seen)


                 lastSeen                string                             Yes      ISO 8601 timestamp (alternative format for last seen)


       Parsed Field Object


       Each object in the parsed array represents a parsed WHOIS field:

Field                                 Type                                  Required                                                                    Description


                      field                                string                                      Yes                                             Field name (e.g., route, descr, origin, mnt-by,

                                                                                                                                              parsed_domains, parsed_emails, rpki-ov-state, changed,

                                                                                                                                                                      last-modified, source, type)


                      value                                 array                                      Yes                                    Array of string values for this field (may be empty array)


       Whois Summary Object


       The whois_summary object provides a summary of current IP WHOIS information:


                      Field                                 Type                                  Required                                                                    Description


                      asn                                  string                                      Yes                                    Autonomous System Number (ASN) associated with the

                                                                                                                                                                                   IP range


                     country                               string                                      Yes                                                    Country code (may be empty string)


                     descr                                 string                                      Yes                                    Description of the IP allocation (organization or network

                                                                                                                                                                                   name)


                       isp                                 string                                      Yes                                            Internet Service Provider or organization name


                 netname                                   string                                      Yes                                                   Network name (may be empty string)


                     phone                                 string                                      Yes                                            Contact phone number (may be empty string)


       Example Request

       Basic IP WHOIS Query
        curl -X GET 'https://tap.group-ib.com/api/v2/utils/graph/ip?ip=3.72.181.255' \ -u 'LOGIN:API_KEY' \ -H 'Accept: application/json'
       Example Response

       Success Response (200 OK)
        { "id": "3.72.181.255", "start": "3.64.0.0", "end": "3.79.255.255", "provider": "ripe", "created_at": null, "updated_at": null, "whois_history": [                                                           {
       "first_seen": "2025-10-29",                     "last_seen": "2025-10-29",         "data": [      {          "first_seen": "2025-10-29T16:34:39Z",                              "last_seen":
       "2025-10-29T16:34:39Z",                          "md5": "101ca07ce44a51a58afb79be13279032",                             "parsed": [                   {            "field": "route",                 "value": []
       },        {                 "field": "descr",                  "value": [         "Amazon EC2 FRA Prefix"                          ]            },             {            "field": "origin",              "value": [
                "AS16509"                      ]            },           {         "field": "mnt-by",             "value": [                  "MAINT-AS16509"                          ]        },             {
       "field": "parsed_domains",                          "value": [              "amazon.com"              ]           },           {                "field": "parsed_emails",                      "value": [
       "noc@amazon.com"                            ]             },          {       "field": "rpki-ov-state",               "value": [                     "valid"            ]           },           {           "field":
       "changed",                   "value": [                   "noc@amazon.com 20201022 #18:22:02Z"                             ]              },              {          "field": "last-modified",
       "value": []            },           {               "field": "source",            "value": []         },          {                "field": "type",                 "value": []            }           ],          "type":

"route",             "values": {},           "values_raw": {},              "first_appeared": false,                          "last_appeared": false,                   "firstSeen": "2025-10-29T16:34:39Z",
        "lastSeen": "2025-10-29T16:34:39Z"                        }    ]      } ], "whois_summary": {                             "asn": "AS16509",         "country": "",        "descr": "Amazon EC2 FRA Prefix",
       "isp": "Amazon EC2 FRA Prefix",                  "netname": "",           "phone": "" }, "createdAt": null, "updatedAt": null, "whoisHistory": [                                         {        "first_seen":
       "2025-10-29",               "last_seen": "2025-10-29",              "data": [            {        "first_seen": "2025-10-29T16:34:39Z",                                 "last_seen": "2025-10-29T16:34:39Z",
           "md5": "101ca07ce44a51a58afb79be13279032",                                     "parsed": [                {                  "field": "route",                  "value": []              },        {          "field":
       "descr",                "value": [               "Amazon EC2 FRA Prefix"                               ]              },          {          "field": "origin",                    "value": [               "AS16509"
           ]           },           {         "field": "mnt-by",                  "value": [                      "MAINT-AS16509"                         ]            },           {               "field": "parsed_domains",
               "value": [                "amazon.com"                  ]            },              {              "field": "parsed_emails",                       "value": [                   "noc@amazon.com"
       ]          },           {            "field": "rpki-ov-state",                    "value": [                 "valid"                  ]         },              {            "field": "changed",                  "value": [
                "noc@amazon.com 20201022 #18:22:02Z"                                        ]            },              {               "field": "last-modified",                      "value": []           },         {
       "field": "source",                 "value": []            },          {              "field": "type",                        "value": []        }          ],            "type": "route",             "values": {},
       "values_raw": {},                "first_appeared": false,                 "last_appeared": false,                           "firstSeen": "2025-10-29T16:34:39Z",                         "lastSeen":
       "2025-10-29T16:34:39Z"                   }       ]     } ], "whoisSummary": {                    "asn": "AS16509",                "country": "",       "descr": "Amazon EC2 FRA Prefix",                     "isp": "Amazon
       EC2 FRA Prefix",             "netname": "",          "phone": "" } }

IP Scoring
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint returns a risk score for one or more IP addresses. Each score is a number from 0 to 100 that reflects the likelihood that the IP is
       associated with malicious activity, based on Group-IB Threat Intelligence data. Use it to enrich and prioritize IP addresses on demand - for example, to
       triage indicators, score traffic, or gate automated response.

       Collection-Specific Information


                                                  Property                                                                       Value


                                                   Method                                                                        POST


                                                    Path                                                                  /api/v2/scoring/ip


                                              Collection Name                                                                  IP Scoring


                                                   Module                                                                       Scoring


                                                    Type                                                                   Utility for Analysis


                                                 Rate Limit                                              1 request per 10 seconds per company per feed (see

                                                                                                                            API Limitations)


                                              Short Description                                             Returns a 0-100 risk score for one or more IPv4

                                                                                                        addresses based on Group-IB Threat Intelligence data.


       Request

       Request URL
        POST /api/v2/scoring/ip
       Request Body


       The request body is a JSON object with a single ips field containing one or more IPv4 addresses.
        { "ips": ["8.8.8.8", "1.1.1.1"] }

Field                 Type                           Required                                            Description


                    ips              array[string]                        Yes                         One or more IPv4 addresses to score. IPv4 only (IPv6,

                                                                                                         hostnames, and CIDR ranges are not supported).


       Request Headers


                 Header              Type                  Required                                  Description                                Example


                  Accept             string                   No                         Content type accepted by the client               application/json


               Content-Type          string                   Yes                             Must be application/json                     application/json


               Authorization         string                   Yes                   Basic authentication credentials (see Initial                Basic

                                                                                                       Steps)                          base64(LOGIN:API_KEY)


                User-Agent           string                   No                       User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                       (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                        useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                       Format:

                                                                                   PlatformType/PlatformName_PlatformVersio

                                                                                   n/AppName_AppVersion/Username/LibNam

                                                                                                    e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                          Header                                         Description                                                   Example


                    Content-Type                                    Response content type                                           application/json


                  Content-Encoding                                    Content encoding                                                   gzip

Header                                                     Description                                                 Example


                 Cache-Control                                              Cache control directives                            max-age=0, must-revalidate, private


                         Allow                                              Allowed HTTP methods                                                POST


       Response Body Schema

       Root Object
       { "items": {    "": {     "ip": string,     "riskScore": integer   } }}


                 Field                           Type                            Required                                            Description


                items                            object                            Yes                       Map keyed by the queried IP address. Each value is an IP

                                                                                                               score object. An IP with no intelligence data returns a

                                                                                                             score of 0; an empty items object is returned when there

                                                                                                                                   are no results.


       IP Score Object


                 Field                           Type                            Required                                            Description


                  ip                             string                            Yes                                         The scored IP address


               riskScore                         integer                           Yes                          Risk score from 0 to 100 (see interpretation below)


       Risk Score Interpretation


                       Score                                      Level                                                   Description


                       0-39                                        Low                       Minor or no indicators; likely benign. Well-known public infrastructure

                                                                                                              commonly falls in the 20-35 range.


                       40-59                                   Suspicious                                 Multiple weak indicators; worth monitoring.


                       60-79                                      High                                        Highly likely suspicious; investigate.

Score                                       Level                                                    Description


                      80-100                                      Malicious                          Confirmed malicious; immediate action recommended.


       Example Request


       Note: In the examples below, set the GIB_CREDENTIALS environment variable to your LOGIN:API_KEY (your email and API key) before running the
       command.

       Basic Request
       curl -X POST 'https://tap.group-ib.com/api/v2/scoring/ip' \ -u "$GIB_CREDENTIALS" \ -H 'Accept: application/json' \ -H 'Content-Type:
       application/json' \ -d '{"ips": ["8.8.8.8", "1.1.1.1"]}'
       Example Response

       Success Response (200 OK)
        { "items": { "1.1.1.1": { "ip": "1.1.1.1",         "riskScore": 25    },   "8.8.8.8": {   "ip": "8.8.8.8",   "riskScore": 25   } }}

Domain Scoring
       Summary


       Disclaimer: This is an endpoint-specific documentation. For common information including Authentication, Response Status Codes, Rate Limits,
       Additional Notes, and Troubleshooting, please refer to related articles in Integrations.


       This endpoint returns a risk score for one or more domains. Each score is a number from 0 to 100 that reflects the likelihood that the domain is
       associated with malicious activity, based on Group-IB Threat Intelligence data. Use it to enrich and prioritize domains on demand - for example, to
       triage indicators, score observed domains, or gate automated response. It is the domain counterpart of the IP Scoring endpoint and uses the same
       0-100 scale.

       Collection-Specific Information


                                                  Property                                                                     Value


                                                   Method                                                                       POST


                                                    Path                                                              /api/v2/scoring/domain


                                              Collection Name                                                             Domain Scoring


                                                   Module                                                                      Scoring


                                                    Type                                                                 Utility for Analysis


                                                 Rate Limit                                             1 request per 10 seconds per company per feed (see

                                                                                                                          API Limitations)


                                              Short Description                                         Returns a 0-100 risk score for one or more domains

                                                                                                            based on Group-IB Threat Intelligence data.


       Request

       Request URL
        POST /api/v2/scoring/domain
       Request Body


       The request body is a JSON object with a single domains field containing one or more domains.
        { "domains": ["group-ib.com", "example.corp"] }


                  Field                   Type                            Required                                          Description


                 domains

Field                 Type                           Required                                             Description


                                     array[string]                        Yes                                      One or more domains to score.


       Request Headers


                 Header              Type                  Required                                  Description                                Example


                  Accept             string                   No                         Content type accepted by the client               application/json


               Content-Type          string                   Yes                             Must be application/json                     application/json


               Authorization         string                   Yes                   Basic authentication credentials (see Initial                Basic

                                                                                                       Steps)                          base64(LOGIN:API_KEY)


                User-Agent           string                   No                       User-Agent string with product metadata        SIEM/QRadar_2020.10.6/G

                                                                                       (optional but recommended - especially         roupIB_TI_1.0.0/gibuser@g

                                                                                        useful in troubleshooting on our end).        roup-ib.com/ciaops_3.0.0

                                                                                                       Format:

                                                                                   PlatformType/PlatformName_PlatformVersio

                                                                                   n/AppName_AppVersion/Username/LibNam

                                                                                                    e_LibVersion


       Response


       Note: For response status codes and error handling, see Troubleshooting and Error Codes.

       Response Headers


                       Header                                            Description                                                   Example


                    Content-Type                                    Response content type                                           application/json


                  Content-Encoding                                    Content encoding                                                   gzip


                    Cache-Control                                  Cache control directives                              max-age=0, must-revalidate, private

Header                                                    Description                                              Example


                         Allow                                            Allowed HTTP methods                                             POST


       Response Body Schema

       Root Object
       { "items": {   "": {      "domain": string,     "riskScore": integer   } }}


                 Field                        Type                             Required                                         Description


                items                        object                              Yes                        Map keyed by the queried domain. Each value is a

                                                                                                         domain score object. A domain with no intelligence data

                                                                                                          returns a score of 0; an empty items object is returned

                                                                                                                        when there are no results.


       Domain Score Object


                 Field                        Type                             Required                                         Description


                domain                       string                              Yes                                        The scored domain


               riskScore                     integer                             Yes                        Risk score from 0 to 100 (see interpretation below)


       Risk Score Interpretation


                      Score                                     Level                                                Description


                       0-39                                      Low                                     Minor or no indicators; likely benign.


                      40-59                                  Suspicious                               Multiple weak indicators; worth monitoring.


                      60-79                                     High                                     Highly likely suspicious; investigate.


                      80-100                                  Malicious                          Confirmed malicious; immediate action recommended.


       Example Request

Note: In the examples below, set the GIB_CREDENTIALS environment variable to your LOGIN:API_KEY (your email and API key) before running the
       command.

       Basic Request
       curl -X POST 'https://tap.group-ib.com/api/v2/scoring/domain' \ -u "$GIB_CREDENTIALS" \ -H 'Accept: application/json' \ -H 'Content-Type:
       application/json' \ -d '{"domains": ["group-ib.com", "example.corp"]}'
       Example Response

       Success Response (200 OK)
        { "items": { "example.corp": {     "domain": "example.corp",      "riskScore": 0   },   "group-ib.com": {   "domain": "group-ib.com",   "riskScore": 0
        } }}

Deprecated Collections
       Overview

       This document provides a list of deprecated APIs from our system and suggests alternative APIs to use. The deprecations are part of ongoing
       improvements to enhance system performance and maintainability. Please update your code to use the new APIs to ensure compatibility with future
       versions.


       Collections:


                   Collection                                Deprecated API endpoint                                           New API endpoint


                   Malware                                  malware/targeted_malware                                        malware/config/updated


        Compromised Data::Cards              compromised/masked_cards compromised/bank_card                          compromised/masked_card/updated

         Compromised Data::Bank                                                                                    compromised/bank_card_group/updated

                     Cards


               Compromised                                    compromised/account                                   compromised/account_group/updated

               Data::Accounts


                   Phishing                                      attacks/phishing                                       attacks/phishing_group/updated


                      IOC                                          ioc/common                                                 ioc/primary/updated


       IOC Primary returns the same indicators as IOC Common, plus risk scores, evaluation metadata and attribution. See IOC Primary.


       Reference:

       For a comprehensive list of all currently supported API endpoints and their detailed descriptions, please refer to the Collections Overview article.

Custom    and native integrations
       List of integrations
       In addition to offering various API versions, such as API 2.0 and STIX/TAXII 2.1, we provide a range of integration solutions for third-party vendors.


       Current integrations are available for download through the following channels:


          · Third-party marketplaces

          · Public repositories

          · The TI Help Center, where you can find details for installation


       The following list outlines the available integrations, along with links for downloading and accessing documentation:


           Vendor                 Integration source             Status           Product type            Author               Documentation access


          Anomali              Internal marketplace               Under                TIP               Anomali                        Built-in

                                                                 update


          ArcSight                  TI Help Center              Beta test             SIEM               Group-IB                    Help Center

               SIEM

        Connector


           Brinqa              Internal marketplace             Ready to             ASMP                 Brinqa                        Built-in

                                                                   use


        Cisco ASA                   TI Help Center              Ready to             NGFW                Group-IB                     On request

                                                                   use


           Cortex                     App Store                 Ready to              SOAR               Group-IB                       Built-in

               SOAR                                                use


          Cyware               Internal marketplace             Ready to               TIP                Cyware                        Built-in

               CTIX                                                use


         EclecticIQ            Internal marketplace             Ready to               TIP              EclecticIQ                      Built-in

                                                                   use


           Google              Internal Marketplace             Ready to              SOAR               Group-IB                    Help Center

          SecOps                                                   use

Vendor     Integration source       Status     Product type     Author      Documentation access


               IBM         App Store          Ready to       SIEM         Group-IB            Built-in

          Security                              use

          QRadar

         SIEM ver.

          7.4.3 +
        LogRhythm        TI Help Center       Ready to       SIEM         Group-IB         Help Center

          Custom                                use


        LogRhythm        TI Help Center      Scheduled       SIEM         Group-IB         Help Center

           Native


               MISP      TI Help Center       Ready to        TIP         Group-IB         Help Center

                                                use


          OpenCTI      Public Repository      Ready to        TIP         Group-IB            Built-in

                                                use


         Palo Alto       TI Help Center      Deprecated      NGFW         Group-IB               -

          FireWall


         Splunk ES         App Store          Ready to       SIEM         Group-IB            Built-in

                                                use


           Splunk          App Store          Ready to       SOAR         Group-IB            Built-in

               SOAR                             use


           Splunk     Internal marketplace    Ready to     TruSTAR         Splunk             Built-in

         TruSTAR                                use


       StrikeReady    Internal marketplace    Ready to       SOAR        StrikeReady          Built-in

                                                use


         Swimlane          App Store          Ready to       SOAR        Swimlane             Built-in

                                                use


       ThreatConn          App store          Ready to        TIP         Group-IB         Help Center

               ect                              use

Vendor                Integration source                 Status             Product type             Author                 Documentation access


          ThreatQ                     App Store                    Ready to                 TIP                 ThreatQ                         Built-in

                                                                      use


           Vertex                     App store                    Ready to                 CIS                 Vertex                          Built-in

          Synapse                                                     use


       Explanatory notes
       Integration statuses:


          · Ready to use: The integration has been published and is available for installation and implementation.

          · Under update: A current version is available, but a major update is scheduled for release within approximately three months.

          · Initial development: Development has commenced, with an expected timeline of up to six months for the initial application release. A
               pre-release version may be requested manually through the Service Desk if the team already possesses the version.

          · Scheduled: application development is planned for the upcoming quarter, but has not been started yet.

       Integration source:


          · Internal Marketplace: Available in the private app store.

          · TI Help Center: Available in the Group-IB Threat Intelligence Help Center.

          · App Store: Available in the public app store.

          · Public Repository: Available in the public GitHub repository.

       Documentation access:


          · Group-IB Help Center: Integration instructions can be found in the Help Center of the Group-IB TI portal.

          · Built-in: Available in the private app store, public app store, or included within the archive of integration installation files.

Google SecOps
       Overview
       The integration allows receiving feeds from the Group-IB Threat Intelligence, and transforming them into the Google SecOps Alerts with Entities
       objects. The application can be installed in two ways: using the installation file ZIP archive at Response -> IDE -> Import package and using Google
       SecOps Market at Marketplace -> Integrations -> and click Install at the application frame.


       Current application contains active (Actions, Connectors) and passive files (Managers). You can add Actions in the Playbooks section to trigger them
       on Alerts creation or apply Playbooks to Entities to get extra enrichment or even run Actions separately for each Entity. You can add a scheduled
       Connector at Settings -> Ingestion -> Connectors to run it as a job at configured intervals. Managers contain common variables, utilities for app needs,
       configs, collection description and mapping filter, which can be applied to change the JSON output in some cases.


       Installation
       Before installing and configuring the integration, check out the start-up instructions in Group-IB TI Integration Starting Guide.


       The installation process assumes that you have access to the Google SecOps Market. There you need to search the application Group-IB TI at
       Marketplace -> Integrations -> and click Install at the application frame. The installation icon will change to gear icon when the process is finished.


       Check the application code at Response -> IDE -> Group-IB TI.


       The alternative way to install the application Group-IB TI is to use the ZIP archive with the installation file at Response -> IDE -> + -> Import package.
       Choose Group-IB_TI_SecOps_vx.x.x.zip archive, which can be downloaded here.

Configuration
       The configuration process includes several steps.


          · The first step is to insert your API credentials, which are applied on the app level and let you avoid configuring it for each Action.

          · The second step concerns configuring Connectors, which generate Alerts for you.

          · The third step describes Alerts configuration and their connection to other subsections.

       Before you begin


       To ensure that Group-IB TI application is installed without errors, verify that you use only the supported versions of any Google SecOps software.

       General information


       The GroupIB TI application is based on requests to the Group-IB TI Portal API, gathering data and uploading it to the Google SecOps Platform.
       Requests gather information from different collections, which are listed in Action / Connector configuration steps. Each collection has Start date and
       Sequence update number parameters. A Sequence update number parameter will be stored at Google SecOps side using siemplify.save_timestamp()
       and extracted by siemplify.fetch_timestamp() functions.


       NOTE: A more detailed description of the API operation logic can be found on the API Logic Explanation page.


       Step 1. App configuration

          · Go to Marketplace -> Integrations -> click Gear at the found application frame.

· Insert your Group-IB TI Portal credentials (API login - your email address used to enter the Group-IB TI Portal, API key - API key, generated at
               your Group-IB TI Profile).

          · Click Test to test the connectivity and to validate your credentials (Ping Action runs at this time. To check the code go to Response -> IDE ->
               Group-IB TI -> Ping).

          · Click Save.


       Step 2. Connectors configuration

          · Go to Settings -> Connectors -> click Plus to add a new Connector.

· In the opened Connector configuration insert your Group-IB TI Portal credentials (API login - your email address used to enter the Group-IB TI
               Portal, API key - API key, generated at your Group-IB TI Profile).

          · Change Case name, Case severity, Case type if applicable or leave default values.

          · Change Start date if applicable or leave it blank. By default it is set to one day back from today. Start date format is YYYY-MM-DD.

          · Choose the Environment you use. And set a schedule parameter Run Every day (1 0 0 0) or Run Every 12 hours (0 12 0 0). You can decrease it
               to minutes for testing purposes but usually you get fresh collections data daily.

          · Click Save.
       For a better visualization of all steps, explore the screenshot on the next page.


       NOTE: Please note that the steps on the screenshot do not always coincide with the steps in the text instructions. Double-check the order of the steps
       and all details described in the text instructions before saving.

· Before running Connector in production it is strongly recommended to open Testing tab -> Run connector once and check the output. New
               Sample Alert will appear. Mark it with a checkbox and click Load to system.


       Warning: Please go to Step 3 Alerts configuration (you’ll find the instruction below) on this stage to set Mapping for the Events before proceeding to
       the next step.


          · At the last stage enable the app by the Slider and click Save.

          · Example screenshot for the Testing tab.

· Check the Logs tab if applicable.
       Step 3. Alerts configuration

       The result of Connectors run generates Alerts in Google SecOps Cases.


       NOTE: [These Alerts can be applied. You can add Actions in the Playbooks section to trigger them on Alerts creation or apply Playbooks to Entities to
       get extra enrichment or even run Actions separately for each Entity]


          · Go to Cases -> choose Alert -> Events tab -> click Gear icon (Configure Event). If you run tests for Connector then an Alert with “T” marker will
               be created (T = Test).

· You should see new Alerts in the Cases list.


       Warning: If you don’t see any test Alerts then there is no data for the 1 day back period. Please go to Step 2 Connectors configuration on that stage
       and extend the Start date for a one week back (or more) before proceeding to the next step.


          · Open a new browser tab and click on the application name (Group-IB TI) -> Mapping -> Entity Fields. You will get to app top level mapping
               configuration, so it will affect all new incoming Alerts to extract JSON fields in the proper way. Set Extracted Fields in the following way:


                · DestinationAddress -> ioc_ip

                · FileHash -> ioc_hash


       Usage
       Go to Step 2 Connectors configuration, point 8 and finnish app configuration.


       The application Group-IB TI provides information about 100% IoC such as IPs and Hashes. You will receive the following IoC using existing Connectors
       daily:


          · TI IoC IP Connector - provides you the opportunity to download all IoC IPs and add them to Alerts as Entities. Created Alert name is IoC by
               default. Contain IoC IP tab in the Alert itself.

          · TI IoC Hash Connector - provides you the opportunity to download all IoC Hashes and add them to Alerts as Entities. Created Alert name is IoC
               by default. Contain IoC Hash tab in the Alert itself.
       Group-IB TI application contains the following Actions:


          ·

Get-Collection-Info-Async - help to extract data from Group-IB TI database by chosen collection. Can be used to run daily to get fresh updates
               only. This Action ignores any Entities. Use the input entity as the start trigger.

          · Get-Graph-Info - used to get WHOIS information based on Domain or IP Address.

          · Get-TI-Search-Info - search Domain, IP Address, File Hash, Bank Card, Email in Group-IB TI database.

          · Get-TI-Search-Info-By-Collection - search Domain, IP Address, URL, File Hash, Bank Card, Email in Group-IB TI database. Specify tag to get
               targeted field results.

          · Ping - used to test connectivity.
       All actions can be divided into two groups:


          · Updates - gather collections information data as is from Group-IB TI API. Receive only fresh updates every day for existing events or receive
               new events. Include Get-Collection-Info-Async Action.

          · Search - gather collections information data and enrich User input (IPs, URLs, Hashes, Bank Cards, etc.) with extra attributed information.
               Include Get-Graph-Info, Get-TI-Search-Info, Get-TI-Search-Info-By-Collection Actions.
       The Updates group contains asynchronous types of Actions. The Search group contains synchronous types of Actions.


          · Go to Response -> Playbooks -> create a new Playbook -> add any Action in Search group hover over it and click to configure.


          · Fill in Parameters and click Save.

· If extra parameters are available - here is the explanation:


               · Enable mapping parser - Enable or Disable mapping parser before return JSON output

               · Collection - choose required collection to download

               · Search tag - by default Tag is empty: q=(q=8.8.8.8). If Tag is set to “domain”: q=: (q=domain:google.com).


       Each Group-IB TI application Action includes a JSON result and to help the User navigate over it in the Output of Playbooks section by its own JSON
       Sample.


          · Go to Response -> Playbooks -> create a new Playbook -> navigate the Output block and click it to configure.

· In the opened frame, find the expanded menu, called Playbook -> click the icon next to _.JsonResult.


          · In the oppended frame choose the required field to extract. It will add Expression, using dot-notation. Click Save. Also you can use Add
               Functions to create combinations of Expressions.

Data filtering
       The entire data filtering process for Google SecOps is exactly the same as in the Group-IB Threat Intelligence system.


       To explore the filtering features for each collection - follow the steps below:


          · Go to the REST API 2.0 page on the Group-IB Threat Intelligence portal.

          · Find the required collection in the list on the left side of the window.

          · Explore the information that describes the collection features.


       Troubleshooting
       First of all, as you begin the troubleshooting process, we kindly ask you to familiarize yourself with the common errors that occur when using our
       application. If errors occur outside of common cases, we will need more details for this purpose. To get to know what happened with the application
       on your side we need to gather information about your system, time when the error occurred and application logs. If you encounter any problems,
       please, follow the instructions below.

Common errors

       To find detailed information about each of the common errors, please check the section Common errors solution.


          · Google SecOps cloud can’t reach Group-IB Threat Intelligence portal.

          · Group-IB token expired or wasn’t created.

          · Group-IB account settings are not properly configured (IP addresses are not added to access list).

          · Group-IB account collections access do not match to collections, chosen in the application.

          · Client blocks incoming data from Group-IB portal (Client didn’t add necessary Threat Intelligence IP addresses to his access list).
       Download logs

       Downloading logs is the most important thing in troubleshooting. There is no direct option in Google SecOps to download log files but you can attach
       any error displayed in Google SecOps GUI as a plain text through the Email or Service Desk ticket.


       Common errors solution

       All necessary instructions can be found at the Integration manual page.

       Google SecOps cloud can’t reach Group-IB Threat Intelligence portal


       Execute the command below in the terminal, using your Group-IB username and Group-IB token credentials instead of LOGIN and API_KEY words.
        curl 'https://tap.group-ib.com/api/v2/sequence_list' -u 'LOGIN:API_KEY' -H 'Accept: */*' -v
       If your Group-IB and proxy credentials are correct, please attach output to Email or Service Desk ticket, we will check your Group-IB profile.


       NOTE: If you have a proxy with authentication, add flag –proxy with relevant proxy configurations:
        --proxy '<*protocol*>://<*user*>:<*password*>@<*IP address*>:<*port*>'.
       If you have a proxy without authentication, add flag –proxy with relevant proxy configurations:
       --proxy '<*protocol*>://<*IP address*>:<*port*>'For example, command can look as:
       curl --proxy https://127.0.0.1:3128 'https://tap.group-ib.com/api/v2/sequence_list' -u 'mr.demo@group-ib.com:wYM2gZ4Tc' -H 'Accept: */*' -v.


       Group-IB token expired or wasn’t created


       Please make sure that your Group-IB token is active and ready to use. For that purpose check your account settings at Group-IB portal.


          · Click the username in the upper-right corner and then go to the Profile tab.

          · Go to the Security and Access tab -> Personal token.

          · Click Generate token if you don’t have one or Generate new token if it is required.

          · Click Save to submit changes.


       Open your application API profile and insert a new Group-IB token in the form. API profile update form requires both of them.

Group-IB account settings are not properly configured


       Please make sure that your Group-IB account settings are properly configured. For that purpose check your account settings at Group-IB portal.


          · Click the username in the upper-right corner and then go to the Profile tab.

          · Go to the Security and Access tab -> IP white list.


       Please make sure that all your public IPs are listed in the box below. If something is missing - please, inform us via Email or Service Desk ticket. We
       will try to solve this issue promptly.


       Group-IB account collections access does not match to collections, chosen in the application


       Please make sure that your Group-IB collection settings match and you didn’t overselect them. For that purpose please compare the application
       collections settings and collections listed at your account settings at Group-IB portal.


          · Click the username in the upper-right corner and then go to the Profile tab.

          · Go to the Security and Access tab.


       Compare collections.

       Client blocks incoming data from Group-IB portal


       Please make sure that URLs and IPs listed in Starting Guide are added to the access list on your side.

LogRhythm
       Python 3.10
        Pytia


       Before installing and configuring the integration, check out the start-up instructions in Group-IB TI Integration Starting Guide.


       Installation

       You can download application here


       The application required Python 3.6.8+ installed on you system. Next python packages are required: pyaml, schedule, requests, urllib3, dataclasses.

       Unpack archive and enter the application directory
        cd group_ib_ti_logrhythm_siem
       Install requirements


          · Windows
               pip install -r requirements_windows.txt
          · Linux
               pip install -r requirements_linux.txt


       Configuration

       Open configuration.yaml file and fill in missing fields.

       Group-IB Threat Intelligence configuration
       client: api_key: username: api_url: https://tap.group-ib.com/api/v2/                      data_dir: C:\Program Files\LogRhythm\LogRhythm Job
       Manager\config\list_import
       Proxy configuration
        proxy: ip_addr: port: protocol: username: password:
       Enable required collections items in the collection section


       Enable required collection with enable: true or disable collection with enable: false. Set start date for each collection. Script will update seqUpdate
       section by its own. If you need fresh download, then set to null seqUpdate: null. You can use terminal dialog to configure collections. Use
       run_configuration.py script for that purpose.
        collections:      attacks/phishing_group:        default_date: '2023-04-19'      enable: true     seqUpdate: null   ioc/common:      default_date:
       '2023-04-19'         enable: true      seqUpdate: null    malware/cnc:         default_date: '2023-04-19'   enable: true    seqUpdate: null ...
       Date format


       YYYY-MM-DD


       Note: attacks/deface, attacks/ddos, attacks/phishing, compromised/bank_card_group, compromised/masked_card, compromised/account_group,
       suspicious_ip/open_proxy, suspicious_ip/socks_proxy, suspicious_ip/tor_node - are very large collections, and it is recommended to specify in the
       default_date field: 1-3 days ago.


       Run the script

       To start daemon process in the background (cron or task scheduler), use next command:
        pythonw run_daemon.pyw
       To run configuration dialog menu which helps you to configure collections, use next command:
        python run_configuration.py
       To run poller script in the terminal, use next command:
        python run_single_poller.py

Automation

       Tip: Use operating system (cron or task scheduler); opportunities to automate daily.


       run_single_poller.py script execution. Or use run_configuration.py, run_daemon.pyw to do it automatically.


       Configuration script steps

       If you run run_configuration.py, please follow next steps.


          · Configure API-key and Username in “Client info”.

          · Select data root, by default it should be “LogRhythm\LogRhythm Job Manager\config\list_import”.

          · Set the collection which you want to download “Collection info”.

          · Set date from you want to get data “Collection info”.

          · Run the script, it will automatically run background process, and you can close Command Prompt.

          · Configure uploading file in LogRhythm following this name:


               · attacks_phishing_group_domain.txt,

               · suspicious_ip_tor_node_ip.txt,

               · suspicious_ip_open_proxy_ip.txt,

               · suspicious_ip_socks_proxy_ip.txt,

               · suspicious_ip_scanner_ip.txt,

               · suspicious_ip_vpn_ip.txt,

               · malware_cnc_ip.txt,

               · malware_cnc_domain.txt,

               · malware_cnc_url.txt,

               · ioc_common_ip.txt,

               · ioc_common_url.txt,

               · ioc_common_domain.txt,
               · ioc_common_hash.txt


       Troubleshooting

          · If you encounter problems, please retrieve logs from the log folder and attach them to Email or Service Desk ticket.

MISP
       For the Group-IB - MISP integration, we have developed a Python script that downloads data from the Group-IB TI server and uses it to create MISP
       events.


       Before installing and configuring the integration, check out the start-up instructions in Group-IB TI Integration Starting Guide.


       Installation

       You can download the integration here.


       The application required Python 3.6.8+ installed on you system. App dependencies: pyaml, requests, urllib3, dataclasses, pymisp.

       Extract the application


       Extract and unpack archive whenever you want. Just make sure that you can reach vendor platform via HTTP/HTTPS requests.


       Unpack archive and enter the application directory using the following command:


       cd GroupIB_TI_MISP

       Install requirements


       Install local package cyberintegrations. Replace X.X.X with current lib version:


       Windows:
        pip install .\libs\cyberintegrations-X.X.X-py3-none-any.whl
       Linux:
        pip install ./libs/cyberintegrations-X.X.X-py3-none-any.whl
       Install python packages from the PyPi.
       pip install pymisp
       Copy custom MISP-objects to the MISP server


       Execute next commands to copy MISP-objects and make the files readable by the web user:
        ``` cp -r /MISP-objects/* /var/www/MISP/app/files/misp-objects/objects/ sudo chown -R www-data:www-data
       /var/www/MISP/app/files/misp-objects/objects/gib-* ```
       Copy custom MISP-objects to the MISP server (docker)


       If you are using docker instance of MISP server then you can set up docker-compose.yml like,
        misp:    volumes:        "/MISP-objects:/var/www/MISP-objects"
       and then run the following commands:
        docker exec -ti bash -c 'cp -r /var/www/MISP-objects/* /var/www/MISP/app/files/misp-objects/objects' docker exec -ti bash -c 'sudo chown -R
       www-data:www-data /var/www/MISP/app/files/misp-objects/objects/gib-*'
       Update custom MISP-objects


       In the MISP interface go to the Global Actions -> List Object Templates and click the Update Objects button on the left side.

       Create MISP server API key


       Create MISP server API key using GUI. Go to MISP interface -> top panel -> Global Actions -> My Profile -> Auth keys -> Add authentication key.


       Configuration

       Open docs/configs/endpoints_config.yaml with some text editor and fill in missing fields. Before proceed, please check again the Starting Guide at our
       TI portal.

Group-IB Threat Intelligence API configuration


       The parameter username is a login to Group-IB TI. The parameter api_key can be generated on the TI portal at your profile.
       ti_client: api_key: username:
       Platform vendor API configuration


       Fill in platform vendor Server configuration params.
       misp: misp_key: misp_url:             misp_verifycert: false
       Proxy configuration


       Fill in proxy configuration params, if required.
       proxy: proxy_ip: proxy_port:           proxy_protocol:    proxy_username:       proxy_password:
       Enable required collections


       The parameter default_date is used for initial start only. After the download process begins it will not be used anymore. Instead of default_date we will
       use seqUpdate parameter to iterate over the next portion. It is technical field. If you need fresh initial start based on the default_date, please set
       seqUpdate parameter to null.


       To start download process for any collection, you need to enable it first. Set enable parameter to true. Set default_date parameter in single quotes, if
       needed or leave it as null. By default, it is set to 3 days back to the present time.
        collections:    attacks/ddos:      default_date: '2021-08-01'       enable: true       seqUpdate: null    attacks/phishing:    default_date: '2021-08-01'
         enable: true      seqUpdate: null     ioc/common:        default_date: '2021-08-01'        enable:true      seqUpdate: 16747401659568 ...
       Date format


       Default date format.


       'YYYY-MM-DD'

       Notes


       Note: To use Firewall rules mode only, enable next collections: ioc/common, attacks/ddos.


       Note: The ioc/common collection contains IoC only and based on malware/cnc, hi/threat, apt/threat, hi/threat_actor, apt/threat_actor collections.


       Note: attacks/deface, attacks/ddos, attacks/phishing_group, compromised/bank_card_group, compromised/masked_card,
       compromised/account_group, suspicious_ip/open_proxy, suspicious_ip/socks_proxy, suspicious_ip/tor_node - are very large collections, and it is
       recommended to specify in the default_date field: 1-3 days ago.

       Extra MISP server settings

       Tags and options


       You can find all available tags in the MISP interface go to the Event Actions -> List Tags.


       Each collection can be marked with its own tag. Set local_custom_tag parameter in single quotes, if needed or leave it as null.
        collections:    attacks/ddos:      local_custom_tag: null     attacks/phishing:        local_custom_tag: 'My Phishing Tag'    ioc/common:
       local_custom_tag: 'Just 100% IoC' ...
       The extra_settings section contains configuration related to MISP side.


          · misp_distribution - can be set on the next levels:


               ·

0: Your organization only.

                  · 1: Your community only.

                  · 2: Connected communities.

                  · 3: All communities.

                  · 4: Shared group.


            · misp_global_custom_tag - all data that is coming from the app can be marked with its own tag. Set misp_global_custom_tag parameter in
                 single quotes, if needed or leave it as null.

            · misp_published - could be set to true to publish events by default or false to leave them unpublished.

            · misp_sharing_group_id - you can find in your interface go to Global Actions -> List Sharing Groups tab -> ID column. This option will work only
                 with misp_distribution set to 4.
        extra_settings : misp_distribution: 0 misp_global_custom_tag: null                        misp_published: false          misp_sharing_group_id: 0 ...
       Intrusion Detection System (IDS) and correlations


       You can customize the IDS to suit your needs if you don’t like how it’s set up. In the app itself you can find MISP-objects folder and the custom objects
       in it. Modify them and follow the instructions in Installation section at Copy custom MISP-objects to the MISP server subsection.


       As an example, open GroupIB_TI_MISP/MISP-objects/gib-malware/definition.json file. Set "to_ids" parameter to true or false (where the "name" nested
       to "attributes").


       The same way you can reconfigure correlations. Set "disable_correlation" parameter to true or false.
        {        "description": "Malware information",     "meta-category": "misc",           "name": "gib-malware",       "required": [         "name"     ],   "uuid":
       "242cbc72-793e-4294-86a7-558ce041ecdd",                   "version": 2,       "attributes": {     "object-id": {          "description": "Object ID in the Group-IB TI",
       "disable_correlation": true,             "to_ids": false,          "misp-attribute": "text",           "ui-priority": 1        },     "name": {           "description": "Malware
       name",         "disable_correlation": false,                "to_ids": true,           "misp-attribute": "text",           "ui-priority": 0,        "multiple": true    }   }}
       Extra collections settings

       Ignore data upload


       To prevent DDOS attacks without malware or Threats without indicators from being uploaded to the MISP server, set next params to true:
       extra_settings: ignore_non_malware_ddos: true                    ignore_non_indicator_threats: true
       Task scheduling automation


       Use operating system (cron or task scheduler) opportunities to automate daily poller.py script execution. You can use Cron (for Unix-based systems)
       or Task Scheduler (for Windows).The User must have appropriate rights.

       Cron:


            · Open file /etc/crontab

            · Set the following job:
        0 0 * * * cd %% && %%/python %%/poller.py
       This job will start polling daily at midnight.

       Task Scheduler:


            · Create a new file GIB_poller.bat with the following content:
                "%%" "%%\poller.py"    pause

            · Go to Control Panel -> Administrative Tools -> Task Scheduler.

            · Choose the Create Task option.

            · Fill in the task name and description.

            · In the Triggers tab create a new daily trigger and set it to be repeated each 12 hours for an infinite amount of days.

            ·

In the Actions tab add a new action and select the .bat file created on the first step.

          · Click the Ok button.


       The script scheduler opportunity


       To run script via Task Scheduler install local package schedule for Windows.


       Windows:


       pip install .\libs\schedule-1.1.0-py2.py3-none-any.whl


       And run the script via PythonW:
        `pythonw run_daemon.pyw`
       Also, you can set upload start time via configuration file. Task Scheduler start time can be configured in docs/configs/endpoints_config.yaml file. Set
       schedule_time parameter to required value (16:00, 00:00, etc.) in extra_settings section.
        extra_settings:      schedule_time: 00:00 ...
       Troubleshooting

          · If you encounter problems, please retrieve logs from the log folder and attach them to Email or Service Desk ticket.

          · If you have problems with proxy configuration, attach the proxy environment by executing this command:
               printenv | grep proxy
       FAQ

          · How to add Group-IB as a creator/owner org?


               Create a company that represents us, and a user inside this company with appropriate rights and use his API key in the integration.

          · Where I can find reports from last threats?


               They are separated similarly to TI interface. hi/threat stands for Cybercriminals and apt/threat stands for Nation-State.

          · What tags we are using for our events?


               Besides tags, that you can set in the configuration, we are using:
                - collection name (but with spaces instead of "_" or "/") - admiralty codes and TLP, where applicable - for **osi/vulnerability** we add
               affected products as tags - for **hi/threat** and **apt/threat** we add "Tailored" tag, similar to the TI portal

          · Why app raise an access deny error in logs?


               Please check that MISP user has correct rights and access. Also, please check if you install integration app separate from the MISP server
               virtual machine. MISP server is a separate app which control its folders rights.

ThreatConnect
       The integration allows receiving feeds from Group-IB Threat Intelligence and transforming them into ThreatConnect Groups and Indicators objects.
       These objects use extra Attribute Types, which should be uploaded via the attributes.json file manually at Gear Icon -> System Settings -> Attribute
       Types, or will be uploaded automatically if your system allows you to see listed ThreatConnect Marketplace apps.


       Current application type - Job App. The ThreatConnect Platform provides the ability for customers to schedule applications as jobs, specifically known
       as Job Apps, that can be run at configured intervals.


       Installation
       Before installing and configuring the integration, check out the start-up instructions in Group-IB TI Integration Starting Guide.


       Before you begin, ensure you have access to the Group-IB TI Portal -> Integrations section, where you can find the ThreatConnect tab and download
       link, or access to the public ThreatConnect GitHub repository. There you need to download the application .tcx archive and install it in your
       ThreatConnect system.


       Step 1: Download the appropriate version of the integration here.


       Step 2: Create a ThreatConnect API User


          · Login to the ThreatConnect web interface as an administrator.

          · Click the Gear icon (top right) -> Organization Settings.

          · In the Membership tab, click Create API User.


       Step 3: Install the Application


          · Go to Gear Icon -> Organization Settings -> Apps.

          · Click Install App.

          · Upload the .tcx file.

          · Click Install.
       Step 4: Verify Installation


          · Ensure you have the correct Group-IB TI username and API token. Check the Group-IB Starting Guide for more info.

          · Once installation is complete, you should see the “Group-IB Threat Intelligence (vx.x.x)” app at Gear Icon -> Organization Settings -> Apps tab
               -> Add Job menu -> Run Program dropdown.

Configuration
       Step 5: Create a Job: follow the instructions in the next Configuration section to create a new job for the app.


       The configuration process includes several steps. The first step is to create a Job App based on the integration app. The second step concerns
       configuring collections. Each collection is a set of data that contains different information for each type of attack. You can find a more detailed
       description at our Group-IB TI Portal.


       Before you begin


          · Ensure you are running a supported version of the ThreatConnect Platform.

          · Verify that the TC Group-IB TI application has been installed without errors.

          · Make sure you have valid Group-IB and ThreatConnect API credentials.


       General information


       The TC GroupIB TI application is based on requests to the Group-IB TI Portal API, gathering data and uploading it to the ThreatConnect Platform.
       Requests gather information from different collections, which are listed in Job App configuration steps. Each collection has Initial date and Sequence
       update number parameters.


       Step 1. Add new Job

          · Go to Gear Icon -> Organization Settings -> Apps tab -> Add Job menu -> Run Program dropdown. Enter the Job name and select the app
               Group-IB Threat Intelligence (vx.x.x). Click Next.

· Fill in ThreatConnect API User, ThreatConnect Owner and Group-IB credentials (Group-IB Login, Group-IB API Key) in the Parameters tab.

          · Enable Attach Group-IB portal links per your preference (enabled by default).

          · Enable required collections and set the Initial date of data collection. Click Next.


          · Configure the Schedule tab with the daily option and click Next.

          · Configure the Output tab and click Save.

          · Activate created Job to set scheduled run in the background or run it once to check.
       Step 2. Collections configuration

       All listed collections can be enabled and run as one separate Job or can be configured as one Job for each collection. This option is available as API
       requests 1-second limit applies only to one collection, but can run in a separate thread.

Here in the example on the screenshot how you can mark collections you need, to get data from Threat Intelligence. Gathered data will be transferred
       to the ThreatConnect Groups and Indicators objects and uploaded to the system. Mark the required collection using the checkbox. After finishing the
       configuration process, click “Next” and finish a Job creation.

       Collection Parameters


          · Initial date - the “starting point” of the collection data download process. When the download process starts this date will be ignored and
               iteration over collection data will be based on “Sequence update number”. So if you need to change this date and get a fresh download
               process you need to set “Sequence update number” to “None”.

          · Sequence update number - Each row in our database has its own unique sequence update number. So, we can get all the events one by one,
               using the iteration. This number helps to fix the “end point” of data for the last day and continue iteration on the next day with new data. The
               “Sequence update number” accepts values “None”, “0” or a random number (e.g.17083410361167). One of these values is required. An empty
               “Sequence update number” field will raise an error.

          · Optional fields (for selected collection only):

                · Apply Hunting Rules (Optional) - collections data will be filtered according to the hunting rules you’ve set up in Group-IB Threat
                    Intelligence.

                · Is in combolist or a unique record (Optional, compromised/account_group collection) - Combolist entries come from collections of
                    usernames and passwords that have been compiled from various sources, do not have compromise date and usually assign low
                    Admiralty. Unique entries come from singular detections and therefore have compromise date and higher Admiralty. N.B: selecting
                    both filters is equal to selecting none. One will see a full set of data without filtering.

                · Probable corporate access (Optional, compromised/account_group collection) - special filtering option for
                    compromised/account_group collection. Data will be filtered in according to your corporate settings Group-IB Threat Intelligence.

                ·

Has password (Optional, compromised/breacheddb collection) - Boolean (default off). On -> has_password=1: only breach records
                 that include a password.

               · IOC type (Optional, ioc/primary collection) - Choice all / network / file (default all). Restricts the IoC Primary feed to network indicators
                 or file indicators; all sends no filter.

               · Suspicious payment type (Optional, compromised/spd collection) - Choice: all / Cryptocurrency Wallet / Bank Account Number /
                 Mobile number / IBAN / Bank card / Unknown / QR payment string (default all). Filters Suspicious Payment Details to a single
                 payment-detail type; all sends no filter.

               · Malware with description (Optional, malware/malware collection) - 3-state Choice: API default / true / false. Include or exclude the
                 malware long-description field; API default sends nothing.


       How Data Pull Works


          · When a job starts, it retrieves the latest Sequence update number based on the chosen Initial date.

          · Data is downloaded in small portions.

          · After each portion, the application stores a new Sequence update number for use in the next run.

        · On the next scheduled execution, the job resumes from the last stored Sequence update number-the Initial date is no longer used.
       Resetting the Collection


       To restart collection from a new Initial date:


          · Set the new Initial date.

          · Change Sequence update number to None.

          · Save changes.

        · Run the job manually or wait for the next scheduled run.
       Storage Considerations


       Some collections can grow rapidly (e.g., Attacks -> DDoS, Compromised -> Bank Cards / Masked Cards, Suspicious IPs, IoC). Plan your ThreatConnect


       Usage
       TIP storage capacity accordingly.


       All downloaded feeds from Group-IB Threat Intelligence are stored in Groups and Indicators within ThreatConnect.


       To access this data:


          · Click the Search & Create tab in the top panel.

          · Select Indicators or Groups.

          · A data table with additional details will open.

Viewing Indicators / Groups Details


          · Select any row in the data table to expand the overview tab.

          · The Overview tab displays:

               · Security label

               · First seen

               · Date added

               · Last modified

               · Description

               · Attributes

               · and other relevant fields.


       Associations Tab The Associations tab lists all related data for the selected indicator or group, including:


          · TQL Queries

          · Groups

          · Indicators

          · and other linked objects

Dashboard View The Dashboard tab (top panel) provides widgets with plots and diagrams summarizing events and activity. The following widgets are
       available:


          · My Recent History

          · Intelligence Breakdown

          · Source Composition

          · Intelligence Lookup

          · Intelligence ROI

          · Indicators Observed (Past 24 Hours)

          · My Open Tasks

          · Intelligence Creation

Data filtering
       Dashboards and widgets can be fully customized to match your needs.


       Once the configuration is complete, the following sourcetypes become available in TC. All data received from a particular collection is marked with
       special tags. The table below displays the mapping of Group-IB collections into Groups and Indicators presented in ThreatConnect Platform. Note: If
       you’re using a POC or partner license, access to data is limited to 30 days. The recommended date ranges below are guidelines and can be adjusted
       according to your needs.


                       Collection                                 Description                                      TC data type                       Tag


                      APT :: Report                 Reports on nation-state APTs activities,                        Campaign                        APT/Thre

                                                 including associated indicators (IOCs), attack                                                        at

                                                   techniques, and MITRE ATT&CK mappings.


                                                                                                                   Intrusion Set                    APT/Thre

                                                                                                                                                    at Actor

Collection                      Description                        TC data type         Tag


                                                                                              File          APT/Thre

                                                                                                                at


                                                                                              URL           APT/Thre

                                                                                                                at


                                                                                            Address         APT/Thre

                                                                                                                at


                                                                                              Host          APT/Thre

                                                                                                                at


                      APT :: Actors   Profiles of nation-state groups detailing their     Intrusion Set     APT/Thre

                                        characteristics, targets, motivations, and                           at Actor

                                                       techniques.


                  Attacks :: DDoS     Data on Distributed Denial of Service (DDoS)          Incident        Attacks/D

                                       attacks, including targeted resources and                              DOS

                                                    attack durations.


                                                                                            Address         Attacks/D

                                                                                                            DOS, CNC,

                                                                                                              DDOS


                 Attacks :: Deface    Records of defacement attacks, highlighting            Report         Attacks/D

                                      compromised websites and related actors.                                eface


                                                                                        URL(defaced site)


                Attacks :: Phishing    Information on phishing attacks, including           Incident        Attacks/P

                                      URLs of phishing websites. Note: do not use                            hishing

                                       IPs for detection - it may cause many false

                                             positives. Focus only on URLs.


                                                                                              URL

Collection                          Description                   TC data type      Tag


                   Attacks :: Phishing Kit    Collections of phishing website templates,     Incident     Attacks/P

                                                 scripts, and configurations used by                      hishing Kit

                                                              attackers.


                                                                                               URL


                                                                                              E-mail


                Compromised Data :: Shops     Sales proposals on compromised data on         Report       Comprom

                                                       darkweb marketplaces                                  ised

                                                                                                          Data/Sho

                                                                                                              p
                                                                                               URL


                                                                                             Address


               Compromised Data :: Accounts   Data on compromised access (credentials,       Report       Comprom

                                                 malware infections) sold in darkweb                         ised

                                                            marketplaces                                  Data/Acc

                                                                                                            ount
                                                                                               URL        Comprom

                                                                                                             ised

                                                                                                          Data/Acc

                                                                                                          ount, CNC


                                                                                             Address      Comprom

                                                                                                             ised

                                                                                                          Data/Acc

                                                                                                          ount, CNC


                                                                                              Host        Comprom

                                                                                                             ised

                                                                                                          Data/Acc

                                                                                                          ount, CNC

Collection                              Description                     TC data type     Tag


               Compromised Data :: Bank Cards   Information about compromised bank cards,          Report       Comprom

                                                sourced from card shops, forums, and public                       ised

                                                                   leaks.                                       Data/Ban

                                                                                                                 k Card
           Compromised Data :: Masked Cards     Information on compromised masked bank             Report       Comprom

                                                cards gathered from illicit marketplaces and                      ised

                                                                  forums.                                       Data/Mas

                                                                                                                ked Card


                        IM :: Discord           Extracted intelligence from Discord channels       Report       Comprom

                                                      and servers, mostly discussions.                            ised

                                                                                                                Data/Disc

                                                                                                                  ord
                       IM :: Telegram               Intelligence collected from Telegram           Report       Comprom

                                                  channels, including credentials, targeted                       ised

                                                    companies and attack discussions.                           Data/Tele

                                                                                                                  gram


                  Compromised Data :: SPD       Data on suspicious payment details (SPD) -         Report       Comprom

                                                    bank accounts, crypto wallets, phone                          ised

                                                      numbers and other data used for                           Data/Sus

                                                       laundering/illicit/stolen funds                           picious

                                                                                                                payment

                                                                                                                 details
                      Darkweb::Forums                      Darkweb forum posts.                    Report       Darkweb/

                                                                                                                 Forums


                       Open Threats             This feed aggregates real-time public reports     Campaign      HI/Open

                                                   on cybersecurity threats from diverse                         Threats

                                                 sources, including vendor blogs and social

                                                   networks.The data is enriched with our

                                                private threat intelligence and categorized by

                                                 threat actors, malware families, and other

                                                  key identifiers, providing comprehensive

                                                           global threat coverage.

Collection                           Description                      TC data type      Tag


                                                                                                File


                                                                                              Address


                                                                                                Host


                                                                                               E-mail


               Cybercriminals :: Report   Financially motivated cybercriminals reports,      Campaign       HI/Threat

                                          including associated indicators (IOCs), attack                     /Threat

                                           techniques, and MITRE ATT&CK mappings.


                                                                                            Intrusion Set   HI/Threat

                                                                                                             /Threat

                                                                                                             Actor


                                                                                                File        HI/Threat

                                                                                                             /Threat


                                                                                                URL         HI/Threat

                                                                                                             /Threat


                                                                                              Address       HI/Threat

                                                                                                             /Threat


                                                                                                Host        HI/Threat

                                                                                                             /Threat


               Cybercriminals :: Actors         Profiles of financially motivated           Intrusion Set   HI/Threat

                                          cybercriminals detailing their characteristics,                    Actor

                                              targets, motivations, and techniques.

Collection                      Description                    TC data type     Tag


                  IOC :: Common        General indicators of Compromise (IoCs)         Campaign      IoC/Com

                                      from threat reports (cybercriminals and APT)                     mon

                                       and Malware sections. Consists of Hashes

                                        (MD5, SHA1, SHA256), IPs, domains and

                                              URLs. Major source of IOCs


                                                                                          File


                                                                                          URL


                                                                                        Address


                      IOC::Primary       Same as IOC::Common; Enriched with            Campaign      IoC/Prima

                                      evaluation block and risk score for each IOC                      ry


                                                                                          File


                                                                                          URL


                                                                                         Host


                                                                                        Address


                      Malware :: C2             Information on malware                    URL        Malware/

                                       Command-and-Control (C&C) servers used                        CNC, CNC

                                           for data exfiltration and command

                                        distribution. This feed is also part of IOC

                                                        Common


                                                                                        Address


                                                                                         Host


                Malware :: Configs       Extracted malware configuration data.          Report       Malware

                                                                                                      Config

Collection                              Description                     TC data type      Tag


                                                                                                      File        Malware,

                                                                                                                  Malware

                                                                                                                   Config


                                                                                                     Host


                                                                                                    Address


                      Malware :: Report                 Detailed malware descriptions.               Report       Malware

                                                                                                                   Report


                    Malware :: Signature          Suricata signatures for malware detection.       Signature      Suricata,

                                                                                                                  Signature


                     Malware :: Yara rule        YARA rules for identifying specific malware       Signature       YARA,

                                                                   families.                                      Signature


                Compromised Data :: Git Leaks    Publicly available code from repositories like     Incident       OSI/Git

                                                 GitHub, filtered by your hunting rules. Note:                      Leak

                                                     hunting rules are on by default here


               Compromised Data :: Public Leak   Public data leaks from sources like Pastebin,      Incident      OSI/Publi

                                                 ghostbin, and others., including credentials,                     c Leak

                                                   database dumps, configuration files, and

                                                  logs. Note: hunting rules are on by default

                                                                     here


                      OSI :: Vulnerability         Information on software vulnerabilities,       Vulnerability   OSI/Vulne

                                                      associated exploits, and available                           rability

                                                           proof-of-concept details.


                 Suspicious IP :: Open Proxy        Information on publicly available proxy         Address         Open

                                                 servers, including potentially misconfigured                      Proxy

                                                                   proxies.

Collection                                     Description                                       TC data type                         Tag


                Suspicious IP :: Scanners                IP addresses identified as scanning or                            Address                          Scanner

                                                              probing corporate networks.


               Suspicious IP :: Socks Proxy           IP addresses of infected hosts configured as                         Address                           Socks

                                                      SOCKS proxies used for anonymized attacks.                                                             Proxy


                Suspicious IP :: Tor Node              Data about known Tor exit nodes used as                             Address                         Tor Node

                                                                     anonymity relays.


                  Suspicious IP :: VPN                 Information about public and private VPN                            Address                            VPN

                                                      servers identified as potentially malicious or

                                                                       suspicious.


       Note: Collection IOC :: Primary - is specially created to get only IoC and has different attribution parameters in place. Contains information from the
       following collections: [APT:: Report, APT :: Actors, Cybercriminals :: Reports, Cybercriminals :: Actors, Malware :: C2]. It is possible to find correlations
       between collections but this is not the case. The main idea of IOC :: Primary collection is to use it for detection rules. It is a replacement for IOC ::


       Troubleshooting
       Common, so you don’t need to use both in parallel.


       First of all, as you begin the troubleshooting process, we kindly ask you to familiarize yourself with the common errors that occur when using our
       application. If errors occur outside of common cases, we will need more details for this purpose. Before starting, please review the Common Errors
       and Solutions listed below - if your issue is not listed, gather the following details for support:


          · Your system information

          · The exact time the error occurred

          · Application logs (see “Log Collection” section)


       Enable Debug Logging

       Before collecting logs, enable debug mode for the failed job:


          · In ThreatConnect, go to Organization Settings -> Apps tab -> Jobs.

          · Locate the job related to the Group-IB TI integration.

          · Edit the job configuration and change log level to debug.

          · Save the changes and allow the job to run again so debug entries are written to the logs.
       Log Collection

       When contacting support, always include application logs:


          · Go to Organization Settings -> Apps tab -> Jobs.

          · Expand the settings for the failed job.

          ·

Select View Log.

          · Click Download to save the log file.

          · Attach the log to your support request via Email or Service Desk.


       Testing API Connectivity via cURL

       To verify that your Group-IB TI credentials are valid and the API is accessible, run the following curl command from your terminal: curl
       'https://tap.group-ib.com/api/v2/sequence_list' -u 'LOGIN:API_KEY' -H 'Accept: */*' -v


          · Replace with the email address used for your Group-IB Threat Intelligence account.

          · Replace with your personal API key (not your password).


       If authentication succeeds, you’ll receive a list of available collections. If it fails, refer to the HTTP status code and the “Common Errors & Solutions”
       section below.


       If your Group-IB and proxy credentials are correct, attach the command output to your support request via Email or Service Desk so we can verify your
       Group-IB profile. Using a proxy:


          · With authentication:

                · --proxy '://:@:'


          · Without authentication:

                · --proxy '://:'


       Example: curl --proxy https://127.0.0.1:3128 'https://tap.group-ib.com/api/v2/sequence_list' -u 'LOGIN:API_KEY' -H 'Accept: */*' -v


       Common Errors and Solutions


                                   Issue                                                                  Resolution


               ThreatConnect token expired or missing       Go to Gear -> Org Settings -> Membership tab and ensure the API token exists and is active. Renew

                                                                                                          if expired.

Issue                                                                       Resolution


                 Group-IB API key expired or missing             In the Group-IB TI Portal, go to Profile -> Security and Access -> Personal Token, generate a new

                                                                                            token, and update it in the job configuration.


                Server cannot reach Group-IB TI Portal           Run the cURL test from the ThreatConnect server. If using a proxy, verify configuration. If needed,

                                                                                           test from another machine and whitelist its IP.


               Group-IB account settings misconfigured            In Profile -> Security and Access -> IP Whitelist, ensure all ThreatConnect server IPs are listed.


                    Mismatched collection access               Verify that the collections enabled in ThreatConnect match those granted in your Group-IB account.


               License expired or Partner/POC limitation                    Check your license status. Partner/POC licenses typically expire in 30 days.


                    Client blocking incoming data                 Add all URLs and IPs listed in the Group-IB TI Integration Starting Guide to your firewall or proxy

                                                                                                              allowlist.


                            API key errors                                 Regenerate the API key and copy it without extra spaces or hidden characters.


       Data Input Error Code (HTTP) in TC

       When configuring or running the Group-IB Threat Intelligence Data Input in TC, the app communicates with the Group-IB API. If something goes wrong,
       HTTP status code will appear in your logs. Below are common error code and how to resolve this:


                          Code                                     Cause                                                       Solution


                     403: Forbidden                 Authenticated, but denied access            Ensure the TC server IP is in your access list in the Group-IB profile.

                                                                                                 Confirm the API key is valid and has permissions for the selected

                                                                                                            collections. Use curl to test other endpoints.


                429: Too Many Requests                     API rate limit exceeded.            Reduce request frequency. The allowed rate depends on your license.

                                                                                                                    Wait a few minutes and retry.

ArcSight
       ArcSight SIEM
                SIEM Connector
                     Connector
       The integration connects Group-IB Threat Intelligence to ArcSight, giving security teams a continuous stream of external threat data across multiple
       feed types - each suited to different SOC workflows:


          · Indicators of compromise feed directly into correlation rules and alert enrichment.

          · Compromised credential and card data can drive automated responses when employee or customer accounts appear in breaches.

          · APT and cybercriminals reports with full MITRE ATT&CK mapping support threat hunting and actor attribution.

          · Attack campaign feeds provide early warning for brand and infrastructure threats.

          · Suspicious IP feeds populate active lists for real-time blocking, while malware and C2 data enable correlation against known adversary
               infrastructure.


       Technically, a Python poller fetches data from the Group-IB TI portal and writes JSON files to a local folder, which the ArcSight FlexConnector monitors
       and forwards as structured CEF events to the Logger.


       Note: Initial Steps must also be completed before proceeding.


       Requirements

          · ArcSight FlexConnector 7.7.0.8044.0 or newer (JSON Folder Follower)

          · Docker >= 24 with the Compose plugin (recommended), or Python 3.10+ installed with the following modules:
               black==24.10.0 certifi==2024.12.14 charset-normalizer==2.0.12 ciaops==1.0.1 click==8.1.8 dataclasses==0.6 idna==3.10 isort==5.13.2
               mypy-extensions==1.0.0 packaging==24.2 pathspec==0.12.1 platformdirs==4.3.6 pyaml==21.10.1 python-dotenv==1.0.1 PyYAML==6.0.2
               requests==2.32.3 tomli==2.2.1 typing_extensions==4.12.2 urllib3==1.26.9

          · Threat Intelligence credentials (username + API key) with access to the collections you intend to enable


       Configuration

       Copy the example config and open it for editing.

       Docker
       cp .env.example .env $EDITOR .env
       Set your credentials:
        GIB_USERNAME= GIB_API_KEY=
       Enable the collections you want:
        GIB_COLLECTIONS_IOC__COMMON_ENABLE=true GIB_COLLECTIONS_IOC__COMMON_DEFAULT_DATE=2026-01-01
       Encoding rule: collection names use __ (double underscore) in place of /, uppercased. For example: apt/threat ->
       GIB_COLLECTIONS_APT__THREAT_ENABLE


       PII redaction: by default, sensitive fields (passwords, emails, card numbers) are redacted before data reaches ArcSight. This is controlled by two
       settings:
        GIB_REDACT_PII=true           # true (default) = redact. Recommended for production.                # false = send plaintext. Only for trusted environments
                       #         or IR workflows that need raw values. GIB_REDACT_KEY=         # HMAC secret for reproducible hashing across runs.                #
       Generate once: openssl rand -hex 32                    # Leave blank to auto-generate per process start                # (hashes then change on restart;
       cross-run joins break).
       Note: GIB_REDACT_KEY is ignored if GIB_REDACT_PII=false.


       All collections default to false - an unconfigured deploy fetches nothing. Enable only collections your API key has been granted access to.

Bare-metal/VM
       cp configuration.sample.yaml configuration.yaml $EDITOR configuration.yaml
       Fill in your credentials and enable collections:
        client: username: api_key: redact_pii: true redact_key: collections: ioc/common:              enable: true   default_date: 2026-01-01
       Note: If default_date is not set, the initial poll starts from 3 days ago. Avoid a very early start date for high-volume collections such as suspicious_ip/*.


       Deploy

       Download the Group-IB Threat Intelligence SIEM Connector for ArcSight from here and unpack it.

       Docker


          · Build and start the container:
               docker compose up -d --build

          · Check it is running:
               docker compose logs -f gib-poller
       JSON files will appear in ./data on the host. The FlexConnector should be pointed at this directory.


       Note: The container runs as non-root UID 10001. Create the required directories first:
        mkdir -p data logs state sudo chown -R 10001:10001 data logs state
       The container includes a healthcheck that verifies the data/ directory is accessible. You can monitor container health with:
       docker compose ps
       Bare-metal/VM


          · Install dependencies:
               pip install -r requirements.txt

          · Run the poller from the working directory:
               cd /opt/current/arcsight/connectors/gib python3.10 GIB_poller.py

          · Schedule it to run hourly via cron:
               5 * * * * cd /opt/current/arcsight/connectors/gib && \    flock -n .gib_poller.lock python3.10 GIB_poller.py >> logs/cron.log 2>&1
       ArcSight FlexConnector Setup
       Create a Receiver


          · Log in to the ArcSight web interface.

          · Go to Configuration -> Receivers -> Add.

          · Set Type to SmartMessage Receiver, encoding UTF-8, source type CEF.

        · Enable, save, and note the Receiver Name.
       Configure the FlexConnector


          · Before running runagentsetup.sh, copy all configs/*.jsonparser.properties into /current/user/agent/flexagent/gib_root_parser/

          · Run the setup wizard:
               ./runagentsetup.sh -i console

          · In the wizard, select Add a connector -> ArcSight FlexConnector JSON Folder Follower and set:


                · JSON Log Folder Location: the path to the data/ directory (host path of the ./data bind mount for Docker, or the working directory for
                   Bare-metal/VM)

                · JSON Configuration File Name Prefix: configs/gib_root_parser


               Note: The “Folder does not exist” warning is harmless if the poller has not run yet.

          ·

Set destination to ArcSight Logger SmartMessage (encrypted), enter host:port, Receiver name from above, Compression Disabled, CEF
               Version 0.1.

          · Fill in metadata (Name, Location, DeviceLocation, Comment) - avoid empty or digits-only values.

          · Install as a service and start it:
            service arc_ start
       Verify Data Flow


       In ArcSight web UI go to Analyze -> Search and run:
        receiver=""
       If events appear, the integration is working correctly.


       Working with the Integration
       Enabling and Configuring Collections


       Each collection is toggled independently. Open your .env (Docker) or configuration.yaml (Bare-metal/VM) and enable the collections you need.


       Docker
        GIB_COLLECTIONS_APT__THREAT_ENABLE=true GIB_COLLECTIONS_APT__THREAT_DEFAULT_DATE=2026-01-01
       GIB_COLLECTIONS_IOC__COMMON_ENABLE=true
       Bare-metal/VM
        collections: apt/threat:     enable: true   default_date: 2026-01-01 ioc/common:         enable: true
       The default_date field sets how far back the first poll reaches. If omitted, it defaults to 3 days ago. After the first run the poller tracks its own position -
       changing default_date later has no effect unless you delete the .state checkpoint file.


       Note: For high-volume collections such as suspicious_ip/*, set a recent default_date (e.g. last 2 days) to avoid ingesting an overwhelming backlog on
       the first run.


       After editing .env, apply the changes:
       docker compose up -d
       Checking the Poller is Running


       Docker
        docker compose ps docker compose logs --tail 50 gib-poller
       Bare-metal/VM
       pgrep -af GIB_poller tail -50 logs/current_session_poll.log
       Result


       A healthy run produces lines like:
        [INFO] apt/threat - 12 portions fetched, seqUpdate 1735200000 [INFO] ioc/common - 3 portions fetched, seqUpdate 1735200100
       If a collection is skipped with a not granted warning, your API key does not have access to it.


       To confirm JSON files are being written:
        ls -lh data/
       Files follow the naming pattern:
        ___.json

Adjusting Poll Frequency


       By default the poller runs hourly (Bare-metal/VM via cron) or every 900 seconds (Docker loop mode). To change the Docker interval:
        GIB_POLL_INTERVAL=1800 # 30 minutes
       To switch to one-shot mode (useful if you prefer to drive execution from an external scheduler):
       GIB_RUN_MODE=once
       Querying Data in ArcSight


       Log in to the ArcSight web interface and go to Analyze -> Search.


       See all events from this integration:
        receiver=""
       Filter to a specific collection:
        receiver="" AND name CONTAINS "apt/threat"
       Search within a time range:
        receiver="" AND deviceReceiptTime >= 2026-01-01T00:00:00
       Find events for a specific indicator:
        receiver="" AND destinationAddress = "192.0.2.1"
       Filter by threat category:
       receiver="" AND deviceEventCategory CONTAINS "Malware"
       Resetting a Collection


       To re-fetch a collection from scratch, delete the .state checkpoint file and restart the poller. The next run will treat default_date as the starting point
       again.


       Docker
        docker compose stop rm state/.state docker compose up -d
       Bare-metal/VM
        rm .state python3.10 GIB_poller.py
       Available Collections

       The table below lists all collections available for ingestion. Enable only those your API key has been granted access to.


                                    Collection                                                    Contents                                        Notes


                                    apt/threat

Collection                                Contents                                    Notes


                                                     APT threat reports with MITRE ATT&CK mapping


                            apt/threat_actor         APT actor profiles - TTPs, targets, infrastructure


                                hi/threat           Cybercriminals threat reports with MITRE mapping


                             hi/threat_actor           Cybercriminals actor profiles - TTPs, targets,

                                                                      infrastructure


                             attacks/ddos            DDoS campaign records - target, dates, method


                             attacks/deface         Web defacement campaigns - target domain, actor


                          attacks/phishing_kit      Phishing kit fingerprints and hosting infrastructure


                      compromised/account_group     Compromised credentials from stealer logs. Emails      High volume - set a recent

                                                    and passwords are redacted before writing to disk.            default_date


                      compromised/bank_card_group     Compromised payment cards. PAN is masked

                                                                       (first6-last4).


                        compromised/breacheddb         Breached database records - email domain,           High volume - set a recent

                                                        location, phone, IP. Supersedes the legacy                default_date

                                                                   breached collection.


                           compromised/mule              Money mule records (legacy collection)            Auto-skipped if not granted


                           compromised/spd            Stolen personal data - type, service type, IBAN,

                                                        bank card, linked threat actor and malware

Collection                                Contents                                      Notes


                               ioc/primary          Primary curated IOCs with per-indicator risk scores

                                                    (domain, URL, IP, hash) plus linked threat actor and

                                                                      malware family


                              ioc/common               Aggregated indicators of compromise - IPs,

                                                                  domains, URLs, hashes


                            malware/malware            Malware sample reports - family, behaviour,

                                                                     targeted sectors


                              malware/cnc               C2 infrastructure - IPs, domains, protocols


                            osi/git_repository      Leaked credentials and secrets found in public Git       High volume - set a recent

                                                                        repositories                                default_date


                             osi/public_leak          Sensitive data found in public paste sites and         High volume - set a recent

                                                                          forums                                    default_date


                         suspicious_ip/tor_node                     Tor exit node IP list                  Very high volume - use a recent

                                                                                                                    default_date


                        suspicious_ip/open_proxy               Open HTTP/HTTPS proxy IPs                   Very high volume - use a recent

                                                                                                                    default_date


                        suspicious_ip/socks_proxy                    SOCKS proxy IPs                       Very high volume - use a recent

                                                                                                                    default_date


       Troubleshooting
       No Events Appearing in ArcSight Search

Issue                                       Likely cause                                  Fix


                 Query returns no results                   FlexConnector service not running                   Run: service

                                                                                                            arc_<name> status -

                                                                                                              start it if stopped


               Service is running but no data    Wrong JSON Log Folder Location in FlexConnector config            Re-run

                                                                                                             runagentsetup.sh

                                                                                                             and verify the path

                                                                                                            matches the actual

                                                                                                               data/ directory


       Service running, path correct, still no        Poller has not run yet or is not producing files      Check data/ for .json

                           data                                                                              files. If empty, run

                                                                                                             the poller manually

                                                                                                                 and check

                                                                                                            logs/current_session

                                                                                                                  _poll.log


           Events arrive but CEF fields are        .jsonparser.properties files not in place before setup     Stop the service,

                          empty                                                                                    copy all

                                                                                                            configs/*.jsonparser.

                                                                                                                properties to

                                                                                                            flexagent/gib_root_p

                                                                                                               arser/, restart


       Authentication & API Errors


                           Issue                                       Likely cause                                  Fix


                 401 Unauthorized in logs                       Wrong or expired API key                       Regenerate the

                                                                                                            token in the TI portal

                                                                                                             and update .env or

                                                                                                             configuration.yaml

Issue                                       Likely cause                                     Fix


               Collection skipped with “not          API key does not have access to that collection               Disable the

                    granted” warning                                                                          collection or contact

                                                                                                               Group-IB to extend

                                                                                                                     access


          Connection timeout or SSL error     Proxy or firewall blocking outbound HTTPS to tap.group-ib.com     Configure proxy

                                                                                                                  settings via

                                                                                                              GIB_PROXY_* in .env

                                                                                                              or the proxy section

                                                                                                              in configuration.yaml


       Docker-Specific Issues


                          Issue                                       Likely cause                                     Fix


       Container exits immediately on start                  Missing or malformed .env file                     Verify .env exists

                                                                                                              and GIB_USERNAME

                                                                                                               / GIB_API_KEY are

                                                                                                                set. Run: docker

                                                                                                                 compose logs

                                                                                                                    gib-poller

        Permission denied writing to data/              Host directories not owned by UID 10001               Run: sudo chown -R

                         or logs/                                                                              10001:10001 data

                                                                                                                   logs state


       ciaops not found during image build           No internet access and vendor/ wheel is missing                  Place

                                                                                                              ciaops-1.0.1-py3-non

                                                                                                              e-any.whl in vendor/

                                                                                                                   and rebuild

Issue                                             Likely cause                                        Fix


           FlexConnector cannot see new      data/ bind mount path mismatch between container and connector host          Ensure the

                     JSON files                                                                                      FlexConnector JSON

                                                                                                                     Log Folder Location

                                                                                                                      points to the same

                                                                                                                       host path as the

                                                                                                                      ./data bind mount


               docker compose ps shows            data/ directory missing or not accessible inside the container     Check that the ./data

                container as unhealthy                                                                                 bind mount was

                                                                                                                        created before

                                                                                                                       starting: mkdir -p

                                                                                                                     data && sudo chown

                                                                                                                     -R 10001:10001 data


       Collections Returning No Data


                        Issue                                             Likely cause                                        Fix


          Collection enabled but no events       default_date set too far in the past for a high-volume collection    Set a more recent

                       appear                                                                                        default_date, delete

                                                                                                                      .state to reset the

                                                                                                                       checkpoint, and

                                                                                                                       restart the poller


         Some collections work, others do                      Mixed access rights on the API key                           Check

                         not                                                                                         logs/current_session

                                                                                                                         _poll.log for

                                                                                                                     per-collection skip or

                                                                                                                       error messages

Issue                                                  Likely cause                                          Fix


          Data stops arriving after running                    Poller process crashed or cron job stopped                     Docker: docker

                        fine                                                                                                   compose ps.

                                                                                                                             Bare-metal/VM:

                                                                                                                           pgrep -af GIB_poller

                                                                                                                           and check cron logs


       PII Redaction Issues


                       Issue                                                  Likely cause                                          Fix


          Emails and passwords arriving in              GIB_REDACT_PII set to false, or not set in an older config                  Set

               ArcSight as plaintext                                                                                       GIB_REDACT_PII=tru

                                                                                                                           e in .env (Docker) or

                                                                                                                            redact_pii: true in

                                                                                                                           configuration.yaml.

                                                                                                                            Restart the poller.


        Hashes differ between runs for the    GIB_REDACT_KEY is blank - a new random key is generated each process start            Set

                    same email                                                                                             GIB_REDACT_KEY to

                                                                                                                              a stable secret

                                                                                                                            (openssl rand -hex

                                                                                                                             32). Store it as a

                                                                                                                             secret and reuse

                                                                                                                             across restarts.

           Need plaintext values for an IR                        Production redaction settings active                              Set

                   investigation                                                                                           GIB_REDACT_PII=fal

                                                                                                                            se temporarily in a

                                                                                                                                controlled

                                                                                                                           environment. Ensure

                                                                                                                              Logger access

                                                                                                                           controls are in place.

                                                                                                                             Revert after the

                                                                                                                              investigation.

Custom  API tools
       TI Data Export Utility
       This guide provides step-by-step instructions on how to install, configure and use the Group-IB TI Data Export Utility for exporting attributed and
       non-attributed threat intelligence data in various formats.

Glossary

       EU (Export Utility) Refers to the Group-IB TI Data Export Utility used for retrieving and exporting threat intelligence data.


       AD (Attributed Data) Exported threat intelligence data that includes attribution details such as threat actor names, malware families, or source
       references.


       IoC (Indicator of Compromise) Non-attributed technical indicators such as IP addresses, domains, file hashes, or filenames used for threat detection.


       seqUpdate A mechanism that supports incremental export, ensuring the tool continues from the last exported record and avoids reprocessing already
       exported data.


       TI (Threat Intelligence) Group-IB’s platform for collecting, analyzing, and distributing cyber threat intelligence.


       Collection A defined data stream or dataset within the Threat Intelligence platform (e.g., hi/threat, attacks/deface) from which data can be exported.


       Keyword Filtering An optional setting that allows filtering of export results based on the presence of specific keywords in certain fields (e.g., expertise,
       tags).


       BI Tools (Business Intelligence Tools) Software platforms used to analyze and visualize data to support decision-making. Common examples include
       Microsoft Power BI, Tableau, and Looker. In cybersecurity, BI tools are often used for trend analysis, historical threat tracking, and reporting.


       Format The output file type selected for exported data. Supported formats include CSV, XLSX, JSON, and TXT.

Introduction

       The Group-IB TI Data Export Utility is a command-line tool designed to export threat intelligence data in structured formats for internal analysis,
       automation, or integration with other systems. It supports both attributed (AD Export) and non-attributed (IoC Export) data.


       Before using the Group-IB TI Data Export Utility, please review the startup instructions in the Group-IB TI Integration Starting Guide.


       Once you have completed the initial setup, follow the steps below.

Use Cases

       The TI Data Export Utility is a command-line tool designed to export structured threat intelligence data from the Group-IB TI platform. Below are
       practical, realistic use cases where this tool helps streamline cybersecurity workflows across security operations, threat hunting, and compliance
       teams.


       1. IOC Export for Local Storage and Integration Purpose: Export threat indicators (IPs, hashes, domains, URLs) into a local directory for further use. Use
       case: The utility can place exported IOCs into a designated folder where other systems (such as SIEM or SOAR) can pick them up for integration.
       Value: Offers a flexible method to stage IOCs locally, enabling controlled ingestion into security platforms without requiring direct API integration.


       2. Customized Threat Monitoring via Hunting Rules Correlation Purpose: Export threat data based on applied Hunting Rules configured in the TI
       Platform Use case: Users can extract threat reports and indicators that align with their configured hunting rules, focusing only on intelligence matching
       their environment. Value: Enables tailored threat visibility and reduces the volume of irrelevant data.


       3. Populate Internal Dashboards or Threat Repositories Purpose: Save exported TI data into your own internal systems such as threat portals,
       spreadsheets, or data lakes. Use case: The exported data can be manually uploaded to internal BI tools for pivoting, searching, or cross-referencing
       with internal telemetry. Value: Enables centralized access to threat intelligence across multiple teams.

Installation

       Important! The application requires Python 3.10.X-3.12.X installed on your system.

       Steps:


          · Download the archive package from here and unpack it.

          · Navigate to the utility directory
               cd group_ib_ti_data_export_utility

          · Install dependencies
               pip install -r requirements.txt
       Warning! It is recommended to use python and pip aliases instead of python3 and pip3.

       Offline Installation


       If you are not connected to the Internet, use the following commands:


          · For Windows:
               pip install -r requirements_windows.txt

          · For Linux and Linux-based systems:
               pip install -r requirements_linux.txt

Running the Utility

       To start the utility, run the following command:
        python run_configuration.py
       The Main Menu will appear, from which all configuration and export actions are accessible.

CLI Menu Structure Overview

       Below is a simplified visual representation of the tool’s menu structure. It helps users understand how the different configuration sections are
       organized and interact with each other.


       Use this visual as a reference while working through each section described below.


       Data Export Utility Options

1. Client Configuration Menu


       This menu allows you to configure your client profile settings. Use the arrow keys to navigate between options. To modify a setting, select it and press
       Enter.


                             Option                                                                     Description


                           Credentials                                            Add and manage credentials (API key, URL, username).


                       Proxy Configuration                                               Add proxy connection settings if needed.


                      Destination Directory                                 Specify the export output path, where retrieved data will be saved.

Option                                                                     Description


                    Frequency Configuration                      Set how often the tool should run (e.g., once a day, twice a day, four times a day, or hourly).


       1.1 Credentials


       This menu allows you to configure multiple credentials.


                               Option                                                                     Description


                          Show Credentials                                               Display all currently configured credentials.


                         Update a Credential                                        Modify an existing credential without affecting others.


                      Update All Credentials                                                Configure all credentials sequentially.


       Required Fields


                               Option                                                                     Description


                              API Key                                           The client API key, generated in the TI portal profile settings.


                              API URL                                The API network address. By default, it is set to https://tap.group-ib.com/api/v2/.


                             Username                                                 The client username, used to log into the TI portal.


       1.2 Proxy Configuration (Optional)

Option                     Description


                          IP Address    Enter the IP address of your proxy server.


                           Password     Enter the password for your proxy server.


                                 Port            Enter the required port.


                            Protocol           Enter the required protocol.


                           Username        Enter the username for your proxy.


                         Enable proxy          Enable / Disable the proxy.


       2. Export Configuration

2.1 Attributed Data (AD Export)


       This option allows you to configure the export of data with attribution from the TI system. Menu options:


                              Option                                                                   Description


                          Change Status                                              Enable / Disable export. Options: False and True.


                    Change File Configuration                   Select one or more export formats from the available options: CSV, XLSX, JSON and TXT.

                                                             Multiple formats can be selected simultaneously for download. Note: This option applies only to

                                                                Attributed Data (AD Export). Non-Attributed Data (IoC Export) is always downloaded in TXT

                                                                                                          format.


                        Collection Settings                                             Configure collection settings (see below).


                      Keyword-based filtering                           Enable / Disable keyword filtering with specifying filter field and keyword.


       Collection Settings include


       To modify collection settings, select the Change Configuration option and start typing the name of the desired collection from the suggested list. Once
       selected, configure the collection options:


          ·

Change Start Date: Enter a new start date in the specified format.

          · Change End Date: Enter a new end date (optional, for “Run: data for period”).

          · Change Status: Enable or disable the collection export. True enables, False disables.

          · Clear seqUpdate: Resets the export progress. If the seqUpdate is cleared, data export will start from the specified start date. If left unchanged,
               the export will resume from where it last stopped.

          · Set Filtering Flags: Change the status of filtering flags like apply_hunting_rules, is_tailored, or apply_has_exploit if applicable for the selected
               collection. Use True to enable filtering and False to disable.


       Keyword-based filtering


       To modify keyword-based filtering settings, press enter and start typing the name of the desired collection from the suggested list. Once selected,
       proceed with the following options:


          · Enable/Disable Filtering: Turn filtering by the keywords on or off.

          · Set Filtering Field: Specify the field to filter by. This must be entered manually.

          · Set Filtering Keyword: Define the keyword to use for filtering. This must be entered manually.

          · Set Both Field & Keyword: Configure both the filtering field and the keyword in a single operation.


       Note: To filter by the expertise field using the keyword Ransomware in the hi/threat collection, set expertise as the filtering field and Ransomware as
       the keyword.


       Important! Filtering is available only for the fields listed in the List_of_filter_fields_for_collections.txt file. If a required field does not appear on the list,
       please contact support through the Service Desk. Our team will review the proposal and provide further assistance if the enhancement is applicable.

       2.2 Non-Attributed Data (IoC Export)


       Follows the same process as Attribution Data Export, but it exports data without attribution. For configuration follow the same process as described in
       the AD Export.


       3. Running Export Operations

3.1 Run Test Connection


       This option checks whether the Data Export Tool works properly with the current configuration and can reach the TI API. If errors are encountered, the
       utility will notify you.

       3.2 Run: Data for Period (AD Export)


       This option starts the data export for the period set in the Attribution Data for Period settings. Upon completion, the file will be saved in the directory
       specified under Client Configuration -> Data Directory. If the directory was not specified, that file will be stored under data -> result directory.

       3.3 Run: TI_Data_Export_Utility (AD/IoC Export)


       This option starts the Data Export Tool in the background. Ensure that the AD Export and IoC Export settings are configured before running the script.


       The file formats used will match those selected in the Attribution Data Export and Non-Attribution Data Export configuration sections. Upon
       completion, the file will be saved in the directory specified under Client Configuration -> Data Directory. If the directory was not specified, that file will
       be stored under data -> updated directory for AD Export and data -> ioc for IoC Export.

Tips and Best Practices

          · Clear seqUpdate when starting a new export run. Even if a new start date is specified, the utility will continue from the last saved seqUpdate
               unless it is manually cleared. This ensures the export uses the defined date range instead of resuming from the previous state.

          · Run a test connection before launching an export. Always use the “Run Test Connection” option to verify that your configuration is correct and
               connectivity with the TI API is functional.

          · Review filtering flags for each collection. Ensure filters such as apply_hunting_rules, is_tailored, or apply_has_exploit are configured as needed,
               as they significantly affect the resulting data set.

          · Use keyword filtering to narrow results. If supported for the collection, enabling keyword-based filtering helps reduce noise and retrieve more
               relevant, actionable threat intelligence.

          · Use separate credentials for multi-tenant environments. If you manage exports for multiple organizations, it is recommended to configure
               distinct credentials for each to maintain clarity and separation of data.

TI Python library
       The ciaops Python library is available on PyPI: ciaops. It simplifies work with the Group-IB TI, DRP, and ASM APIs and gives you flexibility to customize
       search and retrieval of data.


       ciaops
       ciaops - Python library to communicate with Group-IB Products (TI, DRP, ASM) via API.


       License

       This project is licensed under the MIT License - see the LICENSE file in the project repository for details.


       Installation

       Lib deps: requests, urllib3.


       ciaops lib is available on PyPI:
        pip install ciaops
       Or use a Portal WHL archive. Replace X.X.X with current lib version:
        pip install ./ciaops-X.X.X-py3-none-any.whl


       Usage
       Initialization


       Initialize a poller with your credentials. TLS certificate verification is enabled by default.


       Call set_verify() only when you need to override the default: pass False to disable verification (for example, local testing behind a corporate proxy), or
       pass a path to a custom CA bundle.
        from ciaops import TIPoller, DRPPoller, ASMPoller # Threat Intelligence ti = TIPoller(username='example@gmail.com', api_key='API_KEY',
       api_url='TI_API_URL') # Digital Risk Protection drp = DRPPoller(username='example@gmail.com', api_key='API_KEY', api_url='DRP_API_URL') # Attack
       Surface Management asm = ASMPoller(username='example@gmail.com', api_key='API_KEY', api_url='ASM_API_URL') # Override only when needed:
       ti.set_verify(False)             # disable TLS check (local testing only) ti.set_verify('/path/to/ca-bundle') # custom CA bundle
       Proxy setup (all pollers share the same interface):
        ti.set_proxies(      proxy_protocol='https',    proxy_ip='10.0.0.1',    proxy_port='3128',   proxy_username='user',     # optional
       proxy_password='secret',        # optional )
       Use pollers as context managers to ensure the session is always closed:
        with TIPoller(username='...', api_key='...', api_url='...') as ti:   generator = ti.create_update_generator('apt/threat', sequpdate=16172928022293)       for
       portion in generator:         print(portion.parse_portion())
       Tag your integration in the User-Agent header with set_product() - required by some on-premise deployments:
        ti.set_product(      product_type='SIEM',      product_name='MySIEM',        product_version='2.1',   integration_name='ciaops-siem',
       integration_version='1.0', )
       Collection constants


       Use typed constants instead of bare strings to avoid typos and get IDE autocomplete:
        from ciaops.collection_meta import TICollections, DRPCollections, ASMCollections # TI examples TICollections.APT_THREAT                          #
       "apt/threat" TICollections.COMPROMISED_ACCOUNT_GROUP # "compromised/account_group" TICollections.MALWARE_CNC                                      #
       "malware/cnc" # DRP DRPCollections.VIOLATION                          # "violation" # ASM ASMCollections.ASSETS_UPDATED               # "assets/updated"
       ASMCollections.ISSUES_UPDATED                    # "issues/updated"

Look up the recommended TTL for any TI collection:
        TICollections.get_ttl(TICollections.MALWARE_CNC)              # 90 (days) TICollections.get_ttl(TICollections.COMPROMISED_MESSENGER) # None (no
       expiry)
       Use constants anywhere a collection name string is expected:
       poller.set_keys(TICollections.APT_THREAT, keys) generator = poller.create_update_generator(TICollections.MALWARE_CNC, sequpdate=...)
       Collections mapping


       Method set_keys() sets keys to search in the selected collection. It should be a python dict mapping_keys = {key: value} where
        key - result name
        value - dot-notation string with searchable keys
        mapping_keys = {"result_name": "searchable_key_1.searchable_key_2"}
       Parser finds keys recursively in the API response, using dot-notation in value. If you want to add your own data to the results start the value with a star
       *.
        mapping_keys = { "network": "indicators.params.ip", "result_name": "*My_Value" }
       For set_keys() or set_iocs_keys() methods you can make a full template to get nested data in the way you want.
        mapping_keys = { 'network': {     'ips': 'indicators.params.ip' }, 'url': 'indicators.params.url', 'type': '*network' }
       poller.set_keys(collection_name="apt/threat", keys=mapping_keys) poller.set_iocs_keys(collection_name="apt/threat", keys={"ips":
       "indicators.params.ip"})
       Portions generator


       Use the methods create_update_generator() and create_search_generator() to create a generator, which returns portions of limited feeds.
        Update generator - goes through the feeds in ascending order. Feed iteration is based on the seqUpdate field.
        Search generator - goes through the feeds in descending order. Feed iteration is based on the resultId field.
        generator = poller.create_update_generator(        collection_name='compromised/account_group',            date_from='2021-01-30',       date_to='2021-02-03',
       query='8.8.8.8',     sequpdate=20000000,        limit=200 )
       Each portion (iterable object) is presented as a Parser class object. You can get raw data (in JSON format) or a parsed portion (python dictionary
       format), using its methods and attributes.
        for portion in generator:   parsed_json = portion.parse_portion(as_json=False)          iocs = portion.get_iocs(as_json=False)         sequpdate =
       portion.sequpdate       count = portion.count     raw_json = portion.raw_json      raw_dict = portion.raw_dict
       Attribute sequpdate of the generator iterable object gives you the last sequence update number (seqUpdate) of the feed, which you can save locally.


       Attribute count of the generator iterable object shows you the number of feeds left in the queue. For the search generator, count returns the total
       number of feeds in the queue.


       Methods parse_portion() and get_iocs() of generator iterable objects use your mapping keys (IoCs keys) to return parsed data. You can override
       mapping keys using the keys parameter in these functions.
        parsed_json = portion.parse_portion(as_json=False) iocs = portion.get_iocs(as_json=False, keys=mapping_override_keys)
       You can also use the bulk_parse_portion() method to get multiple parsed dicts from every feed.
       new_parsed_json = portion.bulk_parse_portion(          keys_list=[{"ips": "indicators.params.ip"}, {"url": "indicators.params.url"}],    as_json=False, )
       TIPoller extra methods

       Available collections


       Call get_available_collections() to discover which collections your API key can access before iterating.
        collection_list = ti.get_available_collections() seq_update_dict = ti.get_seq_update_dict(date='2020-12-12') compromised_account_sequpdate =
       seq_update_dict.get('compromised/account_group') # Check which collections have active hunting rules applied hunting_collections =
       ti.get_hunting_rules_collections()
       Find feed by ID


       Returns a Parser object for a single feed by its ID.
       feed = ti.search_feed_by_id(collection_name='apt/threat', feed_id='abc123') parsed = feed.parse_portion()
       Download file

Download a binary file embedded inside a threat report.
       binary = ti.search_file_in_threats( collection_name='hi/threat', feed_id='feed_id', file_id='file_id_inside_feed', )
       Download PDF reports
       # Download a PDF for an HI or APT threat pdf_bytes = ti.download_threat_pdf(threat_id='abc123') # Download an HI analytic report PDF (use the
       file.name field from an hi/analytic record) pdf_bytes = ti.download_analytic_report_pdf(file_name='/23ae4ab7.../file/450ffbd4...') with
       open('report.pdf', 'wb') as f:   f.write(pdf_bytes)
       Risk scoring


       Score one or more IPs or domains against the TI database. Scores range from 0 to 100. For endpoint details and score interpretation, see the IP
       Scoring and Domain Scoring articles.
        # IP scoring - single or multiple ti.get_ip_scoring('8.8.8.8') ti.get_ip_scoring(['8.8.8.8', '1.1.1.1']) # Domain scoring - single or multiple
       ti.get_domain_scoring('group-ib.com') ti.get_domain_scoring(['group-ib.com', 'example.corp']) # -> {"items": {"group-ib.com": {"domain": "group-ib.com",
       "riskScore": 0}}}
       MITRE ATT&CK


       Fetch the full MITRE ATT&CK technique vocabulary or a ready-to-use ID->name map.
        # Raw vocabulary (includes all AttackPattern details) vocab = ti.get_mitre_techniques() # Convenient ID -> name dict mitre_map =
       ti.get_mitre_attack_pattern_map() # -> {"T1059": "Command and Scripting Interpreter", "T1078": "Valid Accounts", ...} technique_name =
       mitre_map.get("T1059")
       Global search


       Search across all TI collections by query string.
       results = ti.global_search('8.8.8.8') # -> [{"apiPath": "suspicious_ip/scanner", "count": 14, ...}, ...]
       DRPPoller methods
       from ciaops import DRPPoller drp = DRPPoller(username='...', api_key='...', api_url='DRP_URL')
       Update generator - iterate violation feeds:
        generator = drp.create_update_generator(         collection_name='violation',     sequpdate=1700000000000000,                 subtypes=[6],      # 1=counterfeit
       2=piracy 3=partner_policy 4=trademark 5=malware 6=phishing 7=fraud               section=[1, 2],         # 1=Web 2=Mobile 3=Marketplace 4=Social 5=Advertising
       6=Messengers        brands=['brand_id'],   approve_states=['under_review'], ) for portion in generator:          data = portion.parse_portion()
       Change violation status (only when status=detected and approveState=under_review):
        drp.change_status(feed_id='violation_id', status='approve') # or 'reject'
       Brands and subscriptions:
       brands = drp.get_brands() subscriptions = drp.get_subscriptions()
       ASMPoller methods
       from ciaops import ASMPoller asm = ASMPoller(username='...', api_key='...', api_url='ASM_URL')
       List companies:
        companies = asm.get_companies()               # all companies active = asm.get_companies(status='active')
       Update generator - uses POST requests with automatic rate limiting:
        generator = asm.create_update_generator(          collection_name='assets/updated', # or 'leaks/updated', 'issues/updated'
       company_id='company-uuid',           # or list of UUIDs    date_from='2024-01-01',        date_to='2024-06-01',                # optional   count=500,
       # max 5000      status=['new', 'confirmed'],      # optional filter   type=['domain', 'ip'],           # optional filter (assets only) ) for portion in generator:
       data = portion.parse_portion()
       Dashboard scores and issue/asset management are also available (get_dashboard_scores(), get_issue_evidence(), add_issue_comment(),
       change_issue_status(), add_assets(), remove_assets(), change_asset_status()).

       Close session


       Always close the session in a try...finally block, or use the context manager:
        from ciaops import TIPoller from ciaops.exception import InputException, ConnectionException try:                  poller =
       TIPoller(username='example@gmail.com', api_key='API_KEY', api_url='API_URL')                   # ... do work ... except InputException as e:    logger.error("Wrong
       input: %s", e) except ConnectionException as e:        logger.error("Connection error: %s", e) finally:       poller.close_session()

Parsing

       Common example of an API response from a collection (received feeds):
        api_response = [     {         'iocs': {           'network': [           {'ip': [1, 2], 'url': 'url.com'},        {'ip': [3], 'url': ''}    ]      }    },   {      'iocs': {
       'network': [      {'ip': [4, 5], 'url': 'new_url.com'}                 ]      }   }]
       Parse portion method


       Your mapping dict for the parse_portion() or bulk_parse_portion() methods:
        mapping_keys = {         'network': {'ips': 'iocs.network.ip'},       'url': 'iocs.network.url',       'type': '*custom_network' }
       Result of parse_portion() output:
        parsing_result = [       {'network': {'ips': [[1, 2], [3]]}, 'url': ['url.com', ''], 'type': 'custom_network'},   {'network': {'ips': [[4, 5]]}, 'url': ['new_url.com'], 'type':
       'custom_network'} ]
       Get IoCs method


       Your mapping dict for the get_iocs() method:
        mapping_keys = {         'ips': 'iocs.network.ip',       'url': 'iocs.network.url' }
       Result of get_iocs() output:
        parsing_result = {       'ips': [1, 2, 3, 4, 5],   'url': ['url.com', 'new_url.com'] }


       Records limits

       The default limit is 100 records per request. Due to the different sizes of feeds, there are different limits for getting data. To change the record limit in
       the response, add the limit parameter to the request (for example, limit=500). Per-collection limits are listed in the API Limitations article.
        curl -X 'GET' 'https:///api/v2/apt/threat/updated?limit=500&seqUpdate=16172928022293'


       Troubleshooting
       401 response code


       Returned if no credentials were sent. Make sure you send the Authorization header and use Basic authentication.

       403 response code


       Possible reasons:


          · IP limitation. Make sure you send the request from an allowed IP address (see Initial Steps).

          · API key issue. Make sure your API key is active and valid.

          · No access to the feed. Make sure you have access to the requested feed (Profile page -> Security and Access).

       504 response code or timeout


       Try setting a smaller limit when requesting the API.


       For additional questions, contact Group-IB via the Service Desk.

TI Postman configuration
       Prerequisites

       Before configuring Group-IB TI Postman, ensure you have reviewed the Group-IB TI Integration Starting Guide for initial setup instructions.


       Warning: Never make this configuration publicly available in Postman, especially with your credentials. Always use the native desktop application
       instead of the cloud version.


       Installation

          · Download the Configuration File: You can download the current configuration file here.

          · Import into Postman:

               · Open the Postman application.

               · Click Import and select the previously downloaded configuration file.


       Configuration

          · Navigate to the Group-IB Threat Intelligence API (v2.x.x) section in Postman.

          · Click the Variables button.

          · Locate the username and api_key variables and set them in the active Postman environment.


       Usage

          · Select an API collection from the available list.

          · Choose an endpoint (e.g., GET /api/v2/hi/threat/updated).

          · Configure the request parameters as needed.

          · Click Send to execute the request and view the response.

Example Requests

       The following examples demonstrate how to send API requests and interpret responses in Group-IB TI Postman. These examples cover common use
       cases such as retrieving threat data. Each request type includes sample usage scenarios and response examples:


       GET Example: Retrieving Threat Data


       GET Example: Retrieving Malware Data

Additional Notes

          · Ensure your API key has the required permissions for the selected endpoints.

          · Refer to the API Documentation for a full list of supported queries and parameters.

          · If you encounter issues, check the Troubleshooting section or contact support.

Developer Guide
       Common Dev   info
       Authentication


       Basic authentication is necessary to access API methods. You should provide credentials with each request in username and API-key format.


       Curl example:
        curl 'https://tap.group-ib.com/api/v2/sequence_list' -u 'LOGIN:API_KEY'
       Note: LOGIN is your username to log in to the Group-IB portal. API_KEY key you have generated on the previous step.


       Rest API Scope


       There are several ways to get feeds:


          · Global search
          · Receive data

          · Retrieve feed by ID
       Global search


       It is possible to perform a global search across all collections.

       Request format:
       curl 'https://tap.group-ib.com/api/v2/search?q=8.8.8.8' -u 'LOGIN:API_KEY'
       Params:

Name                    Type                                Required                                                         Description


                      q                     string                                 true                                                           Search query


       Response example:
        [      {      "apiPath": "attacks/ddos",      "count": 389,        "detailedLinks": [],        "label": "Attack :: DDoS",       "link":
       "https://tap.group-ib.com/attacks/ddos?q=ip:8.8.8.8"           },     {      "apiPath": "attacks/deface",          "count": 1,        "detailedLinks": [],   "label": "Attack
       :: Deface",           "link": "https://tap.group-ib.com/attacks/deface?q=ip:8.8.8.8"       },     ... ]
       Global search simplifies the process of searching through all collections and indicates which collections generally have matching entries. However, to
       get the found items, you need to perform the same search query in the collection specified in the apiPath parameter using one of the methods
       described below.

       Receive data


       Using this method, you can read feeds sorted by their seqUpdate value in ascending order. Every time a feed changes, its seqUpdate increases, and
       this feed appears at the top of the queue. This value is stored on the integration side and used to request only new data.


       Group-IB TI uses continuous seqUpdate numbering across feeds. For example, seqUpdate 1999998 can be in compromised/account_group, and
       seqUpdate 1999999 can be in attacks/ddos. This example explains sequence semantics only.


       Warning: Using df/dt together with seqUpdate in /updated endpoints is a legacy pattern and may produce inconsistent results. Use sequence_list +
       seqUpdate for update polling. Note: df/dt parameters are valid for /api/v2/search.


       Request format:
        GET /api/v2//updated
       Params:


                     Name                    Type                                Required                                                         Description


                      q                     string                                 false                                                          Search query


                   seqUpdate                integer                                false                                       seqUpdate to get the next data chunk


                     limit                  integer                                false                              Feed portion size. Default: 100. Maximum depends on

                                                                                                                                    collection (see API Limitations).


       Rate limit reminder: 1 request per 10 seconds per company per feed per route (see API Limitations).

       Procedure:


            · Use a sequence_list request to get an update for a specific date to start the session. Date format: YYYY-MM-DD Request format:
               GET /api/v2/sequence_list?date=
               Note: Date must be in this format: YYYY-MM-DD (for example, 2021-11-11).

            · Received seqUpdate can be used as a parameter for further requests. When you submit this argument as a parameter, you will get a portion of
               feeds starting with the next seqUpdate for this collection. Request format:

GET /api/v2//updated?seqUpdate=

          · To get the next portion of feeds, use the top-level seqUpdate value from the response (not the seqUpdate of individual items).

          · Repeat step 3 while the response contains data (the returned array is not empty).

          · Save the last top-level seqUpdate value for future reference after each iteration.
       Retrieve Feed by ID


       Each item in the system is uniquely identifiable by its id field. You can retrieve a specific feed by using the following request.


       Request format:
        GET /api/v2//
       If the above request does not return the expected result, use the following alternative request format:
        GET /api/v2/?q=id:


       Additional Resources

       Status codes:


       For detailed information on status codes, error explanations, and troubleshooting steps, please refer to Troubleshooting and Error Codes. This guide
       includes:


          · Steps to verify access if you encounter authorization issues

          · Explanations of common error codes, such as 400(Bad request), 401(Unauthorized), and 404(Not Found).

          · Recommendations for handling rate limits and server errors.

       Specific features in some collections:


          · Collection limits are route-specific and can differ significantly. Use the current limits from API Limitations.

       Misc:


          · For complete sequence/search iteration details, see API Logic Explanation.

          · For endpoint-level global search behavior and schema, see Search.

          · You can find additional JSON schema details and constraints in related endpoint articles.


       User-Agent mask with product metadata information


       The User-Agent request header contains a string with attributes that servers and network nodes can use to determine the application category,
       operating system, vendor, and/or version of the user agent.


       The view of the User-Agent string is:
        /_/_//_

Field                                                                      Description


                         Platform type                  Platform type. Must be one of the following: SIEM, SOAR, TIP, XDR, IRP, NGFW, SGRC, SCRIPT, CIS, IDR,

                                                                                                            EDR.


                        Platform name                                          Official platform name. Examples: QRadar, ThreatQuotinet.


                       Platform version                                                          Vendor platform version.


                          App name                           Integration application name, e.g. Threat Intelligence, Attack Surface Management, Digital Risk

                                                                                                         Protection


                         App version                                                          Integration application version.


                          Username                                                   Username used for authorization in the TI portal.


                           Lib name                                                     Library token if used (for example, ciaops).


                          Lib version                                                  Library version if used (for example, 0.14.1).


       Note: Using a client library is optional. If no library is used in the integration, specify unknown instead of Lib name and Lib version.


       Examples:


          · SIEM/QRadar_2020.10.6/GroupIB_TI_1.0.0/gibuser@group-ib.com/gibunipy_0.5.12

          · TIP/ThreatQuotient_2.5.0/Group_IB_Threat_Intelligence_1.2.0/gibuser@group-ib.com/unknown

          · SCRIPT/unknown/GIB_TI-A_PanOS_unknown/gibuser@group-ib.com/pytia_0.5.13


       App name


       Detailed view of the application name
        Group-IB___


       Abbreviation

       Product:


          · TI - Threat Intelligence

          · DRP - Digital Risk Protection

          · ASM - Attack Surface Management

          ·

MXDR - Managed Extended Detection and Response

       Platform:


          · TIP - Threat Intelligence Platform

          · SIEM - Security Information and Event Management

          · SOAR - Security Orchestration, Automation and Response

          · IRP - Incident Response Platform

          · NGFW - Next Generation Firewall

          · IDR - Identity Detection and Response

          · EDR - Endpoint Detection and Response

          · XDR - Extended Detection and Response

          · SGRC - Security Government, Risk management and Compliance

       Collections:


          · APT - Advanced Persistent Threat - Nation-state reports (pro-government)

          · HI - Human Intelligence - Cyber-criminals reports (non-government, all others)

          · IoC - Indicator of Compromise

          · OSI - Open Systems Interconnection Model

API Logic Explanation
       API logic

       To iterate over received portions from API response, you should follow one of the next iteration logic:


          · Sequence update iteration - based on seqUpdate parameter, which was retrieved from previous response. Uses updated endpoint (/updated)
               after collection name (/apt/threat) >>> /api/v2/apt/threat/updated.


       To search IPs, domains, hashes, emails, etc., you should follow the next logic:


       Search logic - First you should reach /api/v2/search endpoint with any q parameter >>> /api/v2/search?q=8.8.8.8. In the output response you will
       receive collections, which contains the search result (8.8.8.8). Use Sequence update iteration as a next step to retrieve all events.


       To get the latest updates on each collection events you should follow the next logic:


          · Sequence update logic - first you should reach /api/v2/sequence_list endpoint with date and collection parameters (optional) >>>
               /api/v2/search?date=2022-01-01&collection=apt/threat. In the output response you will receive seqUpdate number, which you should use in
               the next request to collection /updated endpoint. Use Sequence update iteration as a next step to retrieve all events.

Sequence Update logic

       Most collections at the Threat Intelligence portal has /updated endpoint. And this endpoint uses updated logic based on seqUpdate key field which
       comes from JSON response.


       The seqUpdate key - is a time from Epoch converted to a big number (microseconds), using the next formula:


       UTC timestamp * 1000 * 1000


       Note: Don’t rely on this formula. Because of the rising amount of data it could be changed. For that purpose /api/v2/sequence_list endpoint was
       created. Use this endpoint to get the required seqUpdate number.

       API response


       Each row in our database has its own unique sequence update number. So, we can get all the events one by one. To check it you can explore JSON
       output and then explore each item in the "items" field. So, each item contains a seqUpdate field. And the last element’s seqUpdate is put to the top
       level of JSON output. You can use it to get the next portion of feeds. Each collection has its own updated route like /api/v2/apt/threat/updated, so we
       can use the next output as an example.
        {      "count": 1761,   "items": [     {"id": "fake286ca753feed3476649438e4e4488"...},               {"id": "fake51d29357b22b80564a1d2f9fc8751"...},                    {
         "author": null,        "companyId": [],             "id": "fake4f16300296d20ef9b909dc0d354fb",                     ......,      "indicators": [           {
       "dateFirstSeen": null,                "dateLastSeen": null,             "deleted": false,                      "description": null,               "domain": "fake-fakesop.net",
                     "id": "fakebe483bb82759fbee7038235e0f52d0",                     .....         }             ],           "indicatorsIds": [
       "fakebe483bb82759fbee7038235e0f52d0"                       ],     "isPublished": true,          "isTailored": false,              "labels": [],        "langs": [        "en"
            ],       "malwareList": [],            ......,      "seqUpdate": 16172928022293            },   ],         "seqUpdate": 16172928022293 }
       Iteration steps


       To iterate over /api/v2/apt/threat/updated endpoint data, you need to collect this field number ("seqUpdate": 16172928022293) right at the top level
       of the JSON response, received from previous request or from /sequence_list endpoint.
        curl -X 'GET' 'https:///api/v2/sequence_list'
       Add gathered seqUpdate in the next request, using endpoint params.
        curl -X 'GET' 'https:///api/v2/apt/threat/updated?seqUpdate=16172928022293'
       In the received JSON output check the "count": 1751. -> Gather seqUpdate from last feed or at top level -> Put it in next request ->
        curl -X 'GET' 'https:///api/v2/apt/threat/updated?seqUpdate=16172928536227'
       In the received JSON output, check the "count": 1741 -> Gather seqUpdate from last feed or at top level -> Repeat till the end.

       Stop the iteration


       The “stop word” in that logic is items "count" or "items" list length. For the collection apt/threat in above example, the limit is set to 10 by default, the
       other collections usually have 100 limit. The limit depends on the amount of data to not overload the JSON output. For example, usually you receive a
       portion of 100 feeds (not 10) for the first iteration. -> Then could be a portion of 23 feeds -> Then a portion of 0 feeds -> The end.

Search logic

       Search logic is used to find attribution to the search value in the Threat Intelligence database.

       Global search


       To find events related to IP, domain, hash, email, etc., you should send a request to the /api/v2/search endpoint with any q parameter
       (/api/v2/search?q=8.8.8.8). It will return a list of collections, which contains this searchable parameter. As a next step we need to use Sequence
       update iteration over all items in each collection. You can specify the searchable type keyword to avoid side results by setting q parameter like
       /api/v2/search?q=ip:8.8.8.8. The same can be done for domain, email, hash, etc. (/api/v2/search?q=domain:google.com,
       /api/v2/search?q=email:example@gmail.com).
        [      {     "apiPath": "suspicious_ip/open_proxy",         "label": "Suspicious IP :: Open Proxy",      "link":
       "https://tap.group-ib.com/api/v2/suspicious_ip/open_proxy?q=ip:8.8.8.8",                 "count": 14,      "time": 0.304644684,        "detailedLinks": null   },    {
            "apiPath": "attacks/ddos",       "label": "Attack :: DDoS",     "link": "https://tap.group-ib.com/api/v2/attacks/ddos?q=ip:8.8.8.8",            "count": 1490,
            "time": 0.389418291,       "detailedLinks": null   },   {"apiPath": "attacks/deface"...},     {"apiPath": "malware/config"...},   {"apiPath":
       "suspicious_ip/scanner"...} ]
       Iteration steps


       On the first search step we receive information that collection attacks/ddos contain 1490 items ("count": 1490). Let’s extract all of them. First we need
       to send a request to this collection with the q parameter (?q=ip:8.8.8.8). Then we retrieve the "seqUpdate" field right at the top level of the JSON
       response and use it in the next request ("seqUpdate": 1673373011294).
        { "count": 1490, "items": [      {     "body": null,    "cnc": {"cnc": "http://ex-ex.net/drv/"...},    "company": null,     "companyId": null,      "dateBegin": null,
               "dateEnd": null,   "dateReg": "2017-08-16T00:00:00+00:00",          "evaluation": {},    "favouriteForCompanies": [],      "headers": [],
       "hideForCompanies": [],        "id": "examplec58903baddc84b8c51eaef1f904374025d",                  "isFavourite": false,   ...   } ], ..., "seqUpdate":
       1673373011294 }
       So the next request should look like this /api/v2/attacks/ddos/updated?q=ip:8.8.8.8&seqUpdate=1673373011294. We can also set the limit parameter
       in the requests, like limit=500. Explore the example below.
        curl -X 'GET' 'https:///api/v2/search?q=ip:8.8.8.8'
       Add gathered seqUpdate in the next request, using endpoint params.
        curl -X 'GET' 'https:///api/v2/attacks/ddos/updated?seqUpdate=1673373011294'
       In the received JSON output check the “count”: 1390. -> Gather seqUpdate from last feed or at top level -> Put it in next request ->
        curl -X 'GET' 'https:///api/v2/attacks/ddos/updated?seqUpdate=1673375930599'
       In the received JSON output, check the "count": 1290 -> Gather seqUpdate from last feed or at top level -> Repeat till the end.

       Stop the iteration


       The “stop word” in that logic is items "count" or "items" list length. For the collection attacks/ddos in the above example, the limit is set to 100 by
       default, the other collections may differ. The limit depends on the amount of data to not overload the JSON output. For example, usually you receive a
       portion of 100 feeds for the first iteration. -> Then could be a portion of 23 feeds -> Then a portion of 0 feeds -> The end.

Preventing and investigating cybercrime
 since 2003


 intelligence@group-ib.com   www.group-ib.com
 +65 3159-3798               blog.group-ib.com
