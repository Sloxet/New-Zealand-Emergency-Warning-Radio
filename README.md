<p align="center">
 <img src="https://github.com/Sloxet/New-Zealand-Emergency-Warning-Radio/blob/main/Logo.png?raw=true" title="Emergency Warning Radio" alt="Emergency Warning Radio" width="750">
</p>
Emergency Warning Radio (Te Reo Irirangi Whakatūpato Ohotata) is a radio automation software designed for Aotearoa New Zealand. It continuously monitors and automatically rebroadcasts watches and warnings from authorised sources, including the Meteorological Service, GNS Science, New Zealand Police, Fire and Emergency New Zealand, and Regional and District Councils.

# Features
* **Multi-Source Integration:**<br>
Constantly monitors and aggregates warnings from the Meteorological Service, GNS Science, New Zealand Police, Fire and Emergency New Zealand, and Regional and District Councils.

* **Specific Area Message Encoding (SAME):**<br> 
Translates warnings from the Common Alerting Protocol CAP-NZ Technical Standard[[1]](https://www.civildefence.govt.nz/assets/Uploads/publications/Common-Alerting-Protocol/Common-Alerting-Protocol-CAP-NZ-Technical-Standard-TS04-18-FINAL.pdf "[1]") to the Specific Area Message Encoding (SAME)[[2]](https://en.wikipedia.org/wiki/Specific_Area_Message_Encoding "[2]") protocol.

* **FM Modulation:** <br>
This project includes the fm_transmitter library, created by Josef Miegl,[[3]](https://github.com/markondej/fm_transmitter "[2]") to modulate an FM Signal on frequencies 162.400-162.550 MHz. This feature can be enabled or disabled if the user prefers to use their own equipment or lacks authorisation to transmit on these frequencies[[4]](#end-user-licence-agreement "[1]").

* **Customisable Settings:** 
  * **SAME Configuration**<br>
 Baud Rate (Default: 520.83 Hz)<br>
 MARK Frequency (Default: 2083.3 Hz)<br>
 SPACE Frequency (Default: 1562.5 Hz)
 
  * **Station Configuration**<br>
 Callsign (Default: LLLLLLLL)<br>
 Frequency (Default: 162.400 MHz)<br>
 Region (Default: Auckland)<br>
 Suburb or Locality (Default: Takanini)
 
  * **Audio Configuration**<br>
 Onboard (Default: True)<br>
 Audio Driver (Default: WDM)<br>
 Output Device (Default: None)


# End User Licence Agreement
### New Zealand:
To use the transmitting functions of New Zealand Emergency Warning Radio, person(s) or organisations are required to hold the General User Radio Licence for Amateur Radio Operators or the Radio Operator Certificate of Competency issued by an Approved Radio Examiner (ARX).

This requirement applies not only within Aotearoa New Zealand but also extends to its territories and dependant territories. Failure to meet the licencing requirements necessitates the deployment of the software in a controlled environment, ensuring compliance with legal and regulatory standards.

### Australia:
To use the transmitting functions of New Zealand Emergency Warning Radio in Australia, person(s) or organisations are required to hold a Satellite apparatus licence issued by the Australian Communications and Media Authority. This requirement is due to the 162.400-162.550 MHz frequency band being designated for inter-satellite services rather than general use in Australia.

This requirement applies to the entirety of Australia, including states, internal territories, and external territories such as the Ashmore and Cartier Islands, Heard Island and McDonald Islands, the Australian Capital Territory, Cocos (Keeling) Islands, Northern Territory, Jervis Bay Territory, Norfolk Island, the Coral Sea Islands, Christmas Island and the Australian Antarctic Territory. 

Before transmitting, consult the Register of Radiocommunications Licences (RRL)[[5]](https://web.acma.gov.au/rrl/register_search.main_page "[5]") to confirm the legality of your chosen frequency and location. Make sure your transmission doesn't interfere with existing signals. Failure to meet the licencing requirements and Register of Radiocommunications Licences (RRL) requirements necessitates the deployment of the software in a controlled environment, ensuring compliance with legal and regulatory standards.

### United States:
The use of this software within the United States, including U.S. Territories, Tribal Governments, and Freely Associated States, is strictly prohibited unless it is deployed in a controlled environment. Transmitting invalid Specific Area Message Encoder (SAME) tones over the airwaves in the United States is a punishable offence (47 CFR § 11.45[[6]](https://www.law.cornell.edu/cfr/text/47/11.45 "[6]")).

Additionally, the frequency band 162.400-162.550 MHz is reserved for government broadcasts in the United States, including Puerto Rico, American Samoa, the U.S. Virgin Islands, the Federated States of Micronesia, Commonwealth of the Northern Mariana Islands, Guam, Republic of the Marshall Islands, and Palau.

### Other:
For person(s) or organisations outside of the aforementioned regions intending to use this software for educational or demonstration purposes, it is their responsibility to ensure compliance with local radio band allocations and laws related to transmitting in their respective regions. Failure to comply may result in legal consequences as per local regulations.

# Software Liability

> In no event shall Beatrice Kerling Voight or any applicable third-party providers of New Zealand Emergency Warning Radio be liable for any damages, including but not limited to, direct, indirect, special, incidental, or consequential damages or other losses arising out of the use of or inability to use the software licenced under this Agreement. This section constitutes the entire liability of Beatrice Kerling Voight, any applicable third-party providers of New Zealand Emergency Warning Radio, and your sole and exclusive remedy concerning misappropriation or infringement of intellectual property rights related to the software.
