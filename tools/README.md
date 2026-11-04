# Group-IB TI — bộ công cụ CTF

Credentials: `tools/.gib_creds` (một dòng `email:API_KEY`), hoặc biến môi trường `GIB_USER` / `GIB_KEY`.
Trên Windows nên `export PYTHONIOENCODING=utf-8` (Git Bash) hoặc `$env:PYTHONIOENCODING="utf-8"` (PowerShell), nếu không emoji trong dữ liệu sẽ làm crash lệnh print.

## Lệnh

```bash
python tools/scan.py <term> [<term> ...]         # scan đầy đủ, tự nhận loại (ip/domain/email/hash/url/text)
python tools/scan.py spyroid --all --pages 5     # thêm collection ít dùng, lấy nhiều trang hơn
python tools/gib.py get <path> k=v ...           # GET thô, ví dụ: get hi/threat_actor/<id>
python tools/gib.py item hi/threat <id>          # lấy 1 bản ghi theo id
```

Kết quả thô lưu ở `out/<term>/`: JSON của từng collection, `actor_*.json`, `report_<id>.json` và `.txt` (toàn văn đã bỏ HTML), `_pivots.json`.

## `scan.py` làm gì
1. Tra WHOIS cho domain, email hoặc IP (`utils/graph/domain`, `utils/graph/ip`, có lịch sử registrant, email, phone) và scoring (`POST scoring/ip|domain`).
2. Gọi `<collection>/updated?q=...` trên các collection threat, actor, open threats, IOC, C2, malware, phishing kit, darkweb.
3. Chỉ giữ những bản ghi thật sự chứa từ khóa (`q` bị tách token nên có nhiều kết quả khớp nhầm).
4. **Tự mở các threat actor mà kết quả tham chiếu tới** (`GET hi/threat_actor/<id>`), rồi đọc **mọi báo cáo** của actor đó (`GET hi/threat/<id>`) và in đoạn trích quanh từ khóa.
5. In danh sách pivot: email, Telegram, URL, IP, nickname/forum, contacts.

## Những điều đã kiểm chứng (2026-11-04)
| Điều | Chi tiết |
|---|---|
| Tìm qua feed chỉ phủ khoảng 30 ngày | `hi/threat`, `hi/threat_actor` `/updated?q=` chỉ trả về bản ghi cập nhật từ khoảng 2026-10-04. Actor và báo cáo cũ hơn (vd BalonxSistema) **không tìm được theo tên**. |
| Lấy theo ID thì không giới hạn | `GET /api/v2/hi/threat_actor/<id>`, `/hi/threat/<id>`, `/apt/...` đều chạy được. `q=id:<id>` trên feed thì **không** chạy với bản ghi cũ. |
| IOC / C2 có dữ liệu cũ | `ioc/primary`, `ioc/common`, `malware/cnc` tìm được IP/domain/hash cũ, và có `threatActorList` (id actor). **Đây là đường pivot chính.** |
| `hi/open_threats` | 750k bài (X/Twitter, tin tức, blog), tìm toàn văn được, có dữ liệu cũ. Hợp cho từ khóa tự do. |
| Cú pháp `q` | Kiểu Lucene. Từ trần như `spyroid`, `name:x`, `"cụm từ chính xác"` đều chạy. Không đặt trong `"..."` thì email/domain bị tách token (`a@gmail.com` khớp với mọi `gmail.com`). Dạng `threatActor.name:x` báo 400. |
| Collection "Individual" rỗng | `darkweb/forums`, `compromised/messenger` (Telegram), `compromised/discord`, `compromised/access`, accounts, leaks chỉ trả dữ liệu theo công ty hoặc hunting rule, nên với tài khoản này luôn bằng 0. Cần dữ liệu Telegram/forum thì dùng **portal / Prevyn AI**. |
| Không có qua API | Graph đầy đủ (chỉ có WHOIS), `ai-assistant/*` (404), `utils/graph` (404), `ioc/ioc`. |
| `/api/v2/search` | **Tránh dùng.** Lần duy nhất gọi thì nginx trả 403, ngay sau đó key bị "Permission denied". |
| Rate limit | Khoảng 1 req/s cho mỗi route feed. Endpoint không phải feed (`hi/threat_actor?q=`) dễ bị 429. `gib.py` tự giãn nhịp và thử lại khi gặp 429. |
| `sequence_list?date=YYYY-MM-DD` | Trả về seqUpdate theo ngày cho mỗi collection, nhưng không mở rộng được khoảng tìm kiếm của feed. |

## Quy trình giải một đề OSINT
1. Rút ra mọi chỉ báo cụ thể trong đề (tên app, package, domain, IP, hash, nickname) rồi `scan.py` từng cái.
2. Đề chỉ cho từ khóa mơ hồ: `scan.py <từ khóa>` (open_threats thường có kết quả). Lấy domain/IP từ đó rồi scan tiếp.
3. Từ IOC sang actor ID, rồi đọc báo cáo của actor (scan tự làm). Đọc `out/<term>/report_*.txt` để xem toàn văn.
4. Domain: xem WHOIS history, email registrant cũ thường là danh tính thật.
5. Đến danh tính (email/nickname) thì thường phải OSINT ngoài nền tảng: Google account từ Gmail (GHunt, review Google Maps), username trên các mạng xã hội.
6. Bước cần Telegram/forum: hỏi Prevyn AI trên portal (nó có quyền vào Individual collections).
