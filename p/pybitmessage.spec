Name: pybitmessage
Version: 0.4.2
Release: 8.1
Summary: Send encrypted messages
License: MIT
URL: https://github.com/Bitmessage/PyBitmessage
Source0: PyBitmessage-%{version}.tar.gz
Patch0: pybitmessage-0.4.2-Makefile.patch
BuildArch: noarch
Group: Office/Email
Requires: PyQt4, openssl-libs, gst123

%description
Bitmessage is a P2P communications protocol used to send encrypted messages
to another person or to many subscribers. It is decentralized and
trustless, meaning that you need-not inherently trust any entities like
root certificate authorities. It uses strong authentication which means
that the sender of a message cannot be spoofed, and it aims to hide
"non-content" data, like the sender and receiver of messages, from passive
eavesdroppers like those running warrantless wiretapping programs.

%prep
%setup -q -n PyBitmessage-%{version}
%patch 0

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=/usr

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%doc README.md LICENSE
%{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Tue Jan 28 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
* Sat Sep 28 2013 Bob Mottram (4096 bits) <bob@robotics.uk.to> - 0.4.0-1
- Raised default demanded difficulty from 1 to 2 for new addresses
- Added v4 addresses:
  pubkeys are now encrypted and tagged in the inventory
- Use locks when accessing dictionary inventory
- Refactored the way inv and addr messages are shared
- Give user feedback when disk is full
- Added chan true/false to listAddresses results
- When replying using chan address, send to whole chan not just sender
- Refactored of the way PyBitmessage looks for interesting new objects
  in large inv messages from peers
- Show inventory lookup rate on Network Status tab
- Added SqlBulkExecute class
  so we can update inventory with only one commit
- Updated Russian translations
- Move duplicated SQL code into helper
- Allow specification of alternate settings dir
  via BITMESSAGE_HOME environment variable
- Removed use of gevent. Removed class_bgWorker.py
- Added Sip and PyQt to includes in build_osx.py
- Show number of each message type processed
  in the API command clientStatus
- Use fast PoW
  unless we're explicitly a frozen (binary) version of the code
- Enable user-set localization in settings
- Fix Archlinux package creation
- Fallback to language only localization when region doesn't match
- Fixed brew install instructions
- Added German translation
- Made inbox and sent messages table panels read-only
- Allow inbox and sent preview panels to resize
- Count RE: as a reply header, just like Re: so we don't chain Re: RE:
- Fix for traceback on OSX
- Added backend ability to understand shorter addresses
- Convert 'API Error' to raise APIError()
- Added option in settings to allow sending to a mobile device
  (app not yet done)
- Added ability to start daemon mode when using Bitmessage as a module
- Improved the way client detects locale
- Added API commands:
  getInboxMessageIds, getSentMessageIds, listAddressBookEntries,
  trashSentMessageByAckData, addAddressBookEntry,
  deleteAddressBookEntry, listAddresses2, listSubscriptions
- Set a maximum frequency for playing sounds
- Show Invalid Method error in same format as other API errors
- Update status of separate broadcasts separately
  even if the sent data is identical
- Added Namecoin integration
- Internally distinguish peers by IP and port
- Inbox message retrieval API
  functions now also returns read status
* Mon Jul 29 2013 Bob Mottram (4096 bits) <bob@robotics.uk.to> - 0.3.5-1
- Inbox message retrieval API functions now also returns read status
- Added right-click option to mark a message as unread
- Prompt user to connect at first startup
- Install into /usr/local by default
- Add a missing rm -f to the uninstall task.
- Use system text color for enabled addresses instead of black
- Added support for Chans
- Start storing msgid in sent table
- Optionally play sounds on connection/disconnection or when messages arrive
- Adding configuration option to listen for connections when using SOCKS
- Added packaging for multiple distros (Arch, Puppy, Slack, etc.)
- Added Russian translation
- Added search support in the UI
- Added 'make uninstall'
- To improve OSX support, use PKCS5_PBKDF2_HMAC_SHA1
  if PKCS5_PBKDF2_HMAC is unavailable
- Added better warnings for OSX users who are using old versions of Python
- Repaired debian packaging
- Altered Makefile to avoid needing to chase changes
- Added logger module
- Added bgWorker class for background tasks
- Added use of gevent module
- On not-Windows: Fix insecure keyfile permissions
- Fix 100%% CPU usage issue
* Sun Jun 30 2013 Bob Mottram (4096 bits) <bob@robotics.uk.to> - 0.3.4-1
- Switched addr, msg, broadcast, and getpubkey message types
  to 8 byte time. Last remaining type is pubkey.
- Added tooltips to show the full subject of messages
- Added Maximum Acceptable Difficulty fields in the settings
- Send out pubkey immediately after generating deterministic
  addresses rather than waiting for a request
* Sat Jun 29 2013 Bob Mottram (4096 bits) <bob@robotics.uk.to> - 0.3.3-1
- Remove inbox item from GUI when using API command trashMessage
- Add missing trailing semicolons to pybitmessage.desktop
- Ensure $(DESTDIR)/usr/bin exists
- Update Makefile to correct sandbox violations when built
  via Portage (Gentoo)
- Fix message authentication bug
* Fri Jun 28 2013 Bob Mottram (4096 bits) <bob@robotics.uk.to> - 0.3.211-1
- Removed multi-core proof of work
  as the multiprocessing module does not work well with
  pyinstaller's --onefile option.
* Mon Jun 03 2013 Bob Mottram (4096 bits) <bob@robotics.uk.to> - 0.3.2-1
- Bugfix: Remove remaining references to the old myapp.trayIcon
- Refactored message status-related code. API function getStatus
  now returns one of these strings: notfound, msgqueued,
  broadcastqueued, broadcastsent, doingpubkeypow, awaitingpubkey,
  doingmsgpow, msgsent, or ackreceived
- Moved proof of work to low-priority multi-threaded child
  processes
- Added menu option to delete all trashed messages
- Added inv flooding attack mitigation
- On Linux, when selecting Show Bitmessage, do not maximize
  automatically
- Store tray icons in bitmessage_icons_rc.py
* Sat May 25 2013 Jonathan Warren (4096 bits) <jonathan@bitmessage.org> - 0.3.1-1
- Added new API commands: getDeterministicAddress,
  addSubscription, deleteSubscription
- TCP Connection timeout for non-fully-established connections
  now 20 seconds
- Don't update the time we last communicated with a node unless
  the connection is fully established. This will allow us to
  forget about active but non-Bitmessage nodes which have made
  it into our knownNodes file.
- Prevent incoming connection flooding from crashing
  singleListener thread. Client will now only accept one
  connection per remote node IP
- Bugfix: Worker thread crashed when doing a POW to send out
  a v2 pubkey (bug introduced in 0.3.0)
- Wrap all sock.shutdown functions in error handlers
- Put all 'commit' commands within SQLLocks
- Bugfix: If address book label is blank, Bitmessage wouldn't
  show message (bug introduced in 0.3.0)
- Messaging menu item selects the oldest unread message
- Standardize on 'Quit' rather than 'Exit'
- [OSX] Try to seek homebrew installation of OpenSSL
- Prevent multiple instances of the application from running
- Show 'Connected' or 'Connection Lost' indicators
- Use only 9 half-open connections on Windows but 32 for
  everyone else
- Added appIndicator (a more functional tray icon) and Ubuntu
  Messaging Menu integration
- Changed Debian install directory and run script name based
  on Github issue #135
* Mon May 6 2013 Bob Mottram (4096 bits) <bob@sluggish.dyndns.org> - 0.3.0-1
- Added new API function: getStatus
- Added error-handling around all sock.sendall() functions
  in the receiveData thread so that if there is a problem
  sending data, the threads will close gracefully
- Abandoned and removed the connectionsCount data structure;
  use the connectedHostsList instead because it has proved to be
  more accurate than trying to maintain the connectionsCount
- Added daemon mode. All UI code moved into a module and many
  shared objects moved into shared.py
- Truncate display of very long messages to avoid freezing the UI
- Added encrypted broadcasts for v3 addresses or v2 addresses
  after 2013-05-28 10:00 UTC
- No longer self.sock.close() from within receiveDataThreads,
  let the sendDataThreads do it
- Swapped out the v2 announcements subscription address for a v3
  announcements subscription address
- Vacuum the messages.dat file once a month: will greatly reduce the file size
- Added a settings table in message.dat
- Implemented v3 addresses:
  pubkey messages must now include two var_ints: nonce_trials_per_byte
  and extra_bytes, and also be signed. When sending a message to a v3
  address, the sender must use these values in calculating its POW or
  else the message will not be accepted by the receiver.
- Display a privacy warning when selecting 'Send Broadcast from this address'
- Added gitignore file
- Added code in preparation for a switch from 32-bit time to 64-bit time.
  Nodes will now advertise themselves as using protocol version 2.
- Don't necessarily delete entries from the inventory after 2.5 days;
  leave pubkeys there for 28 days so that we don't process the same ones
  many times throughout a month. This was causing the 'pubkeys processed'
  indicator on the 'Network Status' tab to not accurately reflect the
  number of truly new addresses on the network.
- Use 32 threads for outgoing connections in order to connect quickly
- Fix typo when calling os.environ in the sys.platform=='darwin' case
- Allow the cancelling of a message which is in the process of being
  sent by trashing it then restarting Bitmessage
- Bug fix: can't delete address from address book
* Tue Apr 9 2013 Bob Mottram (4096 bits) <bob@sluggish.dyndns.org> - 0.2.8-1
- Fixed Ubuntu & OS X issue:
  Bitmessage wouldn't receive any objects from peers after restart.
- Inventory flush to disk when exiting program now vastly faster.
- Fixed address generation bug (kept Bitmessage from restarting).
- Improve deserialization of messages
  before processing (a 'best practice').
- Change to help Macs find OpenSSL the way Unix systems find it.
- Do not share or accept IPs which are in the private IP ranges.
- Added time-fuzzing
  to the embedded time in pubkey and getpubkey messages.
- Added a knownNodes lock
  to prevent an exception from sometimes occurring when saving
  the data-structure to disk.
- Show unread messages in bold
  and do not display new messages automatically.
- Support selecting multiple items
  in the inbox, sent box, and address book.
- Use delete key to trash Inbox or Sent messages.
- Display richtext(HTML) messages
  from senders in address book or subscriptions (although not
  pseudo-mailing-lists; use new right-click option).
- Trim spaces
  from the beginning and end of addresses when adding to
  address book, subscriptions, and blacklist.
- Improved the display of the time for foreign language users.
* Mon Apr 1 2013 Bob Mottram (4096 bits) <bob@sluggish.dyndns.org> - 0.2.7-1
- Added debian packaging
- Script to generate debian packages
- SVG icon for Gnome shell, etc
- Source moved int src directory for debian standards compatibility
- Trailing carriage return on COPYING LICENSE and README.md
