MIT = """MIT License

Copyright (c) 2026 OpenStrap

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

INDEX = """
# Legal
Loopr is a free iPhone app that reads your fitness band over Bluetooth and works out sleep, recovery and strain on the phone. It has no account and no server. These pages cover the app.

- [Privacy policy](privacy.html). What Loopr stores, where it stays, and what Apple shares with me during TestFlight.
- [Terms](terms.html). The rules for using the app, including what it is not.
- [Notice](notice.html). Who Loopr is not affiliated with, and the open-source work it credits.
- [Imprint](imprint.html). Who publishes Loopr and how to reach me.
"""

PRIVACY = """
# Privacy policy
Last updated: {UPDATED}

> Short version. Loopr keeps your data on your iPhone. It has no account, no server, no analytics and no ads. I, the developer, never receive your health data from the app.

## Who is responsible
Pascal Lindenau, Forddamm 7, 12107 Berlin, Germany. Email: [{EMAIL}](mailto:{EMAIL}). I am the controller under the EU General Data Protection Regulation (GDPR) for the little personal data that reaches me, which is described below.

## What Loopr stores on your iPhone
Depending on what you use, Loopr stores:

- readings from your band, such as heart rate, heart rate variability, motion and battery level;
- scores Loopr calculates from those readings, such as sleep, recovery and strain;
- your profile (for example age, height and weight), goals, journal entries, cycle entries and workouts;
- workout routes, if you record a workout with location turned on;
- data from Apple Health that you allow Loopr to read;
- your app settings.

This data is stored in Loopr's own storage on the iPhone and in a shared app container that its widgets, Live Activities and Apple Watch app read from. Loopr does not upload it anywhere. Health, journal and route data are special categories of personal data under Article 9 GDPR, and Loopr keeps them on the device for that reason.

If you back up your iPhone to iCloud or to a computer, the backup can include Loopr's data. Apple's terms cover those backups.

## Bluetooth and your band
Loopr talks to your band directly over Bluetooth. It does not connect to WHOOP's servers and never asks for WHOOP account details.

## Apple Health
Loopr reads and writes only the Apple Health data types you approve in the iOS permission sheet. You can change this at any time in the Health app or in iOS Settings. Deleting Loopr's own data does not delete what it saved to Apple Health. Loopr has a separate control for that.

## Location
Loopr asks for location only to draw the route of a workout you record. The route stays on the iPhone.

## AI provider settings
You can save an AI provider address and API key in Loopr. The key is stored in the iOS Keychain on this device only. The current version of Loopr does not send any requests to an AI provider. If a future version does, this policy will say so first, and nothing will be sent until you turn it on.

## TestFlight
While Loopr is in beta, you install it through Apple's TestFlight app. Apple runs TestFlight and shares some data with me so I can fix problems:

- which build you installed, when you installed it and how often you opened it;
- crash reports, which include device model and iOS version;
- feedback and screenshots you choose to send from TestFlight;
- your name and email address, but only if I invited you by email. If you joined through the public link, Apple does not share your email address with me.

I use this data only to find and fix bugs, based on my legitimate interest in shipping a working app (Article 6(1)(f) GDPR). Feedback you send is voluntary. Apple keeps TestFlight data under its own privacy policy, and I delete what I receive when the beta ends or when you ask me to. Apple's own collection is covered by the [Apple Privacy Policy](https://www.apple.com/legal/privacy/) and the privacy notice in the TestFlight app.

## Email
If you email me, I use your address and message to answer you (Article 6(1)(b) and (f) GDPR). I delete the conversation when it is no longer needed, unless the law requires me to keep it.

## Export and deletion
In Loopr you can export your whole database as a file, delete a single day, or delete everything. Removing an AI provider deletes its saved key. Deleting the app removes its storage from the iPhone, subject to how iOS handles backups and Keychain items.

## Your rights
Under the GDPR you can ask me for access to, correction of, or deletion of personal data I hold about you. You can also ask me to restrict or stop processing it, ask for a copy in a portable format, and object to processing based on legitimate interest. Write to [{EMAIL}](mailto:{EMAIL}).

You can also complain to a data protection authority. The one responsible for me is the Berliner Beauftragte für Datenschutz und Informationsfreiheit, Alt-Moabit 59-61, 10555 Berlin.

## Children
Loopr is not meant for anyone under 16.

## Changes
If Loopr starts handling data differently, I will update this page and the date at the top before that version ships.
"""

TERMS = """
# Terms
Last updated: {UPDATED}

## 1. Scope
These terms apply when you download or use Loopr, including test versions distributed through TestFlight. Pascal Lindenau publishes Loopr. His details are in the [imprint](imprint.html). If you do not agree to these terms, do not use Loopr.

## 2. What Loopr is
Loopr is a free fitness and wellness app. It reads a supported band over Bluetooth and calculates estimates such as sleep, recovery and strain on your iPhone. Loopr is an independent project. It is not affiliated with, sponsored by or endorsed by WHOOP, Inc. or any other hardware maker.

