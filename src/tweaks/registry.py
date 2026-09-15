def _solarium_fallback():
    """Force Solarium Fallback for iOS 26.x and iOS 27.

    Same restore path as every other GP plist tweak — not a new exploit.
    iOS 26 reads SolariumForceFallback.
    iOS 27 UIKit reads UISolariumForceFallback.
    Both are written so one switch covers both major versions.
    """
    from .tweak_classes import CompanionKeyTweak
    return CompanionKeyTweak(
        FileLocation.globalPreferences,
        key="SolariumForceFallback",
        value=True,
        companion_keys={
            "UISolariumForceFallback": True,
        },
    )
