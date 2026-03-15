from typing import Optional

try:
    from argostranslate import package, translate
except Exception:  # pragma: no cover
    package = None
    translate = None


def translate_text(text: str, source_lang: str = "th", target_lang: str = "en") -> str:
    """
    translate ocr text using argos translate if available, otherwise return the original text.
    """
    if not text:
        return ""

    if package is None or translate is None:
        return text

    installed_packages = package.get_installed_packages()
    available = [
        p
        for p in installed_packages
        if p.from_code == source_lang and p.to_code == target_lang
    ]

    if not available:
        return text

    translator = translate.load_installed()[0]
    result: Optional[str] = translator.translate(text)
    return result or text