## 3. Not a medical device
Loopr is for general fitness and wellness only. It is not a medical device and does not give medical advice. It is not meant to diagnose, treat, cure or prevent any disease. Its numbers are estimates from published research methods, not clinical measurements. Talk to a doctor about any health concern, and do not delay care because of something Loopr shows.

## 4. Test versions and experimental features
TestFlight builds are test versions. They can have bugs, lose data or stop working, and Apple ends each build after 90 days. Support for WHOOP 5.0 and MG bands is marked Experimental and stays off until you turn it on. It can pause or fail, and some band features are missing. A firmware update from the band's maker can change or break compatibility at any time, and Loopr has no control over that.

## 5. Who can use Loopr
You must be at least 16 years old.

## 6. Your responsibilities
- You decide what to do with the information Loopr shows, including any exercise or training choices. Exercise carries risk.
- You use Loopr only with hardware you own or are allowed to use.
- You check whether using Loopr fits any agreement you have with your band's maker, such as a membership agreement.
- You keep your own backups. Loopr can export your data. Use it.

## 7. Other services
Loopr can work with Apple Health and with an AI provider you configure yourself. Those services have their own terms, and I am not responsible for them.

## 8. No guarantees
Loopr is free. I do not promise that it is accurate, complete, available at all times or compatible with any particular band or firmware. Statutory rights that cannot be excluded remain unaffected.

## 9. Liability
I am liable without limit for damage caused intentionally or through gross negligence, for injury to life, body or health, and under the German Product Liability Act (Produkthaftungsgesetz). In all other cases I am not liable, because Loopr is given away for free (sections 521 and 599 of the German Civil Code apply accordingly).

## 10. Source code licence
Loopr's source code is released under the MIT License. The MIT License governs copying and changing the code. These terms govern using the app.

## 11. Changes
I may update these terms. The date at the top shows the latest version. If a change matters for how you use Loopr, the app or the TestFlight notes will say so.

## 12. Governing law
German law applies, excluding the UN Convention on Contracts for the International Sale of Goods. If you are a consumer living in another country, you keep the protection of the mandatory consumer laws of that country. If you are a merchant, the courts of Berlin have exclusive jurisdiction.

## 13. Contact
Questions about these terms: [{EMAIL}](mailto:{EMAIL}).
"""

NOTICE = """
# Notice
Last updated: {UPDATED}

## Independence
Loopr is an independent project. It is not affiliated with, sponsored by, endorsed by or connected to WHOOP, Inc. "WHOOP" is a trademark of WHOOP, Inc. Loopr uses the name only to say which bands it can talk to.

Loopr contains no WHOOP source code, binaries, firmware, logos or product photos. It does not connect to WHOOP's servers and does not use a WHOOP account. It reads the band you own, over Bluetooth, so that you can see your own data.

## How the Bluetooth support was built
Loopr's Bluetooth support builds on the MIT-licensed OpenStrap projects, which were developed by observing the band's own Bluetooth traffic. Loopr's message parsers are tested against recorded band messages.

## OpenStrap
Parts of Loopr's Bluetooth, protocol and analytics code come from or are based on [OpenStrap Edge](https://github.com/OpenStrap/edge), [OpenStrap protocol](https://github.com/OpenStrap/protocol) and [OpenStrap analytics](https://github.com/OpenStrap/analytics). Their licence:

{MIT}

## GRDB
Loopr stores data with [GRDB.swift](https://github.com/groue/GRDB.swift), licensed under the MIT License. The full licence ships inside the app, under Settings, Legal and licenses.

## Fonts
Loopr includes Barlow Condensed, IBM Plex Mono, Manrope and Space Grotesk under the SIL Open Font License 1.1. Each licence ships inside the app.

## BodyParts3D
The hand and forearm in the onboarding film and its poster are adapted from BodyParts3D, © The Database Center for Life Science, licensed under [CC Attribution-Share Alike 2.1 Japan](https://creativecommons.org/licenses/by-sa/2.1/jp/deed.en) ([source](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html)). The film and poster are adaptations and are shared under the same licence.
"""

IMPRINT = """
# Imprint
Information under section 5 of the German Digital Services Act (DDG)

## Publisher
Pascal Lindenau
Forddamm 7
12107 Berlin
Germany

## Contact
Email: [{EMAIL}](mailto:{EMAIL})

## Responsible for content under section 18(2) MStV
Pascal Lindenau, address as above.

## Consumer dispute resolution
I am not willing or obliged to take part in dispute resolution proceedings before a consumer arbitration board.
"""

def _mit_block():
    return "\n\n".join("> "+p.replace("\n"," ") for p in MIT.split("\n\n"))

PAGES = [
    ("index.html", "Legal", "Legal documents for Loopr: privacy policy, terms, notice and imprint.", INDEX),
    ("privacy.html", "Privacy policy", "How Loopr handles your data. It stays on your iPhone.", PRIVACY),
    ("terms.html", "Terms", "Terms for using the Loopr app.", TERMS),
    ("notice.html", "Notice", "Independence notice and open-source credits for Loopr.", NOTICE.replace("{MIT}", _mit_block())),
    ("imprint.html", "Imprint", "Legal notice for Loopr under section 5 DDG.", IMPRINT),
]
