# دليل مستودع Holographic AI Governor (HAG-2.0 Scaling) 🚀

استخدم هذا الملف كمرجع أساسي Onboarding لأي وكيل ذكاء اصطناعي يعمل في هذا المشروع (HAG-2.0 Final).

## 🟢 المهمة (Mission)
بناء ذكاء اصطناعي سيادي يتمتع بحصانة ذاتية وكفاءة فائقة في استخدام الموارد. المرحلة الثانية (HAG-2.0) تكتمل بتفعيل التكرار الأصيل والتناظرات الجبرية.

## 🔵 الهيكل التقني (Phase 2.0 Core)
*   `src/agents/native_recursive.py`: بروتوكول **RLM-Native** لإدارة السياق الفائق (10M+ توكن). ✅
*   `src/agents/lie_augmenter.py`: محرك **LieAugmenter** لاكتشاف التناظرات الجبرية. ✅
*   `src/indexing/clbf_engine.py`: محرك **CLBF** المتسلسل لخفض الذاكرة وتسريع الرفض. ✅
*   `src/governor/governor.py`: نواة **EKRLS** لحماية نزاهة الاستدلال. ✅
*   `src/indexing/ribbon.py`: فهرسة **Ribbon** (GF(2) logic). ✅
*   `src/geometry/engine.py`: حسابات **Spacetime Engine**. ✅

## 🟡 الأنماط البرمجية الملزمة (Mandatory Patterns)
1.  **الرفض السريع (Fast Rejection):** استخدم `CLBF` لتصفية المدخلات غير الصلة قبل معالجتها من قبل النماذج المكلفة.
2.  **التكرار الأصيل (RLM-N):** لا تقم بتحميل السياق الضخم؛ استخدم `NativelyRecursiveAgent` لإدارة السياق ككائن خارجي في REPL.
3.  **الثبات تجاه التناظر:** استخدم `LieAugmenter` لضمان أن مخرجات النظام لا تتأثر بالتحولات غير الضرورية في البيانات.
4.  **نظام الحكم (Governance):** يجب أن تمر كافة سلاسل الاستدلال عبر `Governor` لفحص قيمة $Q$.

## 🔴 مقاييس النجاح (Success Metrics)
*   **Context:** 10M+ Tokens.
*   **Data Efficiency:** +40% (via Symmetry).
*   **RAM Efficiency:** +24% (via CLBF).
*   **Logic Integrity:** 96.18% precision.

---
**تنبيه للنظام:** "التناظر هو مفتاح التعميم. استخدم RLM-N للاستكشاف النشط وليس الحفظ السلبي."
