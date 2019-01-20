# swisstone-to-vcard
Convert Swisstone BBM 610 Contacts Backup to vcard format

When migrating from a Swisstone BBM 610 to an Android Smartphone it is not possible to easily migrate your contacts.

In the phone settings you can backup the contacts and send them to the new device via bluetooth but the format is a simple .txt file
and looks like this:

NAME
<name>
TEL
<telephone number>
...

For modern android phones you will need the contacts in vcard format. This python script converts the backup into vcard format.

Command Syntax: python vcard-converter.py <location of backup> [new location]

The new location is optional. If not specified it will be saved in the original location with the same name but a .vcf ending.
