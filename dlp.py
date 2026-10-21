import re
EG_NID_REGEX = r'\b[2-3][0-9]{13}\b'
def detect_and_mask(text):
  for m in re.finditer(EG_NID_REGEX, text):
    nid = m.group()
    masked = nid[:7] + '*******'
    print(nid, masked)
    text = text.replace(nid, masked)
    return text
    sample = 'NID 29901011234567 leaked'
    print(detect_and_mask(sample))
