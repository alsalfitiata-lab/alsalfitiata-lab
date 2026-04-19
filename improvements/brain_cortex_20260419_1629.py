"""
تحسين تلقائي بواسطة الوكيل الذاتي
الملف الأصلي: brain/cortex.py
المشكلة: Cortex integration with memory for personalized recommendations is weak
النهج: Add smart retry with exponential backoff for API failures
التاريخ: 2026-04-19 16:29
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
