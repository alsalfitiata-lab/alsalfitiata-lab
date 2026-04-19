"""
تحسين تلقائي بواسطة الوكيل الذاتي
الملف الأصلي: brain/cortex.py
المشكلة: Cortex does not handle API requests efficiently, leading to slow responses
النهج: Add smart retry with exponential backoff for API failures
التاريخ: 2026-04-19 13:42
"""

def _retry_api_call(self, func, max_retries=3):
    """Smart retry with backoff"""
    for i in range(max_retries):
        try:
            return func()
        except Exception as e:
            if i == max_retries - 1:
                raise
            time.sleep(2 ** i)
    return None
